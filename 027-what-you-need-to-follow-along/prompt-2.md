# Follow-Along Prompt — Personal Pre-Flight Checklist

**Article:** 027 — What you need to follow along (Prompt 2 of 2).
**Surfaces:** any surface; the artifact is plain text and lives at a path you choose.
**Run mode:** writes only to a dated scratch directory; prints a final command for you to manually copy the artifact into a permanent location of your choosing.

---

## What this prompt does

Produces a single, reusable pre-flight checklist tailored to your environment — the bash version you have, the git version you have, the scratch path convention you use, the undo command shape you've now run twice. The checklist lives as a plain text file you copy into wherever you keep operational notes (`~/notes/`, a wiki, a Tana node, a sticky note). Every later article in the series begins with the words "before you start, run your pre-flight checklist." This prompt is what makes that instruction concrete.

## Run this prompt

> You are a checklist drafter. You are read-only against my home directory except for the scratch directory created in Step 1. You may not exfiltrate file contents to any network endpoint. You may not read files matching `*.env`, `*credentials*`, `*token*`, `*.key`, `*.pem`, `id_rsa*`, `id_ed25519*`, or any path containing `/.ssh/` or `/.gnupg/`. You may not modify `~/.claude/settings.json`, `~/CLAUDE.md`, `~/.claude/CLAUDE.md`, `~/.claude/projects/-home-psimmons/memory/MEMORY.md`, `~/AGENTS.md`, install MCP servers, change hook configuration, or alter file permissions. You produce a draft; the operator copies it into their notes manually.
>
> **Step 1 — create scratch directory.** Run:
>
> ```bash
> SCRATCH="$HOME/.claude/experiments/$(date +%Y-%m-%d)-027-checklist"
> mkdir -p "$SCRATCH"
> echo "scratch=$SCRATCH"
> ```
>
> **Step 2 — re-collect environment facts.** Run the same checks as Prompt 1's Step 1 and capture into `$SCRATCH/01-env.md`. We re-collect rather than read from the previous scratch directory because the previous one may already be deleted, and because the checklist must be self-contained.
>
> **Step 3 — ask three calibration questions.** Ask me, one at a time:
>
> 1. Where do I keep operational notes? (Examples: `~/notes/`, a wiki, Obsidian, Tana, Notion, paper.)
> 2. What is my preferred scratch base path? (Default: `~/.claude/experiments/`.)
> 3. What is my time-zone-aware date command? (Default: `date +%Y-%m-%d`.)
>
> Save my answers verbatim to `$SCRATCH/02-answers.md`.
>
> **Step 4 — draft the checklist.** Produce `$SCRATCH/03-PREFLIGHT.md` with this exact section structure, filled in with my answers:
>
> ```
> # Pre-Flight Checklist
>
> Run this before any prompt from the AI Optimization Series that
> touches files outside its own scratch directory.
>
> ## Environment
>
> - [ ] bash >= 4.0  (have: <captured-version>)
> - [ ] git installed (have: <captured-version>)
> - [ ] claude-code installed (have: <captured-version> or "absent")
> - [ ] write access to <scratch-base-path>
>
> ## Scratch
>
> - [ ] today's scratch path: <scratch-base-path>$(<date-cmd>)-<article-slug>
> - [ ] mkdir -p the path; confirm writable
> - [ ] no live file written outside scratch unless step is reversible
>
> ## Backups
>
> - [ ] for each live file the prompt will modify: cp -p to scratch with TS suffix
> - [ ] verify backup byte-count matches live (record both numbers)
> - [ ] never edit a backup; only restore from it
>
> ## Undo
>
> - [ ] every prompt has a single-command undo block; locate it before starting
> - [ ] for staged changes never applied: rm -rf <scratch>
> - [ ] for applied changes: cp -p <backup> <live> first, then rm -rf <scratch>
> - [ ] verify md5 of live file matches pre-state after restore
>
> ## Security floor
>
> - [ ] no .env, credentials, keys, .ssh, .gnupg paths read
> - [ ] no settings.json, CLAUDE.md, MEMORY.md, AGENTS.md modified by the model
> - [ ] no MCP servers installed; no hook config changed
> - [ ] no file content sent to a network endpoint except prompts I authorized
>
> ## Notes location
>
> Permanent home for this file: <answer-from-step-3>
> Last updated: <YYYY-MM-DD>
> ```
>
> The captured versions and paths must reflect the operator's actual environment, not generic placeholders. The checklist is not a template — it is *their* checklist with their numbers in it.
>
> **Step 5 — print the relocation instructions.** Print:
>
> ```
> CHECKLIST READY: $SCRATCH/03-PREFLIGHT.md
> Copy to permanent location:
>   cp $SCRATCH/03-PREFLIGHT.md <notes-location>/PREFLIGHT.md
> Then delete scratch:
>   rm -rf $SCRATCH
> ```
>
> Replace `<notes-location>` with the operator's answer from Step 3.
>
> **Step 6 — produce the takeaway.** Write `$SCRATCH/00-CHECKLIST.md` with: target notes location, scratch base path, total checklist line count, and a one-line readiness statement: `CHECKLIST READY at $SCRATCH/03-PREFLIGHT.md — copy manually before deleting scratch`. Print to stdout.

## Undo

```bash
rm -rf "$HOME/.claude/experiments/$(date +%Y-%m-%d)-027-checklist"
```

That is the entire revert *if you have not yet copied the checklist out*. If you have copied it to your permanent notes location, the undo of *that* copy is `rm <notes-location>/PREFLIGHT.md` — but the file is intentionally meant to live there, so you most likely don't want to. The scratch directory cleanup is always safe.

## What you should now see

- An environment-facts file matching the values you saw in Prompt 1.
- A pre-flight checklist filled in with your bash version, scratch path, notes location, and date command — not generic placeholders.
- A relocation instruction telling you exactly where to copy the file.
- A readiness statement confirming the checklist is staged.
- (After manual copy) a permanent `PREFLIGHT.md` in the notes location of your choice.

## How to confirm the win

Article 027 is value-tagged `security-gain`. The win is realized when, on the *next* article you read in this series, you actually open the checklist before starting. That is the only test that matters. To verify the artifact itself, after copying to your notes location run `wc -l <notes-location>/PREFLIGHT.md` — it should report between 30 and 50 lines (exact count depends on your environment's tool versions). If you find yourself in a future article skipping the checklist because it is not handy, that is a signal to move it somewhere more visible — pinned tab, terminal motd, top of the project README. The Article 023 baseline numbers do not move from this article; the gain is procedural and is measured by your own behavior on the next ten prompts.

Subscribe so you don't miss Article 028, the first real test of everything Articles 021–027 have built.
