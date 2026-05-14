# Prompt 1 — Dry-Run Reference

**Run on:** 2026-05-05 (Opus 4.7, 1M context)
**Environment:** Linux 6.18.7, bash 5.x, Claude Code session
**Status:** All 7 steps produced output. Undo verified clean.

Worked example for Article 022 Prompt 1. Numbers are illustrative and reflect the operator's environment on the date above.

---

## Inputs

Export source: same Claude Code transcript used in Article 021 dry-run-2 — a 47-segment session totaling ~31,400 estimated tokens. Operator authorized the read.

## 03-aggregate.md

| bucket | count | total_tokens | pct |
|---|---|---|---|
| conversation_history | 38 | 14,880 | 47.4% |
| memory_files | 3 | 6,210 | 19.8% |
| system_prompt | 1 | 1,028 | 3.3% |
| current_turn | 2 | 1,930 | 6.1% |
| tool_definitions | 1 | 840 | 2.7% |
| (overhead) | — | 6,512 | 20.7% |

## 04-stackbar.md

```
| HHHHHHHHHHHHHHHHHHHHHHHMMMMMMMMMM-----CCCSSTT---- |
H conversation_history 14,880 47.4%
M memory_files          6,210 19.8%
- overhead              6,512 20.7%
C current_turn          1,930  6.1%
S system_prompt         1,028  3.3%
T tool_definitions        840  2.7%
```

## 05-flag.md

Dominant bucket: `conversation_history` at 47.4%. Interpretation: this session ran long and accumulated tool results that the model carried into every subsequent turn. The fix is conversation-lifecycle discipline — the topic of Article 030. Secondary flag: `memory_files` at 19.8% is below the 25% threshold but worth watching; Article 037 covers refactoring.

## 00-INVENTORY.md (final)

```
export_source: ~/.claude/projects/-home-psimmons/<session-id>.jsonl
total_tokens_est: 31,400
dominant_bucket: conversation_history (47.4%)
interpretation: Long session with heavy tool results — start a fresh conversation sooner. See Article 030.
```

## Notable result

Two flags fired: a primary on `conversation_history` (>50% would have been blocking; 47.4% is a near-miss worth acting on) and a secondary on `memory_files`. The `tool_definitions` bucket is small (2.7%) only because Claude Code lazy-loads tools — on Claude Desktop with several MCP servers active, this number is often 10–20%, which would route the operator to Article 040.

## Undo verified

```
$ rm -rf "$HOME/.claude/experiments/2026-05-05-022-inventory"
$ ls "$HOME/.claude/experiments/" | grep 022-inventory || echo "(absent)"
(absent)
```

UNDO VERIFIED: `rm -rf "$HOME/.claude/experiments/$(date +%Y-%m-%d)-022-inventory"`

State fully restored. The transcript was read but not modified.

## Security-floor self-check

- [x] Did not exfiltrate file contents to any network endpoint.
- [x] Did not read `.env`, credentials, tokens, keys, or `.ssh`/`.gnupg` paths.
- [x] Did not modify `~/.claude/settings.json`, `~/CLAUDE.md`, `~/.claude/CLAUDE.md`, `MEMORY.md`, or `~/AGENTS.md`.
- [x] Did not install MCP servers or change hook configuration.
- [x] All writes confined to `$HOME/.claude/experiments/2026-05-05-022-inventory/`.
- [x] Bucket aggregation produced counts and percentages only — no segment bodies copied to scratch.
