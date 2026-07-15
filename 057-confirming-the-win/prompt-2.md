Copy the prompt below and paste it into Claude, ChatGPT, or your model of choice. The article linked from this directory's README explains what to expect.

````text
You are a remediation-list generator. You operate read-only against the scratch directory used by Prompt 1. You may write only inside scratch. You may not modify any live file, install MCP servers, exfiltrate file contents, or read `*.env`, `*credentials*`, `*token*`, `*.key`, `*.pem`, `id_rsa*`, `id_ed25519*`, `/.ssh/`, or `/.gnupg/` paths.

**Step 1 — locate scratch and inputs.** Run:

```bash
SCRATCH="$HOME/.claude/experiments/$(date +%Y-%m-%d)-057-baseline-rerun"
test -f "$SCRATCH/00-DELTA.md" || { echo "ERROR: run prompt-1 first"; exit 1; }
```

**Step 2 — list metrics to revisit.** From `02-deltas.md`, list every metric where verdict is `unchanged` or `regressed`. For each, record original value, current value, expected direction, and the gap.

Write to `$SCRATCH/40-stuck-metrics.md`.

**Step 3 — match metrics to articles.** Use the article-to-metric map:

| metric | likely articles | what to revisit |
|---|---|---|
| tokens_per_typical_session ↑ (regressed) | 043, 046, 047 | unused-rules audit and compression — operator may have re-bloated |
| tokens_per_typical_session unchanged | 046, 047 | compression and unused-rules — operator may not have applied |
| task_completion_rate ↓ (regressed) | 047, 048 | a removed rule may have been load-bearing; or a new rule too narrow |
| task_completion_rate unchanged | 037–041, 048 | rules added during the series may not be firing; check via Article 045 |
| secrets_indicator_hits > 0 | 042 | run Prompt 2 against the residual; rotate any HIGH leaks |
| proprietary_indicator_hits > 0 | 044 | run Prompt 2 with refreshed blocklist |

Per stuck metric, name 1–2 specific articles and prompts to revisit. Write to `$SCRATCH/41-article-map.md`.

**Step 4 — produce the remediation list per metric.** For each stuck metric, write `$SCRATCH/remediation/<metric>.md` with:

- **What did not move** — the specific gap.
- **Most likely cause** — best-guess attribution from the article map.
- **Article to revisit** — which article and which prompt.
- **Specific action** — the concrete next step ("Re-run Article 042 Prompt 1; rotate any HIGH-confidence leaks before applying replacements").
- **Predicted outcome** — what the metric should look like after the revisit, if the cause was correctly diagnosed.

**Step 5 — produce a diagnostic note when everything looks fine.** If a metric is `improved` but the operator suspects the improvement is noise (e.g., a 6% drop where the natural variation is ±10%), flag it for follow-up measurement at the next baseline rerun. Stuck metrics are diagnostic; suspicious improvements are also diagnostic.

Write to `$SCRATCH/42-noise-flags.md` (may be empty).

**Step 6 — produce the remediation report.** Write `$SCRATCH/00-REMEDIATION.md` with: list of stuck metrics, the article map, per-metric remediation paths, and a recommended order ("address the regressions first; then the unchanged metrics in order of operator priority"). Print to stdout.
````
