Copy the prompt below and paste it into Claude, ChatGPT, or your model of choice. The article linked from this directory's README explains what to expect.

````text
You are a permissions-tightening planner. You operate read-only against the live settings files identified in Prompt 1. You may write only inside the scratch directory used by Prompt 1. **You may not modify any live settings file. You may not execute (run) any fixture command. The dry-run is a regex/glob match exercise, not a tool call.** You may not exfiltrate file contents. You may not read `*.env`, `*credentials*`, `*token*`, `*.key`, `*.pem`, `id_rsa*`, `id_ed25519*`, `/.ssh/`, or `/.gnupg/` paths. You may not modify hooks or install MCP servers.

**Step 1 — locate scratch and select the target.** Run:

```bash
SCRATCH="$HOME/.claude/experiments/$(date +%Y-%m-%d)-050-permissions"
test -f "$SCRATCH/02-risk.md" || { echo "ERROR: run prompt-1 first"; exit 1; }
```

Pick the target rule: the highest-risk HIGH-blast + EASY-revocable rule from Prompt 1, or a specific `RULE=<rule_id>` from the operator's environment. Record in `$SCRATCH/20-target.md`.

**Step 2 — back up settings.** Copy the affected settings file:

```bash
TARGET_FILE="<path from 02-risk.md>"; TS="$(date +%Y%m%d-%H%M%S)"
cp -p "$TARGET_FILE" "$SCRATCH/backup-${TS}-$(basename "$TARGET_FILE")"
```

Verify byte and md5 match. Record in `$SCRATCH/21-backup-verified.md`.

**Step 3 — propose tightened replacements.** Examine the target rule and produce 2–3 candidate tightenings, ordered by how aggressive the tightening is. Each candidate names:

- The replacement pattern.
- The legitimate use cases it still allows.
- The use cases it now requires approval for (blast-radius reduction).
- An estimated daily approval-prompt rate (how often will the operator be asked to approve once the rule is tightened).

Examples for `Bash(*)` (most aggressive → least aggressive):

1. `Bash(ls:*)`, `Bash(cat:*)`, `Bash(git status:*)`, `Bash(git diff:*)` — read-only canonical
2. Above plus `Bash(grep:*)`, `Bash(rg:*)`, `Bash(find:*)`, `Bash(test:*)` — read-only extended
3. Above plus `Bash(git commit:*)`, `Bash(git add:*)` — write-allowed for the operator's commit workflow only

Write to `$SCRATCH/22-candidates.md`. Pick one as the recommended candidate, with rationale.

**Step 4 — collect a fixture set.** Pull the operator's recent command history (or session transcripts if the path is supplied via `HISTORY=<path>`). The fixture set is the last ~200 distinct commands the operator has run that fall under the target rule's tool. Each fixture is a real example of the rule firing in production. Write to `$SCRATCH/23-fixtures.md` with: fixture id, command (truncated), and timestamp if available. **Do not execute any fixture.**

**Step 5 — dry-run the tightened rule.** For each fixture, match it against the recommended replacement:

- **STILL-ALLOWED** — the fixture matches a pattern in the tightened rule.
- **NOW-PROMPTED** — the fixture would require approval under the tightened rule.
- **NOW-DENIED** — the fixture would be denied entirely (only if the tightening introduces a new deny rule).

Write to `$SCRATCH/24-dry-run.md`: per-fixture verdict and the matching pattern (or "no match"). Compute totals: how many fixtures are still allowed; how many would now prompt; how many would be denied. The "now prompted" count is the operator's daily approval-prompt cost — the trade-off they accept for the blast-radius reduction.

**Step 6 — produce the JSON patch.** Generate `$SCRATCH/25-patch.json` representing the change to the live settings file. Use a small JSON-patch (RFC 6902) format — adds, removes, replaces — explicit enough to apply with `jq` or `python -m jsonpatch`, but **do not run the apply yourself**. Verify the patch is syntactically valid by parsing it; do not apply.

**Step 7 — produce the staging report.** Write `$SCRATCH/00-PLAN.md` with: target rule, recommended replacement, fixture totals (still-allowed / now-prompted / now-denied), JSON patch path, and the exact apply command (e.g., `python -m jsonpatch apply 25-patch.json $TARGET_FILE`) — but do not run it. Print to stdout.
````
