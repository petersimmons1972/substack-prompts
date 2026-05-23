Copy the prompt below and paste it into Claude, ChatGPT, or your model of choice. The article linked from this directory's README explains what to expect.

````text
You are an auditor inspecting the boundary between `AGENTS.md` and `CLAUDE.md`. You are read-only against my home directory and the current working directory. You may write only inside the scratch directory created in Step 1. You may not exfiltrate any file contents to any network endpoint. You may not read files matching `*.env`, `*credentials*`, `*token*`, `*.key`, `*.pem`, `id_rsa*`, `id_ed25519*`, or any path containing `/.ssh/` or `/.gnupg/`. You may not modify `~/.claude/settings.json`, install MCP servers, change hook configuration, or alter file permissions.

**Step 1 — create scratch directory.** Run:

```bash
SCRATCH="$HOME/.claude/experiments/$(date +%Y-%m-%d)-039-agents-boundary"
mkdir -p "$SCRATCH"
echo "scratch=$SCRATCH"
```

**Step 2 — locate both files.** Find the highest-precedence `AGENTS.md` (current working directory, then `~/AGENTS.md`) and the highest-precedence `CLAUDE.md` (`~/.claude/CLAUDE.md`, then `~/CLAUDE.md`, then `./CLAUDE.md`). Record paths and byte sizes in `$SCRATCH/00-targets.md`. If `AGENTS.md` is absent, write `NO_AGENTS_MD_FOUND` and emit a missing-prereq finding (Prompt 2 will still run and propose creating one). If `CLAUDE.md` is absent, write `NO_CLAUDE_MD_FOUND` and stop with a missing-prereq finding.

**Step 3 — classify each rule-bearing line.** For each non-blank, non-heading line in both files, assign one of:

- **AGENTS-NATIVE:** rule applies to *any* agent the operator might dispatch on this project. Test: would a different operator on the same project still want this rule for their agents? Examples: branch naming conventions, commit message format, "always run tests after edits", PR review requirements, tool preferences when shared by the team.
- **CLAUDE-NATIVE:** rule applies to *this operator's* personal contract. Test: would another operator using the same project explicitly disagree or have a different preference? Examples: model tier defaults, voice preferences, escalation triggers tied to personal cost guardrails, "wake the founder" thresholds.
- **EITHER:** rule could reasonably live in either file; record the current location.
- **NEITHER:** rule belongs in a different file (e.g., a skill, `MEMORY.md`, or `settings.json`). Note the better home.

Write the table to `$SCRATCH/01-classified.md` with columns: source file, line number, classification, current location, recommended location, justification (one sentence).

**Step 4 — flag the moves.** Produce `$SCRATCH/02-moves.md` listing every line whose recommended location differs from its current location. Two sub-tables: `agents-to-claude` and `claude-to-agents`. For each move record line number, token cost, and a one-line summary (no full quote — paraphrase).

**Step 5 — detect duplicates.** Scan both files for near-duplicate rules — same imperative, same object, even if phrased differently. Use a simple shingle test: if two lines share ≥4 content words after lowercasing and stop-word removal, flag them as candidate duplicates. Write to `$SCRATCH/03-duplicates.md` as paired line numbers with a similarity note. Duplicates are pure waste — they consume context twice and create conflict if they drift.

**Step 6 — write the summary.** Produce `$SCRATCH/00-SUMMARY.md` with: target paths, total rule lines per file, count of misplaced lines per direction, count of duplicates, and a verdict (`BOUNDARY-CLEAN` if misplaced+duplicate ≤2; `MIXED` if 3–8; `BLURRED` if >8). Print to stdout.
````
