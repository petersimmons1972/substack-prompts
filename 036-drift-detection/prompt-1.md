Copy the prompt below and paste it into Claude, ChatGPT, or your model of choice. The article linked from this directory's README explains what to expect.

````text
You are a memory-file auditor checking claims against live state. You are read-only against my home directory. You may write only inside the scratch directory created in Step 1. You may not exfiltrate any file contents to any network endpoint. You may not read files matching `*.env`, `*credentials*`, `*token*`, `*.key`, `*.pem`, `id_rsa*`, `id_ed25519*`, or any path containing `/.ssh/` or `/.gnupg/`. You may not modify `~/.claude/settings.json`, `~/CLAUDE.md`, `~/.claude/CLAUDE.md`, `~/.claude/projects/-home-psimmons/memory/MEMORY.md`, `~/AGENTS.md`, any other memory file, any hook, or install MCP servers.

**Step 1 — create scratch directory.** Run:

```bash
SCRATCH="$HOME/.claude/experiments/$(date +%Y-%m-%d)-036-drift"
mkdir -p "$SCRATCH"
echo "scratch=$SCRATCH"
```

**Step 2 — enumerate memory files.** List the candidate set: `~/CLAUDE.md`, `~/.claude/CLAUDE.md`, `~/.claude/projects/-home-psimmons/memory/MEMORY.md`, `~/AGENTS.md`, plus any `~/projects/*/CLAUDE.md` or `~/projects/*/AGENTS.md` files reachable read-only. Write the discovered list to `$SCRATCH/00-files.md`. Skip any file matching the deny-list path patterns above (none should match, but log each skip).

**Step 3 — extract claims.** For each memory file, extract claims that reference specific live state. Five claim types:

- **C1 — file path:** any absolute path or `~`-prefixed path mentioned as existing.
- **C2 — command:** any bash/CLI command quoted as a working invocation (e.g., `~/bin/health-check.sh`, `kubectl get pods -n default`).
- **C3 — function/script reference:** any function name or script basename used as if importable/runnable.
- **C4 — flag/option:** any CLI flag (`--foo`) or environment variable (`$BAR`) named as having a specific behavior.
- **C5 — version/count:** any specific number that asserts current state (e.g., "9 nodes ready," "29 allow rules").

Write per-file claim lists to `$SCRATCH/01-claims-<basename>.md`. Each row: `id`, `type`, `claim_text` (≤80 chars), `verifier_command` — the command that would test the claim, e.g., `test -e <path>`, `command -v <cli>`, `grep -q <flag> <file>`.

**Step 4 — verify each claim.** For every claim, run the verifier command read-only and record the result: `OK`, `STALE`, `UNVERIFIABLE` (verifier could not be safely run, e.g., would require modifying state). For C5 (version/count), `STALE` requires the live count to differ from the claimed count by more than ±1. Write `$SCRATCH/02-verified.md`.

**Step 5 — risk-rank stale claims.** For each `STALE` claim, assign a risk: `high` (the AI will act on this and break something — typically C1, C2, C4 stale), `medium` (the AI will state this confidently to the user — typically C3, C5 stale), `low` (informational drift, no action consequence). Write `$SCRATCH/03-ranked.md`.

**Step 6 — produce the drift report.** Write `$SCRATCH/00-DRIFT.md` with: total claims found, claims verified OK, claims stale, claims unverifiable, top 10 stale claims by risk with file:line, claim, verifier, and live state. Print to stdout. Do not echo memory file bodies — only the extracted claims and the verifier results.
````
