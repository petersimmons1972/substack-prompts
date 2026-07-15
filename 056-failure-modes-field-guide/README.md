# Failure modes you'll see again

Prompts referenced in [Plutarch TX](https://plutarchtx.substack.com) article **056-failure-modes-field-guide**.

→ **Read the article:** <https://plutarchtx.substack.com/p/failure-modes-field-guide>

_Published: 2026-05-23_

## How to use

Each `prompt-N.md` file is the prompt itself, with the teaching wrapper
stripped. Open the file, copy the contents, paste into Claude / ChatGPT /
your model of choice. The article (linked above) explains what the prompt
does and what to expect when you run it.

## Prompts in this article

### [`prompt-1.md`](./prompt-1.md) — Failure-Mode Tagging — Map Recent Sessions to Five Shapes

Tags every failure occurrence in the operator's recent sessions with one of five canonical shapes. The five shapes are: **sycophancy** (agreeing with bad ideas; reversing position when challenged); **loop-on-loop** (repeating the same approach despite failure); **false confidence** (asserting wrong facts confidently); **silent degradation** (output gets worse without erroring); **scope-creep** (the model takes on more than asked, often introducing new bugs). The output is a frequency table per shape plus exemplar quotes the operator can re-read to recognize the pattern in real time. Prompt 2 picks the most common shape and designs an interrupt phrase that catches it next time.

### [`prompt-2.md`](./prompt-2.md) — Personal Interrupt — Catch the Most Common Shape Next Time

Takes the most common failure shape from Prompt 1 and designs a personal interrupt — either a phrase the operator will say (or paste) when they notice the pattern starting, or a memory-file rule that prevents the model from completing the pattern. The output is a one-paragraph interrupt with a triggering criterion and an expected behavior change. The prompt then re-tests the interrupt against an exemplar from Prompt 1 (counterfactual: would the interrupt have caught the pattern earlier?).

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Attribution
to Plutarch TX appreciated when republishing.
