# Surface Selection Prompt — Replay on the Better-Fit Surface

**Article:** 025 — Which tool, when (Prompt 2 of 2).
**Depends on:** Prompt 1's `04-mismatches.md`.
**Surfaces:** the prompt itself can run from any surface; the *replay* must execute on the surface Prompt 1 recommended.
**Run mode:** writes only to a dated scratch directory; the operator drives the replay manually on the target surface.

---

## What this prompt does

Picks the highest-severity mismatch from Prompt 1, walks you through replaying that task on the recommended surface, and captures the turns/tokens delta side by side with the original. Where Prompt 1 audited, Prompt 2 produces evidence. The result is a single-row before/after comparison you can hold up next to the rubric: "this task ran in 14 turns on chat; on Claude Code it ran in 4."

## Run this prompt

> You are a surface-replay coordinator. You are read-only against my home directory. You may write only inside the scratch directory used by Prompt 1. You may not exfiltrate file contents to any network endpoint. You may not read files matching `*.env`, `*credentials*`, `*token*`, `*.key`, `*.pem`, `id_rsa*`, `id_ed25519*`, or any path containing `/.ssh/` or `/.gnupg/`. You may not modify `~/.claude/settings.json`, `~/CLAUDE.md`, `~/.claude/CLAUDE.md`, `~/.claude/projects/-home-psimmons/memory/MEMORY.md`, `~/AGENTS.md`, install MCP servers, change hook configuration, or alter file permissions. The replay step is operator-driven; you produce a runbook, the operator executes it.
>
> **Step 1 — locate the mismatches.** Run:
>
> ```bash
> SCRATCH="$HOME/.claude/experiments/$(date +%Y-%m-%d)-025-surface-fit"
> test -f "$SCRATCH/04-mismatches.md" || { echo "ERROR: run prompt-1 first"; exit 1; }
> ```
>
> Read `$SCRATCH/04-mismatches.md`. Pick the row with the highest `mismatch_severity`; ties broken by largest `idx` (most recent). Record `idx`, `task_summary`, `surface_used`, `best_fit_surface`, and `recommended_action` in `$SCRATCH/10-candidate.md`.
>
> **Step 2 — measure the original.** From the evidence path or pasted record in `01-tasks.md`, count: turns (user-assistant pairs), estimated total tokens (`ceil(bytes / 4)` over the conversation), and elapsed time if recorded. Write to `$SCRATCH/11-original-metrics.md`. If the original is a paste with no turn structure, ask me for the turn count; do not guess.
>
> **Step 3 — produce the replay runbook.** Write `$SCRATCH/12-runbook.md` with step-by-step instructions for me to replay the task on the recommended surface. The runbook must include:
>
> - The recommended surface and how to start a fresh session there.
> - The single user prompt (or first turn, for multi-turn tasks) I should paste, derived from the task description but generalized to remove identifying detail.
> - The expected output shape so I know when the task is complete.
> - The metrics to record after the replay finishes: turns, total tokens (estimated if the surface does not expose a counter), elapsed time.
> - A safety reminder that the replay should not include credentials, client names, or proprietary content. If the task originally involved such content, I should construct an equivalent test case with public or fabricated data.
>
> **Step 4 — pause for the human-driven replay.** The model does not execute the replay. Print:
>
> ```
> RUNBOOK READY: open $SCRATCH/12-runbook.md, run the replay, then continue with Step 5.
> ```
>
> and stop.
>
> **Step 5 — accept the replay metrics.** When I return with the replay results, I will paste the metrics. Save them verbatim to `$SCRATCH/13-replay-metrics.md`: turns, estimated tokens, elapsed time, subjective-quality note (1–5 vs original).
>
> **Step 6 — produce the comparison.** Write `$SCRATCH/14-comparison.md` as a 2-row table comparing original and replay across turns, tokens, time, and quality. Compute the delta (`replay - original`) for each numeric column.
>
> **Step 7 — write the takeaway.** Produce `$SCRATCH/00-DELTA.md` with: candidate task summary, original surface, replay surface, turns delta, tokens delta, time delta, quality delta, and a one-sentence verdict — `BETTER_FIT_CONFIRMED` if any of (turns, tokens, time) decreased ≥20% with quality ≥ original − 1; `BETTER_FIT_REJECTED` if quality dropped or no metric improved meaningfully; `INCONCLUSIVE` otherwise. Print to stdout.

## Undo

```bash
rm -rf "$HOME/.claude/experiments/$(date +%Y-%m-%d)-025-surface-fit"
```

That is the entire revert. The prompt produces a runbook and tabulates results; it does not run the replay itself, modify any live file, or send anything to a network endpoint.

## What you should now see

- A single named candidate task — the most-mismatched one from Prompt 1.
- A runbook you can follow to replay it on the recommended surface.
- A side-by-side metrics table after you complete the replay.
- A delta showing whether the better-fit surface saved turns, tokens, or time.
- A verdict file confirming or rejecting the surface-fit recommendation for this task class.

## How to confirm the win

Article 025 is value-tagged `context-savings`. The win is realized when `BETTER_FIT_CONFIRMED` fires and the operator has a turns or tokens delta in their hand. Across typical operators, severe mismatches (severity-3) tend to produce 50–80% turn reductions when replayed on the right surface — a multi-file refactor that took 18 turns of copy-paste on Claude.ai chat will typically take 4–6 turns on Claude Code with filesystem access. Moderate mismatches (severity-2) produce 20–40% improvements. If your candidate's delta is below 20%, either the rubric over-estimated the mismatch or the task's bottleneck was not surface-related. Either outcome is informative — keep `00-DELTA.md` for the Article 057 end-to-end review.

Subscribe so you don't miss Article 026, where the next lever is the prompt itself.
