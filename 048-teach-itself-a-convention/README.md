# Ask the AI to teach itself a new convention

_Replace the correction cycle with a procedure — the convention loop that produces rules which demonstrably work_

Prompts referenced in [Plutarch TX](https://plutarchtx.substack.com) article **048-teach-itself-a-convention**.

→ **Read the article:** <https://plutarchtx.substack.com/p/teach-itself-a-convention>

## How to use

Each `prompt-N.md` file is the prompt itself, with the teaching wrapper
stripped. Open the file, copy the contents, paste into Claude / ChatGPT /
your model of choice. The article (linked above) explains what the prompt
does and what to expect when you run it.

## Prompts in this article

### [`prompt-1.md`](./prompt-1.md) — Convention Loop — Encode a Recurring Need as a Memory-File Rule

Identifies one recurring friction in recent sessions that would be solved by a memory-file rule, encodes it as the smallest possible rule, and stages it in scratch. The article calls this the convention loop: observe a repeated need, encode a rule, verify the rule fires, refine for false positives. This prompt covers the first two steps. Prompt 2 verifies and refines. The encoding step prefers the *minimum* rule that produces the behavior — if a one-line bullet works, do not write a four-paragraph section.

### [`prompt-2.md`](./prompt-2.md) — Convention Loop — Verify the Rule Fires; Refine for False Positives

Takes the candidate rule from Prompt 1, runs three representative tasks against it (one trigger-positive, one trigger-negative, one borderline), measures whether the rule fires correctly, and refines the rule based on the results. The output is a final rule the operator copy-pastes into `~/CLAUDE.md` by hand, plus a verification log. The discipline: a rule that has not been verified to fire is a rule that does not yet exist.

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Attribution
to Plutarch TX appreciated when republishing.
