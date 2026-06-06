Copy the prompt below and paste it into Claude, ChatGPT, or your model of choice. The article linked from this directory's README explains what to expect.

````text
You are a rule verifier and refiner. You operate read-only against `~/CLAUDE.md` and the scratch directory used by Prompt 1. You may write only inside scratch. You may not modify any live file, `~/.claude/settings.json`, any hook, or install MCP servers. You may not exfiltrate file contents. You may not read `*.env`, `*credentials*`, `*token*`, `*.key`, `*.pem`, `id_rsa*`, `id_ed25519*`, `/.ssh/`, or `/.gnupg/` paths.

**Step 1 — locate scratch and inputs.** Run:

```bash
SCRATCH="$HOME/.claude/experiments/$(date +%Y-%m-%d)-048-convention"
test -f "$SCRATCH/03-rule-draft.md" || { echo "ERROR: run prompt-1 first"; exit 1; }
mkdir -p "$SCRATCH/staged"
cp -p "$HOME/CLAUDE.md" "$SCRATCH/staged/CLAUDE-original.md"
```

**Step 2 — stage the candidate rule.** Produce a `CLAUDE-test.md` containing the live `~/CLAUDE.md` plus the candidate rule inserted into the proposed section from `03-rule-draft.md`. Write to `$SCRATCH/staged/CLAUDE-test.md`. Verify byte and md5 of the original backup. Record in `$SCRATCH/10-staged.md`.

**Step 3 — define three verification tasks.** Read `03-rule-draft.md` and the predictions from `04-prediction.md`. Build:

1. **TRIGGER-POSITIVE** — a task that should *clearly* invoke the rule. The rule must fire here; if it does not, the rule is wrong.
2. **TRIGGER-NEGATIVE** — a task that should *clearly not* invoke the rule. The rule must not fire here; if it does, the rule's trigger is too broad.
3. **BORDERLINE** — a task that the rule's trigger could plausibly catch but the operator's intent is ambiguous. Either outcome is acceptable; the rule's behavior here informs the refinement.

Write to `$SCRATCH/11-tasks.md`: `task_id`, `prompt`, `expected_fire`, `category`.

**Step 4 — run the verification (synthetic mode).** For each task, simulate model behavior under both files:

- **Baseline run** (against `CLAUDE-original.md`) — record whether the rule's trigger signature appears in the synthetic trace.
- **Test run** (against `CLAUDE-test.md`) — record whether the rule fires.

Synthetic mode means the verifier checks whether the rule's grep-able trigger fires, given the task's prompt — not whether the model produces specific text. Live mode (`LIVE=1`) requires a sandboxed Claude Code session and is opt-in.

Write traces to `$SCRATCH/transcripts-test/<task_id>-{baseline,test}.jsonl` and a summary to `$SCRATCH/12-verification.md`.

**Step 5 — judge the rule.** From the verification, classify:

- **READY** — TRIGGER-POSITIVE fires, TRIGGER-NEGATIVE does not fire, BORDERLINE behavior is acceptable. The rule is ready to commit to `~/CLAUDE.md`.
- **TOO-NARROW** — TRIGGER-POSITIVE did not fire. The rule's trigger missed the case it was written for. Refine the trigger.
- **TOO-BROAD** — TRIGGER-NEGATIVE fired. The rule fires when it should not. Add an exception or tighten the trigger.
- **UNCLEAR-BORDERLINE** — BORDERLINE behavior is wrong in the operator's judgment. Add an explicit clause.

Write to `$SCRATCH/13-judgment.md` with the verdict and a refined rule text (or "no refinement needed" if READY).

**Step 6 — refine and re-verify (if not READY).** If the verdict is anything other than READY, regenerate `CLAUDE-test.md` with the refined rule, re-run Steps 4–5. Repeat up to two refinement passes. After two failures, stop and produce a "needs-human-redraft" report — the rule is harder than it looked and the operator should redraft from the corrections.

**Step 7 — produce the install instructions.** Write `$SCRATCH/00-INSTALL.md` with: the final rule text, the proposed section (file + heading + insert position), a one-line `git apply` command for the unified diff `$SCRATCH/14-install.patch` if generated, and a verification log summarizing the firing/non-firing outcomes. Print to stdout. Do not run apply.
````
