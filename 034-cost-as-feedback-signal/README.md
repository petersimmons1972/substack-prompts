# Cost as a feedback signal

Prompts referenced in [Plutarch TX](https://plutarchtx.substack.com) article **034-cost-as-feedback-signal**.

→ **Read the article:** <https://plutarchtx.substack.com/p/cost-as-feedback-signal>

## How to use

Each `prompt-N.md` file is the prompt itself, with the teaching wrapper
stripped. Open the file, copy the contents, paste into Claude / ChatGPT /
your model of choice. The article (linked above) explains what the prompt
does and what to expect when you run it.

## Prompts in this article

### [`prompt-1.md`](./prompt-1.md) — Cost-as-Signal Prompt — Per-Task Cost Breakdown

Pulls recent API usage (or subscription consumption metrics) and produces a per-task cost breakdown. The point is to stop reading the bill as a budget alarm and start reading it as a diagnostic — if one task type is consuming half the spend, that task's prompt shape is the highest-leverage place to optimize. Most operators have never broken out cost by task because the surfaces don't do it for them.

### [`prompt-2.md`](./prompt-2.md) — Cost-as-Signal Prompt — Reversible Plan to Reduce the Top Outlier

Reads the cost breakdown from Prompt 1, picks the top spend outlier, and produces a reversible plan to reduce it: model downshift, prompt-shape change, batching, or context pruning. The prompt does not apply the change — it stages the change and the rollback. The reduction is measured against the next Prompt 1 run.

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Attribution
to Plutarch TX appreciated when republishing.
