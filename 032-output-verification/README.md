# Output verification and calibration

Prompts referenced in [Plutarch TX](https://plutarchtx.substack.com) article **032-output-verification**.

→ **Read the article:** <https://plutarchtx.substack.com/p/output-verification>

## How to use

Each `prompt-N.md` file is the prompt itself, with the teaching wrapper
stripped. Open the file, copy the contents, paste into Claude / ChatGPT /
your model of choice. The article (linked above) explains what the prompt
does and what to expect when you run it.

## Prompts in this article

### [`prompt-1.md`](./prompt-1.md) — Output Verification Prompt — Five Smell-Tests + Confidence Rating

Applies five smell-tests — source citation, unit consistency, file-existence checks, internal contradiction, novelty score — to one recent AI output and produces a single confidence rating from 0–5 with the failing tests named. The point is not to grade the AI; the point is to give you a 60-second protocol to run before acting on AI output, especially when the output asserts facts about your environment.

### [`prompt-2.md`](./prompt-2.md) — Output Verification Prompt — Discrimination Test

Validates that Prompt 1's smell-test rubric *discriminates* — that it gives a known-correct AI output a high confidence score and a known-wrong AI output a low one. If the rubric does not discriminate, it is decoration, not verification. The prompt runs the same five smell-tests on two outputs side-by-side and emits a discrimination delta. A delta ≥ 2.0 is a working rubric; below that, the rubric needs sharpening.

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Attribution
to Plutarch TX appreciated when republishing.
