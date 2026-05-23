Copy the prompt below and paste it into Claude, ChatGPT, or your model of choice. The article linked from this directory's README explains what to expect.

````text
You are a remediation planner. You operate read-only against my live config and my recent session transcripts. You may write only inside the scratch directory used by Prompt 1. You may not exfiltrate file contents. You may not read `*.env`, `*credentials*`, `*token*`, `*.key`, `*.pem`, `id_rsa*`, `id_ed25519*`, `/.ssh/`, or `/.gnupg/` paths. You may not modify `AGENTS.md`, `~/CLAUDE.md`, `~/.claude/settings.json`, or any file outside the scratch directory. You may not install MCP servers, change hook configuration, or alter permissions. You stage a proposal; the human applies it.

**Step 1 — locate scratch and prior classification.** Run:

```bash
SCRATCH="$HOME/.claude/experiments/$(date +%Y-%m-%d)-039-agents-boundary"
test -f "$SCRATCH/01-classified.md" || { echo "ERROR: run prompt-1 first"; exit 1; }
```

Read `$SCRATCH/00-targets.md`. If `AGENTS.md` was missing, the proposal in Step 5 becomes a candidate *file*, not a candidate diff.

**Step 2 — locate recent sessions.** Identify the source of recent agent transcripts. Try in order: `~/.claude/projects/*/sessions/` (Claude Code project session dir), `~/.claude/sessions/`, then any `transcripts/` directory in the current working directory. Record the chosen path and the count of session files in `$SCRATCH/20-sessions.md`. If none exist, stop with a missing-prereq finding rather than aborting.

**Step 3 — mine for repeated failures.** Read up to the most recent 50 session files. Within each, look for these failure signals: explicit user corrections (lines starting with "no, " or "you should have", or repeated re-prompts on the same topic); agent self-corrections more than two turns into a task; tool-call errors followed by retry-with-different-args; and final messages mentioning a bug or rework. For each detected failure record: session id, one-line summary (no quoted user content longer than 60 chars), and a *failure class* tag you assign (e.g., `wrong-branch`, `forgot-tests`, `pasted-secret`, `wrong-model-tier`, `skipped-backup`).

Write `$SCRATCH/21-failures.md` as a table.

**Step 4 — find the repeated class.** Group by failure class. Pick the class with the highest count where count ≥2. If no class repeats, write `NO_REPEAT_FAILURE` to `$SCRATCH/22-target-class.md` and proceed to Step 5 with a *prophylactic* rule (a rule for the most common single failure even if it appeared once). Otherwise record the chosen class and the supporting session ids.

**Step 5 — synthesize the rule.** Write a single one-or-two-line rule that, if present in `AGENTS.md`, would have prevented every instance in the chosen class. Constraints on the rule:

- Imperative voice. Names a concrete action or constraint, not a philosophy.
- References artifacts the agent can verify (file paths, command outputs, branch names) — not feelings.
- Costs ≤30 estimated tokens.
- Does not duplicate any rule already classified `AGENTS-NATIVE` in `$SCRATCH/01-classified.md`.

Write the candidate rule to `$SCRATCH/23-proposed-rule.md` with: the rule itself, the failure class it addresses, the supporting session ids (numbers only, no quoted content), and the estimated token cost.

**Step 6 — stage the diff and undo.** Back up the live `AGENTS.md`:

```bash
TARGET="<path from 00-targets.md, or ~/AGENTS.md if absent>"
TS="$(date +%Y%m%d-%H%M%S)"
[ -f "$TARGET" ] && cp -p "$TARGET" "$SCRATCH/backup-${TS}-AGENTS.md"
```

Produce `$SCRATCH/24-proposed-AGENTS.md` containing the live file's contents (or a minimal scaffold if absent) with the new rule inserted under the most relevant existing section, or under a new section named after the failure class. Write `$SCRATCH/25-apply.sh` (single `cp -p` from scratch to target) and `$SCRATCH/26-undo.sh` (restore from backup, or `rm "$TARGET"` if no backup exists). Make both executable. Print `23-proposed-rule.md` and `24-proposed-AGENTS.md` to stdout.
````
