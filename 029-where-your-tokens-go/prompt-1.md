# Token Decomposition Prompt — Where Your Tokens Actually Go

**Article:** 029 — Where your tokens go (Prompt 1 of 2).
**Consumes:** Article 023 baseline (`$HOME/.claude/experiments/<DATE>-baseline/00-BASELINE.md`).
**Surfaces:** Claude Code primary; the bucketing scheme adapts to the API (request-side `usage` field) and ChatGPT custom instructions.
**Run mode:** read-only against your home directory; writes only to a dated scratch directory.

---

## What this prompt does

Decomposes one real session's token cost into named buckets — system prompt, memory files, tool definitions, conversation history, attached files, and tool output — then renders the result as a markdown stacked-bar table so you can see at a glance which bucket dominates. The point is not the absolute number; the point is the *shape*. Most readers discover one bucket they did not know existed eating 30%+ of every turn. The prompt does not modify any live file.

## Run this prompt

> You are an auditor decomposing my AI session into token buckets. You are read-only against my home directory. You may write only inside the scratch directory created in Step 1. You may not exfiltrate any file contents to any network endpoint. You may not read files matching `*.env`, `*credentials*`, `*token*`, `*.key`, `*.pem`, `id_rsa*`, `id_ed25519*`, or any path containing `/.ssh/` or `/.gnupg/`. You may not modify `~/.claude/settings.json`, `~/CLAUDE.md`, `~/.claude/CLAUDE.md`, any memory file, any hook, or install MCP servers. Token estimates use `ceil(words / 0.75)` unless a real tokenizer count is available from the surface itself.
>
> **Step 1 — create scratch directory.** Run:
>
> ```bash
> SCRATCH="$HOME/.claude/experiments/$(date +%Y-%m-%d)-029-token-decomp"
> mkdir -p "$SCRATCH"
> echo "scratch=$SCRATCH"
> ```
>
> All subsequent outputs go inside `$SCRATCH`.
>
> **Step 2 — locate the baseline.** Find the most recent `00-BASELINE.md` under `$HOME/.claude/experiments/*-baseline/`. Copy its summary lines to `$SCRATCH/00-baseline-snapshot.md`. If no baseline exists, write `NO_BASELINE_FOUND` and emit finding **X0 — missing prereq** noting the reader should run Article 023 first; continue with empty-baseline assumptions (zeros for memory totals).
>
> **Step 3 — bucket B1 (system prompt).** Estimate the surface's static system-prompt cost. For Claude Code, use the published harness system prompt size (record as ~3000 tokens estimate; mark `source=published`). For other surfaces, mark `source=unknown` and use 1500 as a conservative placeholder. Write `$SCRATCH/B1-system.md`.
>
> **Step 4 — bucket B2 (memory files).** For `~/CLAUDE.md`, `~/.claude/CLAUDE.md`, `~/.claude/projects/-home-psimmons/memory/MEMORY.md`, and `~/AGENTS.md`, count words and estimate tokens. Sum across files. Do not include file bodies in output — names, sizes, and totals only. Write `$SCRATCH/B2-memory.md`.
>
> **Step 5 — bucket B3 (tool definitions).** Read `~/.claude/settings.json` (read-only via `jq`). Count enabled MCP servers and estimate 400 tokens per server tool definition (industry-typical median). Multiply. Write `$SCRATCH/B3-tools.md` with server names (no tokens, no paths) and estimated total.
>
> **Step 6 — bucket B4 (conversation history).** Pick the most recent transcript or conversation export available on the reader's surface. If none is reachable read-only, write `B4=ESTIMATE_ONLY` and use 8000 tokens as a working placeholder. If a transcript exists, count words and estimate tokens. Write `$SCRATCH/B4-history.md`.
>
> **Step 7 — bucket B5 (attached files / tool output).** Estimate per-turn attached file content and tool output as the average across the last five turns of the chosen transcript. If unavailable, write `B5=NOT_MEASURED` and use 2000 as a placeholder. Write `$SCRATCH/B5-attached.md`.
>
> **Step 8 — render the stacked-bar table.** Produce `$SCRATCH/00-DECOMP.md` containing a markdown table with columns: `bucket`, `name`, `tokens`, `pct_of_total`, `source` (`measured` / `published` / `estimate`). Include a final row `TOTAL`. Below the table, emit a text bar chart: one row per bucket, where each row is `B# name | ████████ tokens (pct%)` and bar length is `round(pct/2)` block characters. Sort descending by tokens. Print to stdout at the end of the run.

## Undo

```bash
rm -rf "$HOME/.claude/experiments/$(date +%Y-%m-%d)-029-token-decomp"
```

That is the entire revert. The prompt does not modify any file outside the scratch directory.

## What you should now see

- Five named buckets with token estimates and a clear `source` label per bucket.
- A markdown stacked-bar table sorted descending — the dominant bucket sits on top.
- A text bar chart that shows the *shape* of the spend, not just the number.
- An honest mix of `measured` and `estimate` rows. Most readers will have 2–3 estimates on first run; that is fine.
- A baseline snapshot showing the numbers from Article 023 alongside the new decomposition.

## How to confirm the win

Article 029 is value-tagged `context-savings`. The win is recognition, not yet reduction — Prompt 2 plans the reduction. After running Prompt 1 you should be able to name your largest bucket without looking. If two buckets are within 10% of each other, note both as candidates. Save `00-DECOMP.md` for Prompt 2.
