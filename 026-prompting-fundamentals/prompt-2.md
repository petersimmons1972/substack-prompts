# Prompting Fundamentals Prompt — Few-Shot Earn-Their-Keep Test

**Article:** 026 — Prompting fundamentals you skipped (Prompt 2 of 2).
**Surfaces:** any surface where you can re-send a prompt; replay step needs API access for fair token measurement.
**Run mode:** writes only to a dated scratch directory; API calls are operator-authorized.

---

## What this prompt does

Few-shot examples are popular advice. They also cost tokens — every turn, on every call. This prompt takes one of your repeatedly-used prompts, adds three carefully-chosen few-shot examples, and runs both versions across a small batch of test inputs to find out whether the examples earn their token cost. The output is a per-test verdict and an aggregate verdict: examples that improve quality on enough cases to justify their per-call overhead, or examples that are a tax with no return.

## Run this prompt

> You are a few-shot economics analyst. You are read-only against my home directory except the scratch directory created in Step 1. You may not exfiltrate file contents to any network endpoint *except* the model API endpoint required for the comparison, and only with operator-authorized prompts. You may not read files matching `*.env`, `*credentials*`, `*token*`, `*.key`, `*.pem`, `id_rsa*`, `id_ed25519*`, or any path containing `/.ssh/` or `/.gnupg/`. You may not modify `~/.claude/settings.json`, `~/CLAUDE.md`, `~/.claude/CLAUDE.md`, `~/.claude/projects/-home-psimmons/memory/MEMORY.md`, `~/AGENTS.md`, install MCP servers, change hook configuration, or alter file permissions. API credentials are read from environment variables and never echoed.
>
> **Step 1 — create scratch directory.** Run:
>
> ```bash
> SCRATCH="$HOME/.claude/experiments/$(date +%Y-%m-%d)-026-fewshot"
> mkdir -p "$SCRATCH"
> echo "scratch=$SCRATCH"
> ```
>
> **Step 2 — capture the repeated prompt.** Ask me for one prompt I have used five or more times — typically a classification, extraction, or formatting task. Save verbatim to `$SCRATCH/01-prompt.txt`. Redact identifiers as in the previous prompt; log substitutions to `$SCRATCH/01-redactions.md`.
>
> If no such prompt exists, flag F0 — operator does not yet have a repeated workflow; the few-shot question is moot until they do. Generate a synthetic example (e.g., "classify a commit message as fix/feat/refactor/chore/docs/test") and continue.
>
> **Step 3 — collect five test inputs.** Ask me for five real test inputs (or generate five if synthetic). The five should span easy and hard cases, not all easy. Save to `$SCRATCH/02-tests.txt`, one per line.
>
> **Step 4 — write three few-shot examples.** Construct three input/output pairs that each demonstrate one common edge case the bare prompt might mishandle. Examples are not test inputs and must not duplicate any test case. Save to `$SCRATCH/03-examples.md` in this XML form:
>
> ```
> <example><input>...</input><output>...</output></example>
> <example><input>...</input><output>...</output></example>
> <example><input>...</input><output>...</output></example>
> ```
>
> **Step 5 — assemble both versions.** Save the bare prompt as `$SCRATCH/04-bare.txt` (the original from Step 2). Save the few-shot version as `$SCRATCH/05-fewshot.txt` — the original prompt plus the three examples wrapped in `<examples>...</examples>` and inserted before the test input.
>
> Compute token counts for both prompt versions (excluding the test input, which is identical for both). Write to `$SCRATCH/06-counts.md`: bare tokens, fewshot tokens, delta (positive — examples cost tokens).
>
> **Step 6 — run both versions over the five tests.** For each of the five test inputs, send the bare prompt and the few-shot prompt to Haiku 4.5 at temperature 0. Capture both responses. Save to `$SCRATCH/07-results.md` as a table with columns: `test_idx`, `bare_response`, `fewshot_response`, `bare_correct` (Y/N/?), `fewshot_correct` (Y/N/?). Mark `?` when correctness requires my judgment; do not guess.
>
> **Step 7 — wait for operator judgment if needed.** If any row has `?`, print:
>
> ```
> AWAITING JUDGMENT: rows {N1, N2, ...} need correctness calls. Read $SCRATCH/07-results.md and resume.
> ```
>
> When I supply the calls, fill them in.
>
> **Step 8 — compute the economics.** For five tests:
>
> - `quality_uplift` = `fewshot_correct_count - bare_correct_count` (range -5 to +5).
> - `tokens_per_call_overhead` = `fewshot_tokens - bare_tokens` from Step 5.
> - `total_overhead_5_calls` = `tokens_per_call_overhead * 5`.
> - `cost_per_quality_point` = `total_overhead_5_calls / max(quality_uplift, 1)`.
>
> Write `$SCRATCH/08-economics.md` with the four numbers and one paragraph of interpretation.
>
> **Step 9 — produce the verdict.** Write `$SCRATCH/00-FEWSHOT.md` with: bare correct, fewshot correct, quality uplift, per-call overhead, total overhead, and a one-sentence verdict — `EXAMPLES_EARN_KEEP` if `quality_uplift ≥ 1` and `cost_per_quality_point < 500`; `EXAMPLES_OVERPRICED` if `quality_uplift ≥ 1` but `cost_per_quality_point ≥ 500`; `EXAMPLES_FREELOADER` if `quality_uplift = 0`; `EXAMPLES_HARMFUL` if `quality_uplift < 0`. Print to stdout.

## Undo

```bash
rm -rf "$HOME/.claude/experiments/$(date +%Y-%m-%d)-026-fewshot"
```

That is the entire revert. The prompt makes API calls but writes only inside the scratch directory.

## What you should now see

- A repeated prompt of yours and a few-shot version with three examples.
- Five test inputs run against both versions.
- A correctness call per test, supplied by you for ambiguous cases.
- An economics block computing per-call overhead and cost per quality point.
- A verdict file naming whether your three examples earn their keep.

## How to confirm the win

Article 026 is value-tagged `context-savings`. The win is realized when `EXAMPLES_FREELOADER` or `EXAMPLES_HARMFUL` fires and you remove the examples — that is a permanent per-call savings on every future use of the prompt. The win is *also* realized (in reverse) when `EXAMPLES_EARN_KEEP` fires and you confirm a worthwhile per-call investment. Across typical operators, examples that earn their keep on a 5-test sample produce 1–3 quality-point uplift; examples that fail to do so are common — Anthropic's prompt-engineering guidance specifically notes that few-shot is most useful for tasks with non-obvious format requirements, less for self-evident tasks. Whichever verdict you get, save the file: it is evidence for the next time someone insists examples are always free.

Subscribe so you don't miss Article 027, where the operating-discipline floor for the rest of the series is locked in.
