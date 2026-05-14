# Which tool, when

Prompts referenced in [Plutarch TX](https://plutarchtx.substack.com) article **025-which-tool-when**.

→ **Read the article:** <https://plutarchtx.substack.com/p/which-tool-when>

## How to use

Each `prompt-N.md` file is the prompt itself, with the teaching wrapper
stripped. Open the file, copy the contents, paste into Claude / ChatGPT /
your model of choice. The article (linked above) explains what the prompt
does and what to expect when you run it.

## Prompts in this article

### [`prompt-1.md`](./prompt-1.md) — Surface Selection Prompt — Audit Your Last 10 Tasks

Reviews your last 10 substantial AI tasks and labels each with the surface that would have been the best fit — Claude Code, Claude Desktop, Claude.ai chat, ChatGPT, OpenAI Codex, the Anthropic API, or the OpenAI API. The labeling uses a fit rubric grounded in `docs/strategy/surface-matrix.md`: tasks needing filesystem access, multi-file edits, and shell tools fit Claude Code; one-shot reasoning with no file context fits chat; long-running scripted work fits the API. The output is a mismatch list — tasks you ran on the wrong surface — that Prompt 2 acts on.

### [`prompt-2.md`](./prompt-2.md) — Surface Selection Prompt — Replay on the Better-Fit Surface

Picks the highest-severity mismatch from Prompt 1, walks you through replaying that task on the recommended surface, and captures the turns/tokens delta side by side with the original. Where Prompt 1 audited, Prompt 2 produces evidence. The result is a single-row before/after comparison you can hold up next to the rubric: "this task ran in 14 turns on chat; on Claude Code it ran in 4."

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Attribution
to Plutarch TX appreciated when republishing.
