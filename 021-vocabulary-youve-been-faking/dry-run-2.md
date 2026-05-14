# Prompt 2 — Dry-Run Reference

**Run on:** 2026-05-05 (Opus 4.7, 1M context)
**Environment:** Linux 6.18.7, bash 5.x, Claude Code session
**Status:** All 6 steps produced output. Undo verified clean.

Worked example for Article 021 Prompt 2. The operator supplied a Claude Code transcript file from `~/.claude/projects/-home-psimmons/`; sizes and counts are illustrative.

---

## Inputs

Export source: `~/.claude/projects/-home-psimmons/<session-id>.jsonl` — a 47-segment Claude Code conversation totaling ~31,400 estimated tokens. Operator authorized read access; the file did not match any forbidden pattern.

## 02-labeled.md (excerpt — first 8 of 47 rows)

| idx | label | bytes | ~tokens | preview |
|---|---|---|---|---|
| 0 | system_prompt | 4112 | 1028 | "You are Claude, an AI assistant…" |
| 1 | memory_injection | 8430 | 2108 | "# Claude Assistant Instructions…" |
| 2 | memory_injection | 1820 | 455 | "# Learning Index — Last Updated…" |
| 3 | user_turn | 312 | 78 | "Help me draft a commit message for…" |
| 4 | assistant_turn | 1190 | 298 | "I'll start by looking at the staged…" |
| 5 | tool_call | 88 | 22 | "Bash(git diff --staged)" |
| 6 | tool_result | 6044 | 1511 | "diff --git a/foo.py…" |
| 7 | assistant_turn | 740 | 185 | "Here's a proposed commit message…" |

## 03-inventory.md

| label | count | total_tokens | pct |
|---|---|---|---|
| tool_result | 12 | 14,880 | 47.4% |
| memory_injection | 3 | 6,210 | 19.8% |
| assistant_turn | 14 | 4,920 | 15.7% |
| system_prompt | 1 | 1,028 | 3.3% |
| tool_call | 12 | 410 | 1.3% |
| user_turn | 5 | 380 | 1.2% |
| (overhead/other) | — | 3,572 | 11.4% |

## 04-surprises.md

1. Tool results were 47% of the conversation — almost half the token budget went to text the model read but the operator never did.
2. Memory injection (CLAUDE.md + MEMORY.md + AGENTS.md) was 20% — larger than every assistant turn combined.
3. User turns were 1.2% of the total. The operator's typing was a rounding error compared to context the model carried into every turn.

## 00-LABELS.md (final)

```
export_source: ~/.claude/projects/-home-psimmons/<session-id>.jsonl
segment_count: 47
total_tokens_est: 31,400
top_label: tool_result (47.4%)
under_estimated: memory_injection — operator expected ~5%, actual 19.8%.
```

## Notable result

The tool_result share (47%) is the kind of finding the operator could not get from documentation alone. It also previews Article 029's deeper decomposition. The L0 flag was not raised — the operator did know how to find their Claude Code transcripts. A first-time reader of the series running this prompt against ChatGPT would likely hit L0 and get pointed forward to Article 031.

## Undo verified

```
$ rm -rf "$HOME/.claude/experiments/2026-05-05-021-label"
$ ls "$HOME/.claude/experiments/" | grep 021-label || echo "(absent)"
(absent)
```

UNDO VERIFIED: `rm -rf "$HOME/.claude/experiments/$(date +%Y-%m-%d)-021-label"`

State fully restored. The transcript file was read but not modified.

## Security-floor self-check

- [x] Did not exfiltrate file contents to any network endpoint.
- [x] Did not read `.env`, credentials, tokens, keys, or `.ssh`/`.gnupg` paths.
- [x] Did not modify `~/.claude/settings.json`, `~/CLAUDE.md`, `~/.claude/CLAUDE.md`, `MEMORY.md`, or `~/AGENTS.md`.
- [x] Did not install MCP servers or change hook configuration.
- [x] All writes confined to `$HOME/.claude/experiments/2026-05-05-021-label/`.
- [x] Transcript previews truncated to 60 chars; no full segment bodies copied for any segment >200 bytes.
- [x] No tokens, secrets, paths, or PII reproduced from the transcript into scratch.
