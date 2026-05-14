# Prompt 2 — Dry-Run Reference

**Run on:** 2026-05-05 (Opus 4.7, 1M context)
**Environment:** Linux 6.18.7, bash 5.x, Claude Code session, cwd=`~/projects/substack`
**Status:** All 6 steps produced output. Backup verified. Undo script verified idempotent.

This is the worked example for Article 029 Prompt 2. It consumes Prompt 1's `00-DECOMP.md` and stages a reduction plan for the largest reducible bucket.

---

## Inputs

Largest bucket from Prompt 1: **B3 tool definitions** at 4400 tokens (27.1%). Reducible. Target: `~/.claude/settings.json` enabled-server list.

## 21-backup-verified.md

```
- live: ~/.claude/settings.json (8117 bytes)
- backup: $SCRATCH/backup-20260505-184501-settings.json (8117 bytes)
- match: OK
```

## 23-diff.md (excerpt)

Enabled MCP servers (11): `engram`, `postgres`, `github`, `Ref`, `claude_ai_Gmail`, `claude_ai_Google_Calendar`, `firecrawl`, `playwright`, `filesystem`, `searxng`, `brave-search`.

Operator self-named active set: `engram`, `postgres`, `github`, `Ref`, `claude_ai_Gmail`. Inactive: `playwright`, `brave-search` (SearxNG covers search; playwright unused this quarter).

Proposed disable: `playwright`, `brave-search`. Estimated delta: 2 × 400 = **–800 tokens** (~–18% of the bucket, ~–4.9% of total).

## 20-PLAN.md (final)

- Target: `~/.claude/settings.json` `enabledMcpjsonServers` array.
- Bucket: B3 — tool definitions.
- Change: remove `playwright` and `brave-search` from enabled servers.
- Apply: human edits `~/.claude/settings.json` after reviewing `23-diff.md`. Single key change.
- Undo: `bash $SCRATCH/24-undo.sh` (restores from byte-identical backup).
- Expected delta on next Prompt 1 run: B3 drops from 4400 → ~3600 tokens. Total drops ~5%.

## Notable result

Prompt 2 staged a backup, produced a tightening proposal, and emitted a single-command undo script — all without touching the live file. Most reduction guidance focuses on memory files (B2) because they are the most visible. In this environment, two unused MCP servers represent more saving than pruning a quarter of `~/CLAUDE.md`. The decomposition lens — not advice — is what produces the right target.

## Undo verified

**File-restore undo (`24-undo.sh`):**

```
$ bash $SCRATCH/24-undo.sh
restored ~/.claude/settings.json from $SCRATCH/backup-...
```

UNDO VERIFIED: `cp -p "$SCRATCH/backup-<TS>-settings.json" "$HOME/.claude/settings.json"` — md5 unchanged before and after.

**Scratch teardown undo:**

```
$ rm -rf "$HOME/.claude/experiments/2026-05-05-029-token-decomp"
$ ls "$HOME/.claude/experiments/" | grep 029
(empty)
```

UNDO VERIFIED: `rm -rf "$HOME/.claude/experiments/$(date +%Y-%m-%d)-029-token-decomp"`

State fully restored. Live `~/.claude/settings.json` md5 unchanged across the entire dry-run.

## Security-floor self-check

- [x] Did not exfiltrate file contents to any network endpoint.
- [x] Did not read `.env`, credentials, tokens, keys, or `.ssh`/`.gnupg` paths.
- [x] Did not modify the live `~/.claude/settings.json` (read via `jq`; backup via `cp -p`; staging proposal written to scratch).
- [x] Did not modify `~/CLAUDE.md`, `~/.claude/CLAUDE.md`, `MEMORY.md`, or `~/AGENTS.md`.
- [x] Did not install MCP servers or change hook configuration.
- [x] All writes confined to `$HOME/.claude/experiments/2026-05-05-029-token-decomp/`.
- [x] MCP server names echoed to scratch; no tokens, paths, or secrets reproduced.
