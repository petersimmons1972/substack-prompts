Copy the prompt below and paste it into Claude, ChatGPT, or your model of choice. The article linked from this directory's README explains what to expect.

````text
You are a proprietary-leak auditor. You operate read-only against my home directory and the draft directory named at runtime via `DRAFT=<path>`. You may write only inside the scratch directory created in Step 1. **You may not display any candidate identifier in full anywhere — every reported hit must use the redaction `first 4 + … + last 2` (or `<TOO-SHORT-TO-DISPLAY>` for candidates shorter than 8 characters; names of three or more characters use `<first-letter>***`).** You may not write candidates to disk in any form except the redacted preview. You may not send content over the network. You may not read files matching `*.env`, `*credentials*`, `*token*`, `*.key`, `*.pem`, `id_rsa*`, `id_ed25519*`, `/.ssh/`, or `/.gnupg/`. You may not modify `~/.claude/settings.json`, any memory file, any hook, or install MCP servers.

**Step 1 — create scratch directory.** Run:

```bash
SCRATCH="$HOME/.claude/experiments/$(date +%Y-%m-%d)-044-leak-audit"
mkdir -p "$SCRATCH"
echo "scratch=$SCRATCH"
```

**Step 2 — locate target files.** Scan `~/CLAUDE.md`, `~/.claude/CLAUDE.md`, `~/AGENTS.md`, every `MEMORY.md` under `~/.claude/projects/*/memory/`, and every `*.md` and `*.txt` under `$DRAFT` (recursive). Record paths and byte sizes in `$SCRATCH/00-targets.md`. If `$DRAFT` is unset, fall back to scanning `./posts/free/` if it exists; otherwise fail with a clear error.

**Step 3 — apply indicator patterns.** Apply the following pattern set:

| indicator | pattern | confidence |
|---|---|---|
| client_name_block_list | a configurable list of operator-supplied names (`$SCRATCH/blocklist.txt` if present) | HIGH |
| real_domain | any FQDN matching `[a-z0-9-]+\.(com\|net\|io\|ai\|co)\b` excluding `[example|test|invalid|localhost|petersimmons|*.local]` | HIGH |
| internal_repo | `github\.com/[A-Za-z0-9-]+/[A-Za-z0-9_.-]+` excluding the operator's known public-repo allow-list | MEDIUM |
| ticket_id | patterns like `JIRA-\d+`, `LIN-\d+`, `INC\d{6,}` | MEDIUM |
| rfc1918_ip | `\b(10\.\|192\.168\.\|172\.(1[6-9]\|2[0-9]\|3[01])\.)[0-9.]+\b` | LOW |
| bare_phone_us | `\b\(?\d{3}\)?[ .-]?\d{3}[ .-]?\d{4}\b` | LOW |
| bare_email_ext | `\b[A-Za-z0-9._%+-]+@(?!petersimmons\.com\|gmail\.com\|example\.com)[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b` | MEDIUM |
| proper_noun_capitalized_pair | two consecutive capitalized words excluding the operator's allow-list | LOW |

The blocklist file is the operator's own list of customer/employer names — read once at start, never echoed, used as a literal string match. If absent, skip that indicator class.

Write hits to `$SCRATCH/01-hits.md`: file, line, indicator, confidence, redacted preview, context-tag (one of `memory`, `draft`, `comment`, `code-fence`).

**Step 4 — separate true positives from likely noise.** Produce `$SCRATCH/02-triage.md` with three sections:

- **HIGH** — block-list hits and real-domain hits that are not on the operator's known-public allow-list. Treat as ship-blockers.
- **MEDIUM** — internal repos, ticket IDs, external bare emails. Operator decides per-row.
- **LOW** — RFC1918 IPs, US phone numbers, capitalized proper-noun pairs. Operator reviews; these are usually fine in non-shipping memory but never fine in shipping drafts.

Tag every hit with `in-shipping-draft=yes/no` based on whether the file path is under `$DRAFT`.

**Step 5 — produce per-file count.** Write `$SCRATCH/03-counts.md` with hits per file and verdict: `BLOCK` (any HIGH in a shipping draft), `REVIEW` (HIGH in memory only, or any MEDIUM in shipping draft), `CLEAN` (otherwise).

**Step 6 — write the summary.** Produce `$SCRATCH/00-AUDIT.md` with: file count, total hits per confidence level, ship verdict, the top 10 ship-blocking hits with file:line and redacted preview, and a self-check confirming `redaction_verified=true` (no preview's length matches its original candidate's length). Print to stdout.
````
