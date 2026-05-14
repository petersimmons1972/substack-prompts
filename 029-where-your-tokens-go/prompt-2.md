You are a token-reduction planner. You operate read-only against my live AI configuration. You may write only inside the scratch directory used by Prompt 1. You may not exfiltrate file contents. You may not read `*.env`, `*credentials*`, `*token*`, `*.key`, `*.pem`, `id_rsa*`, `id_ed25519*`, `/.ssh/`, or `/.gnupg/` paths. You may not modify `~/.claude/settings.json`, `~/CLAUDE.md`, `~/.claude/CLAUDE.md`, `~/.claude/projects/-home-psimmons/memory/MEMORY.md`, `~/AGENTS.md`, any hook, or install MCP servers. You stage a fix; the human applies it.

**Step 1 — locate Prompt 1 output.** Run:

```bash
SCRATCH="$HOME/.claude/experiments/$(date +%Y-%m-%d)-029-token-decomp"
test -f "$SCRATCH/00-DECOMP.md" || { echo "ERROR: run prompt-1 first"; exit 1; }
```

Read `00-DECOMP.md`. Identify the largest bucket. If it is **B1 (system prompt)**, mark it non-reducible and walk down to the next bucket; record the skip in `$SCRATCH/20-reasoning.md`. Reducible buckets are B2 (memory), B3 (tools), B4 (history), B5 (attached). Record the chosen bucket in `$SCRATCH/20-target-bucket.md`.

**Step 2 — map bucket to live target.**

- **B2 (memory):** target the largest single file from `B2-memory.md`.
- **B3 (tools):** target `~/.claude/settings.json` enabled-server list.
- **B4 (history):** target the conversation in question — plan a restart point or handoff document.
- **B5 (attached):** target the prompting habit (large file paste-ins) — produce a guideline, not a file edit.

Write the target to `$SCRATCH/20-target.md`.

**Step 3 — back up the target.** For B2, copy the live file to scratch with a timestamped name and verify byte-count match. For B3, copy `~/.claude/settings.json` similarly. For B4 and B5, no backup needed (no live file mutation planned). Write `$SCRATCH/21-backup-verified.md` with both byte counts where applicable, or `N/A` for B4/B5.

**Step 4 — produce the proposed change.** Write the candidate to `$SCRATCH/22-proposed-<basename>` and the diff narrative to `$SCRATCH/23-diff.md`. Rules by bucket:

- **B2:** identify the three largest sections of the target memory file. Propose moving two to a referenced file (e.g., `~/TOOLS.md`) and replacing in-place with a one-line pointer. Show line-range removals and the pointer text. Estimate token delta.
- **B3:** list MCP servers in priority order based on usage frequency the reader can name. Propose disabling the bottom 1–2 servers. Show before/after `enabledMcpjsonServers` arrays. Estimate token delta as `400 * servers_removed`.
- **B4:** propose a restart-point — the turn at which a fresh conversation with a 5–10 line summary would yield equal-or-better quality at a fraction of context. Estimate token delta as `tokens_after_restart_point - 500`.
- **B5:** produce a one-page guideline naming three habits — paste line ranges not whole files, prefer `head/tail/grep` summaries, attach by reference (path) when the surface supports it. No live edit; the artifact is the guideline.

**Step 5 — produce the undo block.** Write `$SCRATCH/24-undo.sh` containing exactly one command for the bucket type:

- B2/B3: `cp -p "$SCRATCH/backup-<TS>-<basename>" "<target>"`
- B4/B5: `# no live mutation planned; deleting scratch fully reverts`

Make it executable.

**Step 6 — write the plan summary.** Produce `$SCRATCH/20-PLAN.md` with: target, bucket id, what changes (one paragraph), the apply command (if any), the undo command, expected token delta (absolute and as % of total), and the bucket(s) that should drop on the next Prompt 1 re-run. Print to stdout.
