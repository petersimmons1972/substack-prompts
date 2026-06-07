# Memory files as a team contract

_The rules that were personal constraints become team norms the moment a second person opens the repository_

Prompts referenced in [Plutarch TX](https://plutarchtx.substack.com) article **049-memory-files-as-team-contract**.

→ **Read the article:** <https://plutarchtx.substack.com/p/memory-files-as-team-contract>

## How to use

Each `prompt-N.md` file is the prompt itself, with the teaching wrapper
stripped. Open the file, copy the contents, paste into Claude / ChatGPT /
your model of choice. The article (linked above) explains what the prompt
does and what to expect when you run it.

## Prompts in this article

### [`prompt-1.md`](./prompt-1.md) — Team-Contract Audit — Find Personal-Preference Contamination

Audits a team-shared `CLAUDE.md` or `AGENTS.md` for personal-preference contamination — rules that read as "this is how I, the original author, like to work" rather than "this is how the team has agreed to work." Personal-preference rules are not wrong on their own; they are wrong as team contract because they shift the cost of disagreement onto whoever joins next. The prompt does not modify the file. Prompt 2 produces a contributor guideline that codifies how new rules earn their place.

### [`prompt-2.md`](./prompt-2.md) — Team-Contract Audit — Produce a Contributor-Guideline Document

Reads the contamination report from Prompt 1 and produces a contributor-guideline document — `MEMORY-CONTRIBUTING.md` — that codifies how new rules earn their place in the shared memory file. The document is modeled after the team's existing PR norms (the operator points at one or two example PRs from the team's history). The output is staged in scratch; the operator merges it into the team repo by hand. The discipline this prompt is selling: shared memory files deserve the same review process as code, not a different and quieter one.

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Attribution
to Plutarch TX appreciated when republishing.
