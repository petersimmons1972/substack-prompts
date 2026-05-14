# Model Selection Prompt — Replay Against the Smaller Model

**Article:** 024 — Which model, when (Prompt 2 of 2).
**Depends on:** Prompt 1's `00-OVERSPEND.md` and `04-overspends.md`.
**Surfaces:** Claude Code primary; the replay step requires API access (Anthropic or OpenAI) or a chat surface where you can pick the model per-turn.
**Run mode:** writes only to a dated scratch directory; reads transcript metadata only.

---

## What this prompt does

Picks one flagged overspend from Prompt 1, reconstructs the user prompt that produced the original turn, and re-runs that prompt against a smaller model — Haiku 4.5 if the original was Anthropic, GPT-4.1-mini or o4-mini if OpenAI. The two outputs sit side by side in scratch with a quality rubric. The result is evidence for or against the overspend classification: if Haiku produces a substantively equivalent answer, the original turn was an overspend and the cost gap is real. If Haiku falls short, the classifier was wrong — useful information either way.

## Run this prompt

> You are a model-replay analyst. You are read-only against my home directory except for the scratch directory created in Step 1. You may not exfiltrate file contents to any network endpoint *except* the Anthropic or OpenAI API endpoint required to run the replay, and only with the prompt I have explicitly authorized. You may not read files matching `*.env`, `*credentials*`, `*token*`, `*.key`, `*.pem`, `id_rsa*`, `id_ed25519*`, or any path containing `/.ssh/` or `/.gnupg/`. You may not modify `~/.claude/settings.json`, `~/CLAUDE.md`, `~/.claude/CLAUDE.md`, `~/.claude/projects/-home-psimmons/memory/MEMORY.md`, `~/AGENTS.md`, install MCP servers, change hook configuration, or alter file permissions. The API call uses the operator's existing credentials read from environment variables — you do not read or echo the credential values.
>
> **Step 1 — locate the scratch directory and overspends.** Run:
>
> ```bash
> SCRATCH="$HOME/.claude/experiments/$(date +%Y-%m-%d)-024-model-overspend"
> test -f "$SCRATCH/04-overspends.md" || { echo "ERROR: run prompt-1 first"; exit 1; }
> ```
>
> Read `$SCRATCH/04-overspends.md`. Pick the row with the highest `~tokens` value as the replay candidate. Record the source file, turn index, task class, and original model in `$SCRATCH/10-candidate.md`.
>
> **Step 2 — reconstruct the user prompt.** Read the original transcript file to extract the user turn that triggered the candidate assistant turn. Save the user turn verbatim to `$SCRATCH/11-user-prompt.txt`. Save the original assistant response verbatim to `$SCRATCH/12-original-response.txt`. If either contains content that matches the forbidden file patterns or appears to include credentials/secrets, abort the replay and write `REPLAY_BLOCKED_SENSITIVE_CONTENT` to `$SCRATCH/00-REPLAY.md`.
>
> **Step 3 — pick the smaller model.** Map the original model to its smaller-tier counterpart:
>
> - Opus → Haiku 4.5 (Anthropic).
> - Sonnet → Haiku 4.5 (Anthropic).
> - GPT-4 / GPT-5 → GPT-4.1-mini or o4-mini (OpenAI).
> - `unknown` → ask me which API I want to replay against; default to Anthropic Haiku 4.5.
>
> Record the chosen smaller model in `$SCRATCH/13-target-model.md`.
>
> **Step 4 — run the replay.** Send the reconstructed user prompt to the chosen smaller model via its API. Use the same system prompt as the original session if it is recoverable from the transcript; otherwise use no system prompt and note the difference. Save the response verbatim to `$SCRATCH/14-replay-response.txt`. Record the response token count, latency, and model id.
>
> If the API call fails (auth, rate limit, network), record the error in `$SCRATCH/14-replay-response.txt` and continue to Step 5 — the comparison cannot be completed but the staged artifacts remain useful.
>
> **Step 5 — score both responses.** Score the original and the replay against a four-criterion rubric, 1–5 each:
>
> - **Correctness:** does the response answer the user's actual question?
> - **Completeness:** does it cover what the user implicitly needed?
> - **Format fidelity:** does it match the requested or conventional format?
> - **Brevity:** is it free of padding?
>
> Write `$SCRATCH/15-rubric.md` with both scores side-by-side. The rubric scoring is your judgment as the analyst; mark which criteria are objective vs subjective.
>
> **Step 6 — produce the verdict.** Write `$SCRATCH/00-REPLAY.md` with: candidate task class, original model, replay model, original tokens, replay tokens, original score, replay score, score delta, and a one-sentence verdict — `OVERSPEND_CONFIRMED` if replay score ≥ original − 1, `OVERSPEND_REJECTED` if replay score < original − 1, `INCONCLUSIVE` if the API call failed. Print to stdout.

## Undo

```bash
rm -rf "$HOME/.claude/experiments/$(date +%Y-%m-%d)-024-model-overspend"
```

That is the entire revert. The prompt makes one outbound API call but writes only inside the scratch directory; deleting it returns you to your starting state. No live memory or settings file is touched. (The API call itself is not undoable — the request was sent — but it carried only operator-authorized content.)

## What you should now see

- A single named candidate turn from Prompt 1's overspend list.
- The reconstructed user prompt and original response captured in scratch.
- A response from the smaller model for the same prompt.
- A four-criterion rubric scoring both.
- A verdict file naming the candidate as a confirmed or rejected overspend.

## How to confirm the win

Article 024 is value-tagged `context-savings`. The win is realized when `OVERSPEND_CONFIRMED` fires on at least one candidate: you now have evidence in your own scratch directory that a turn you spent on Opus could have run on Haiku for ~10–20% of the cost. Across a typical operator's flagged overspend list, confirming 50–70% of candidates is normal; confirming under 30% suggests the classifier is too aggressive and Prompt 1's task-class definitions need tightening. Take the confirmed verdict to your default-model rule (your `CLAUDE.md` Advisory Protocol section, or your ChatGPT custom instructions) and update it. Re-run the Article 023 baseline afterward; `memory_files_total_tokens` will not move (the change is in the runtime, not the memory file) but your Article 029 token-decomposition prompt will show the tier shift the next time you run it.

Subscribe so you don't miss Article 025, where the same auditing approach is applied to surface choice — Claude Code vs ChatGPT vs Claude Desktop.
