# Lifecycle: create, split, retire

Prompts referenced in [Plutarch TX](https://plutarchtx.substack.com) article **043-memory-file-lifecycle**.

→ **Read the article:** <https://plutarchtx.substack.com/p/memory-file-lifecycle>

_Published: 2026-05-27_

## How to use

Each `prompt-N.md` file is the prompt itself, with the teaching wrapper
stripped. Open the file, copy the contents, paste into Claude / ChatGPT /
your model of choice. The article (linked above) explains what the prompt
does and what to expect when you run it.

## Prompts in this article

### [`prompt-1.md`](./prompt-1.md) — Memory Lifecycle — Stage-Tag Every Memory File

Tags every memory file in the operator's environment with a lifecycle stage — `emerge`, `stabilize`, `bloat`, or `retire-candidate` — based on three signals: line count, repeat-conflict rate, and last-referenced date. Memory files do not announce when they have outgrown their usefulness; they just keep accumulating until the model spends most of its context budget reading them. Stage-tagging surfaces the ones that need attention before they become a problem. The prompt does not modify any file; it produces a labeled inventory.

### [`prompt-2.md`](./prompt-2.md) — Memory Lifecycle — Reversible Split-or-Retire Plan

Picks one bloated memory file from Prompt 1's report and produces a split-or-retire plan. For a split, the file is partitioned into two or three coherent successors with explicit precedence preserved. For a retirement, the file is archived to scratch with a one-line summary of what to keep and what to discard. The plan is staged in scratch as a unified diff and a sidecar archive; the operator applies it by hand. The retirement procedure deliberately preserves history — useful past entries are quoted in the archive, and the live file is replaced with a stub pointing at the archive path.

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Attribution
to Plutarch TX appreciated when republishing.
