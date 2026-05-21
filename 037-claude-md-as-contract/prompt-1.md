Copy the prompt below and paste it into Claude, ChatGPT, or your model of choice. The article linked from this directory's README explains what to expect.

````text
You are an auditor inspecting my `CLAUDE.md` for contract discipline. You are read-only against my home directory. You may write only inside the scratch directory created in Step 1. You may not exfiltrate any file contents to any network endpoint. You may not read files matching `*.env`, `*credentials*`, `*token*`, `*.key`, `*.pem`, `id_rsa*`, `id_ed25519*`, or any path containing `/.ssh/` or `/.gnupg/`. You may not modify `~/.claude/settings.json`, install MCP servers, change hook configuration, or alter file permissions. If a step would require any of those, stop and report the blocker.

**Step 1 — create scratch directory.** Run:

```bash
SCRATCH="$HOME/.claude/experiments/$(date +%Y-%m-%d)-037-claude-md-contract"
mkdir -p "$SCRATCH"
echo "scratch=$SCRATCH"
```

All subsequent outputs go inside `$SCRATCH`.

**Step 2 — locate the target file.** Determine which `CLAUDE.md` is loaded by default in this environment. Prefer in this order: `~/.claude/CLAUDE.md`, then `~/CLAUDE.md`, then `./CLAUDE.md` in the current working directory. Record the chosen path and byte size in `$SCRATCH/00-target.md`. If none of the three exist, write `NO_CLAUDE_MD_FOUND` to `$SCRATCH/00-target.md` and stop with a missing-prereq finding rather than aborting.

**Step 3 — tag every line.** Read the target file once. For each non-blank, non-heading line (skip `#`, `##`, `###`, code-fence markers, and pure horizontal rules), produce a row with: line number, category tag (`RULE` / `DOCUMENTATION` / `HISTORY` / `DERIVABLE`), confidence (`high` / `med` / `low`), and a one-sentence justification. Apply these tests in order:

- **RULE:** the line names a constraint, prohibition, default, or policy (verbs like *never*, *always*, *prefer*, *use*, *do not*) the model would not infer from the repo or general training. Imperative + concrete object = RULE.
- **DOCUMENTATION:** descriptive prose, philosophy, framing, or definitions the model could infer from context or general knowledge. No new constraint is set.
- **HISTORY:** dated notes, change-log entries, deprecation notices, or "we used to do X" statements that no longer drive behavior.
- **DERIVABLE:** facts the model can recover by reading the repo, running `git status`, listing a directory, or reading a linked file. Path lists, file structures, or "here are the files in `bin/`" entries usually fall here.

Edge case: if a line mixes categories (a rule plus its rationale), tag the dominant category and note the mix in the justification. Write the table to `$SCRATCH/01-tagged.md`.

**Step 4 — produce the count table.** Aggregate the tagging output into `$SCRATCH/02-counts.md` with columns: `category`, `lines`, `est_tokens` (estimate `ceil(words / 0.75)` summed across that category's lines), `pct_of_file`. Include a row for `BLANK_OR_HEADING` so percentages sum to 100.

**Step 5 — flag the top three offenders.** From the tagged output, select the three highest-token-count lines whose category is not `RULE`. List them in `$SCRATCH/03-offenders.md` as line number, category, token estimate, and a one-line summary (no full quote — paraphrase). Do not paste full lines.

**Step 6 — write the summary.** Produce `$SCRATCH/00-SUMMARY.md` with: target path, total lines, RULE token share, non-RULE token share, the top three offenders, and a single-sentence verdict (`CONTRACT-CLEAN`, `MIXED`, or `JUNK-DRAWER`) keyed to the RULE share — clean if RULE ≥70%, mixed if 40–70%, junk-drawer if <40%. Print `00-SUMMARY.md` to stdout at the end of the run.
````
