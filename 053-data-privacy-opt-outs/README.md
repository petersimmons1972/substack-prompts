# Data privacy and training opt-outs

_Every AI surface has its own toggles and defaults — inheriting them by inattention is a policy choice_

Prompts referenced in [Plutarch TX](https://plutarchtx.substack.com) article **053-data-privacy-opt-outs**.

→ **Read the article:** <https://plutarchtx.substack.com/p/data-privacy-opt-outs>

## How to use

Each `prompt-N.md` file is the prompt itself, with the teaching wrapper
stripped. Open the file, copy the contents, paste into Claude / ChatGPT /
your model of choice. The article (linked above) explains what the prompt
does and what to expect when you run it.

## Prompts in this article

### [`prompt-1.md`](./prompt-1.md) — Privacy Inventory — Current State on Every Surface

Builds a per-surface privacy inventory. The output is a structured checklist with one section per surface (ChatGPT, Claude.ai, Anthropic API, OpenAI API, Gemini, enterprise tiers if present), each listing the data-handling questions worth answering: training opt-out status, retention period, conversation history settings, model-improvement settings, and any provider-specific toggles. The operator visits each surface in their browser, fills in the current state, and the prompt produces a single-file report that captures their starting position before changes. Prompt 2 stages recommended changes per surface with before/after snapshots.

### [`prompt-2.md`](./prompt-2.md) — Apply Recommended Opt-Outs — Before/After Per Surface

Reads the filled-in inventory from Prompt 1 and produces a per-surface change-list with the recommended privacy posture, the exact toggles to flip, the before/after expected state, and the undo path per change. The output is a checklist the operator works through in their browser. The prompt does not change any provider setting; it makes the change set explicit, defensible, and reversible.

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Attribution
to Plutarch TX appreciated when republishing.
