# Skills as compressible knowledge

Prompts referenced in [Plutarch TX](https://plutarchtx.substack.com) article **040-skills-as-compressible-knowledge**.

→ **Read the article:** <https://plutarchtx.substack.com/p/skills-as-compressible-knowledge>

## How to use

Each `prompt-N.md` file is the prompt itself, with the teaching wrapper
stripped. Open the file, copy the contents, paste into Claude / ChatGPT /
your model of choice. The article (linked above) explains what the prompt
does and what to expect when you run it.

## Prompts in this article

### [`prompt-1.md`](./prompt-1.md) — Skill Break-Even Audit — Compute the Math for Each Skill

Walks every installed skill and computes its **break-even invocation count** — how many times the skill must fire before its always-loaded description has cost less context than inlining the same knowledge into a single prompt would have. A skill with a 200-token description and a 5,000-token body breaks even after ~25 invocations: below that, inlining the body once is cheaper than carrying the description forever. The output is a per-skill table with description size, body size, and the break-even number. The prompt does not modify any live file. Everything written goes inside a dated scratch directory you delete with one command.

### [`prompt-2.md`](./prompt-2.md) — Skill Redesign — Fix the Worst Break-Even

Picks the worst-scoring skill from Prompt 1 (highest break-even or `INVERTED` classification) and stages a redesigned version in scratch. The redesign tightens the description (cheaper to carry every session), or splits the body (so only relevant fragments load), or both. Computes the new break-even and the in-context delta. The prompt does not modify any live file. You review the redesign, copy it manually if you agree, and have a tested rollback path before you change anything.

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Attribution
to Plutarch TX appreciated when republishing.
