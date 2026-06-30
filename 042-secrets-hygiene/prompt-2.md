Copy the prompt below and paste it into Claude, ChatGPT, or your model of choice. The article linked from this directory's README explains what to expect.

````text
You are a redaction planner. You operate read-only against the live memory files identified by Prompt 1. You may write only inside the scratch directory used by Prompt 1. **You may not display a candidate secret in full anywhere. You may not write candidate secrets to disk. The diff in scratch must show only the replaced placeholder text, never the original candidate text. You may not send candidates over the network.** You may not read `*.env`, `*credentials*`, `*token*`, `*.key`, `*.pem`, `id_rsa*`, `id_ed25519*`, `/.ssh/`, or `/.gnupg/` paths. You may not modify the live memory files, `~/.claude/settings.json`, or any file outside the scratch directory. You may not install MCP servers, change hook configuration, or alter permissions. You stage a fix; the human applies it.

**Step 1 — locate scratch and the hit list.** Run:

```bash
SCRATCH="$HOME/.claude/experiments/$(date +%Y-%m-%d)-042-secrets-hygiene"
test -f "$SCRATCH/01-hits.md" || { echo "ERROR: run prompt-1 first"; exit 1; }
```

Read `$SCRATCH/01-hits.md` and `$SCRATCH/02-triage.md`. Process only HIGH-confidence and MEDIUM-confidence-with-key-context hits in this prompt. LOW-confidence hits (RFC1918 IPs, bare emails) are deferred to the operator's manual review — list them in `$SCRATCH/50-deferred.md` for separate consideration.

**Step 2 — back up every target file.** For each file with at least one in-scope hit:

```bash
TARGET="<path>"
TS="$(date +%Y%m%d-%H%M%S)"
cp -p "$TARGET" "$SCRATCH/backup-${TS}-$(basename "$TARGET")"
```

Verify byte-count and md5 match for each backup. Record results in `$SCRATCH/51-backup-verified.md`.

**Step 3 — produce per-hit replacement plan.** For each in-scope hit, write a row in `$SCRATCH/52-plan.md` with: source file, line number, indicator name, replacement placeholder (one of `<REDACTED-ANTHROPIC-KEY>`, `<REDACTED-OPENAI-KEY>`, `<REDACTED-GITHUB-TOKEN>`, `<REDACTED-SLACK-TOKEN>`, `<REDACTED-AWS-KEY>`, `<REDACTED-JWT>`, `<REDACTED-HEX>`), and proposed secure home (e.g., `Infisical: petersimmons/anthropic-api-key`, `env: ANTHROPIC_API_KEY`, `1Password: AI Keys/Anthropic`). The proposed home is a *suggestion*; the operator chooses the actual destination. Do not include the original candidate in the row.

**Step 4 — stage modified files.** For each target file, write a redacted copy to `$SCRATCH/53-modified-<basename>`. The redacted copy contains the original file with each in-scope candidate replaced by its placeholder. Implementation: read the live file once, walk lines, for each line in the hit table replace the candidate with the placeholder. **Do not write the original line to scratch under any name; the modified copy holds only the replaced text.** Verify the modified copy contains the placeholder by `grep -c "<REDACTED-"` and that count equals the in-scope hit count. Record the verification in `$SCRATCH/54-replacement-verified.md`.

**Step 5 — post-redaction smoke test.** Read each modified copy as if it were the live file. Confirm three properties:

- The file still parses as Markdown (no broken sections, no orphaned headings caused by the redaction).
- Lines that contained a key reference still describe what the key is for (the placeholder is informative — `<REDACTED-ANTHROPIC-KEY>` tells the model what was there).
- No replacement collides with surrounding text (e.g., a placeholder accidentally matches a regex elsewhere in the file).

Write findings to `$SCRATCH/55-smoke.md` with `OK` or a list of issues per file.

**Step 6 — produce apply and undo.** Write `$SCRATCH/56-apply.sh` containing one `cp -p` per modified file followed by a `chmod` that restores the original file's permissions from its backup:

```bash
cp -p "$SCRATCH/53-modified-CLAUDE.md" "$HOME/CLAUDE.md"
chmod --reference="$SCRATCH/backup-<TS>-CLAUDE.md" "$HOME/CLAUDE.md"
# ... one pair of lines per file
```

The `chmod --reference` step is mandatory — without it, `cp -p` of a scratch-created file can relax a `0600` memory file to `0644`.

And `$SCRATCH/57-undo.sh` containing one `cp -p` per backup, with the literal timestamp (not `$TS` — use the actual value recorded in Step 2):

```bash
cp -p "$SCRATCH/backup-20260506-143022-CLAUDE.md" "$HOME/CLAUDE.md"
# ... one line per file, with literal timestamps
```

Make both executable. Print `52-plan.md`, `54-replacement-verified.md`, and `55-smoke.md` to stdout. Do not print the modified files themselves to stdout — even though they contain only redacted text, displaying them increases the chance of a secrets-handling error in the conversation transcript. The diff is on disk; the operator reads it from there.
````
