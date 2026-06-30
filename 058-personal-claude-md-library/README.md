# The personal CLAUDE.md library

_Stop restating general rules in every project file — centralize them once and reference them everywhere_

Prompts referenced in [Plutarch TX](https://plutarchtx.substack.com) article **058-personal-claude-md-library**.

→ **Read the article:** <https://plutarchtx.substack.com/p/personal-claude-md-library>

## How to use

Each `prompt-N.md` file is the prompt itself, with the teaching wrapper
stripped. Open the file, copy the contents, paste into Claude / ChatGPT /
your model of choice. The article (linked above) explains what the prompt
does and what to expect when you run it.

## Prompts in this article

### [`prompt-1.md`](./prompt-1.md) — Library Inventory — Tag Every Memory Entry GENERAL or PROJECT-SPECIFIC

Inventories every entry across the operator's memory files (top-level `~/CLAUDE.md`, per-project `CLAUDE.md`s, `AGENTS.md`s, scoped MEMORY indices) and tags each entry as **GENERAL** (transferable across projects, belongs in a personal library) or **PROJECT-SPECIFIC** (belongs only in the project's repo). The output is a tagged inventory. Prompt 2 stages a personal library structure and a migration plan that does not break in-flight projects.

### [`prompt-2.md`](./prompt-2.md) — Library Structure + Migration Plan — Stage Without Breaking Projects

Stages a personal `CLAUDE.md` library structure in scratch and produces a per-project migration plan that does not break in-flight projects. The library is a small, versioned set of files (e.g., `library/01-defaults.md`, `library/02-tools.md`, `library/03-security.md`) holding the GENERAL entries from Prompt 1's tagging. Each project's memory file is rewritten as a thin shim that imports the library by reference and keeps only its PROJECT-SPECIFIC content. Migration happens project-by-project, with rollback paths per project.

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Attribution
to Plutarch TX appreciated when republishing.
