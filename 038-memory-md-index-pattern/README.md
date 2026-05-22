# `MEMORY.md` and the index pattern

_Keep the index in context, the payload on disk — and stop paying per-session for facts the session doesn't need_

Prompts referenced in [Plutarch TX](https://plutarchtx.substack.com) article **038-memory-md-index-pattern**.

→ **Read the article:** <https://plutarchtx.substack.com/p/memory-md-index-pattern>

## How to use

Each `prompt-N.md` file is the prompt itself, with the teaching wrapper
stripped. Open the file, copy the contents, paste into Claude / ChatGPT /
your model of choice. The article (linked above) explains what the prompt
does and what to expect when you run it.

## Prompts in this article

### [`prompt-1.md`](./prompt-1.md) — `MEMORY.md` Index Audit — Classify Every Entry

Reads your `MEMORY.md` entry by entry and classifies each as **INDEX-WORTHY** (a short pointer or topic-name the model should hold in context) or **PAYLOAD** (a body of detail the model should fetch on demand instead of carrying every turn). Flags mismatches: payloads sitting in the index, indexes pointing to nothing, and bare topic names that should be expanded into pointer entries. The output is a classified copy plus a count table. The prompt does not modify any live file. Everything written goes inside a dated scratch directory you delete with one command. Prompt 2 consumes the classification to stage a restructured file.

### [`prompt-2.md`](./prompt-2.md) — `MEMORY.md` Index Restructure — Stage the Split

Reads the entry classification from Prompt 1 and stages a restructured `MEMORY.md` plus zero or more *payload files* in scratch. PAYLOAD entries get extracted into their own files under `$SCRATCH/payloads/`; the staged `MEMORY.md` keeps only INDEX-WORTHY pointers (one per surviving topic, pointing to the new payload file). Computes the token delta — both the in-context savings (the new `MEMORY.md` versus the old) and the on-disk total (no payload was deleted, only moved). The prompt does not touch the live `MEMORY.md` and creates no live payload files. You review, copy manually if you agree, and have an undo for both the file and the new payloads.

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Attribution
to Plutarch TX appreciated when republishing.
