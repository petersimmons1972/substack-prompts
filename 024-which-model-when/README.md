# Which model, when

Prompts referenced in [Plutarch TX](https://plutarchtx.substack.com) article **024-which-model-when**.

→ **Read the article:** <https://plutarchtx.substack.com/p/which-model-when>

## How to use

Each `prompt-N.md` file is the prompt itself, with the teaching wrapper
stripped. Open the file, copy the contents, paste into Claude / ChatGPT /
your model of choice. The article (linked above) explains what the prompt
does and what to expect when you run it.

## Prompts in this article

### [`prompt-1.md`](./prompt-1.md) — Model Selection Prompt — Find Your Overspends

Inspects metadata from your recent AI sessions and produces a list of turns where a smaller/cheaper model would have produced functionally equivalent output. The classifier is conservative — it flags only turns whose task class falls into `classification`, `formatting`, `bulk_judge`, `mechanical_transform`, or `health_check`, the categories Anthropic and OpenAI both document as Haiku- or small-model-appropriate. Architecture decisions, multi-file edits, and reasoning-heavy debugging are never flagged. The output is a ranked list of overspends you can act on in Prompt 2.

### [`prompt-2.md`](./prompt-2.md) — Model Selection Prompt — Replay Against the Smaller Model

Picks one flagged overspend from Prompt 1, reconstructs the user prompt that produced the original turn, and re-runs that prompt against a smaller model — Haiku 4.5 if the original was Anthropic, GPT-4.1-mini or o4-mini if OpenAI. The two outputs sit side by side in scratch with a quality rubric. The result is evidence for or against the overspend classification: if Haiku produces a substantively equivalent answer, the original turn was an overspend and the cost gap is real. If Haiku falls short, the classifier was wrong — useful information either way.

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Attribution
to Plutarch TX appreciated when republishing.
