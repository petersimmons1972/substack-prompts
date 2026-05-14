You are an inventory analyst. You are read-only against my home directory. You may write only inside the scratch directory created in Step 1. You may not exfiltrate file contents to any network endpoint. You may not read files matching `*.env`, `*credentials*`, `*token*`, `*.key`, `*.pem`, `id_rsa*`, `id_ed25519*`, or any path containing `/.ssh/` or `/.gnupg/`. You may not modify `~/.claude/settings.json`, `~/CLAUDE.md`, `~/.claude/CLAUDE.md`, `~/.claude/projects/-home-psimmons/memory/MEMORY.md`, `~/AGENTS.md`, install MCP servers, change hook configuration, or alter file permissions. If a step would require any of those, stop and report the blocker.

**Step 1 — create scratch directory.** Run:

```bash
SCRATCH="$HOME/.claude/experiments/$(date +%Y-%m-%d)-022-inventory"
mkdir -p "$SCRATCH"
echo "scratch=$SCRATCH"
```

**Step 2 — accept the export.** Ask me for one of: a path to a Claude Code transcript file under `~/.claude/projects/`; a path to a Claude.ai or ChatGPT data-export JSON; or a paste of one conversation. If I provide a path, confirm it does not match the forbidden patterns and is under 5 MB. Copy verbatim to `$SCRATCH/01-export.raw`. If no export is available, write `NO_EXPORT_AVAILABLE` and proceed with a synthetic 10-segment example you generate; flag this as finding I0 — operator does not yet know how to export their conversations.

**Step 3 — bucket every segment.** Map each segment to exactly one of these five buckets. The mapping rule, applied in order:

- **`system_prompt`** — the platform-supplied system message.
- **`memory_files`** — any segment loaded from `CLAUDE.md`, `MEMORY.md`, `AGENTS.md`, or labeled in the export as a memory injection.
- **`tool_definitions`** — JSON schemas of tools available to the model (often appears once near session start).
- **`conversation_history`** — every prior user turn, assistant turn, tool call, and tool result that is not the most recent.
- **`current_turn`** — the most recent user turn plus the most recent assistant turn (the "live" exchange).

Write `$SCRATCH/02-buckets.md` with one row per segment: `idx`, `bucket`, `bytes`, `~tokens` (`ceil(bytes / 4)`).

**Step 4 — aggregate.** Produce `$SCRATCH/03-aggregate.md` with one row per bucket: `bucket`, `count`, `total_tokens`, `pct`. Sort descending by `total_tokens`.

**Step 5 — render the stacked bar.** Produce `$SCRATCH/04-stackbar.md` containing a single horizontal markdown bar 50 cells wide, where each cell is one of the bucket initials (`S`, `M`, `T`, `H`, `C`) in proportion to that bucket's percentage. Below the bar print the legend with bucket totals. Example output shape:

```
| MMMMMMMMMMHHHHHHHHHHHHHHHHHHHHHHHHCCCCCCSSTT...... |
S system_prompt    1,028  3.3%
M memory_files     6,210 19.8%
T tool_definitions   840  2.7%
H conversation_hist 14,880 47.4%
C current_turn     1,930  6.1%
```

**Step 6 — flag the dominant bucket.** Identify the bucket with the highest token share. Write `$SCRATCH/05-flag.md` naming the bucket and a one-sentence interpretation. Reference rules:

- `memory_files` >25% → bloat candidate, points at Article 037.
- `conversation_history` >50% → conversation lifecycle issue, points at Article 030.
- `tool_definitions` >15% → too many tools loaded, points at Article 040.
- `system_prompt` >15% → unusual; suggests a custom instructions sprawl.

**Step 7 — write the takeaway.** Produce `$SCRATCH/00-INVENTORY.md` with: export source, total tokens, dominant bucket and its share, and the one-line interpretation from Step 6. Print to stdout.
