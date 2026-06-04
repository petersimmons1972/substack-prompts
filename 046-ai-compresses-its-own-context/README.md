# Ask the AI to compress its own context

_Compression without review is the model rewriting its own contract — compression with review is the model proposing and you deciding_

Prompts referenced in [Plutarch TX](https://plutarchtx.substack.com) article **046-ai-compresses-its-own-context**.

→ **Read the article:** <https://plutarchtx.substack.com/p/ai-compresses-its-own-context>

## How to use

Each `prompt-N.md` file is the prompt itself, with the teaching wrapper
stripped. Open the file, copy the contents, paste into Claude / ChatGPT /
your model of choice. The article (linked above) explains what the prompt
does and what to expect when you run it.

## Prompts in this article

### [`prompt-1.md`](./prompt-1.md) — Compression Prompt — Same Rules, Fewer Tokens, Same Precedence

Asks the model to compress `~/CLAUDE.md` while preserving every rule and the precedence between them. The compressed file is staged in scratch — not applied. The discipline is: the model does the boring work of finding redundant phrasing, and the operator reviews the diff. Compression-without-review is the model quietly rewriting its own contract; compression-with-review is the model proposing a change that the human signs off on.

### [`prompt-2.md`](./prompt-2.md) — Compression Diff Review — SAFE / RISKY / BLOCKING-REJECT

Reviews each removed line in the compression diff and tags it as **SAFE** (truly redundant — the rule survives elsewhere), **RISKY** (the rule survives but in a weakened form — re-read before applying), or **BLOCKING-REJECT** (the rule was lost or its precedence inverted; the patch must not be applied as-is). The output is a per-line review ledger plus a go/no-go recommendation for the patch overall. The operator reads the BLOCKING rows by hand and either fixes them in the compressed draft or rejects the patch.

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Attribution
to Plutarch TX appreciated when republishing.
