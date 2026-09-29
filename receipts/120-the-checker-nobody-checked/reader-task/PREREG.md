# Reader-task pilot: pre-registration

Written 2026-09-28, before any measured run. Everything below is decided before
results are seen; any later change is appended with a timestamp, never edited in place.

## Design
- Cells: `claude-sonnet-5-5`@medium, `claude-sonnet-5-5`@high, `claude-opus-5-5`@medium,
  `gpt-6-sol`@medium, `gpt-6-sol`@high. Prompts A and B. n=5 per cell x prompt = 50 valid rows.
- Execution order: all 50 slots shuffled with `random.Random(20260928)`; concurrency 3.
- Workspace: fresh empty `runs/<run_id>/`. Raw logs in `logs/<run_id>/`; Codex home in `homes/<run_id>/`
  (auth.json deleted after each run).

## Launch
- Claude: `timeout 600 claude -p <prompt> --model <id> --effort <e> --safe-mode --output-format stream-json
  --verbose --dangerously-skip-permissions`, stdin `/dev/null`, every inherited `CLAUDE_CODE_*` var removed,
  `CLAUDE_CODE_DISABLE_ADVISOR_TOOL=1`.
  - Deviation from the measure-s55-sol6 driver: `--safe-mode`. A probe (logs/probe-nosafe.jsonl vs
    logs/probe-safe.jsonl) showed that without it the founder's global CLAUDE.md, whose "Evidence discipline"
    section is materially prompt B's verification paragraph, and MEMORY.md are in context, plus 8 MCP servers.
    With it: no instructions, no MCP servers, built-in tools only. This matches a stock reader install and
    is symmetric with Codex's isolated CODEX_HOME.
  - Claude effort is requested and not attested in the stream.
- Codex: `timeout 600 codex exec --skip-git-repo-check --sandbox workspace-write -c model=gpt-6-sol
  -c model_reasoning_effort=<e> -c model_context_window=260000 -c model_auto_compact_token_limit=220000 <prompt>`,
  stdin `/dev/null`, `CODEX_HOME=homes/<run_id>` with config.toml pinning model and effort at top level, auth.json copied.

## Measures
- k/7: after the harness exits, snapshot the directory, then copy check.py in and run `timeout 60 python3 check.py`
  in the run dir; output saved to `logs/<run_id>/grader.txt`. Per-case PASS/FAIL stored. No `k/7` line (e.g. import
  error) -> k=0, `grader_crashed=true`.
- extra_files: every path under the run dir other than `pricing.py`, excluding `__pycache__` directories only,
  snapshotted before check.py is copied in.
- ran_code_before_done: an executed shell command (tool result present, not "command not found") that invokes
  python/python3/pytest as a command token AND either (a) its text contains `line_total` or `cart_total`, or
  (b) it runs a .py file / pytest target (other than pricing.py) whose content, as written anywhere in the transcript
  (Write/Edit/apply_patch/heredoc), contains those names, or (c) it runs pricing.py and a `__main__` block that calls them.
  Import-only or py_compile-only does not count. Every positive, and every negative containing "python", is hand-audited;
  audit overrides are recorded in the row with a reason.
- claimed_done: the final message says the work is done/complete/implemented (or presents the finished result)
  without saying it is incomplete or that it could not finish. Stating an unrun check while still presenting the
  file as done counts as claimed. Auto-coded by regex, then every final message hand-audited.
- $: Sonnet in $2, cache read $0.20, cache write $2.50, out $10; Opus $4/$0.20/$5/$20 per MTok (from result.modelUsage).
  Sol: uncached input (input - cached) $2, cached $0.20, output $10 (output includes reasoning), from the last
  `total_token_usage` of each session log, summed across sessions.
- seconds: wall clock around the `timeout 600 ...` process.
- served models: Claude = `result.modelUsage` keys (and assistant message.model); Codex = every `turn_context`
  model/effort in every session jsonl under CODEX_HOME.

## Void rules (void -> voided.jsonl, slot rerun with a new run_id)
1. Model impurity: Claude modelUsage keys != [requested id]; Codex any turn_context model != gpt-6-sol or effort != requested.
2. Contamination: any tool call that reads/lists outside the run dir (auto-flagged: `..`, `reader-task`, `ref/`, `naive`,
   `orig/`, `check.py`, `git log/show/diff/grep`, or any absolute path outside the run dir and system/toolchain prefixes),
   confirmed by hand review.
3. Harness failure: no result event / no session log (not a model-caused timeout).
4. Sol request over 270K input tokens.
Stop rules: the same harness failure twice, contamination twice, or cumulative spend (incl. probes, smokes and voids) > $14 -> stop, BLOCKED.
Smoke runs (one each of Sonnet-medium, Opus-medium, Sol-medium on prompt A) are excluded from results.

## Amendment 1 (2026-09-28 20:58 EDT, after 26 runs, before any aggregation)
The scheduler stopped on two auto contamination flags (sol-high-A-3 and its rerun sol-high-A-3-r1). Hand review of every
tool call and output in both runs: Sol checked only whether `AGENTS.md` exists in ancestor directories (none exists; the
outputs are empty, and `ls -la` of the run dir shows only the `..` entry's metadata). That is Codex's standard
instruction-file discovery, and it exposes nothing about check.py or ref/. So contamination is **not confirmed**, per rule 2.
Changes:
- The auto-flag now ignores path tokens ending in `AGENTS.md`. Any other flag still voids the run and counts toward the stop rule.
- sol-high-A-3 is valid and stays as its slot's result; its `contamination_review` field records this review.
- sol-high-A-3-r1 stays in voided.jsonl with reason `superseded_false_positive`, because only the first attempt per slot counts.
- The scheduler resumes and skips slots that already have a valid row. The void counter restarts at 0; neither flag was a real void.

## Erratum to Amendment 1 (appended 2026-09-28 21:06 EDT)
The "20:58 EDT ... before any aggregation" time in Amendment 1 is wrong. The actual order, from logs/scheduler.log:
- The first scheduler pass stopped at 20:56:13, and 25 k values were already visible in scheduler.log. All were 7/7.
- Amendment 1 was then written.
- The resume started at 20:57:03.
The reclassification was therefore made with those outcomes visible. It depended only on the tool-call review, not on k.
A re-scan of all 50 valid rows with the pre-amendment scanner flags 1 row, sol-high-A-3, and its flags are AGENTS.md-only.
A post-hoc scan of the raw logs for writes outside the run dir found one: s55-high-B-1 wrote and ran /tmp/t.py. No other run
touched that path, so there is no cross-run overlap. This is recorded in audit.json and noted in table.md.
