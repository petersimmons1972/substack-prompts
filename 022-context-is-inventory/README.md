# Context is inventory, not magic

Prompts referenced in [Plutarch TX](https://plutarchtx.substack.com) article **022-context-is-inventory**.

→ **Read the article:** <https://plutarchtx.substack.com/p/context-is-inventory>

## How to use

Each `prompt-N.md` file is the prompt itself, with the teaching wrapper
stripped. Open the file, copy the contents, paste into Claude / ChatGPT /
your model of choice. The article (linked above) explains what the prompt
does and what to expect when you run it.

## Prompts in this article

### [`prompt-1.md`](./prompt-1.md) — Inventory Prompt — Bucket Your Session by Where the Tokens Went

Takes a real session export and bins every segment into one of five inventory buckets — `system_prompt`, `memory_files`, `tool_definitions`, `conversation_history`, `current_turn` — then renders a stacked-bar markdown chart of where the tokens actually went. Where Article 021 Prompt 2 labeled segments by *vocabulary*, this prompt aggregates them by *budget category* so you can see the shape of your spend. The operator leaves with one chart they can stick on the wall.

### [`prompt-2.md`](./prompt-2.md) — Inventory Prompt — Verbose vs Terse Memory File Cost

Constructs two synthetic memory files in scratch — one verbose, one terse — that express the same five operator preferences, then computes the per-turn token cost of each over a simulated 20-turn session. The output is a side-by-side spend table that puts a number on the inventory metaphor: the verbose memory file costs N tokens per turn, multiplied by every turn for the rest of your life, while the terse version expresses the same intent for a fraction of the cost.

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Attribution
to Plutarch TX appreciated when republishing.
