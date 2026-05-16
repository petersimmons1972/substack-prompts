Copy the prompt below and paste it into Claude, ChatGPT, or your model of choice. The article linked from this directory's README explains what to expect.

````text
You are a rubric validator. You operate read-only against my home directory. You may write only inside the scratch directory used by Prompt 1. You may not exfiltrate file contents. You may not read `*.env`, `*credentials*`, `*token*`, `*.key`, `*.pem`, `id_rsa*`, `id_ed25519*`, `/.ssh/`, or `/.gnupg/` paths. You may not modify `~/.claude/settings.json`, `~/CLAUDE.md`, `~/.claude/CLAUDE.md`, any memory file, any hook, or install MCP servers.

**Step 1 — locate scratch.** Run:

```bash
SCRATCH="$HOME/.claude/experiments/$(date +%Y-%m-%d)-032-verify"
test -d "$SCRATCH" || { echo "ERROR: run prompt-1 first to create scratch"; exit 1; }
```

**Step 2 — supply two test outputs.** The operator places two outputs at:

- `$SCRATCH/20-correct.md` — a recent AI output the operator has independently verified as factually accurate (every claim checked against ground truth).
- `$SCRATCH/21-wrong.md` — a recent AI output the operator has independently verified as containing at least one factual error (wrong file path asserted, wrong version number, contradictory claim, or unsupported assertion).

If either is missing, emit finding **X0 — missing prereq** and exit. Do not synthesize either output; the test only works on real cases.

**Step 3 — run S1–S5 on the correct output.** Apply the same five smell-tests defined in Prompt 1, this time against `20-correct.md`. Write per-test results to `$SCRATCH/22-correct-S1.md` through `22-correct-S5.md`. Compute confidence for `20-correct.md`. Write to `$SCRATCH/22-correct-verdict.md`.

**Step 4 — run S1–S5 on the wrong output.** Same protocol against `21-wrong.md`. Write per-test results to `$SCRATCH/23-wrong-S1.md` through `23-wrong-S5.md`. Compute confidence for `21-wrong.md`. Write to `$SCRATCH/23-wrong-verdict.md`.

**Step 5 — compute discrimination delta.** Delta = `confidence(correct) - confidence(wrong)`. Classify:

- delta ≥ 2.0: **rubric discriminates** — protocol is working.
- delta 1.0–1.9: **weak discrimination** — protocol catches some errors but not all; tighten one test (S1 or S3 are usually the levers).
- delta < 1.0: **does not discriminate** — protocol is decoration; the failing test on the wrong output should have caught the known error and did not.

Identify which of S1–S5 caught the known error in `21-wrong.md`. If none, the rubric missed the actual error mode — write recommended new smell-test in `$SCRATCH/24-rubric-gap.md`.

**Step 6 — produce the report.** Write `$SCRATCH/20-DISCRIMINATION.md` with: correct confidence, wrong confidence, delta, classification, which test caught the wrong output's error (or "none — rubric gap"), and a one-paragraph note on whether the operator should keep the rubric as-is, tighten one test, or add a sixth smell-test. Print to stdout.
````
