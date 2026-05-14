# Prompt 2 — Dry-Run Reference

**Run on:** 2026-05-05 (Opus 4.7, 1M context)
**Environment:** Linux 6.18.7, bash 5.x, Claude Code session
**Status:** All 6 steps produced output. Checklist staged in scratch; manual copy to permanent location performed. Undo verified clean.

---

## 02-answers.md (operator-supplied)

```
1. notes_location: ~/notes/preflight/
2. scratch_base_path: ~/.claude/experiments/
3. date_command: date +%Y-%m-%d
```

## 03-PREFLIGHT.md (excerpt — first 20 lines)

```
# Pre-Flight Checklist

Run this before any prompt from the AI Optimization Series that
touches files outside its own scratch directory.

## Environment

- [ ] bash >= 4.0  (have: 5.2.21)
- [ ] git installed (have: 2.43.0)
- [ ] claude-code installed (have: 2.x.x)
- [ ] write access to ~/.claude/experiments/

## Scratch

- [ ] today's scratch path: ~/.claude/experiments/$(date +%Y-%m-%d)-<article-slug>
- [ ] mkdir -p the path; confirm writable
- [ ] no live file written outside scratch unless step is reversible

## Backups
... (continues for ~25 more lines)
```

Total checklist length: 42 lines. All blanks filled with operator's actual values.

## Relocation message printed

```
CHECKLIST READY: $SCRATCH/03-PREFLIGHT.md
Copy to permanent location:
  cp $SCRATCH/03-PREFLIGHT.md ~/notes/preflight/PREFLIGHT.md
Then delete scratch:
  rm -rf $SCRATCH
```

Operator executed the copy:

```
$ mkdir -p ~/notes/preflight/
$ cp $SCRATCH/03-PREFLIGHT.md ~/notes/preflight/PREFLIGHT.md
$ wc -l ~/notes/preflight/PREFLIGHT.md
42 ~/notes/preflight/PREFLIGHT.md
```

## 00-CHECKLIST.md (final)

```
notes_location: ~/notes/preflight/
scratch_base: ~/.claude/experiments/
checklist_lines: 42
status: CHECKLIST READY at $SCRATCH/03-PREFLIGHT.md — copy manually before deleting scratch
```

## Notable result

The 42-line checklist is well within the 30–50 expected band. The personalized values (bash 5.2.21, git 2.43.0, ~/notes/preflight/ as the home) make the checklist feel like an artifact the operator owns rather than a generic template. The operator confirmed the file is now visible from their normal note-opening workflow — the test that matters.

Worth flagging for Phase 3: the article body should explicitly recommend that operators *re-run this prompt* annually or whenever they upgrade bash/git/claude-code, so the checklist's tool-version values stay current. The prompt as written supports re-running cleanly (it always uses today's date for scratch, and the manual copy is overwrite-safe with `cp`), but the article should make the maintenance loop explicit.

## Undo verified

```
$ rm -rf "$HOME/.claude/experiments/2026-05-05-027-checklist"
$ ls "$HOME/.claude/experiments/" | grep 027-checklist || echo "(absent)"
(absent)
$ ls ~/notes/preflight/PREFLIGHT.md
~/notes/preflight/PREFLIGHT.md   # intentionally retained
```

UNDO VERIFIED: `rm -rf "$HOME/.claude/experiments/$(date +%Y-%m-%d)-027-checklist"`

The permanent `PREFLIGHT.md` in `~/notes/preflight/` is *meant* to persist; the scratch cleanup does not touch it. If the operator wants to remove the permanent copy, that is a separate `rm` they run intentionally.

## Security-floor self-check

- [x] Did not exfiltrate file contents to any network endpoint.
- [x] Did not read `.env`, credentials, tokens, keys, or `.ssh`/`.gnupg` paths.
- [x] Did not modify `~/.claude/settings.json`, `~/CLAUDE.md`, `~/.claude/CLAUDE.md`, `MEMORY.md`, or `~/AGENTS.md`.
- [x] Did not install MCP servers or change hook configuration.
- [x] Scratch writes confined to `$HOME/.claude/experiments/2026-05-05-027-checklist/`.
- [x] The single write outside scratch — `~/notes/preflight/PREFLIGHT.md` — was operator-driven via manual `cp`, not model-driven; the prompt only printed instructions.
- [x] Checklist content contained no credentials, paths to credentials, or proprietary identifiers.
