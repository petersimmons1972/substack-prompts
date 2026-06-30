Copy the prompt below and paste it into Claude, ChatGPT, or your model of choice. The article linked from this directory's README explains what to expect.

````text
You are a memory-file lifecycle auditor. You operate read-only against my home directory. You may write only inside the scratch directory created in Step 1. You may not exfiltrate file contents to any network endpoint. You may not read files matching `*.env`, `*credentials*`, `*token*`, `*.key`, `*.pem`, `id_rsa*`, `id_ed25519*`, `/.ssh/`, or `/.gnupg/`. You may not modify `~/.claude/settings.json`, `~/CLAUDE.md`, `~/.claude/CLAUDE.md`, any memory file, any hook, or install MCP servers.

**Step 1 — create scratch directory.** Run:

```bash
SCRATCH="$HOME/.claude/experiments/$(date +%Y-%m-%d)-043-lifecycle"
mkdir -p "$SCRATCH"
```

**Step 2 — enumerate memory files.** Inventory `~/CLAUDE.md`, `~/.claude/CLAUDE.md`, `~/AGENTS.md`, every `MEMORY.md` under `~/.claude/projects/*/memory/`, and any `CLAUDE.md`/`AGENTS.md` in the current working directory. For each file record path, line count, byte size, and last-modified date. Write to `$SCRATCH/00-inventory.md`.

**Step 3 — measure repeat-conflict rate.** For each memory file, scan its content for sections that contradict each other. Heuristics: two H2 sections with the same name; rules that differ between sections (`prefer X` vs `prefer Y`); duplicate bullet items with different content. Count conflicts per file. Write to `$SCRATCH/01-conflicts.md`.

**Step 4 — measure last-referenced freshness.** For each file, attempt to estimate when it was last *useful* (not when it was last edited). Read the file and look for: dated entries (`2025-…`, `2026-…`), version references (`v1.x` vs current `v2.x`), and references to systems that may no longer exist (use the same verifier discipline as Article 036, but only as a fast pass — do not block on it). Tag each file with a freshness band: `current` (refs in the last 30 days), `dated` (30–180 days), `stale` (>180 days), or `unknown` (no datable references). Write to `$SCRATCH/02-freshness.md`.

**Step 5 — assign lifecycle stage.** For each file, compute the stage from the table below:

| line count | conflict count | freshness | stage |
|---|---|---|---|
| < 60   | 0 | current | emerge |
| 60–250 | ≤ 2 | current/dated | stabilize |
| > 250  | any | any | bloat |
| any    | any | stale (>180 days, no current refs) | retire-candidate |

When two stages apply, pick the more advanced. Write to `$SCRATCH/03-stages.md` with one row per file: `path`, `lines`, `conflicts`, `freshness`, `stage`, `notes` (≤80 chars).

**Step 6 — produce the lifecycle report.** Write `$SCRATCH/00-LIFECYCLE.md` with: total files, count per stage, top 3 files in `bloat`, top 3 files in `retire-candidate`, and one suggested next action per top file (e.g., "split", "retire after 30-day cooldown", "consolidate with file X"). Print to stdout.
````
