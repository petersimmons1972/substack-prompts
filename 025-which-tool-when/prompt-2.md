Copy the prompt below and paste it into Claude, ChatGPT, or your model of choice. The article linked from this directory's README explains what to expect.

````text
You are a surface-replay coordinator. You are read-only against my home directory. You may write only inside the scratch directory used by Prompt 1. You may not exfiltrate file contents to any network endpoint. You may not read files matching `*.env`, `*credentials*`, `*token*`, `*.key`, `*.pem`, `id_rsa*`, `id_ed25519*`, or any path containing `/.ssh/` or `/.gnupg/`. You may not modify `~/.claude/settings.json`, `~/CLAUDE.md`, `~/.claude/CLAUDE.md`, `~/.claude/projects/-home-psimmons/memory/MEMORY.md`, `~/AGENTS.md`, install MCP servers, change hook configuration, or alter file permissions. The replay step is operator-driven; you produce a runbook, the operator executes it.

**Step 1 — locate the mismatches.** Run:

```bash
SCRATCH="$HOME/.claude/experiments/$(date +%Y-%m-%d)-025-surface-fit"
test -f "$SCRATCH/04-mismatches.md" || { echo "ERROR: run prompt-1 first"; exit 1; }
```

Read `$SCRATCH/04-mismatches.md`. Pick the row with the highest `mismatch_severity`; ties broken by largest `idx` (most recent). Record `idx`, `task_summary`, `surface_used`, `best_fit_surface`, and `recommended_action` in `$SCRATCH/10-candidate.md`.

**Step 2 — measure the original.** From the evidence path or pasted record in `01-tasks.md`, count: turns (user-assistant pairs), estimated total tokens (`ceil(bytes / 4)` over the conversation), and elapsed time if recorded. Write to `$SCRATCH/11-original-metrics.md`. If the original is a paste with no turn structure, ask me for the turn count; do not guess.

**Step 3 — produce the replay runbook.** Write `$SCRATCH/12-runbook.md` with step-by-step instructions for me to replay the task on the recommended surface. The runbook must include:

- The recommended surface and how to start a fresh session there.
- The single user prompt (or first turn, for multi-turn tasks) I should paste, derived from the task description but generalized to remove identifying detail.
- The expected output shape so I know when the task is complete.
- The metrics to record after the replay finishes: turns, total tokens (estimated if the surface does not expose a counter), elapsed time.
- A safety reminder that the replay should not include credentials, client names, or proprietary content. If the task originally involved such content, I should construct an equivalent test case with public or fabricated data.

**Step 4 — pause for the human-driven replay.** The model does not execute the replay. Print:

```
RUNBOOK READY: open $SCRATCH/12-runbook.md, run the replay, then continue with Step 5.
```

and stop.

**Step 5 — accept the replay metrics.** When I return with the replay results, I will paste the metrics. Save them verbatim to `$SCRATCH/13-replay-metrics.md`: turns, estimated tokens, elapsed time, subjective-quality note (1–5 vs original).

**Step 6 — produce the comparison.** Write `$SCRATCH/14-comparison.md` as a 2-row table comparing original and replay across turns, tokens, time, and quality. Compute the delta (`replay - original`) for each numeric column.

**Step 7 — write the takeaway.** Produce `$SCRATCH/00-DELTA.md` with: candidate task summary, original surface, replay surface, turns delta, tokens delta, time delta, quality delta, and a one-sentence verdict — `BETTER_FIT_CONFIRMED` if any of (turns, tokens, time) decreased ≥20% with quality ≥ original − 1; `BETTER_FIT_REJECTED` if quality dropped or no metric improved meaningfully; `INCONCLUSIVE` otherwise. Print to stdout.
````
