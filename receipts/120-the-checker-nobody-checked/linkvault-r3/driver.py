#!/usr/bin/env python3
"""One measured run: the suite's run_harness contract steps 1-7 (called step by
step through run_harness.py's own functions so a ModelVerificationFailure does
not lose the launch result), then score_ws from lib_ws.sh, then per-run
forensics. Appends one JSON record to <records>.

Nothing here re-implements launch, verification, token extraction or scoring:
those are run_harness.py / extract_tokens.py / lib_ws.sh verbatim from the
scratch clone.
"""
import argparse, json, os, re, subprocess, sys, time, filecmp, hashlib

S = "$WORK/measure-s55-sol6"
SUITE = f"{S}/fleet/dispatch-metrics/model-eval-suite"
sys.path.insert(0, f"{SUITE}/runners")
import run_harness as rh  # noqa: E402
import extract_tokens as et  # noqa: E402
import run_review_cell as rrc  # noqa: E402

PRICE_IN, PRICE_OUT = 2.0, 10.0  # registry/model-pricing.yaml, both arms


def jl(path):
    out = []
    if not path or not os.path.exists(path):
        return out
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    out.append(json.loads(line))
                except json.JSONDecodeError:
                    out.append({"_unparseable": line[:200]})
    return out


def tree_files(root):
    res = {}
    for dp, dns, fns in os.walk(root):
        dns[:] = [d for d in dns if d not in ("__pycache__", ".pytest_cache")]
        for fn in fns:
            if fn.endswith(".pyc"):
                continue
            p = os.path.join(dp, fn)
            res[os.path.relpath(p, root)] = p
    return res


def diff_tree(template, workdir):
    t, w = tree_files(template), tree_files(workdir)
    added = sorted(set(w) - set(t))
    deleted = sorted(set(t) - set(w))
    modified = sorted(k for k in set(t) & set(w) if not filecmp.cmp(t[k], w[k], shallow=False))
    return added, deleted, modified


PY_EXERCISE = re.compile(r"\b(pytest|unittest)\b|update_link|deactivate_link")
PY_RUN_FILE = re.compile(r"\bpython3?\s+(?!-m\s+(py_compile|compileall))(?!-c)\S+\.py\b")


WRITES = re.compile(r"open\([^)]*['\"][wa]['\"]|\.write\(|write_text|\btee\b|>\s*\S*\.py|cat\s*>>?")
PY_TOKEN = re.compile(r"(^|[\s;&|(\"'`])(python3?|pytest)(\s|$|['\"])")


def command_exercises_code(cmd):
    """Amendment 1: python/pytest invoked as a command token; the command must
    not write files unless it also runs a separate .py check file; and it runs
    pytest/unittest, a .py file, or inline code referencing the new methods."""
    if not PY_TOKEN.search(cmd):
        return False
    runs_file = bool(PY_RUN_FILE.search(cmd))
    if WRITES.search(cmd) and not runs_file:
        return False
    if re.search(r"py_compile|compileall", cmd) and not PY_EXERCISE.search(cmd):
        return False
    return bool(PY_EXERCISE.search(cmd) or runs_file)


def _old_command_exercises_code(cmd):
    """Pre-registered: a command counts as 'ran tests' iff it runs pytest/
    unittest, runs a .py file (other than py_compile/compileall), or runs an
    inline python snippet that references update_link/deactivate_link.
    Compile-only / import-only does not count."""
    if not re.search(r"python|pytest", cmd):
        return False
    if re.search(r"py_compile|compileall", cmd) and not PY_EXERCISE.search(cmd):
        return False
    return bool(PY_EXERCISE.search(cmd) or PY_RUN_FILE.search(cmd))


