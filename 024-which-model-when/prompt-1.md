# Model Selection Prompt — Find Your Overspends

**Article:** 024 — Which model, when (Prompt 1 of 2).
**Surfaces:** Claude Code primary; the analysis adapts to ChatGPT or any chat surface that exports per-conversation metadata.
**Run mode:** read-only against transcript files; writes only to a dated scratch directory.

---

## What this prompt does

Inspects metadata from your recent AI sessions and produces a list of turns where a smaller/cheaper model would have produced functionally equivalent output. The classifier is conservative — it flags only turns whose task class falls into `classification`, `formatting`, `bulk_judge`, `mechanical_transform`, or `health_check`, the categories Anthropic and OpenAI both document as Haiku- or small-model-appropriate. Architecture decisions, multi-file edits, and reasoning-heavy debugging are never flagged. The output is a ranked list of overspends you can act on in Prompt 2.

## Run this prompt

> You are a model-selection auditor. You are read-only against my home directory. You may write only inside the scratch directory created in Step 1. You may not exfiltrate file contents to any network endpoint. You may not read files matching `*.env`, `*credentials*`, `*token*`, `*.key`, `*.pem`, `id_rsa*`, `id_ed25519*`, or any path containing `/.ssh/` or `/.gnupg/`. You may not modify `~/.claude/settings.json`, `~/CLAUDE.md`, `~/.claude/CLAUDE.md`, `~/.claude/projects/-home-psimmons/memory/MEMORY.md`, `~/AGENTS.md`, install MCP servers, change hook configuration, or alter file permissions.
>
> **Step 1 — create scratch directory.** Run:
>
> ```bash
> SCRATCH="$HOME/.claude/experiments/$(date +%Y-%m-%d)-024-model-overspend"
> mkdir -p "$SCRATCH"
> echo "scratch=$SCRATCH"
> ```
>
> **Step 2 — locate transcripts.** Find Claude Code transcript files under `~/.claude/projects/` modified in the last 14 days. List up to 20 files (newest first) with path, byte size, and modified date in `$SCRATCH/01-transcripts.md`.
>
> If no transcript directory exists, write `NO_TRANSCRIPTS_FOUND` and proceed using a synthetic 10-turn example you generate. Flag this as M0 — the operator does not have local Claude Code session history to audit; for ChatGPT/API users, point at Article 031 for the data-export step.
>
> **Step 3 — sample turns.** From the listed files, sample up to 50 assistant turns (skip system prompts, memory injections, tool calls, tool results, user turns). For each sampled turn record: source file, turn index, byte length, estimated tokens (`ceil(bytes / 4)`), the configured model if the transcript records it (otherwise `unknown`), and a 100-character preview of the user turn that triggered the assistant turn. Write to `$SCRATCH/02-turns.md`.
>
> Truncate previews; never copy full turn bodies.
>
> **Step 4 — classify each turn by task class.** For each row in `02-turns.md`, assign exactly one task class based on the user-turn preview. Use this taxonomy:
>
> - **`classification`** — categorize, label, tag, or sort items.
> - **`formatting`** — reformat existing content (JSON↔YAML, markdown table cleanup, casing).
> - **`bulk_judge`** — score N items against a rubric.
> - **`mechanical_transform`** — rename, search-and-replace, regex application.
> - **`health_check`** — yes/no operational query, `is X up`, `does Y exist`.
> - **`debugging`** — diagnose a failure with reasoning.
> - **`multi_file_edit`** — coordinated changes across 2+ files.
> - **`architecture`** — design decisions, irreversible choices.
> - **`generation`** — long-form prose, code from scratch.
> - **`unclassified`** — not confidently classifiable from the preview.
>
> Write `$SCRATCH/03-classified.md` with `idx`, `task_class`, `model`, `~tokens`.
>
> **Step 5 — flag overspends.** A turn is flagged as an overspend if (a) its task class is in {`classification`, `formatting`, `bulk_judge`, `mechanical_transform`, `health_check`} and (b) its recorded model is Opus or `unknown` (treated as the session default which is typically Opus or Sonnet). Never flag `debugging`, `multi_file_edit`, `architecture`, `generation`, or `unclassified`.
>
> Write `$SCRATCH/04-overspends.md` with the flagged rows plus a column `recommended_tier` (`Haiku` for the five flagged classes). Include count and total tokens that would have moved to a smaller tier.
>
> **Step 6 — produce the takeaway.** Write `$SCRATCH/00-OVERSPEND.md` with five lines: turns sampled, turns flagged as overspends, percentage flagged, total flagged tokens, and the most-frequent flagged task class. Print to stdout.

## Undo

```bash
rm -rf "$HOME/.claude/experiments/$(date +%Y-%m-%d)-024-model-overspend"
```

That is the entire revert. The prompt does not modify any file outside the scratch directory.

## What you should now see

- A list of up to 20 recent transcript files with sizes and dates.
- Up to 50 sampled assistant turns with task-class labels.
- A flagged subset where a smaller model could likely have produced the same answer.
- A token total naming "tokens that probably went to the wrong tier."
- A takeaway file with the most-frequent overspend pattern in your usage.

## How to confirm the win

Article 024 is value-tagged `context-savings`. The win for this prompt is the ranked overspend list — not yet a token reduction. The reduction is realized in Prompt 2 when you replay one flagged turn against a smaller model and observe the quality. To confirm Prompt 1 worked, check `$SCRATCH/00-OVERSPEND.md`: the percentage flagged should be in the 5–30% range for most operators. Above 30% suggests the classifier is over-flagging (re-read the previews and tighten the calls); below 5% suggests either disciplined model usage already or insufficient sample size.

Subscribe so you don't miss Article 025, which extends the same auditing logic from "which model" to "which surface."
