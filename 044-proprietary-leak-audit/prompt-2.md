Copy the prompt below and paste it into Claude, ChatGPT, or your model of choice. The article linked from this directory's README explains what to expect.

````text
You are a redaction-with-meaning-preservation planner. You operate read-only against the live files identified by Prompt 1. You may write only inside the scratch directory used by Prompt 1. **You may not display any candidate identifier in full anywhere. You may not write candidates to disk. The diff in scratch must show only the replacement placeholder text and the surrounding context, never the original candidate.** You may not send content over the network. You may not read `*.env`, `*credentials*`, `*token*`, `*.key`, `*.pem`, `id_rsa*`, `id_ed25519*`, `/.ssh/`, or `/.gnupg/` paths. You may not modify live files, `~/.claude/settings.json`, any hook, or install MCP servers.

**Step 1 — locate scratch and the hit list.** Run:

```bash
SCRATCH="$HOME/.claude/experiments/$(date +%Y-%m-%d)-044-leak-audit"
test -f "$SCRATCH/01-hits.md" || { echo "ERROR: run prompt-1 first"; exit 1; }
```

Read `01-hits.md` and `02-triage.md`. Process HIGH hits in shipping drafts and MEDIUM hits in shipping drafts. Defer to `$SCRATCH/50-deferred.md`: LOW hits anywhere, and memory-only HIGH/MEDIUM hits (operator decides per-file whether to redact memory).

**Step 2 — back up every target file.** For each file with at least one in-scope hit:

```bash
TARGET="<path>"; TS="$(date +%Y%m%d-%H%M%S)"
cp -p "$TARGET" "$SCRATCH/backup-${TS}-$(basename "$TARGET")"
```

Verify byte and md5. Record in `$SCRATCH/51-backup-verified.md`.

**Step 3 — choose a placeholder per indicator.** For each in-scope hit, pick a placeholder that preserves the technical claim:

| indicator | placeholder template | example before/after |
|---|---|---|
| client_name | `<CLIENT_A>`, `<CLIENT_B>`, … (consistent letters across the run) | `Acme rolled it out → <CLIENT_A> rolled it out` |
| real_domain | `<INTERNAL_HOST>` or `example.com` if the line is generic | `prod.acme-internal.com → <INTERNAL_HOST>` |
| internal_repo | `<ORG>/<REPO>` | `github.com/acme-corp/api → <ORG>/<REPO>` |
| ticket_id | `<TICKET-NNN>` | `JIRA-12847 → <TICKET-NNN>` |
| rfc1918_ip | `10.0.0.0/8 (private)` or remove the octet | `192.168.4.12 → <PRIVATE_IP>` |
| bare_phone_us | `<PHONE>` | `(415) 555-1212 → <PHONE>` |
| bare_email_ext | `<EMAIL>` | `jane@acme.com → <EMAIL>` |

Record per-hit decisions in `$SCRATCH/52-plan.md`: `file`, `line`, `indicator`, `placeholder`, `meaning_preserved=yes/no` (the planner's self-assessment of whether the surrounding sentence still makes its point after replacement).

**Step 4 — stage modified files.** For each target with at least one in-scope hit, write a redacted copy to `$SCRATCH/53-modified-<basename>`. Walk lines, replace candidates with placeholders. **Do not write the original line to scratch under any name; the modified copy contains only replaced text.** Verify each modified copy contains the expected placeholder count via `grep -c "<.*>"` against the placeholder list. Record verification in `$SCRATCH/54-replacement-verified.md`.

**Step 5 — meaning-preservation smoke test.** For each modified copy, read three randomly chosen redacted lines and judge whether the technical claim is still intelligible without the original identifier. Score `OK` (meaning preserved) or `BROKEN` (placeholder leaves the sentence ambiguous; rewrite needed). Lines scored BROKEN go on a per-file rewrite list; the operator rewrites the surrounding prose by hand before applying. Record in `$SCRATCH/55-smoke.md`.

**Step 6 — produce apply and undo.** Write `$SCRATCH/56-apply.sh` containing one `cp -p` per modified file (modified copy → live path). Write `$SCRATCH/57-undo.sh` containing one `cp -p` per backup (backup → live path). Make both executable. Print `52-plan.md`, `54-replacement-verified.md`, and `55-smoke.md` to stdout. Do not print modified file contents to stdout.
````
