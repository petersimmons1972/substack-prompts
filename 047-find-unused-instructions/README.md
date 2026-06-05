# Ask the AI to find unused instructions

_Every rule in CLAUDE.md pays a per-session cost whether it fires or not — this procedure finds the ones that never fire_

Prompts referenced in [Plutarch TX](https://plutarchtx.substack.com) article **047-find-unused-instructions**.

→ **Read the article:** <https://plutarchtx.substack.com/p/find-unused-instructions>

## How to use

Each `prompt-N.md` file is the prompt itself, with the teaching wrapper
stripped. Open the file, copy the contents, paste into Claude / ChatGPT /
your model of choice. The article (linked above) explains what the prompt
does and what to expect when you run it.

## Prompts in this article

### [`prompt-1.md`](./prompt-1.md) — Unused Instructions — Identify Lines That Never Fire

Identifies candidate unused instructions in `~/CLAUDE.md` by cross-referencing each rule against recent session transcripts. A rule is "unused" if no session in the operator's recent history reached the trigger that would invoke it. Memory files accumulate rules that seemed important at the time and have not fired since; these are pure overhead — context tokens with zero behavioral effect. The prompt does not modify the file. Prompt 2 stages removal previews and verifies nothing breaks.

### [`prompt-2.md`](./prompt-2.md) — Removal Preview — Cut Unused Rules and Verify Nothing Breaks

Takes the unused-candidate list from Prompt 1, produces a removal preview in scratch (the new `~/CLAUDE.md` with those rules removed), runs a small set of representative tasks against the staged copy, and reports whether behavior changed in any concerning way. The output is a per-candidate verdict — `SAFE-TO-REMOVE`, `KEEP` (a representative task showed degraded behavior), or `INCONCLUSIVE` — plus a unified diff to apply for the safe rows. The operator applies the diff manually only after reading the verification report.

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Attribution
to Plutarch TX appreciated when republishing.
