# Surface Selection Prompt — Audit Your Last 10 Tasks

**Article:** 025 — Which tool, when (Prompt 1 of 2).
**Surfaces:** Claude Code primary; the audit logic is surface-agnostic.
**Run mode:** read-only against transcript metadata; writes only to a dated scratch directory.

---

## What this prompt does

Reviews your last 10 substantial AI tasks and labels each with the surface that would have been the best fit — Claude Code, Claude Desktop, Claude.ai chat, ChatGPT, OpenAI Codex, the Anthropic API, or the OpenAI API. The labeling uses a fit rubric grounded in `docs/strategy/surface-matrix.md`: tasks needing filesystem access, multi-file edits, and shell tools fit Claude Code; one-shot reasoning with no file context fits chat; long-running scripted work fits the API. The output is a mismatch list — tasks you ran on the wrong surface — that Prompt 2 acts on.

## Run this prompt

> You are a surface-fit auditor. You are read-only against my home directory. You may write only inside the scratch directory created in Step 1. You may not exfiltrate file contents to any network endpoint. You may not read files matching `*.env`, `*credentials*`, `*token*`, `*.key`, `*.pem`, `id_rsa*`, `id_ed25519*`, or any path containing `/.ssh/` or `/.gnupg/`. You may not modify `~/.claude/settings.json`, `~/CLAUDE.md`, `~/.claude/CLAUDE.md`, `~/.claude/projects/-home-psimmons/memory/MEMORY.md`, `~/AGENTS.md`, install MCP servers, change hook configuration, or alter file permissions.
>
> **Step 1 — create scratch directory.** Run:
>
> ```bash
> SCRATCH="$HOME/.claude/experiments/$(date +%Y-%m-%d)-025-surface-fit"
> mkdir -p "$SCRATCH"
> echo "scratch=$SCRATCH"
> ```
>
> **Step 2 — gather candidate tasks.** Ask me to list, paste, or point at evidence for the last 10 substantial AI tasks I ran in the past 14 days. Substantial means: more than 3 turns, or a single turn that produced shipped output. Acceptable evidence:
>
> - Claude Code transcript filenames under `~/.claude/projects/`.
> - A bulleted list I paste.
> - A file path I authorize you to read.
>
> If fewer than 10 tasks are available, work with what you have and flag T0 — operator does not yet have 14 days of varied AI usage to audit; this article will be more useful re-run after some time.
>
> Save the list verbatim to `$SCRATCH/01-tasks.md` with one task per row: `idx`, `task_summary` (≤120 chars), `surface_used`, `evidence_path` (or `pasted`).
>
> **Step 3 — establish the fit rubric.** Write `$SCRATCH/02-rubric.md` with the following surface profiles, then refer back to them in Step 4:
>
> - **Claude Code** — fit when: filesystem read/write, multi-file edits, shell tools, git, repo navigation, long-running orchestration.
> - **Claude Desktop** — fit when: cross-platform MCP-based tool use (calendar, Drive, Gmail), local files via Filesystem MCP, conversational research with persistence.
> - **Claude.ai chat** — fit when: one-shot reasoning, prose generation, no file context required, mobile-friendly.
> - **ChatGPT** — fit when: OpenAI-only features (advanced voice, image generation, deep research), broad consumer tooling.
> - **OpenAI Codex** — fit when: cloud-based code execution, GitHub-integrated PR workflows.
> - **Anthropic API** — fit when: scripted/bulk work, prompt caching matters, batch processing, latency-controlled.
> - **OpenAI API** — fit when: scripted/bulk work using OpenAI models, batch jobs, structured output via JSON mode.
>
> **Step 4 — label each task.** For each task in `01-tasks.md`, assign exactly one `best_fit_surface` from the rubric. Write `$SCRATCH/03-labeled.md` with: `idx`, `task_summary`, `surface_used`, `best_fit_surface`, `match` (Y/N), `mismatch_severity` (1–3 if N, blank if Y).
>
> Severity scale:
>
> - 1 = mild — wrong surface but worked anyway, modest token waste.
> - 2 = moderate — wrong surface caused extra turns, manual workarounds, or copy-paste plumbing.
> - 3 = severe — wrong surface fundamentally limited what was possible (e.g., asking Claude.ai chat to refactor a multi-file repo).
>
> **Step 5 — produce the mismatch summary.** Write `$SCRATCH/04-mismatches.md` with the rows where `match=N`, sorted by `mismatch_severity` descending. Include columns from Step 4 plus `recommended_action` (one sentence: "next time, use X because Y").
>
> **Step 6 — write the takeaway.** Produce `$SCRATCH/00-FIT.md` with: tasks audited, mismatches, severity distribution (counts at 1/2/3), the most-common mismatch pattern (e.g., "chat surface used for multi-file work"), and a one-sentence recommendation. Print to stdout.

## Undo

```bash
rm -rf "$HOME/.claude/experiments/$(date +%Y-%m-%d)-025-surface-fit"
```

That is the entire revert. The prompt does not modify any file outside the scratch directory.

## What you should now see

- A list of your last 10 (or fewer) substantial AI tasks with the surface used.
- A fit-rubric reference card you can keep.
- A labeled mismatch list, sorted by severity.
- A one-sentence "next time, use X" for each mismatch.
- A takeaway naming your most-frequent mismatch pattern.

## How to confirm the win

Article 025 is value-tagged `context-savings`. The win for this prompt is the mismatch list — not yet a token reduction. The reduction is realized in Prompt 2 when you re-run the most-mismatched task on the better-fit surface and observe the turns/tokens delta. To confirm Prompt 1 worked, check `$SCRATCH/00-FIT.md`: the mismatch count should be in the 2–6 range for most operators (out of 10). Higher than 6 suggests the rubric is stricter than the operator's pragmatic constraints; lower than 2 suggests the operator already has surface-selection discipline and the article will be a confirmation rather than a discovery.

Subscribe so you don't miss Article 026, where prompt structure replaces surface choice as the lever.
