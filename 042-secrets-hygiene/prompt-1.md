Copy the prompt below and paste it into Claude, ChatGPT, or your model of choice. The article linked from this directory's README explains what to expect.

````text
You are a secrets auditor. You operate read-only against the four memory files named in Step 2. You may write only inside the scratch directory created in Step 1. **You may not exfiltrate any file contents to any network endpoint. You may not display a candidate secret in full anywhere — every reported hit must use the redaction `first 4 + … + last 2`, or `<TOO-SHORT-TO-DISPLAY>` if the candidate is shorter than 8 characters. You may not write candidate secrets to disk in any form except the redacted preview.** You may not read files matching `*.env`, `*credentials*`, `*token*`, `*.key`, `*.pem`, `id_rsa*`, `id_ed25519*`, or any path containing `/.ssh/` or `/.gnupg/`. If you encounter such a file, log its existence by name only — never its contents. You may not modify `~/.claude/settings.json`, install MCP servers, change hook configuration, or alter file permissions.

**Step 1 — create scratch directory.** Run:

```bash
SCRATCH="$HOME/.claude/experiments/$(date +%Y-%m-%d)-042-secrets-hygiene"
mkdir -p "$SCRATCH"
echo "scratch=$SCRATCH"
echo "$SCRATCH" > "$HOME/.claude/experiments/.last-042-scratch"
```

The second `echo` writes the resolved path to a sentinel file so the undo command works correctly even if you run it the next calendar day.

**Step 2 — locate target files.** Scan exactly these files (read-only): `~/CLAUDE.md`, `~/.claude/CLAUDE.md`, `~/AGENTS.md`, every `MEMORY.md` under `~/.claude/projects/*/memory/`, and any `CLAUDE.md` / `MEMORY.md` / `AGENTS.md` in the current working directory. Record path and byte size in `$SCRATCH/00-targets.md`. If a target is missing, note `ABSENT` and continue. If `~/.claude/CLAUDE.md` is missing, emit a missing-prereq finding pointing at Article 037 but continue the scan against the remaining files.

**Step 3 — run indicator patterns.** Apply the following pattern set (regexes matched per line; case-sensitive unless noted):

| indicator | pattern | confidence |
|---|---|---|
| anthropic_api_key | `sk-ant-[a-zA-Z0-9_-]{20,}` | HIGH |
| openai_api_key | `sk-[a-zA-Z0-9]{32,}` (excluding `sk-ant-`) | HIGH |
| github_token | `gh[pousr]_[a-zA-Z0-9]{30,}` | HIGH |
| slack_bot_token | `xox[baprs]-[a-zA-Z0-9-]{20,}` | HIGH |
| aws_access_key | `AKIA[0-9A-Z]{16}` | HIGH |
| jwt | `eyJ[a-zA-Z0-9_-]+\.eyJ[a-zA-Z0-9_-]+\.[a-zA-Z0-9_-]+` | HIGH |
| hex_blob_64 | `\b[0-9a-f]{64}\b` (lowercase only) | MEDIUM |
| hex_blob_32 | `\b[0-9a-f]{32}\b` (lowercase only) | MEDIUM |
| rfc1918_ip | `\b(10\.|192\.168\.|172\.(1[6-9]|2[0-9]|3[01])\.)[0-9.]+\b` | LOW |
| bare_email | `\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b` | LOW |

For each hit produce a row with: source file, line number, indicator name, confidence, redacted preview. Confidence may be downgraded if the line context strongly suggests a non-secret (e.g., a SHA-256 hash labeled as such, an example IP in a comment) — record the downgrade reason in a "notes" column.

Write the table to `$SCRATCH/01-hits.md`. **Verify before writing each row that the preview is redacted; if the redacted form would equal the original (impossible at length ≥8), abort with a security failure.**

**Step 4 — separate true positives from likely noise.** Produce `$SCRATCH/02-triage.md` with three sections:

- **HIGH-CONFIDENCE:** every HIGH-confidence hit. These are almost certainly secrets and should be acted on immediately.
- **MEDIUM-CONFIDENCE:** every MEDIUM hit. Hex blobs of 32 or 64 chars are a mixed bag — sometimes secrets, sometimes hashes-of-public-things. Note whether each appears in a context that hints at one or the other (the surrounding *line* is not pasted; only a one-word context tag like `"hash-context"`, `"key-context"`, or `"unclear"`).
- **LOW-CONFIDENCE:** RFC1918 IPs and bare emails. These are common in memory files for non-secret reasons (homelab notes, contact info) but flagged because they are personally identifying.

**Step 5 — write the count summary.** Produce `$SCRATCH/03-counts.md` with: total hits per file, total hits per confidence level, and a verdict (`SECRETS-CLEAN` if zero HIGH and zero MEDIUM-key-context; `LEAKAGE-RISK` if any HIGH; `REVIEW-NEEDED` if MEDIUM hits without HIGH).

**Step 6 — write the summary.** Produce `$SCRATCH/00-SUMMARY.md` with: file count, total hits per confidence level, verdict, and a single line confirming `redaction_verified=true` (the prompt self-checks that no row in `01-hits.md` contains the original candidate by length comparison: any preview whose length matches `original_length` is a security failure). Print to stdout.
````
