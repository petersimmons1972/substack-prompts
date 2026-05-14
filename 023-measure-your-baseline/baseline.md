# Baseline Measurement Prompt

**Article:** 023 — Measure your baseline.
**Reused by:** 028, 029, 042, 044, 047, 057, 060.
**Surfaces:** Claude Code primary; portions adaptable to Claude.ai / ChatGPT.
**Run mode:** read-only against your home directory; writes only to a dated scratch directory.

---

## What this prompt does

Captures four numbers and four artifacts that describe your current AI configuration. You will run this once today, save the output, and re-run it after each later article to measure your delta. The prompt does not modify any live configuration file. Every operation that touches state goes inside a single dated scratch directory you can delete with one command.

## Run this prompt

> You are an auditor inspecting my AI configuration. You are read-only against my home directory. You may write only inside the scratch directory I create below. You may not exfiltrate any file contents to any network endpoint. You may not read files matching `*.env`, `*credentials*`, `*token*`, `*.key`, `*.pem`, `id_rsa*`, or any path containing `.ssh/`. If you encounter such a file, log its existence by name only — never its contents.
>
> **Step 1 — create scratch directory.** Run:
>
> ```bash
> SCRATCH="$HOME/.claude/experiments/$(date +%Y-%m-%d)-baseline"
> mkdir -p "$SCRATCH"
> echo "scratch=$SCRATCH"
> ```
>
> Record the path. All subsequent file outputs go inside `$SCRATCH`.
>
> **Step 2 — capture memory file inventory.** For each of `~/CLAUDE.md`, `~/.claude/CLAUDE.md`, `~/.claude/projects/-home-psimmons/memory/MEMORY.md`, `~/AGENTS.md`, and any `CLAUDE.md` / `MEMORY.md` / `AGENTS.md` found within the current working directory, record: absolute path, byte size, line count, word count, approximate token count (estimate as `ceil(words / 0.75)`), and last-modified date. Write the inventory to `$SCRATCH/01-memory-inventory.md` as a markdown table. Do not include file contents.
>
> **Step 3 — capture skill and hook inventory.** List the names of files under `~/.claude/skills/` (one level deep) and `~/.claude/hooks/` (recursively). For each, record name and byte size only. No contents. Write to `$SCRATCH/02-skill-hook-inventory.md`.
>
> **Step 4 — capture permission surface.** Read `~/.claude/settings.json` and any `.claude/settings.json` in the current working directory. Extract only: number of allow rules, number of deny rules, number of ask rules, list of broad-wildcard rules (rules ending in `*` or `**`), and the names of configured hooks. Do NOT include the rules themselves verbatim if they reference specific paths or tokens. Write to `$SCRATCH/03-permission-surface.md`.
>
> **Step 5 — secrets-exposure indicators.** Run a redacted scan against `~/CLAUDE.md`, `~/.claude/CLAUDE.md`, and any `MEMORY.md` for patterns that look like secrets: strings of 32+ hex characters, strings starting with `sk-`, `xoxb-`, `ghp_`, `AKIA`, `eyJ` followed by 20+ chars, AWS-style account IDs, RFC1918 IPs, and bare email addresses. For each hit, report only: file name, line number, redacted preview (first 4 chars + `…` + last 2 chars). Never the full match. Write to `$SCRATCH/04-secrets-indicators.md`.
>
> **Step 6 — context budget snapshot.** Estimate, for a typical session start in this environment, how many tokens are consumed by memory files alone before the user's first message. Sum the token estimates from step 2 for files that load by default (`~/.claude/CLAUDE.md` and any `MEMORY.md` it points to). Write to `$SCRATCH/05-context-budget.md` with a single number plus the breakdown.
>
> **Step 7 — write the baseline summary.** Produce `$SCRATCH/00-BASELINE.md` containing exactly these eight lines:
>
> ```
> baseline_date: <YYYY-MM-DD>
> memory_files_total_tokens: <number>
> memory_files_count: <number>
> skills_count: <number>
> hooks_count: <number>
> allow_rules: <number>
> broad_wildcard_rules: <number>
> secrets_indicator_hits: <number>
> ```
>
> Print the contents of `$SCRATCH/00-BASELINE.md` to stdout at the end of the run.

## Undo

```bash
rm -rf "$HOME/.claude/experiments/$(date +%Y-%m-%d)-baseline"
```

That is the entire revert. The prompt does not modify any file outside the scratch directory; deleting the scratch directory restores you to your starting state.

## What you should now see

- A single number for total memory-file tokens that you did not previously have.
- A count of skills and hooks active in your environment.
- A permission surface summary you can compare against future runs.
- A redacted list of strings that *might* be secrets in your memory files. (Article 042 acts on this.)
- A reusable baseline you re-run at the end of the series and after each value-tagged article.

## How to confirm the win in later articles

Each later article that lowers context usage or improves security posture will instruct you to re-run this prompt and compare against `$SCRATCH/00-BASELINE.md`. The delta is the proof.
