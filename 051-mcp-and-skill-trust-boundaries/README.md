# Trust boundaries with MCP servers and skills

_The MCP server you added in February and have not audited since — it has been reading your context for ninety days_

Prompts referenced in [Plutarch TX](https://plutarchtx.substack.com) article **051-mcp-and-skill-trust-boundaries**.

→ **Read the article:** <https://plutarchtx.substack.com/p/mcp-and-skill-trust-boundaries>

## How to use

Each `prompt-N.md` file is the prompt itself, with the teaching wrapper
stripped. Open the file, copy the contents, paste into Claude / ChatGPT /
your model of choice. The article (linked above) explains what the prompt
does and what to expect when you run it.

## Prompts in this article

### [`prompt-1.md`](./prompt-1.md) — MCP/Skill Audit — Provenance, Capability, Observed Behavior

Audits installed MCP servers and skills for source provenance (where did it come from, who wrote it), declared capabilities (what tools it exposes, what scopes it requests), and observed behavior (what it has actually done in recent sessions). The output is a per-component trust card: a short summary an operator can read in one sitting to decide whether to keep, scope, or remove the component. The prompt does not modify configuration; Prompt 2 stages a scoped permission proposal for one weak-provenance component.

### [`prompt-2.md`](./prompt-2.md) — Trust-Boundary Report — Scoped Permission Proposal for One Component

Picks one component flagged `WEAK-provenance` + `STATE-MODIFYING` from Prompt 1 and produces a trust-boundary report plus a scoped permission proposal. The scope ratchets the component down from "whatever its manifest declares" to a specific subset of capabilities, paths, or domains the operator can defend. The output is a JSON patch against `~/.claude/settings.json` (RFC 6902) that the operator applies by hand. The proposal includes a re-evaluation date so the component earns trust by observation rather than by manifest.

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Attribution
to Plutarch TX appreciated when republishing.
