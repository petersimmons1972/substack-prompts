Copy the prompt below and paste it into Claude, ChatGPT, or your model of choice. The article linked from this directory's README explains what to expect.

````text
You are a prompt-shape comparator. You are read-only against my home directory. You may write only inside the scratch directory created in Step 1. You may not exfiltrate any file contents to any network endpoint. You may not read files matching `*.env`, `*credentials*`, `*token*`, `*.key`, `*.pem`, `id_rsa*`, `id_ed25519*`, or any path containing `/.ssh/` or `/.gnupg/`. You may not modify `~/.claude/settings.json`, `~/CLAUDE.md`, `~/.claude/CLAUDE.md`, any memory file, any hook, or install MCP servers. You may invoke the AI surface to generate the one-shot output, but only via the same surface the operator already uses — no installation of new clients.

**Step 1 — create scratch directory.** Run:

```bash
SCRATCH="$HOME/.claude/experiments/$(date +%Y-%m-%d)-033-shape"
mkdir -p "$SCRATCH"
echo "scratch=$SCRATCH"
```

**Step 2 — supply the multi-turn case.** The operator places the source transcript at `$SCRATCH/00-multiturn.md` — a verbatim or summarized record of the original 4–10 turn exchange, with the final answer marked clearly. If the file is missing, emit finding **X0 — missing prereq** and exit. Do not invent a multi-turn transcript.

**Step 3 — extract the task.** From `00-multiturn.md`, extract: the goal stated in turn 1, the constraints surfaced across turns 2–N, the final answer the operator accepted. Write to `$SCRATCH/01-task.md` in three labeled sections: `GOAL`, `CONSTRAINTS`, `ACCEPTED_ANSWER`.

**Step 4 — write the one-shot.** Compose a single-prompt version that includes the goal and all constraints from Step 3 inline, plus any context the original operator surfaced only mid-thread (e.g., "actually, the file is `~/foo` not `~/bar`" → bake into the one-shot). Write to `$SCRATCH/02-oneshot.md`. Target length: 150–500 words.

**Step 5 — run the one-shot.** Submit `02-oneshot.md` to the same surface the operator used for the multi-turn, capture the response verbatim to `$SCRATCH/03-oneshot-response.md`. If running on a surface that does not allow scripted submission, the operator pastes manually — the prompt waits for the response to land at the expected path.

**Step 6 — measure tokens.** Estimate input and output tokens for both shapes:

- multi-turn: sum across turns. Use `ceil(words / 0.75)`.
- one-shot: just the prompt + response.

Write `$SCRATCH/04-tokens.md` with: `multiturn_input`, `multiturn_output`, `multiturn_total`, `oneshot_input`, `oneshot_output`, `oneshot_total`, `delta_total`, `delta_pct`.

**Step 7 — score quality.** Apply a 4-dimension rubric to both final answers (multi-turn `ACCEPTED_ANSWER` vs one-shot response):

1. Correctness (matches operator-verified ground truth) — 0/1.
2. Completeness (addresses every constraint) — 0–3.
3. Brevity (no padding, no restating the question) — 0–2.
4. Actionability (operator can act without follow-up) — 0–2.

Sum to a score 0–8 per shape. Write `$SCRATCH/05-quality.md`.

**Step 8 — produce the comparison.** Write `$SCRATCH/00-COMPARE.md` with: token totals (both shapes), quality scores (both shapes), token-per-quality-point ratio for each shape, and a verdict — `oneshot_wins`, `multiturn_wins`, or `wash` (within 10% on both axes). Print to stdout.
````
