# Prompt 1 — Dry-Run Reference

**Run on:** 2026-05-05 (Opus 4.7, 1M context)
**Environment:** Linux 6.18.7, bash 5.x, Claude Code session
**Status:** All 6 steps produced output. Undo verified clean.

---

## Inputs

`~/.claude/projects/-home-psimmons/` contained 17 transcript files modified in the last 14 days, totaling ~24 MB. Top-20 listing produced; sampled 50 assistant turns from the newest 8 files.

## 03-classified.md (excerpt)

| idx | task_class | model | ~tokens |
|---|---|---|---|
| 12 | classification | unknown | 84 |
| 13 | debugging | unknown | 1,210 |
| 14 | formatting | unknown | 116 |
| 17 | architecture | unknown | 2,440 |
| 19 | mechanical_transform | unknown | 92 |
| 21 | bulk_judge | unknown | 380 |
| 22 | generation | unknown | 1,890 |
| 24 | health_check | unknown | 38 |

(50 rows total; truncated for the dry-run.)

## 04-overspends.md

12 of 50 sampled turns (24%) flagged as overspends:

| task_class | count | total_tokens | recommended_tier |
|---|---|---|---|
| formatting | 4 | 488 | Haiku |
| classification | 3 | 252 | Haiku |
| mechanical_transform | 2 | 184 | Haiku |
| bulk_judge | 2 | 660 | Haiku |
| health_check | 1 | 38 | Haiku |

Total flagged tokens: **1,622**.

Reasoning-heavy turns (debugging: 9, architecture: 4, generation: 7, multi_file_edit: 6, unclassified: 12) were correctly not flagged.

## 00-OVERSPEND.md

```
turns_sampled: 50
turns_flagged: 12
pct_flagged: 24%
flagged_tokens: 1,622
top_class: formatting (4 turns, 488 tokens)
```

## Notable result

24% flagged is at the upper edge of the expected 5–30% band. The most-frequent overspend class — `formatting` — is the textbook Haiku case (reformat JSON, clean up markdown), and is exactly what Anthropic's pricing guidance points at as the right Haiku use case. The classifier did not flag any debugging or architecture turn even when previews looked superficially routine, because those classes are explicitly excluded by Step 5's allow-list.

The M0 flag did not fire — operator had abundant local Claude Code history. A first-time reader running this against ChatGPT alone will likely hit M0 and be routed to Article 031.

## Undo verified

```
$ rm -rf "$HOME/.claude/experiments/2026-05-05-024-model-overspend"
$ ls "$HOME/.claude/experiments/" | grep 024-model || echo "(absent)"
(absent)
```

UNDO VERIFIED: `rm -rf "$HOME/.claude/experiments/$(date +%Y-%m-%d)-024-model-overspend"`

State fully restored. Transcripts were read but not modified.

## Security-floor self-check

- [x] Did not exfiltrate file contents to any network endpoint.
- [x] Did not read `.env`, credentials, tokens, keys, or `.ssh`/`.gnupg` paths.
- [x] Did not modify `~/.claude/settings.json`, `~/CLAUDE.md`, `~/.claude/CLAUDE.md`, `MEMORY.md`, or `~/AGENTS.md`.
- [x] Did not install MCP servers or change hook configuration.
- [x] All writes confined to `$HOME/.claude/experiments/2026-05-05-024-model-overspend/`.
- [x] Previews truncated to 100 chars; no full assistant or user turn bodies copied.
