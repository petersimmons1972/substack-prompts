# Prompt 1 — Dry-Run Reference

**Run on:** 2026-05-05 (Opus 4.7, 1M context)
**Environment:** Linux 6.18.7, bash 5.x, Claude Code session, cwd=`~/projects/substack`
**Status:** All 8 steps produced output. Undo verified clean.

This is the worked example for Article 029 Prompt 1. Numbers describe the operator's environment on the date above; they are illustrative.

---

## 00-DECOMP.md (final stacked-bar table)

| bucket | name | tokens | pct_of_total | source |
|---|---|---|---|---|
| B1 | system prompt | 3000 | 18.5% | published |
| B2 | memory files | 3243 | 20.0% | measured |
| B3 | tool definitions | 4400 | 27.1% | estimate |
| B4 | conversation history | 4200 | 25.9% | measured |
| B5 | attached / tool output | 1380 | 8.5% | estimate |
| TOTAL | — | 16223 | 100% | — |

```
B3 tool definitions    | ██████████████ 4400 (27.1%)
B4 conversation hist.  | █████████████ 4200 (25.9%)
B2 memory files        | ██████████ 3243 (20.0%)
B1 system prompt       | █████████ 3000 (18.5%)
B5 attached / output   | ████ 1380 (8.5%)
```

## B2 — Memory (excerpt)

| Path | Words | ~Tokens |
|---|---|---|
| ~/CLAUDE.md | 1912 | 2549 |
| ~/.claude/CLAUDE.md | (absent) | 0 |
| MEMORY.md | 236 | 314 |
| ~/AGENTS.md | 285 | 380 |

Total memory bucket: **3243** tokens.

## B3 — Tools (excerpt)

11 enabled MCP servers detected in `~/.claude/settings.json` (`engram`, `postgres`, `github`, `Ref`, `claude_ai_Gmail`, `claude_ai_Google_Calendar`, plus 5 others). Estimate: 11 × 400 = **4400 tokens**. Marked `source=estimate` — true count requires per-server tool listing which the prompt does not retrieve.

## B4 — History

Picked the most recent transcript snippet (last 50 turns of the active session). Word count: 3150. Estimated tokens: **4200**.

## B5 — Attached / tool output

Last five turns averaged 276 tokens of tool output per turn × 5 = **1380 tokens** working figure.

## Notable result

The largest bucket is **B3 tool definitions at 27.1%**. This is the bucket most readers cannot see — there is no surface UI that shows it. Memory files (the bucket most articles focus on) are only 20% in this environment. The decomposition reframes the optimization target: pruning memory files saves less than disabling two unused MCP servers.

## Undo verified

```
$ rm -rf "$HOME/.claude/experiments/2026-05-05-029-token-decomp"
$ ls "$HOME/.claude/experiments/" | grep 029
(empty)
```

UNDO VERIFIED: `rm -rf "$HOME/.claude/experiments/$(date +%Y-%m-%d)-029-token-decomp"`

State fully restored. No file outside the scratch directory was modified.

## Security-floor self-check

- [x] Did not exfiltrate file contents to any network endpoint.
- [x] Did not read `.env`, credentials, tokens, keys, or `.ssh`/`.gnupg` paths.
- [x] Did not modify `~/.claude/settings.json` (read-only via `jq`).
- [x] Did not modify `~/CLAUDE.md`, `~/.claude/CLAUDE.md`, `MEMORY.md`, or `~/AGENTS.md`.
- [x] Did not install MCP servers or change hook configuration.
- [x] All writes confined to `$HOME/.claude/experiments/2026-05-05-029-token-decomp/`.
- [x] Memory file contents not echoed — names, sizes, and word counts only.
