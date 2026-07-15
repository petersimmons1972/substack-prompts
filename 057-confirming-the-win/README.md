# Confirming the win, end-to-end

Prompts referenced in [Plutarch TX](https://plutarchtx.substack.com) article **057-confirming-the-win**.

→ **Read the article:** <https://plutarchtx.substack.com/p/confirming-the-win>

_Published: 2026-05-24_

## How to use

Each `prompt-N.md` file is the prompt itself, with the teaching wrapper
stripped. Open the file, copy the contents, paste into Claude / ChatGPT /
your model of choice. The article (linked above) explains what the prompt
does and what to expect when you run it.

## Prompts in this article

### [`prompt-1.md`](./prompt-1.md) — Re-Run the Baseline — Produce a Delta Table

Re-runs Article 023's canonical baseline measurement against the current environment and produces a delta table comparing the two measurements. The four numbers from Article 023 are: `tokens_per_typical_session`, `task_completion_rate`, `secrets_indicator_hits`, and `proprietary_indicator_hits` (per the baseline's standard four-metric set; the operator may have extended it). The delta table shows for each metric: original, current, change, expected direction, and verdict (improved / unchanged / regressed).

### [`prompt-2.md`](./prompt-2.md) — Revisit Articles for Stuck Metrics

For each metric that did not improve in Prompt 1's delta table, identifies the relevant article and prompts in the series and produces a per-metric remediation list. The list is the operator's instructions for the next pass. The prompt does not re-run those articles; it points at them with specific, evidence-grounded recommendations. Stuck metrics are diagnostic, not failures: each one names a workflow that did not actually change.

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Attribution
to Plutarch TX appreciated when republishing.
