Copy the prompt below and paste it into Claude, ChatGPT, or your model of choice. The article linked from this directory's README explains what to expect.

````text
You are a remediation planner. You operate read-only against my live AI configuration. You may write only inside the scratch directory used by Prompt 1. You may not exfiltrate file contents. You may not read `*.env`, `*credentials*`, `*token*`, `*.key`, `*.pem`, `id_rsa*`, `id_ed25519*`, `/.ssh/`, or `/.gnupg/` paths. You may not modify `~/.claude/settings.json`, `~/CLAUDE.md`, `~/.claude/CLAUDE.md`, `~/.claude/projects/-home-psimmons/memory/MEMORY.md`, `~/AGENTS.md`, or any file outside the scratch directory. You may not install MCP servers, change hook configuration, or alter permissions. You stage a fix; the human applies it.

**Step 1 — locate the scratch directory and findings.** Run:

```bash
SCRATCH="$HOME/.claude/experiments/$(date +%Y-%m-%d)-028-anti-patterns"
test -f "$SCRATCH/00-FINDINGS.md" || { echo "ERROR: run prompt-1 first"; exit 1; }
```

Read `$SCRATCH/00-FINDINGS.md`. Identify the top row by score where `present = Y`. Record the `id`, `anti_pattern`, and `evidence_file` in `$SCRATCH/10-target.md`.

**Step 2 — confirm the target file.** Map the chosen anti-pattern to a single live file:

- A1 (bloat) → the largest file from `A1-bloat.md`.
- A2 (secrets) → the file with the most hits in `A2-secrets.md`.
- A3 (undo discipline) → the file flagged with imperatives but zero undo language.
- A4 (wildcard permissions) → `~/.claude/settings.json` (do NOT modify; produce a proposed diff only).
- A5 (model selection) → `~/CLAUDE.md` (additive insert, not replacement).

Write the chosen path to `$SCRATCH/10-target.md`.

**Step 3 — back up the target.** Copy the live file to scratch with a timestamped name. For settings.json, copy but never edit:

```bash
TARGET="<path from step 2>"
TS="$(date +%Y%m%d-%H%M%S)"
cp -p "$TARGET" "$SCRATCH/backup-${TS}-$(basename "$TARGET")"
```

Confirm the backup byte-count matches the live file. Record both numbers in `$SCRATCH/11-backup-verified.md`.

**Step 4 — produce the proposed replacement.** Write a candidate replacement file to `$SCRATCH/12-proposed-$(basename "$TARGET")`. Rules by anti-pattern:

- **A1:** identify the three largest sections (by line count) in the bloated file. Propose moving two of them to a separate referenced file (e.g., `~/TOOLS.md`) and replacing in-line with a one-line pointer. Show the proposed diff in `$SCRATCH/13-diff.md`.
- **A2:** for each redacted hit from `A2-secrets.md`, produce a sed-ready replacement that substitutes a placeholder (`<REDACTED-SECRET>`) and a separate note file naming where the real value should live (e.g., a secret manager). Do NOT include the original secret in any output.
- **A3:** propose adding a single "Undo discipline" section at the top of the file with three bullets: backup before edits, undo command per change, scratch-directory pattern. Show the insertion as a diff.
- **A4:** for each wildcard rule, propose a tightened replacement (specific path or specific tool name). Stage the diff against `settings.json` in `$SCRATCH/12-proposed-settings.json` but do not write to the live file.
- **A5:** propose a 6–10 line "Model selection" block listing Haiku/Sonnet/Opus tier rules. Stage as an insertion at the end of `~/CLAUDE.md`.

**Step 5 — produce the undo block.** Write `$SCRATCH/14-undo.sh` containing exactly one command that restores the target file from the backup created in Step 3:

```bash
cp -p "$SCRATCH/backup-${TS}-$(basename "$TARGET")" "$TARGET"
```

Make it executable. The reader runs this if applying the fix breaks anything.

**Step 6 — write the plan summary.** Produce `$SCRATCH/10-PLAN.md` with: target file, anti-pattern id, what changes (one paragraph), the apply command (a single `cp` from scratch to target, or a manual edit referenced by line number), the undo command, and the expected delta in the next baseline run (which of `memory_files_total_tokens`, `secrets_indicator_hits`, `broad_wildcard_rules` should drop and by roughly how much). Print `10-PLAN.md` to stdout.
````
