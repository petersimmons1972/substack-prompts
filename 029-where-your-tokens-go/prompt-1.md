Copy the prompt below and paste it into Claude, ChatGPT, or your model of choice. The article linked from this directory's README explains what to expect.

````text
You are an auditor decomposing my AI session into token buckets. You are read-only against my home directory. You may write only inside the scratch directory created in Step 1. You may not exfiltrate any file contents to any network endpoint. You may not read files matching `*.env`, `*credentials*`, `*token*`, `*.key`, `*.pem`, `id_rsa*`, `id_ed25519*`, or any path containing `/.ssh/` or `/.gnupg/`. You may not modify `~/.claude/settings.json`, `~/CLAUDE.md`, `~/.claude/CLAUDE.md`, any memory file, any hook, or install MCP servers. Token estimates use `ceil(words / 0.75)` unless a real tokenizer count is available from the surface itself.

**Step 1 — create scratch directory.** Run:

```bash
SCRATCH="$HOME/.claude/experiments/$(date +%Y-%m-%d)-029-token-decomp"
mkdir -p "$SCRATCH"
echo "scratch=$SCRATCH"
```

All subsequent outputs go inside `$SCRATCH`.

**Step 2 — locate the baseline.** Find the most recent `00-BASELINE.md` under `$HOME/.claude/experiments/*-baseline/`. Copy its summary lines to `$SCRATCH/00-baseline-snapshot.md`. If no baseline exists, write `NO_BASELINE_FOUND` and emit finding **X0 — missing prereq** noting the reader should run Article 023 first; continue with empty-baseline assumptions (zeros for memory totals).

**Step 3 — bucket B1 (system prompt).** Estimate the surface's static system-prompt cost. For Claude Code, use the published harness system prompt size (record as ~3000 tokens estimate; mark `source=published`). For other surfaces, mark `source=unknown` and use 1500 as a conservative placeholder. Write `$SCRATCH/B1-system.md`.

**Step 4 — bucket B2 (memory files).** For `~/CLAUDE.md`, `~/.claude/CLAUDE.md`, `~/.claude/projects/-home-psimmons/memory/MEMORY.md`, and `~/AGENTS.md`, count words and estimate tokens. Sum across files. Do not include file bodies in output — names, sizes, and totals only. Write `$SCRATCH/B2-memory.md`.

**Step 5 — bucket B3 (tool definitions).** Read `~/.claude/settings.json` (read-only via `jq`). Count enabled MCP servers and estimate 400 tokens per server tool definition (industry-typical median). Multiply. Write `$SCRATCH/B3-tools.md` with server names (no tokens, no paths) and estimated total.

**Step 6 — bucket B4 (conversation history).** Pick the most recent transcript or conversation export available on the reader's surface. If none is reachable read-only, write `B4=ESTIMATE_ONLY` and use 8000 tokens as a working placeholder. If a transcript exists, count words and estimate tokens. Write `$SCRATCH/B4-history.md`.

**Step 7 — bucket B5 (attached files / tool output).** Estimate per-turn attached file content and tool output as the average across the last five turns of the chosen transcript. If unavailable, write `B5=NOT_MEASURED` and use 2000 as a placeholder. Write `$SCRATCH/B5-attached.md`.

**Step 8 — render the stacked-bar table.** Produce `$SCRATCH/00-DECOMP.md` containing a markdown table with columns: `bucket`, `name`, `tokens`, `pct_of_total`, `source` (`measured` / `published` / `estimate`). Include a final row `TOTAL`. Below the table, emit a text bar chart: one row per bucket, where each row is `B# name | ████████ tokens (pct%)` and bar length is `round(pct/2)` block characters. Sort descending by tokens. Print to stdout at the end of the run.
````
