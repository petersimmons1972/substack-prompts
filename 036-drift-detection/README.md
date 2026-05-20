# Drift detection

Prompts referenced in [Plutarch TX](https://plutarchtx.substack.com) article **036-drift-detection**.

→ **Read the article:** <https://plutarchtx.substack.com/p/drift-detection>

## How to use

Each `prompt-N.md` file is the prompt itself, with the teaching wrapper
stripped. Open the file, copy the contents, paste into Claude / ChatGPT /
your model of choice. The article (linked above) explains what the prompt
does and what to expect when you run it.

## Prompts in this article

### [`prompt-1.md`](./prompt-1.md) — Drift Detection Prompt — Audit Memory Claims Against Live State

Audits memory files for claims about specific files, functions, flags, paths, or commands and verifies each claim against live state. Memory files accumulate facts that drift — a path moves, a flag is renamed, a function is deleted — and the AI keeps confidently using the stale claim long after the fact has changed. This prompt finds the stale claims. It does not fix them; Prompt 2 does.

### [`prompt-2.md`](./prompt-2.md) — Drift Correction Prompt — Stage Memory Fixes Without Touching Live Files

Takes the drift report from Prompt 1 and, for every stale claim, produces a staged correction — either a rewritten line of memory text or a deletion proposal — written to scratch as a unified diff against the live file. The diff is not applied. The operator reviews the diff, decides what to keep, and applies the survivors by hand. The whole point of the staging step is to keep the AI out of the memory file: a model that can rewrite its own instructions can also drift them sideways without the operator noticing.

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Attribution
to Plutarch TX appreciated when republishing.
