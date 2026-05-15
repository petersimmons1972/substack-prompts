# Built-in instruments on each surface

Prompts referenced in [Plutarch TX](https://plutarchtx.substack.com) article **031-built-in-instruments**.

→ **Read the article:** <https://plutarchtx.substack.com/p/built-in-instruments>

## How to use

Each `prompt-N.md` file is the prompt itself, with the teaching wrapper
stripped. Open the file, copy the contents, paste into Claude / ChatGPT /
your model of choice. The article (linked above) explains what the prompt
does and what to expect when you run it.

## Prompts in this article

### [`prompt-1.md`](./prompt-1.md) — Built-in Instruments Prompt — Enumerate and Run

Enumerates the built-in instruments your primary surface ships with — status lines, slash commands, conversation export, usage panels, hook-emitted state files — and runs each at least once, capturing its output to scratch. The result is a single index of *what your surface tells you about itself*. Most operators have never run the full set; the unrun instruments are usually where the cheapest wins live (you cannot optimize what you cannot measure).

### [`prompt-2.md`](./prompt-2.md) — Built-in Instruments Prompt — Single-Command Status Aggregator

Reads the instrument index from Prompt 1 and produces a single bash script — staged in scratch — that aggregates the most useful subset into one status reading. You run the script when you want a fast snapshot: cost-shape, context-shape, security-surface, health. The script is read-only, has its own undo (delete the file), and lives outside any auto-loaded path until you decide to install it. The prompt does not modify your shell rc, your bin directory, or any settings file.

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Attribution
to Plutarch TX appreciated when republishing.
