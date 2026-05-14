# Conversation lifecycle and context decay

Prompts referenced in [Plutarch TX](https://plutarchtx.substack.com) article **030-conversation-lifecycle**.

→ **Read the article:** <https://plutarchtx.substack.com/p/conversation-lifecycle>

## How to use

Each `prompt-N.md` file is the prompt itself, with the teaching wrapper
stripped. Open the file, copy the contents, paste into Claude / ChatGPT /
your model of choice. The article (linked above) explains what the prompt
does and what to expect when you run it.

## Prompts in this article

### [`prompt-1.md`](./prompt-1.md) — Conversation Lifecycle Prompt — Relevance-by-Turn and Restart Point

Inspects one long ongoing conversation (or the last available transcript), estimates per-turn relevance to the *current* working topic, and marks the optimal restart point — the turn after which a fresh conversation with a short carry-forward summary would yield equal or better quality at a fraction of the context cost. The output is a relevance-by-turn table and a single recommended restart turn number. The prompt does not modify any conversation, transcript, or memory file.

### [`prompt-2.md`](./prompt-2.md) — Conversation Lifecycle Prompt — Forward Handoff Document

Generates a forward-handoff document for one ongoing conversation — a 250–600 word artifact you paste as the first message of a fresh session to carry forward only what matters: current goal, decisions made, files touched, open questions, and explicit non-goals. The handoff is written to scratch only. You read it, edit if needed, and start a new conversation with it. The current conversation is never closed by the prompt; you decide whether to keep it or end it.

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Attribution
to Plutarch TX appreciated when republishing.
