# Multi-turn vs one-shot

Prompts referenced in [Plutarch TX](https://plutarchtx.substack.com) article **033-multi-turn-vs-one-shot**.

→ **Read the article:** <https://plutarchtx.substack.com/p/multi-turn-vs-one-shot>

## How to use

Each `prompt-N.md` file is the prompt itself, with the teaching wrapper
stripped. Open the file, copy the contents, paste into Claude / ChatGPT /
your model of choice. The article (linked above) explains what the prompt
does and what to expect when you run it.

## Prompts in this article

### [`prompt-1.md`](./prompt-1.md) — Multi-turn vs One-shot Prompt — Convert and Compare

Takes one multi-turn task you completed recently — typically 4–10 turns of back-and-forth — and rewrites it as a single one-shot prompt. Then runs both: the original transcript (already in your history) and the new one-shot. Compares quality and token cost. The point is to make the right shape for the task obvious by measurement, not preference.

### [`prompt-2.md`](./prompt-2.md) — Multi-turn vs One-shot Prompt — Reshape Failed One-shot into Checkpointed Flow

Takes a one-shot prompt that produced a poor result and reshapes it as a multi-turn flow with explicit checkpoints. Each checkpoint is a question the AI must answer correctly before the next step proceeds. The point is to recognize the inverse failure mode of Prompt 1: tasks where state must be confirmed mid-flight, and where one-shot compression hides errors that a checkpoint would have caught immediately.

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Attribution
to Plutarch TX appreciated when republishing.
