# Anti-patterns Audit Prompt — Find and Rank

**Article:** 028 — Anti-patterns audit (Prompt 1 of 2).
**Consumes:** Article 023 baseline (`$HOME/.claude/experiments/<DATE>-baseline/00-BASELINE.md`).
**Surfaces:** Claude Code primary; the audit logic adapts to ChatGPT custom instructions and API-side system prompts with minor edits.
**Run mode:** read-only against your home directory; writes only to a dated scratch directory.

---

## What this prompt does

Inspects your live AI configuration for the five most common anti-patterns — bloated memory files, secrets in memory files, missing undo discipline, wildcard permissions, and absent model-selection guidance — then ranks every finding by blast radius (how bad if exploited or hit) and ease of fix (how cheap to remediate). The output is a single ranked table you can hand to Prompt 2. The prompt does not modify any live file. Everything written goes inside a dated scratch directory you delete with one command.

## Run this prompt

> You are an auditor inspecting my AI configuration for anti-patterns. You are read-only against my home directory. You may write only inside the scratch directory created in Step 1. You may not exfiltrate any file contents to any network endpoint. You may not read files matching `*.env`, `*credentials*`, `*token*`, `*.key`, `*.pem`, `id_rsa*`, `id_ed25519*`, or any path containing `/.ssh/` or `/.gnupg/`. If you encounter such a file, log its existence by name only — never its contents. You may not modify `~/.claude/settings.json`, install MCP servers, change hook configuration, or alter file permissions. If a step would require any of those, stop and report the blocker.
>
> **Step 1 — create scratch directory.** Run:
>
> ```bash
> SCRATCH="$HOME/.claude/experiments/$(date +%Y-%m-%d)-028-anti-patterns"
> mkdir -p "$SCRATCH"
> echo "scratch=$SCRATCH"
> ```
>
> All subsequent outputs go inside `$SCRATCH`. If the directory already exists, continue — files will overwrite.
>
> **Step 2 — locate the baseline.** Find the most recent `00-BASELINE.md` under `$HOME/.claude/experiments/*-baseline/`. Read its eight summary lines and copy them verbatim into `$SCRATCH/00-baseline-snapshot.md`. If no baseline exists, write `NO_BASELINE_FOUND` and proceed; later articles assume one exists, so flag this as finding A0.
>
> **Step 3 — audit anti-pattern A1: bloated memory files.** For `~/CLAUDE.md`, `~/.claude/CLAUDE.md`, `~/.claude/projects/-home-psimmons/memory/MEMORY.md`, and `~/AGENTS.md`, count lines, words, and estimated tokens (`ceil(words / 0.75)`). Flag any single file >2,500 tokens, any total >4,000 tokens, or any duplicated headings/sections across files. Write `$SCRATCH/A1-bloat.md` with the table and the flags. Do not include file bodies.
>
> **Step 4 — audit anti-pattern A2: secrets in memory files.** Re-run the Article 023 secrets-indicator scan (`sk-`, `xoxb-`, `ghp_`, `AKIA`, `eyJ` + 20 chars, 32+ hex, RFC1918 IPs, bare emails) across the same four files. Report only file name, line number, and a redacted preview (first 4 chars + `…` + last 2 chars). Never the full match. Write `$SCRATCH/A2-secrets.md`.
>
> **Step 5 — audit anti-pattern A3: undo discipline.** Search the four memory files for the strings `backup`, `undo`, `revert`, `restore`, `mv .bak`, `git checkout`, `experiments/`. Count occurrences per file. If a file contains executable instructions (imperatives like "run", "delete", "modify") but zero undo language, flag it. Write `$SCRATCH/A3-undo.md`.
>
> **Step 6 — audit anti-pattern A4: wildcard permissions.** Read `~/.claude/settings.json` and any `.claude/settings.json` in the current working directory. Count: total allow rules, rules ending in `*` or `**`, rules containing mid-string globs, and rules granting `Bash(*)` or equivalent shell-wide grants. Do not echo rule strings that contain paths. Write `$SCRATCH/A4-permissions.md`.
>
> **Step 7 — audit anti-pattern A5: model selection.** Search the four memory files for the strings `Opus`, `Sonnet`, `Haiku`, `gpt-`, `o1`, `o3`, `model`, `tier`. If zero references appear in any file, flag A5 as present (no model-selection discipline encoded). Write `$SCRATCH/A5-model-selection.md`.
>
> **Step 8 — rank findings.** Produce `$SCRATCH/00-FINDINGS.md` containing a markdown table with columns: `id`, `anti_pattern`, `present` (Y/N), `blast_radius` (1–5), `ease_of_fix` (1–5, 5=easiest), `score` (`blast_radius * ease_of_fix`), `evidence_file`. Sort descending by score. Print the table to stdout at the end of the run.

## Undo

```bash
rm -rf "$HOME/.claude/experiments/$(date +%Y-%m-%d)-028-anti-patterns"
```

That is the entire revert. The prompt does not modify any file outside the scratch directory; deleting the scratch directory restores you to your starting state.

## What you should now see

- A snapshot of your Article 023 baseline numbers, beside the new findings.
- A per-file bloat table that names the largest single contributor to your session-start token cost.
- A redacted secrets list — file names and line numbers only, never the matched string.
- A wildcard-permission count and a flag if you have shell-wide `Bash(*)` grants.
- A single ranked findings table with the highest-leverage fix at the top, ready for Prompt 2.

## How to confirm the win

Article 028 is value-tagged `both`. Re-run the Article 023 baseline prompt after acting on Prompt 2's remediation plan and compare `00-BASELINE.md` line-for-line against the original. You should see at least one of: `memory_files_total_tokens` lower (context-savings delta), `secrets_indicator_hits` lower, or `broad_wildcard_rules` lower (security-gain delta). If neither moves, the audit found nothing actionable in your environment — file the findings table for the next sweep and continue the series.
