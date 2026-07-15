Copy the prompt below and paste it into Claude, ChatGPT, or your model of choice. The article linked from this directory's README explains what to expect.

````text
You are a baseline re-runner. You operate read-only against the original baseline at `BASELINE=<path>` (defaults to `$HOME/.claude/experiments/baseline-original.md` if present, or the latest `*-023-baseline/` scratch directory). You may write only inside the scratch directory created in Step 1. You may not modify any live file, install MCP servers, exfiltrate file contents, or read `*.env`, `*credentials*`, `*token*`, `*.key`, `*.pem`, `id_rsa*`, `id_ed25519*`, `/.ssh/`, or `/.gnupg/` paths.

**Step 1 — create scratch directory and locate baseline.** Run:

```bash
SCRATCH="$HOME/.claude/experiments/$(date +%Y-%m-%d)-057-baseline-rerun"
mkdir -p "$SCRATCH"
test -f "$BASELINE" || { echo "ERROR: original baseline not found at $BASELINE"; exit 1; }
cp -p "$BASELINE" "$SCRATCH/00-original.md"
```

**Step 2 — run the canonical measurement prompt.** Execute the same baseline measurement Article 023 defined. The standard four metrics:

- **tokens_per_typical_session** — measure tokens-loaded across a representative typical session (e.g., a code review or a small implementation task). Average across 3 runs.
- **task_completion_rate** — sample 10 small canonical tasks; count how many completed without operator intervention.
- **secrets_indicator_hits** — re-run Article 042's prompt-1 scan and record HIGH/MEDIUM/LOW counts.
- **proprietary_indicator_hits** — re-run Article 044's prompt-1 scan and record HIGH/MEDIUM/LOW counts.

Record the current measurements in `$SCRATCH/01-current.md` with the same shape as `00-original.md`.

**Step 3 — compute deltas.** Write `$SCRATCH/02-deltas.md`:

| metric | original | current | delta | expected_direction | verdict |
|---|---|---|---|---|---|
| tokens_per_typical_session | N | M | M − N | down (compression, removed unused) | improved / unchanged / regressed |
| task_completion_rate | N% | M% | M − N | up (better rules, more recall) | improved / unchanged / regressed |
| secrets_indicator_hits | N | M | M − N | down to 0 (after Article 042) | improved / unchanged / regressed |
| proprietary_indicator_hits | N | M | M − N | down to 0 (after Article 044) | improved / unchanged / regressed |

Use a tolerance band: changes within ±5% are `unchanged`; changes outside the band are `improved` or `regressed` based on the expected direction.

**Step 4 — break down sources of change.** For each metric that improved, attribute the change to the article(s) most likely responsible. Memory bytes removed can usually be traced to Articles 043, 046, 047. Task completion changes often track to Articles 037–041, 048. Secret/proprietary indicator drops trace to Articles 042 and 044. Write to `$SCRATCH/03-attribution.md`.

**Step 5 — flag regressions.** Any metric that landed in the `regressed` column is a finding. Write `$SCRATCH/04-regressions.md` with: which metric regressed, by how much, and the most likely cause (e.g., a memory-file rule was removed in Article 047 that was actually load-bearing, and `task_completion_rate` dropped). Each regression rolls into Prompt 2 as a revisit candidate.

**Step 6 — produce the delta report.** Write `$SCRATCH/00-DELTA.md` with: the four-row delta table, per-metric attribution, regression flags, and a one-paragraph "what worked, what didn't" summary. Print to stdout.
````
