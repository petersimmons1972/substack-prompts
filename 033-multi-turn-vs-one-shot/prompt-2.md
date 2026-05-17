Copy the prompt below and paste it into Claude, ChatGPT, or your model of choice. The article linked from this directory's README explains what to expect.

````text
You are a flow-reshape designer. You are read-only against my home directory. You may write only inside the scratch directory used by Prompt 1. You may not exfiltrate any file contents to any network endpoint. You may not read `*.env`, `*credentials*`, `*token*`, `*.key`, `*.pem`, `id_rsa*`, `id_ed25519*`, `/.ssh/`, or `/.gnupg/` paths. You may not modify `~/.claude/settings.json`, `~/CLAUDE.md`, `~/.claude/CLAUDE.md`, any memory file, any hook, or install MCP servers.

**Step 1 — locate scratch.** Run:

```bash
SCRATCH="$HOME/.claude/experiments/$(date +%Y-%m-%d)-033-shape"
mkdir -p "$SCRATCH"
```

**Step 2 — supply the failed one-shot.** The operator places the failed one-shot at `$SCRATCH/20-failed-oneshot.md` and the bad response at `$SCRATCH/21-bad-response.md`. The operator also describes in `$SCRATCH/22-failure-mode.md` (one paragraph) what went wrong: e.g., "the AI assumed file X existed when it did not," "the AI invented a flag that does not exist on this version," "the AI wrote correct code for the wrong language." If any of the three files are missing, emit finding **X0 — missing prereq**.

**Step 3 — diagnose the missing checkpoint.** Map the failure mode to one of four diagnostic categories:

- **D1 — state-assumption:** failure assumed the state of a file/version/setting without checking.
- **D2 — ambiguity-collapse:** failure picked one interpretation of an ambiguous request without surfacing alternatives.
- **D3 — long-jump:** failure executed multiple dependent steps without verifying any.
- **D4 — context-blindness:** failure used training-data defaults instead of the operator's environment-specific values.

Write to `$SCRATCH/23-diagnosis.md` with the chosen category and a one-paragraph justification.

**Step 4 — design checkpoints.** For each diagnostic category, design a checkpoint that catches it:

- D1 → "Before proceeding, run `ls <path>` and confirm the file exists; if it does not, stop and report."
- D2 → "Before proceeding, list the 2–3 plausible interpretations of '<ambiguous phrase>' and ask me to pick one."
- D3 → "After step N, summarize the change you just made in one sentence and wait for me to confirm before step N+1."
- D4 → "Before answering, confirm the version/flag/path I am using by inspecting <specific live signal>; do not assume defaults."

Write the chosen checkpoints to `$SCRATCH/24-checkpoints.md`. Use exactly 1–3 checkpoints — more becomes its own friction.

**Step 5 — compose the multi-turn flow.** Write `$SCRATCH/25-multiturn-flow.md` with the full reshape: an opening turn that states the goal and constraints, a checkpoint instruction (from Step 4), and explicit pauses where the AI must wait. Mark the pauses with the literal phrase `<<CHECKPOINT — wait for human>>`.

**Step 6 — predict the recovery.** For each checkpoint, name what error it would have caught in the original failed run. Write to `$SCRATCH/26-recovery-prediction.md`. If a checkpoint cannot be tied to a specific original-error catch, drop it — it is not earning its friction.

**Step 7 — produce the plan.** Write `$SCRATCH/20-RESHAPE.md` with: failure mode, diagnostic category, checkpoint count, predicted recoveries, and the full reshaped flow. Print to stdout.
````
