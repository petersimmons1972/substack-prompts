# Prompt 2 — Dry-Run Reference

**Run on:** 2026-05-05 (Opus 4.7, 1M context)
**Environment:** Linux 6.18.7, bash 5.x, Claude Code session
**Status:** All 8 steps produced output. Undo verified clean. No live memory file read or modified.

---

## Inputs

Five generic preferences as written into `00-preferences.md`. No real memory file was read; both compared files are synthetic constructions in scratch.

## 03-counts.md

| filename | words | bytes | tokens (cl100k_base) |
|---|---|---|---|
| 01-verbose-CLAUDE.md | 742 | 4,510 | 996 |
| 02-terse-CLAUDE.md | 64 | 408 | 92 |

Verbose-to-terse ratio: **10.83x** for the same five preferences.

## 04-cumulative.md

| version | 1 turn | 5 turns | 10 turns | 20 turns | delta @20 |
|---|---|---|---|---|---|
| verbose | 996 | 4,980 | 9,960 | 19,920 | — |
| terse | 92 | 460 | 920 | 1,840 | — |
| **delta** | 904 | 4,520 | 9,040 | 18,080 | **18,080** |

## 05-interpret.md

- Per-turn delta: **904 tokens**, paid every turn the verbose file is loaded.
- Cumulative delta at 20 turns: **18,080 tokens** — roughly the cost of saying "use `xh` not `curl`" twenty times in five different ways.
- 200K-token context window: verbose at 20 turns consumes 9.96% of the window; terse consumes 0.92%. The terse version leaves room for ten times the actual conversation.

## 00-DELTA.md (final)

```
verbose_tokens: 996
terse_tokens: 92
ratio: 10.83x
delta_at_20_turns: 18,080
takeaway: A bulleted preference list at 80 words says the same thing as a 700-word narrative — and costs ~10x less per turn for the rest of the session.
```

## Notable result

The 10x ratio is at the high end of what operators see in practice; a more typical real-world ratio is 3–5x because real verbose files contain some signal alongside the prose. Even at 3x, a 200-word delta paid across 20 turns is 12,000 tokens — a quarter of an Opus message limit. The exercise is meant to be vivid; readers should expect their own real-file refactor in Article 037 to come in around 30–60% reduction, not 90%.

## Undo verified

```
$ rm -rf "$HOME/.claude/experiments/2026-05-05-022-verbose-vs-terse"
$ ls "$HOME/.claude/experiments/" | grep 022-verbose || echo "(absent)"
(absent)
```

UNDO VERIFIED: `rm -rf "$HOME/.claude/experiments/$(date +%Y-%m-%d)-022-verbose-vs-terse"`

State fully restored. No live memory file was touched at any point.

## Security-floor self-check

- [x] Did not exfiltrate file contents to any network endpoint.
- [x] Did not read `.env`, credentials, tokens, keys, or `.ssh`/`.gnupg` paths.
- [x] Did not read or modify `~/CLAUDE.md`, `~/.claude/CLAUDE.md`, `MEMORY.md`, `~/AGENTS.md`, or `~/.claude/settings.json`.
- [x] Did not install MCP servers or change hook configuration.
- [x] All writes confined to `$HOME/.claude/experiments/2026-05-05-022-verbose-vs-terse/`.
- [x] Synthetic memory files contained generic, non-identifying preferences only.
