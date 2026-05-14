# Where your tokens actually go

Prompts referenced in [Plutarch TX](https://plutarchtx.substack.com) article **029-where-your-tokens-go**.

→ **Read the article:** <https://plutarchtx.substack.com/p/where-your-tokens-go>

## How to use

Each `prompt-N.md` file is the prompt itself, with the teaching wrapper
stripped. Open the file, copy the contents, paste into Claude / ChatGPT /
your model of choice. The article (linked above) explains what the prompt
does and what to expect when you run it.

## Prompts in this article

### [`prompt-1.md`](./prompt-1.md) — Token Decomposition Prompt — Where Your Tokens Actually Go

Decomposes one real session's token cost into named buckets — system prompt, memory files, tool definitions, conversation history, attached files, and tool output — then renders the result as a markdown stacked-bar table so you can see at a glance which bucket dominates. The point is not the absolute number; the point is the *shape*. Most readers discover one bucket they did not know existed eating 30%+ of every turn. The prompt does not modify any live file.

### [`prompt-2.md`](./prompt-2.md) — Token Reduction Plan Prompt — Shrink the Largest Bucket

Reads the bucket table from Prompt 1, picks the largest bucket where reduction is feasible, and produces a reversible plan to shrink it — backup, proposed change in scratch, single-line undo. The prompt does not apply the change. You review, decide, and apply manually with a tested rollback path in hand. If the largest bucket is one the reader cannot directly modify (e.g., the harness system prompt), the plan switches to the next-largest reducible bucket and explains why.

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Attribution
to Plutarch TX appreciated when republishing.
