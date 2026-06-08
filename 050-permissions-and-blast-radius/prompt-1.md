Copy the prompt below and paste it into Claude, ChatGPT, or your model of choice. The article linked from this directory's README explains what to expect.

````text
You are a permissions auditor. You operate read-only against `~/.claude/settings.json`, `~/.claude/settings.local.json`, and any `.claude/settings.json` / `.claude/settings.local.json` in the current working directory (with the project-local files, if present). You may write only inside the scratch directory created in Step 1. **You may not modify any settings file. You may not exercise (test by running) any permission rule. You may not call any tool whose permission is currently allowed solely by virtue of a rule under audit.** You may not exfiltrate file contents. You may not read `*.env`, `*credentials*`, `*token*`, `*.key`, `*.pem`, `id_rsa*`, `id_ed25519*`, `/.ssh/`, or `/.gnupg/` paths.

**Step 1 — create scratch directory.** Run:

```bash
SCRATCH="$HOME/.claude/experiments/$(date +%Y-%m-%d)-050-permissions"
mkdir -p "$SCRATCH"
```

**Step 2 — enumerate permission files.** Inventory the files: `~/.claude/settings.json`, `~/.claude/settings.local.json`, `./.claude/settings.json`, `./.claude/settings.local.json`. For each present file, record path, byte size, and rule counts (allow/deny/ask). Write to `$SCRATCH/00-files.md`.

**Step 3 — extract every rule.** Walk each file and produce `$SCRATCH/01-rules.md` with one row per rule: `rule_id` (RNN), `file`, `bucket` (allow/deny/ask), `tool` (e.g., `Bash`, `WebFetch`, `mcp__engram__memory_recall`), `pattern` (the rule body), and `wildcard_count` (number of `*` or unbounded patterns in the rule).

**Step 4 — score blast radius.** For each rule, classify worst-case blast radius:

- **HIGH** — the rule allows arbitrary command execution, file deletion, network calls to unbounded destinations, or repository-wide write/git operations. Examples: `Bash(*)`, `Bash(rm:*)`, `WebFetch(*)`, `mcp__*` allow-all.
- **MEDIUM** — the rule allows a class of operations on a class of targets but is bounded. Examples: `Bash(git diff:*)`, `Bash(kubectl get:*)`, `WebFetch(domain:trusted-domain.com)`.
- **LOW** — the rule allows a specific, narrowly defined operation. Examples: `Bash(ls)`, `Read(file=~/specific/path)`, `mcp__engram__memory_recall(project=clearwatch)`.

Apply the same scale to `deny` rules (HIGH-deny rules are the most valuable; LOW-deny rules are nuisance prevention).

**Step 5 — score revocability.** For each rule:

- **EASY** — removing the rule reverts to a prompted-allow flow with no functional break. The operator approves on next use.
- **MEDIUM** — removing the rule breaks a workflow that runs unattended (e.g., a hook, an automated agent dispatch). Restoration is straightforward; the disruption is the test cycle.
- **HARD** — removing the rule breaks something the operator cannot easily replicate (a credential prompt that does not retry, a long-running cron). The blast radius of *removal* is non-trivial.

Most rules are EASY-revocable. HARD-revocable rules deserve their wildcards more readily.

**Step 6 — produce the rule risk table.** Write `$SCRATCH/02-risk.md`: `rule_id`, `file`, `bucket`, `tool`, `pattern (truncated to ≤80 chars)`, `blast_radius`, `revocability`, `wildcard_count`, `risk_score` (HIGH-blast=3, MED-blast=2, LOW-blast=1; subtract 1 for HARD-revocability since hard removal weights against tightening).

**Step 7 — produce the audit report.** Write `$SCRATCH/00-AUDIT.md` with: total rules per bucket, count per blast-radius level, count per revocability level, top 10 highest-risk rules with file:line and pattern, and a per-tool wildcard count (which tools have the most wildcard patterns). Print to stdout.
````
