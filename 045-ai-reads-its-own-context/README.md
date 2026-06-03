# Ask the AI to read its own context

_The model believes it is following your rules — this procedure checks whether that belief is accurate_

Prompts referenced in [Plutarch TX](https://plutarchtx.substack.com) article **045-ai-reads-its-own-context**.

→ **Read the article:** <https://plutarchtx.substack.com/p/ai-reads-its-own-context>

## How to use

Each `prompt-N.md` file is the prompt itself, with the teaching wrapper
stripped. Open the file, copy the contents, paste into Claude / ChatGPT /
your model of choice. The article (linked above) explains what the prompt
does and what to expect when you run it.

## Prompts in this article

### [`prompt-1.md`](./prompt-1.md) — Self-Summary Prompt — What Does the Model Think Its Rules Are

Asks the model to summarize the operational rules it believes apply to the current session — without leading the answer. The point is to surface the gap between what the operator wrote in `CLAUDE.md` and what the model has actually internalized after compression, summarization, and the operator's various session-time instructions. Drift between intent and effect is invisible until you ask the model what *it* thinks the contract is. The prompt does not modify any file; it produces a self-summary the operator compares against the live `CLAUDE.md` in Prompt 2.

### [`prompt-2.md`](./prompt-2.md) — Self-Summary Diff — Compare the Model's Summary to the Real CLAUDE.md

Compares the model's self-summary from Prompt 1 against the live `~/CLAUDE.md` line by line. Each rule in `CLAUDE.md` is matched to the closest claim in the self-summary; each claim in the self-summary is matched back to the source rule. Mismatches fall into three classes: **HALLUCINATED** (the model believes a rule that does not appear in `CLAUDE.md`), **MISSED** (a rule the operator wrote that the model did not internalize), or **DRIFTED** (the model recalled the rule but with a meaningful variation). The output is a triage report. The operator decides which mismatches need a `CLAUDE.md` rewrite, which need session reminders, and which are acceptable.

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Attribution
to Plutarch TX appreciated when republishing.
