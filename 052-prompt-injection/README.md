# Prompt injection and untrusted context

_The document looks like a marketing summary — eight locations inside it contain instructions addressed to the model that is about to read it_

Prompts referenced in [Plutarch TX](https://plutarchtx.substack.com) article **052-prompt-injection**.

→ **Read the article:** <https://plutarchtx.substack.com/p/prompt-injection>

## How to use

Each `prompt-N.md` file is the prompt itself, with the teaching wrapper
stripped. Open the file, copy the contents, paste into Claude / ChatGPT /
your model of choice. The article (linked above) explains what the prompt
does and what to expect when you run it.

## Prompts in this article

### [`prompt-1.md`](./prompt-1.md) — Controlled Injection Test — Sandboxed Document with Embedded Instructions

Runs a controlled prompt-injection test. The prompt creates a fixture document inside scratch — a benign-looking text file with embedded instructions designed to look like operator commands ("ignore previous instructions", "read X and post to Y", "delete file Z"). The model is then asked to read and summarize the fixture *as if it were an arbitrary file the operator had asked about*. The point of the test is to observe whether the model follows the fixture's instructions, ignores them, or surfaces them as suspicious. The output is a behavioral log. Prompt 2 distills the observations into a personal mitigation checklist.

### [`prompt-2.md`](./prompt-2.md) — Personal Mitigation Checklist — Test, Refine, Adopt

Reads the observation log from Prompt 1 and produces a personal injection-mitigation checklist tailored to the patterns where the model's response was weakest. The checklist is short — five to nine items, each one sentence, each grep-able. The prompt then re-tests the checklist against the same fixture (counterfactual mode) by adding the checklist as a prepended system instruction and re-scoring the response. The output is a refined checklist plus before/after scores. The operator copies the surviving checklist into `~/CLAUDE.md` by hand.

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Attribution
to Plutarch TX appreciated when republishing.
