Copy the prompt below and paste it into Claude, ChatGPT, or your model of choice. The article linked from this directory's README explains what to expect.

````text
You are an auditor inspecting configured hooks for discipline value. You are read-only against my `~/.claude/hooks/` directory and `~/.claude/settings.json` (read-only — never write to settings.json). You may write only inside the scratch directory created in Step 1. You may not exfiltrate any file contents to any network endpoint. You may not read files matching `*.env`, `*credentials*`, `*token*`, `*.key`, `*.pem`, `id_rsa*`, `id_ed25519*`, or any path containing `/.ssh/` or `/.gnupg/`. You may not modify `~/.claude/settings.json`, install MCP servers, change hook configuration, or alter file permissions.

**Step 1 — create scratch directory.** Run:

```bash
SCRATCH="$HOME/.claude/experiments/$(date +%Y-%m-%d)-041-hook-inventory"
mkdir -p "$SCRATCH"
echo "scratch=$SCRATCH"
```

**Step 2 — enumerate configured hooks.** Read `~/.claude/settings.json` (read-only) and extract the `hooks` object. List every event-key (e.g., `PreToolUse`, `PostToolUse`, `SessionStart`, `Stop`) and every hook entry under each. For each hook record: event, matcher, command path, command bytes (if the path resolves to a file under `~/.claude/hooks/`), and the configured matchers that gate it. Write to `$SCRATCH/01-configured.md`. Do not echo the full command strings if they contain absolute paths to private files — record the basename and the directory only.

If the project has a `.claude/settings.json`, repeat for the project-scoped config and record both. If neither file contains a `hooks` block, write `NO_HOOKS_CONFIGURED` and stop with a missing-prereq finding (Prompt 2 will design a hook from scratch).

**Step 3 — read each hook script.** For each hook whose command resolves to a script under `~/.claude/hooks/`, read the script file (no `.env` or credential files; if a hook script references one, log the reference and skip the read). Capture: line count, declared shell, presence of `set -e` or equivalent error handling, presence of an explicit timeout, presence of an explicit fail-open vs fail-closed behavior, and any external command it invokes. Write to `$SCRATCH/02-scripts.md`.

**Step 4 — tag each hook.** For every hook, assign one of:

- **DISCIPLINE-AUTOMATION:** the hook *enforces* a verifiable discipline the operator has documented as a recurring failure mode (look for matches in `CLAUDE.md` or `AGENTS.md` rules — e.g., a hook that blocks editing without a backup pairs with a "backup-first" rule). Read-only: the hook stops bad state, doesn't compose advice.
- **NICE-TO-HAVE:** the hook does something useful (logging, telemetry, mild reminder) but is not enforcing a documented discipline.
- **MISPLACED-LOGIC:** the hook is composing context, injecting advice, or running heavy logic that should live elsewhere (e.g., a `SessionStart` hook that prepends a long advisory paragraph — that's a memory file). Note the better home.
- **DEFENSIVE-INFRA:** the hook protects the harness itself (health checks, auth refresh, lock files); not a discipline per se but legitimate.

Write `$SCRATCH/03-tagged.md` with columns: hook id (event:matcher:basename), tag, justification (one sentence), recommended action (`KEEP`, `RETIRE`, `RELOCATE`, `INVESTIGATE`).

**Step 5 — flag the failures.** Produce `$SCRATCH/04-failures.md` listing hooks tagged `MISPLACED-LOGIC` (with a recommended new home) and any hook missing error handling or fail-open/fail-closed declarations (operational risk: a hook that crashes silently can swallow tool calls). Do not paste hook bodies; describe in one line per finding.

**Step 6 — write the summary.** Produce `$SCRATCH/00-SUMMARY.md` with: total hooks, count by tag, count of hooks missing error handling, and a verdict (`HOOKS-DISCIPLINED` if ≥70% are DISCIPLINE-AUTOMATION or DEFENSIVE-INFRA; `MIXED` if 30–70%; `HOOK-OVERREACH` if <30%). Print to stdout.
````
