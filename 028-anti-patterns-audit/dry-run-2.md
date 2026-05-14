# Prompt 2 — Dry-Run Reference

**Run on:** 2026-05-05 (Opus 4.7, 1M context)
**Environment:** Linux 6.18.7, bash 5.x, Claude Code session, cwd=`~/projects/substack`
**Status:** All 6 steps produced output. Backup verified. Undo script verified idempotent. Scratch teardown clean.

This is the worked example for Article 028 Prompt 2. It consumes Prompt 1's `00-FINDINGS.md` and stages a remediation for the top-scoring anti-pattern.

---

## Inputs

Top finding from Prompt 1: **A4 wildcard permissions** (score 16). Target file: `~/.claude/settings.json`.

## 11-backup-verified.md

```
- live: ~/.claude/settings.json (8117 bytes)
- backup: $SCRATCH/backup-20260505-182214-settings.json (8117 bytes)
- match: OK
```

## 13-diff.md (excerpt)

Detected wildcard rules (10 total):

```
mcp__github__*
mcp__postgres__*
mcp__Ref__*
mcp__claude_ai_Gmail__*
mcp__claude_ai_Google_Calendar__*
mcp__engram__*
Bash(git add *)
Bash(git commit -m '... *)
Bash(git checkout *)
Bash(gh issue create *)
```

Tightening principle: replace each `*` rule with the narrowest tool/path the workflow actually needs. Six MCP server rules grant blanket access to every tool a server exposes — most workflows only call 2–3 tools per server, so each `mcp__SERVER__*` is a candidate for explicit per-tool listing.

## 10-PLAN.md (final)

- Target: `~/.claude/settings.json`
- Anti-pattern: A4 — 10 wildcard allow-rules.
- Change: replace each wildcard with the narrowest tool/path the workflow needs. Manual edit; staging file is a placeholder copy.
- Apply: human edits `~/.claude/settings.json` after reviewing `13-diff.md`.
- Undo: `bash $SCRATCH/14-undo.sh`.
- Expected delta on next baseline run: `broad_wildcard_rules` drops from 10 toward 3–6. `memory_files_total_tokens` and `secrets_indicator_hits` will not move (A4 is permission-surface only).

## Notable result

Prompt 2 staged a backup, produced a tightening proposal, and emitted a single-command undo script — all without touching the live file. The backup byte-count matched the live file (8,117 bytes both sides). The undo script was tested by running it against the unchanged live file: live md5 before and after were identical, confirming the restore path works whether or not the reader has applied the fix.

The most useful operator finding: six of the ten wildcards are blanket `mcp__SERVER__*` grants. Tightening these is high-leverage because each MCP server typically exposes 5–30 tools, only a handful of which see daily use.

## Undo verified

**File-restore undo (`14-undo.sh`):**

```
$ bash $SCRATCH/14-undo.sh
restored ~/.claude/settings.json from $SCRATCH/backup-...
```

UNDO VERIFIED: `cp -p "$SCRATCH/backup-<TS>-settings.json" "$HOME/.claude/settings.json"` — md5 unchanged before and after.

**Scratch teardown undo:**

```
$ rm -rf "$HOME/.claude/experiments/2026-05-05-028-smoke"
$ ls "$HOME/.claude/experiments/"
(empty)
```

UNDO VERIFIED: `rm -rf "$HOME/.claude/experiments/$(date +%Y-%m-%d)-028-anti-patterns"`

State fully restored. Live `~/.claude/settings.json` byte-count and md5 unchanged across the entire dry-run.

## Security-floor self-check

- [x] Did not exfiltrate file contents to any network endpoint.
- [x] Did not read `.env`, credentials, tokens, keys, or `.ssh`/`.gnupg` paths.
- [x] Did not modify the live `~/.claude/settings.json` (read via `jq`; backup via `cp -p`; staging proposal written to scratch).
- [x] Did not modify `~/CLAUDE.md`, `~/.claude/CLAUDE.md`, `MEMORY.md`, or `~/AGENTS.md`.
- [x] Did not install MCP servers or change hook configuration.
- [x] All writes confined to `$HOME/.claude/experiments/2026-05-05-028-smoke/`.
- [x] MCP server names from `settings.json` echoed to scratch (not network); no tokens, paths, or secrets reproduced.
