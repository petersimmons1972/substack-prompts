Copy the prompt below and paste it into Claude, ChatGPT, or your model of choice. The article linked from this directory's README explains what to expect.

````text
You are a remediation planner. You operate read-only against my live `CLAUDE.md`. You may write only inside the scratch directory used by Prompt 1. You may not exfiltrate file contents. You may not read `*.env`, `*credentials*`, `*token*`, `*.key`, `*.pem`, `id_rsa*`, `id_ed25519*`, `/.ssh/`, or `/.gnupg/` paths. You may not modify the live `CLAUDE.md`, `~/.claude/settings.json`, `~/AGENTS.md`, `MEMORY.md`, or any file outside the scratch directory. You may not install MCP servers, change hook configuration, or alter permissions. You stage a fix; the human applies it.

**Step 1 — locate the scratch directory and tagging.** Run:

```bash
SCRATCH="$HOME/.claude/experiments/$(date +%Y-%m-%d)-037-claude-md-contract"
test -f "$SCRATCH/01-tagged.md" || { echo "ERROR: run prompt-1 first"; exit 1; }
```

Read `$SCRATCH/00-target.md` to recover the target path and `$SCRATCH/01-tagged.md` for the line tags. If `00-target.md` contains `NO_CLAUDE_MD_FOUND`, stop with a missing-prereq finding.

**Step 2 — back up the target.** Copy the live `CLAUDE.md` to scratch with a timestamped name:

```bash
TARGET="<path from 00-target.md>"
TS="$(date +%Y%m%d-%H%M%S)"
cp -p "$TARGET" "$SCRATCH/backup-${TS}-CLAUDE.md"
```

Confirm the backup byte-count and md5 match the live file. Record both numbers in `$SCRATCH/11-backup-verified.md`.

**Step 3 — produce the rewrite.** Build `$SCRATCH/12-proposed-CLAUDE.md` from the tagged file using these rules:

- Keep every line tagged `RULE` (any confidence).
- Drop every line tagged `DOCUMENTATION`, `HISTORY`, or `DERIVABLE`.
- Keep every section heading whose section retains at least one RULE line; drop headings whose entire section was non-RULE.
- Preserve list formatting and indentation. Do not re-paraphrase rules — copy them verbatim from the live file.
- If a section had a one-line philosophical preamble before its rules, drop the preamble.
- At the top of the rewrite, add a single comment line: `<!-- rewritten 2026-MM-DD via article 037; see scratch for original -->`.

**Step 4 — measure the delta.** Compute for both the live file and the rewrite: byte size, line count, word count, estimated tokens (`ceil(words / 0.75)`). Write `$SCRATCH/13-delta.md` with a two-row table and a `tokens_saved` field. Compute the percentage reduction.

**Step 5 — sanity-check the rewrite.** Read `$SCRATCH/12-proposed-CLAUDE.md` and verify three properties: (a) every line that survived is either a heading or contains an imperative or constraint verb; (b) no heading is left orphaned with zero content; (c) no rule references a section that was dropped (search for `see §`, `see section`, named cross-references). Write findings to `$SCRATCH/14-sanity.md` with `OK` or a list of issues.

**Step 6 — produce the apply and undo blocks.** Write `$SCRATCH/15-apply.sh` containing:

```bash
cp -p "$SCRATCH/12-proposed-CLAUDE.md" "$TARGET"
```

And `$SCRATCH/16-undo.sh` containing:

```bash
cp -p "$SCRATCH/backup-${TS}-CLAUDE.md" "$TARGET"
```

Make both executable. Print `13-delta.md` and `14-sanity.md` to stdout. Do not run `15-apply.sh`.
````
