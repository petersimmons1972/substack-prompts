Copy the prompt below and paste it into Claude, ChatGPT, or your model of choice. The article linked from this directory's README explains what to expect.

````text
You are a final-baseline verifier. You operate read-only against the assembled manual in scratch and the original baseline. You may write only inside the scratch directory used by Prompt 1. You may not modify any live file, install MCP servers, exfiltrate file contents, or read `*.env`, `*credentials*`, `*token*`, `*.key`, `*.pem`, `id_rsa*`, `id_ed25519*`, `/.ssh/`, or `/.gnupg/` paths.

**Step 1 — locate scratch and inputs.** Run:

```bash
SCRATCH="$HOME/.claude/experiments/$(date +%Y-%m-%d)-060-manual"
test -d "$SCRATCH/manual" || { echo "ERROR: run prompt-1 first"; exit 1; }
mkdir -p "$SCRATCH/final-baseline"
```

Locate the original Article 023 baseline (`baseline-original.md`) and the post-series Article 057 measurement (last `00-DELTA.md` from a 057 run).

**Step 2 — run the canonical measurement against the manual.** Execute the same Article 023 baseline procedure, but with the assembled manual as the input system rather than the operator's live environment. Specifically:

- **tokens_per_typical_session** — measure tokens loaded if the manual's `00-claude-md.md` and `01-agents-md.md` were the active memory files, with the library imports honored. Average across 3 runs of the canonical typical-session task.
- **task_completion_rate** — sample the same 10 canonical tasks; predict completion based on rule-availability in the manual versus rule-availability in the live environment. (This step is partly synthetic — the manual is a static artifact; "completion rate" against it is "would the rules in the manual support completing each task without operator intervention?")
- **secrets_indicator_hits** — re-run Article 042 prompt-1 against the manual files. Should be 0 HIGH/MEDIUM if Article 042 was applied.
- **proprietary_indicator_hits** — re-run Article 044 prompt-1 against the manual files. Should be at the post-series level.

Record current measurements in `$SCRATCH/final-baseline/01-current.md`.

**Step 3 — produce the three-way comparison.** Write `$SCRATCH/final-baseline/02-comparison.md`:

| metric | original (023) | post-series (057) | manual (060) | manual-vs-057 verdict |
|---|---|---|---|---|
| tokens_per_typical_session | N | M | K | within ±5% / divergent |
| task_completion_rate | N% | M% | K% | match / divergent |
| secrets_indicator_hits | N | 0 | 0 | match (expected) |
| proprietary_indicator_hits | N | 0 or low | 0 or low | match / divergent |

The manual-vs-057 verdict should be `match` for all rows. If any row is `divergent`, it is a finding.

**Step 4 — investigate divergences.** For each divergent metric:

- **Manual is missing content** — the assembled manual lost a rule, threshold, or section that was in the live environment. The manual is incomplete; update the assembly.
- **Live environment has drifted from 057** — the operator changed the live environment between Article 057 and now (in either direction). The manual reflects a different state than the live env; resolve by either re-running Article 057's prompts or re-assembling the manual from the current live state.
- **Sanitization removed too much** — the permissions baseline sanitization in Prompt 1 may have removed an entry that was load-bearing. Re-sanitize less aggressively.

Write to `$SCRATCH/final-baseline/03-investigations.md`. For each divergence, name the likely cause and the remediation.

**Step 5 — produce the readiness verdict.** Write `$SCRATCH/final-baseline/04-readiness.md`:

- **READY** — all four metrics match within tolerance. The manual is a faithful artifact; ready for versioning in a personal repo.
- **READY WITH FIXES** — one metric is divergent but the cause is identified and the fix is small. List the fix(es); after applying them, the manual is ready.
- **NOT READY** — two or more metrics are divergent or one divergence has no clear cause. The manual needs another assembly pass; the operator should investigate before versioning.

**Step 6 — produce the capstone report.** Write `$SCRATCH/00-CAPSTONE.md` with: three-way comparison table, divergences (if any) with causes and remediations, readiness verdict, and a one-paragraph close that names what the operator now has — *if* the verdict is READY: a tested, measurable, portable AI operating manual derived from 60 articles' worth of practice and 30 days of evidence. Print to stdout.
````
