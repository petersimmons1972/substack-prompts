# The model and tool selection cheat sheet

Prompts referenced in [Plutarch TX](https://plutarchtx.substack.com) article **059-selection-cheat-sheet**.

→ **Read the article:** <https://plutarchtx.substack.com/p/selection-cheat-sheet>

_Published: 2026-05-25_

## How to use

Each `prompt-N.md` file is the prompt itself, with the teaching wrapper
stripped. Open the file, copy the contents, paste into Claude / ChatGPT /
your model of choice. The article (linked above) explains what the prompt
does and what to expect when you run it.

## Prompts in this article

### [`prompt-1.md`](./prompt-1.md) — Personalized Selection Cheat Sheet — Derive From Usage Data

Builds a personalized model and tool selection cheat sheet from the operator's actual usage data — not from generic guidance. The cheat sheet maps task classes to recommended models, surfaces, and escalation rules based on what has actually worked for this operator over the last 30 days. The output is a one-page reference. Prompt 2 stress-tests it by routing the next three real tasks through it.

### [`prompt-2.md`](./prompt-2.md) — Stress-Test — Three Real Tasks Through the Cheat Sheet

Stress-tests the cheat sheet against the next three real tasks the operator handles. For each task, the operator notes the cheat-sheet recommendation, follows it, and records the outcome plus any case where they would have chosen differently in retrospect. The prompt produces the test scaffold and the scoring rubric; the operator runs the test in their normal flow over a day or two and logs back. The output is a refined cheat sheet plus a "where it was wrong" list to inform the next quarter's update.

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Attribution
to Plutarch TX appreciated when republishing.
