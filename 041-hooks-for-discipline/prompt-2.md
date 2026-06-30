Copy the prompt below and paste it into Claude, ChatGPT, or your model of choice. The article linked from this directory's README explains what to expect.

````text
You are a hook designer. You operate read-only against my live config and session transcripts. You may write only inside the scratch directory used by Prompt 1. You may not exfiltrate file contents. You may not read `*.env`, `*credentials*`, `*token*`, `*.key`, `*.pem`, `id_rsa*`, `id_ed25519*`, `/.ssh/`, or `/.gnupg/` paths. You may not modify `~/.claude/settings.json` (this is a hard boundary), install MCP servers, change hook configuration, or alter permissions. You stage a spec; the human installs it.

**Step 1 — locate scratch and prior tagging.** Run:

```bash
SCRATCH="$HOME/.claude/experiments/$(date +%Y-%m-%d)-041-hook-inventory"
test -f "$SCRATCH/03-tagged.md" || { echo "ERROR: run prompt-1 first"; exit 1; }
```

**Step 2 — locate session transcripts.** As in Article 039 Prompt 2: try `~/.claude/projects/*/sessions/`, `~/.claude/sessions/`, or any project `transcripts/` directory. Record the path and file count in `$SCRATCH/40-sessions.md`. If none exist, fall back to recent git log + commit messages within the current working directory and note the fallback. If no signal source is available, stop with a missing-prereq finding.

**Step 3 — mine for hook-shaped failures.** Within the most recent 50 transcripts (or commit messages), look for failures that are *deterministic and verifiable* — the class of failure a hook can catch. Examples:

- committed without running tests
- edited live file without backup
- claimed task done before verification
- pushed to `main` without intent
- skipped scratch directory pattern
- left a TODO comment in committed code

For each candidate, record session id (no quoted user content longer than 60 chars), failure class, and whether the failure is detectable from a tool call (PreToolUse / PostToolUse hooks) or a session boundary (SessionStart / Stop). Write to `$SCRATCH/41-failures.md`.

**Step 4 — pick the target failure.** Choose the failure class with the highest count where count ≥2 *and* the failure is deterministically detectable. If no class meets both criteria, pick the highest-count detectable class regardless of recurrence and label the spec *prophylactic*. Write the choice and rationale to `$SCRATCH/42-target.md`.

**Step 5 — draft the hook script.** Write `$SCRATCH/43-hook.sh` containing the proposed hook body. Constraints:

- **Shebang and `set -euo pipefail`** at the top.
- **Explicit timeout discipline** — the hook script must complete in under 5 seconds against a typical session; document its expected runtime.
- **Fail mode declared in a comment:** `FAIL_OPEN` (allow the tool call if the hook fails — for non-blocking advisory hooks) or `FAIL_CLOSED` (block the tool call if the hook fails — for security-critical hooks). For most discipline hooks, `FAIL_CLOSED` on a clear violation, `FAIL_OPEN` on script error.
- **Read-only** behavior wherever possible; if the hook writes a state file, it writes to `~/.claude/.hook-state/<hook-name>` and never to the operator's working tree.
- **No network calls.** No external service. Local-state only.
- **Idempotent** — running the hook twice produces the same outcome.
- **No secret handling** — if the hook touches a memory file or commit message, never echo the matched content; redact (`first 4 + … + last 2`) before logging.

Make the script executable in scratch (`chmod +x $SCRATCH/43-hook.sh`). Do not copy it under `~/.claude/hooks/` — that requires a `settings.json` change, which is out of bounds.

**Step 6 — produce the install plan and undo.** Write `$SCRATCH/44-install-plan.md` containing:

- The exact JSON patch the operator should add to `~/.claude/settings.json` under the relevant event key. Example shape (do not write to settings.json itself):

  ```json
  {
    "hooks": {
      "PreToolUse": [
        {
          "matcher": "Bash",
          "hooks": [
            { "type": "command", "command": "$HOME/.claude/hooks/<basename>" }
          ]
        }
      ]
    }
  }
  ```

- The proposed install path (`~/.claude/hooks/<basename>`).
- The five-step manual install sequence: (a) review `43-hook.sh`; (b) `cp -p $SCRATCH/43-hook.sh ~/.claude/hooks/<basename>`; (c) edit `~/.claude/settings.json` to add the patch; (d) test with one deliberate trigger; (e) keep `45-undo.sh` open in a terminal in case of misbehavior.

Write `$SCRATCH/45-undo.sh`:

```bash
rm -f "$HOME/.claude/hooks/<basename>"
# Then manually remove the JSON patch from ~/.claude/settings.json.
# Note: this prompt did not write to settings.json; you did, and only you can revert it.
```

Print `42-target.md`, `43-hook.sh`, and `44-install-plan.md` to stdout.
````
