# Prompting fundamentals you skipped

Prompts referenced in [Plutarch TX](https://plutarchtx.substack.com) article **026-prompting-fundamentals**.

→ **Read the article:** <https://plutarchtx.substack.com/p/prompting-fundamentals>

## How to use

Each `prompt-N.md` file is the prompt itself, with the teaching wrapper
stripped. Open the file, copy the contents, paste into Claude / ChatGPT /
your model of choice. The article (linked above) explains what the prompt
does and what to expect when you run it.

## Prompts in this article

### [`prompt-1.md`](./prompt-1.md) — Prompting Fundamentals Prompt — XML Restructure A/B

Takes one of your recent verbose prompts, restructures it with XML tags and explicit role framing per Anthropic's prompt-engineering guidance, sends both versions to the same model, and reports the token delta and the quality delta side by side. The goal is to put a number on a frequently-cargo-culted technique. If XML structuring earns its keep on your task, you'll see it in the metrics; if it doesn't, you'll see that too. Either result corrects a common assumption.

### [`prompt-2.md`](./prompt-2.md) — Prompting Fundamentals Prompt — Few-Shot Earn-Their-Keep Test

Few-shot examples are popular advice. They also cost tokens — every turn, on every call. This prompt takes one of your repeatedly-used prompts, adds three carefully-chosen few-shot examples, and runs both versions across a small batch of test inputs to find out whether the examples earn their token cost. The output is a per-test verdict and an aggregate verdict: examples that improve quality on enough cases to justify their per-call overhead, or examples that are a tax with no return.

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Attribution
to Plutarch TX appreciated when republishing.
