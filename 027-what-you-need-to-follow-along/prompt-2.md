You are a checklist drafter. You are read-only against my home directory except for the scratch directory created in Step 1. You may not exfiltrate file contents to any network endpoint. You may not read files matching `*.env`, `*credentials*`, `*token*`, `*.key`, `*.pem`, `id_rsa*`, `id_ed25519*`, or any path containing `/.ssh/` or `/.gnupg/`. You may not modify `~/.claude/settings.json`, `~/CLAUDE.md`, `~/.claude/CLAUDE.md`, `~/.claude/projects/-home-psimmons/memory/MEMORY.md`, `~/AGENTS.md`, install MCP servers, change hook configuration, or alter file permissions. You produce a draft; the operator copies it into their notes manually.

**Step 1 — create scratch directory.** Run:

```bash
SCRATCH="$HOME/.claude/experiments/$(date +%Y-%m-%d)-027-checklist"
mkdir -p "$SCRATCH"
echo "scratch=$SCRATCH"
```

**Step 2 — re-collect environment facts.** Run the same checks as Prompt 1's Step 1 and capture into `$SCRATCH/01-env.md`. We re-collect rather than read from the previous scratch directory because the previous one may already be deleted, and because the checklist must be self-contained.

**Step 3 — ask three calibration questions.** Ask me, one at a time:

1. Where do I keep operational notes? (Examples: `~/notes/`, a wiki, Obsidian, Tana, Notion, paper.)
2. What is my preferred scratch base path? (Default: `~/.claude/experiments/`.)
3. What is my time-zone-aware date command? (Default: `date +%Y-%m-%d`.)

Save my answers verbatim to `$SCRATCH/02-answers.md`.

**Step 4 — draft the checklist.** Produce `$SCRATCH/03-PREFLIGHT.md` with this exact section structure, filled in with my answers:

```
# Pre-Flight Checklist

Run this before any prompt from the AI Optimization Series that
touches files outside its own scratch directory.

## Environment

- [ ] bash >= 4.0  (have: <captured-version>)
- [ ] git installed (have: <captured-version>)
- [ ] claude-code installed (have: <captured-version> or "absent")
- [ ] write access to <scratch-base-path>

## Scratch

- [ ] today's scratch path: <scratch-base-path>$(<date-cmd>)-<article-slug>
- [ ] mkdir -p the path; confirm writable
- [ ] no live file written outside scratch unless step is reversible

## Backups

- [ ] for each live file the prompt will modify: cp -p to scratch with TS suffix
- [ ] verify backup byte-count matches live (record both numbers)
- [ ] never edit a backup; only restore from it

## Undo

- [ ] every prompt has a single-command undo block; locate it before starting
- [ ] for staged changes never applied: rm -rf <scratch>
- [ ] for applied changes: cp -p <backup> <live> first, then rm -rf <scratch>
- [ ] verify md5 of live file matches pre-state after restore

## Security floor

- [ ] no .env, credentials, keys, .ssh, .gnupg paths read
- [ ] no settings.json, CLAUDE.md, MEMORY.md, AGENTS.md modified by the model
- [ ] no MCP servers installed; no hook config changed
- [ ] no file content sent to a network endpoint except prompts I authorized

## Notes location

Permanent home for this file: <answer-from-step-3>
Last updated: <YYYY-MM-DD>
```

The captured versions and paths must reflect the operator's actual environment, not generic placeholders. The checklist is not a template — it is *their* checklist with their numbers in it.

**Step 5 — print the relocation instructions.** Print:

```
CHECKLIST READY: $SCRATCH/03-PREFLIGHT.md
Copy to permanent location:
  cp $SCRATCH/03-PREFLIGHT.md <notes-location>/PREFLIGHT.md
Then delete scratch:
  rm -rf $SCRATCH
```

Replace `<notes-location>` with the operator's answer from Step 3.

**Step 6 — produce the takeaway.** Write `$SCRATCH/00-CHECKLIST.md` with: target notes location, scratch base path, total checklist line count, and a one-line readiness statement: `CHECKLIST READY at $SCRATCH/03-PREFLIGHT.md — copy manually before deleting scratch`. Print to stdout.