def claude_forensics(events, workdir):
    top_models, sub_models = {}, {}
    cmds, tool_paths, init = [], [], None
    final_text = None
    for e in events:
        if e.get("type") == "system" and e.get("subtype") == "init" and init is None:
            init = {k: e.get(k) for k in ("model", "tools", "mcp_servers", "permissionMode", "claude_code_version", "cwd")}
            init["mcp_servers"] = [m.get("name") if isinstance(m, dict) else m for m in (init.get("mcp_servers") or [])]
        if e.get("type") == "assistant":
            m = e.get("message", {}).get("model")
            bucket = sub_models if e.get("parent_tool_use_id") else top_models
            bucket[m] = bucket.get(m, 0) + 1
            for c in e.get("message", {}).get("content", []) or []:
                if c.get("type") == "tool_use":
                    inp = c.get("input", {}) or {}
                    if c.get("name") == "Bash":
                        cmds.append(inp.get("command", ""))
                    for key in ("file_path", "path", "notebook_path"):
                        if key in inp:
                            tool_paths.append((c.get("name"), inp[key]))
                    if c.get("name") == "Bash":
                        for p in re.findall(r"(?:^|[\s'\"=(])(/[^\s'\";|&<>)]+)", inp.get("command", "")):
                            tool_paths.append(("Bash", p))
                if c.get("type") == "text" and not e.get("parent_tool_use_id"):
                    final_text = c.get("text")
        if e.get("type") == "result":
            if e.get("result"):
                final_text = e.get("result")
    outside = sorted({f"{n}:{p}" for n, p in tool_paths
                      if p.startswith("/") and not p.startswith(workdir)
                      and not p.startswith(("/dev/", "/tmp", "/usr", "/bin", "/proc"))})
    return dict(top_models=top_models, sub_models=sub_models, cmds=cmds,
                outside_paths=outside, init=init, final_text=final_text)


