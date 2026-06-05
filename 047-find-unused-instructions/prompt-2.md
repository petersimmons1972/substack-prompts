Copy the prompt below and paste it into Claude, ChatGPT, or your model of choice. The article linked from this directory's README explains what to expect.

````text
You are a removal-preview verifier. You operate read-only against `~/CLAUDE.md`. You may write only inside the scratch directory used by Prompt 1. You may not modify any live file, `~/.claude/settings.json`, any hook, or install MCP servers. You may not exfiltrate file contents. You may not read `*.env`, `*credentials*`, `*token*`, `*.key`, `*.pem`, `id_rsa*`, `id_ed25519*`, `/.ssh/`, or `/.gnupg/` paths.

**Step 1 — locate scratch and inputs.** Run:

```bash
SCRATCH="$HOME/.claude/experiments/$(date +%Y-%m-%d)-047-unused"
test -f "$SCRATCH/00-UNUSED.md" || { echo "ERROR: run prompt-1 first"; exit 1; }
mkdir -p "$SCRATCH/staged" "$SCRATCH/transcripts-test"
cp -p "$HOME/CLAUDE.md" "$SCRATCH/staged/CLAUDE-original.md"
```

**Step 2 — back up and stage the removal.** For each rule with verdict `UNUSED-CANDIDATE` (excluding `UNUSED-CANDIDATE-CROSSREF`), produce a candidate-removed copy of `CLAUDE.md` at `$SCRATCH/staged/CLAUDE-test.md`. Verify byte and md5 of the backup at `$SCRATCH/staged/CLAUDE-original.md`. Record in `$SCRATCH/30-staged.md`.

**Step 3 — define the verification task set.** Pull representative tasks from `01-rules.md`'s categories. The default set is six tasks (operator may extend via `TASKS=path/to/tasks.txt`):

1. *Behavioral default* — "list files in ~/projects" (should use `ls`, not stray to a tool).
2. *Tool preference* — "fetch the homepage of example.com" (should use `xh`, not `curl`).
3. *Pre-flight* — "edit a single character in a file" (should run `git status` first if first write op).
4. *Memory* — "summarize the project state" (should hit `memory_recall` if R1 still applies).
5. *Cost guardrail* — "scenario: estimated $7 compute task" (should stop and notify).
6. *Project priority* — "ambiguous task — choose between Clearwatch chart fix and homelab DNS tweak" (should default to Clearwatch).

Each task is recorded with: `task_id`, `prompt`, `expected_behavior`, `category`. Write to `$SCRATCH/31-tasks.md`.

**Step 4 — run the verification (twice).** For each task in the set:

a. **Baseline run** — execute against the original `CLAUDE.md` (i.e., the operator's current setup). Capture the model's response shape and tool calls into `$SCRATCH/transcripts-test/<task_id>-baseline.jsonl`.

b. **Test run** — execute against the staged `CLAUDE-test.md` (rules removed). Capture into `<task_id>-test.jsonl`.

Use a small harness: a Python script that reads each task and either writes a synthetic "expected behavior" check (no live model call needed) or, if `LIVE=1` is set, makes a live call into a sandboxed Claude Code session. The synthetic mode is the default — it checks whether the rule's trigger signature would fire under the model's current routing, not whether the model produces specific text.

**Step 5 — score behavior delta.** Compare `<task>-baseline.jsonl` to `<task>-test.jsonl`. For each task, score:

- **NO-DELTA** — both runs produced the same trigger signatures and same expected-behavior outcome.
- **DELTA-NEUTRAL** — slight wording or tool-order change, but expected behavior intact.
- **DELTA-DEGRADED** — expected behavior diverged (the rule's trigger that should have fired did not, or the wrong tool was selected).

Write to `$SCRATCH/32-behavior.md`.

**Step 6 — produce per-candidate verdict.** For each removed rule, infer:

- **SAFE-TO-REMOVE** — every task that exercised the rule's category came back NO-DELTA or DELTA-NEUTRAL.
- **KEEP** — at least one task in the rule's category came back DELTA-DEGRADED.
- **INCONCLUSIVE** — no task in the verification set exercised the rule's category. Operator decides whether to add a task and re-run, or to leave the rule in place.

Write to `$SCRATCH/33-verdicts.md`.

**Step 7 — produce the removal patch and report.** Generate `$SCRATCH/34-removal.patch` as a unified diff against the live `CLAUDE.md`, including only `SAFE-TO-REMOVE` rules. Run `git apply --check` from `$HOME` and record results in `$SCRATCH/35-patch-check.md`. Write `$SCRATCH/00-PLAN.md` with: candidate count, verdicts breakdown, byte savings if applied, patch path, and the exact `git apply` command. Print to stdout. Do not run apply.
````
