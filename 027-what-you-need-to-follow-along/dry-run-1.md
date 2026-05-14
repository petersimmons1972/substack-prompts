# Prompt 1 — Dry-Run Reference

**Run on:** 2026-05-05 (Opus 4.7, 1M context)
**Environment:** Linux 6.18.7, bash 5.x, Claude Code session
**Status:** All 8 steps produced output. Backup, modify, and restore cycle verified. Undo verified clean.

---

## 01-environment.md

```
GNU bash, version 5.2.21(1)-release
git version 2.43.0
claude-code version 2.x.x
Linux 6.18.7
```

All required tools present. No blockers.

## 03-pre-state.md

```
bytes: 247
md5:   3c5a...7e2f
```

## 04-backup-verified.md

```
- live: $SCRATCH/02-test-artifact.md (247 bytes)
- backup: $SCRATCH/02-test-artifact.md.bak-20260505-184412 (247 bytes)
- match: OK
```

## 05-post-state.md (after modification)

```
bytes: 280
md5:   8b91...4c0d   (differs from pre-state — confirmed)
```

## 06-restored.md

```
bytes: 247
md5:   3c5a...7e2f   (matches pre-state — restore confirmed)
```

## 00-FOLLOWALONG.md (final)

```
bash: 5.2.21
git: 2.43.0
claude-code: present
scratch: /home/<user>/.claude/experiments/2026-05-05-027-followalong
backup_byte_match: Y
restored_md5_match: Y
verdict: READY
```

## Notable result

The cycle ran end-to-end without intervention: pre-state captured, backup taken, modification applied, post-state distinct, restore returned md5 to pre-state. This is the canonical motion every later article assumes. The exercise took ~30 seconds of actual work and produced a verifiable record. Operators with missing `git` would be told to install before continuing; operators without Claude Code would be told the rest of the series is mostly accessible but a handful of Claude-Code-primary prompts will be skipped.

The restore step (Step 6) is what most operators have never explicitly practiced — they back up reflexively but rarely verify the restore actually works until the day they need it. Practicing on a throwaway file is exactly the right context.

## Undo verified

```
$ rm -rf "$HOME/.claude/experiments/2026-05-05-027-followalong"
$ ls "$HOME/.claude/experiments/" | grep 027-followalong || echo "(absent)"
(absent)
```

UNDO VERIFIED: `rm -rf "$HOME/.claude/experiments/$(date +%Y-%m-%d)-027-followalong"`

## Security-floor self-check

- [x] Did not exfiltrate file contents to any network endpoint.
- [x] Did not read `.env`, credentials, tokens, keys, or `.ssh`/`.gnupg` paths.
- [x] Did not modify `~/.claude/settings.json`, `~/CLAUDE.md`, `~/.claude/CLAUDE.md`, `MEMORY.md`, or `~/AGENTS.md`.
- [x] Did not install MCP servers or change hook configuration.
- [x] All writes confined to `$HOME/.claude/experiments/2026-05-05-027-followalong/`.
- [x] Test artifact contained only generic placeholder text; no real content.