def codex_forensics(events):
    models, efforts, cmds = {}, {}, []
    max_req_in, compactions, final_text = 0, 0, None
    tc_consistent = True
    for e in events:
        t, p = e.get("type"), e.get("payload", {}) or {}
        if t == "turn_context":
            models[p.get("model")] = models.get(p.get("model"), 0) + 1
            efforts[p.get("effort")] = efforts.get(p.get("effort"), 0) + 1
        if t == "compacted" or (t == "event_msg" and "compact" in str(p.get("type", ""))):
            compactions += 1
        if t == "event_msg" and p.get("type") == "token_count":
            last = (p.get("info") or {}).get("last_token_usage") or {}
            max_req_in = max(max_req_in, int(last.get("input_tokens", 0) or 0))
            tot = int(last.get("total_tokens", 0) or 0)
            if tot and tot != int(last.get("input_tokens", 0) or 0) + int(last.get("output_tokens", 0) or 0):
                tc_consistent = False
        if t == "event_msg" and p.get("type") == "agent_message":
            final_text = p.get("message")
        if t == "event_msg" and p.get("type") == "task_complete" and p.get("last_agent_message"):
            final_text = p.get("last_agent_message")
        if t == "response_item" and p.get("type") in ("function_call", "custom_tool_call", "local_shell_call"):
            args = p.get("arguments") or p.get("input") or p.get("action") or ""
            if isinstance(args, str):
                try:
                    a = json.loads(args)
                except Exception:
                    a = args
            else:
                a = args
            if isinstance(a, dict):
                c = a.get("cmd") or a.get("command") or a.get("input") or ""
                if isinstance(c, list):
                    c = " ".join(map(str, c))
                cmds.append(str(c))
            else:
                cmds.append(str(a))
    return dict(models=models, efforts=efforts, cmds=cmds, max_request_input_tokens=max_req_in,
                compactions=compactions, total_eq_in_plus_out=tc_consistent, final_text=final_text)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--harness", required=True)
    ap.add_argument("--model", required=True)
    ap.add_argument("--effort", required=True)
    ap.add_argument("--run-id", required=True)
    ap.add_argument("--brief", required=True)
    ap.add_argument("--template", required=True)
    ap.add_argument("--private", default=None)
    ap.add_argument("--records", required=True)
    ap.add_argument("--phase", required=True)
    ap.add_argument("--append-file", default=None)
    ap.add_argument("--arm", default="base")
    a = ap.parse_args()

    scratch = f"{S}/runs"
    os.environ["SCRATCH"] = scratch
    outdir = f"{scratch}/out"
    os.makedirs(outdir, exist_ok=True)
    rec = {"run_id": a.run_id, "phase": a.phase, "harness": a.harness, "requested_model": a.model,
           "requested_effort": a.effort, "brief": os.path.basename(a.brief),
           "started_at": time.strftime("%Y-%m-%dT%H:%M:%S%z")}

    if a.harness == "claude-cli":
        # Ruling A (coordinator, 2026-09-28): advisor off, inherited session vars scrubbed.
        scrubbed = sorted(k for k in os.environ if k.startswith("CLAUDE_CODE_"))
        for k in scrubbed:
            del os.environ[k]
        os.environ["CLAUDE_CODE_DISABLE_ADVISOR_TOOL"] = "1"
        rec["env_scrubbed"] = scrubbed
        rec["env_set"] = {"CLAUDE_CODE_DISABLE_ADVISOR_TOOL": "1"}
        if a.append_file:
            os.environ["EXPECTED_APPEND_SYSTEM_PROMPT_FILE"] = a.append_file
            rec["env_set"]["EXPECTED_APPEND_SYSTEM_PROMPT_FILE"] = a.append_file
            rec["append_file_sha256"] = hashlib.sha256(open(a.append_file, "rb").read()).hexdigest()
    rec["arm"] = a.arm
    entry = rh.load_registry_entry(a.harness)
    rh.verify_recipe_content_hash(entry)
    rec["harness_recipe_version"] = entry["harness_recipe_version"]
    rec["harness_recipe_content_hash"] = entry["harness_recipe_content_hash"]
    extra = rrc.gpt6_cap_argv(a.harness, a.model) if a.harness == "codex" else []
    rec["extra_args"] = extra
    lr = rh._LAUNCHERS[a.harness](a.run_id, a.brief, a.template, outdir, a.model, a.effort, extra)
    rec["exit_code"] = lr["exit_code"]
    rec["wallclock_s"] = round(lr["wallclock_s"], 1)
    rec["session_log"] = lr.get("session_log")
    if lr["exit_code"] != 0:
        rec["launch_stderr_tail"] = (lr.get("stderr") or "")[-600:]
    try:
        rec["model_verified"] = rh.verify_model(entry, lr, a.model)
        rec["model_verification_error"] = None
    except rh.ModelVerificationFailure as e:
        rec["model_verified"] = False
        rec["model_verification_error"] = str(e)
    try:
        rec["tokens"] = et.extract_tokens(a.harness, lr.get("session_log"))["tokens"]
    except Exception as e:  # noqa
        rec["tokens"] = None
        rec["token_error"] = str(e)
    rec["completion_status"] = rh.check_completion(entry, lr)

    events = jl(lr.get("session_log"))
    workdir = f"{scratch}/workdirs/{a.run_id}"
    if a.harness == "claude-cli":
        fx = claude_forensics(events, workdir)
        rec["served_models_top"] = fx["top_models"]
        rec["served_models_subagent"] = fx["sub_models"]
        rec["fallback_to_sonnet5"] = fx["top_models"].get("claude-sonnet-5", 0) > 0
        rec["apparatus_init"] = fx["init"]
        rec["outside_workdir_paths"] = fx["outside_paths"]
        res = [e for e in events if e.get("type") == "result"]
        mu = (res[-1].get("modelUsage") if res else None) or {}
        rec["model_usage_keys"] = sorted(mu)
        rec["model_usage"] = mu
        rec["void_other_model"] = sorted(mu) != [a.model]
        s55 = mu.get(a.model) or {}
        rec["tokens_suite_extractor"] = rec["tokens"]
        rec["tokens"] = {"input": s55.get("inputTokens", 0), "cache_read": s55.get("cacheReadInputTokens", 0),
                         "cache_creation": s55.get("cacheCreationInputTokens", 0), "output": s55.get("outputTokens", 0),
                         "reasoning": s55.get("thinkingTokens", 0), "source": "result.modelUsage"} if s55 else None
    else:
        fx = codex_forensics(events)
        rec["served_models_top"] = fx["models"]
        rec["effort_observed"] = fx["efforts"]
        rec["max_request_input_tokens"] = fx["max_request_input_tokens"]
        rec["under_270k_cap"] = fx["max_request_input_tokens"] < 270000
        rec["compactions"] = fx["compactions"]
        rec["total_eq_in_plus_out"] = fx["total_eq_in_plus_out"]
        rec["fallback_to_sonnet5"] = False
    rec["commands"] = fx["cmds"]
    rec["final_text_tail"] = (fx["final_text"] or "")[-400:]

    tk = rec["tokens"] or {}
    if tk:
        if a.harness == "claude-cli":
            prompt_all = tk["input"] + tk["cache_read"] + tk["cache_creation"]
        else:
            prompt_all = tk["input"]
        rec["prompt_tokens_all"] = prompt_all
        rec["usd_all_prompt"] = round((prompt_all * PRICE_IN + tk["output"] * PRICE_OUT) / 1e6, 4)
        rec["usd_suite_convention"] = round((tk["input"] * PRICE_IN + tk["output"] * PRICE_OUT) / 1e6, 4)
        if a.harness == "claude-cli":  # all models in modelUsage count toward spend
            rec["usd_all_models"] = round(sum(((u.get("inputTokens",0)+u.get("cacheReadInputTokens",0)+u.get("cacheCreationInputTokens",0))*PRICE_IN + u.get("outputTokens",0)*PRICE_OUT)/1e6 for u in rec["model_usage"].values()), 4)
        else:
            rec["usd_all_models"] = rec["usd_all_prompt"]

    if a.private:
        cmd = (f'export SCRATCH="{scratch}"; source "{SUITE}/runners/lib_ws.sh"; '
               f'score_ws "{a.run_id}" "{a.private}"')
        p = subprocess.run(["bash", "-c", cmd], capture_output=True, text=True)
        line = [l for l in p.stdout.splitlines() if l.startswith(("PASS", "INCONCLUSIVE"))]
        rec["score_line"] = line[-1] if line else None
        m = re.match(r"PASS (\d+)/(\d+)", rec["score_line"] or "")
        if m:
            rec["hidden_passed"], rec["hidden_total"] = int(m.group(1)), int(m.group(2))
            rec["pass_fraction"] = round(int(m.group(1)) / int(m.group(2)), 4)
        else:
            rec["hidden_passed"] = rec["hidden_total"] = rec["pass_fraction"] = None
        sp = f"{outdir}/{a.run_id}.score.txt"
        rec["score_file"] = sp
        if os.path.exists(sp):
            rec["failed_tests"] = [l.strip() for l in open(sp) if re.match(r"\s*(FAIL|ERROR)", l)][:40]

        added, deleted, modified = diff_tree(a.template, workdir)
        rec["files_added"], rec["files_deleted"], rec["files_modified"] = added, deleted, modified
        required = {"linkvault/resolver.py"}
        oos = sorted(set(added + deleted + modified) - required)
        rec["out_of_scope_files"] = oos
        rec["out_of_scope_existing_src"] = sorted(set(deleted + modified) - required)
        rec["out_of_scope_edits"] = bool(oos) or bool(rec.get("outside_workdir_paths"))
        res_path = f"{workdir}/linkvault/resolver.py"
        src = open(res_path).read() if os.path.exists(res_path) else ""
        both = bool(re.search(r"def update_link\(", src) and re.search(r"def deactivate_link\(", src))
        rec["both_methods_defined"] = both
        ft = (fx["final_text"] or "").strip()
        rec["ends_with_question"] = ft.endswith("?")
        rec["stopped_early"] = (not both) or (rec["completion_status"] != "completed")
        ran = [c for c in fx["cmds"] if command_exercises_code(c)]
        rec["test_commands"] = ran[:5]
        rec["unverified_done"] = both and rec["completion_status"] == "completed" and not ran
        allcmd = " ".join(fx["cmds"]) + " ".join(rec.get("outside_workdir_paths") or [])
        rec["contamination_touch"] = bool(re.search(r"private|reference/|calibration|run_tests|model-eval-suite", allcmd))
    rec["finished_at"] = time.strftime("%Y-%m-%dT%H:%M:%S%z")
    with open(a.records, "a") as f:
        f.write(json.dumps(rec) + "\n")
    print(json.dumps({k: rec.get(k) for k in ("run_id", "exit_code", "model_verified", "served_models_top",
                                                "hidden_passed", "usd_all_prompt", "wallclock_s")}))


if __name__ == "__main__":
    main()
