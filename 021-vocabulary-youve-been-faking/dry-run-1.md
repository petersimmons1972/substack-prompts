# Prompt 1 — Dry-Run Reference

**Run on:** 2026-05-05 (Opus 4.7, 1M context)
**Environment:** Linux 6.18.7, bash 5.x, Claude Code session, cwd=`~/projects/substack`
**Status:** All 6 steps produced output. Undo verified clean.

This is the worked example for Article 021 Prompt 1. Numbers describe the operator's environment on the date above; they are illustrative.

---

## Inputs

Paragraph chosen: a 142-word paragraph from `~/projects/substack/docs/strategy/series-ai-optimization-brief.md`, the "Thesis" section. The operator pasted it directly rather than providing a path.

## 02-counts.md (excerpt)

```
bytes:       908
characters:  907
words:       142
sentences:   5
```

## 03-tokens.md

| Method | Token estimate |
|---|---|
| `ceil(words / 0.75)` | 190 |
| `ceil(characters / 4)` | 227 |
| `tiktoken cl100k_base` | 198 |

Spread: 190–227 (~19% range). The two heuristics bracket the exact count; the words/0.75 ratio is the closest. Recommended mnemonic: **a paragraph of my prose costs roughly 1.4 tokens per word once formatting and punctuation are included.**

## 04-shapes.md (excerpt)

| Shape | Tokens | Ratio vs source |
|---|---|---|
| Source prose | 198 | 1.00x |
| As JSON (one key per sentence) | 264 | 1.33x |
| As Python comment block | 219 | 1.11x |
| First sentence in Mandarin | 41 (vs 38 English) | 1.08x |

The JSON wrapping cost a third more tokens for the same content. The Python comment prefix added ~10%. Mandarin came in nearly 1:1 because `cl100k_base` allocates substantial dedicated vocabulary for common CJK characters; older tokenizers would balloon this number 3–5x.

## 00-VOCAB.md (final)

```
source_words: 142
source_tokens: 198
bytes_per_token: 4.59
words_per_token: 0.717
takeaway: a paragraph of my prose costs roughly 200 tokens — about 1.4 tokens per word.
```

## Notable result

The exact tiktoken count (198) landed within 4% of the words/0.75 heuristic (190) and 13% below the chars/4 heuristic (227). For operators without `tiktoken` installed, the words/0.75 ratio is the better default. The JSON shape's 33% surcharge is a useful warning for Article 022's discussion of "structure tax."

## Undo verified

```
$ rm -rf "$HOME/.claude/experiments/2026-05-05-021-vocabulary"
$ ls "$HOME/.claude/experiments/" | grep 021-vocabulary || echo "(absent)"
(absent)
```

UNDO VERIFIED: `rm -rf "$HOME/.claude/experiments/$(date +%Y-%m-%d)-021-vocabulary"`

State fully restored. No file outside the scratch directory was modified.

## Security-floor self-check

- [x] Did not exfiltrate file contents to any network endpoint.
- [x] Did not read `.env`, credentials, tokens, keys, or `.ssh`/`.gnupg` paths.
- [x] Did not modify `~/.claude/settings.json`.
- [x] Did not modify `~/CLAUDE.md`, `~/.claude/CLAUDE.md`, `MEMORY.md`, or `~/AGENTS.md`.
- [x] Did not install MCP servers or change hook configuration.
- [x] All writes confined to `$HOME/.claude/experiments/2026-05-05-021-vocabulary/`.
- [x] Source paragraph was operator-supplied; no unauthorized file reads occurred.
