Copy the prompt below and paste it into Claude, ChatGPT, or your model of choice. The article linked from this directory's README explains what to expect.

````text
You are a memory-correction stager. You operate read-only against my home directory. You may write only inside the scratch directory used by Prompt 1 (or create it if Prompt 1 was skipped). You may not exfiltrate any file contents to any network endpoint. You may not read `*.env`, `*credentials*`, `*token*`, `*.key`, `*.pem`, `id_rsa*`, `id_ed25519*`, `/.ssh/`, or `/.gnupg/` paths. You may not modify `~/.claude/settings.json`, `~/CLAUDE.md`, `~/.claude/CLAUDE.md`, `~/.claude/projects/-home-psimmons/memory/MEMORY.md`, `~/AGENTS.md`, any other memory file, any hook, or install MCP servers. **You must not edit live memory files under any circumstance.** All corrections are written to scratch only as patch files.

**Step 1 — create or reuse scratch.** Run:

```bash
SCRATCH="$HOME/.claude/experiments/$(date +%Y-%m-%d)-036-drift"
mkdir -p "$SCRATCH/patches"
```

**Step 2 — load the drift report.** If `$SCRATCH/00-DRIFT.md` and `$SCRATCH/03-ranked.md` exist, read them. If not, re-run Prompt 1's Steps 2–5 to produce them, then continue. Stale claims of risk `low` are excluded from staging — they are recorded but not corrected, to keep the patch surface small.

**Step 3 — derive the corrected text for each stale claim.** For each `STALE` claim of risk `high` or `medium`, propose one of three actions:

- **REWRITE** — the claim is still relevant but the specifics changed. Produce the new line, computed from the verifier's live state. Example: claim says `~/bin/health-check.sh` but verifier shows `~/bin/cluster-health.sh` exists; rewrite the line with the new path.
- **DELETE** — the claim points to a thing that no longer exists in any form. Example: a flag that was removed entirely. Propose a deletion of the line.
- **DEFER** — the live state is ambiguous (verifier returned `UNVERIFIABLE`, or the live state has shifted in a way the auditor cannot resolve mechanically). Do not propose a change; record the claim with a `human-review` tag.

Write the per-claim decisions to `$SCRATCH/04-decisions.md`: one row per claim with `id`, `file`, `line`, `action`, `old_text`, `new_text` (empty for DELETE / DEFER), `rationale` (≤120 chars).

**Step 4 — produce one patch file per memory file.** For each memory file with at least one REWRITE or DELETE decision, generate a unified diff of all proposed changes against the current file content. Write to `$SCRATCH/patches/<basename>.patch`. Use standard `diff -u` format so the operator can review it with `git apply --check` or apply it manually. Do **not** run `patch` or `git apply`. Do **not** write into the original file.

**Step 5 — verify the patches are syntactically valid.** For each patch, run `git apply --check "$SCRATCH/patches/<basename>.patch"` from the directory containing the live file (read-only check; `--check` does not modify state). Record PASS/FAIL in `$SCRATCH/05-patch-check.md`. Patches that fail the check must be regenerated; if they fail twice, downgrade their decisions to DEFER and rewrite the patch without those rows.

**Step 6 — produce the staging report.** Write `$SCRATCH/00-CORRECT.md` with: total stale claims considered, count by action (REWRITE / DELETE / DEFER), per-file patch path, patch-check result, and an "apply when ready" block showing the exact `git apply` command the operator would run for each patch — but do not run it. Print to stdout. Do not echo memory-file bodies; print only the proposed corrections and rationales.

**Step 7 — record a human-review queue.** Write `$SCRATCH/06-review-queue.md` listing every DEFER claim with the file, line, claim text, verifier output, and a one-sentence reason the auditor could not resolve it. This is the operator's manual to-do list.
````
