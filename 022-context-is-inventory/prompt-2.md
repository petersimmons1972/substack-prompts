# Inventory Prompt — Verbose vs Terse Memory File Cost

**Article:** 022 — Context is inventory, not magic (Prompt 2 of 2).
**Surfaces:** Claude Code primary; the principle applies to ChatGPT custom instructions and OpenAI/Anthropic API system prompts.
**Run mode:** writes only to a dated scratch directory; never modifies live memory files.

---

## What this prompt does

Constructs two synthetic memory files in scratch — one verbose, one terse — that express the same five operator preferences, then computes the per-turn token cost of each over a simulated 20-turn session. The output is a side-by-side spend table that puts a number on the inventory metaphor: the verbose memory file costs N tokens per turn, multiplied by every turn for the rest of your life, while the terse version expresses the same intent for a fraction of the cost.

## Run this prompt

> You are a context-inventory analyst. You are read-only against my home directory. You may write only inside the scratch directory created in Step 1. You may not read or modify any of: `~/.claude/settings.json`, `~/CLAUDE.md`, `~/.claude/CLAUDE.md`, `~/.claude/projects/-home-psimmons/memory/MEMORY.md`, `~/AGENTS.md`. You may not exfiltrate file contents. You may not install MCP servers, change hook configuration, or alter file permissions. You may not read `*.env`, `*credentials*`, `*token*`, `*.key`, `*.pem`, `id_rsa*`, `id_ed25519*`, `/.ssh/`, or `/.gnupg/` paths.
>
> **Step 1 — create scratch directory.** Run:
>
> ```bash
> SCRATCH="$HOME/.claude/experiments/$(date +%Y-%m-%d)-022-verbose-vs-terse"
> mkdir -p "$SCRATCH"
> echo "scratch=$SCRATCH"
> ```
>
> **Step 2 — define five preferences.** Write five operator-style preferences to `$SCRATCH/00-preferences.md`. Use generic, non-identifying examples — do not copy lines from my real memory files (you cannot read them anyway). Suggested set:
>
> 1. Use `xh` for HTTP requests, not `curl`.
> 2. Run tests after every code edit.
> 3. Never commit secrets; use a secret manager.
> 4. For HTTP debugging, prefer `mitmproxy` to print statements.
> 5. Default model tier: Sonnet for execution, Haiku for mechanical work, Opus for irreversible decisions.
>
> **Step 3 — write the verbose version.** Produce `$SCRATCH/01-verbose-CLAUDE.md` expressing the five preferences in a chatty, narrative style — paragraphs, examples, anecdotes, motivation. Target 600–900 words total.
>
> **Step 4 — write the terse version.** Produce `$SCRATCH/02-terse-CLAUDE.md` expressing the same five preferences as a single bulleted list, one bullet per preference, no examples or anecdotes. Target under 80 words total.
>
> **Step 5 — token-count both.** Compute token estimates for each file. If `tiktoken` is available, use `cl100k_base`; otherwise use `ceil(words / 0.75)`. Write to `$SCRATCH/03-counts.md` with: filename, words, byte size, token estimate, method.
>
> **Step 6 — simulate a 20-turn session spend.** Memory files are loaded once and persist across turns; their token cost is paid once per turn for the duration of the session. Compute, for each version, the cumulative token cost over 1, 5, 10, and 20 turns:
>
> ```
> cumulative_tokens(file, n_turns) = file_tokens * n_turns
> ```
>
> Write `$SCRATCH/04-cumulative.md` as a table with columns: `version`, `1_turn`, `5_turns`, `10_turns`, `20_turns`, and a `delta_at_20` column showing verbose minus terse.
>
> **Step 7 — interpret.** Write `$SCRATCH/05-interpret.md` with three observations:
>
> - The per-turn delta in absolute tokens.
> - The cumulative delta at 20 turns expressed as "this many extra tokens to say the same thing five times."
> - The fraction of a 200K-token context window the verbose file would consume after 20 turns vs the terse file.
>
> **Step 8 — produce the takeaway.** Write `$SCRATCH/00-DELTA.md` with five lines: verbose tokens, terse tokens, ratio (`verbose/terse`), 20-turn delta in absolute tokens, and a one-sentence takeaway naming the rule the operator can apply to their own memory files. Print to stdout.

## Undo

```bash
rm -rf "$HOME/.claude/experiments/$(date +%Y-%m-%d)-022-verbose-vs-terse"
```

That is the entire revert. The prompt creates only synthetic files in scratch; deleting the scratch directory restores you to your starting state. No live memory file is read or modified.

## What you should now see

- Two synthetic memory files expressing the same intent at very different word counts.
- A token estimate for each, computed by the same method.
- A cumulative cost table showing the spend over 1, 5, 10, 20 turns.
- A concrete number for "what verbosity costs me by the twentieth turn."
- A takeaway file naming the rule that drops out of the comparison.

## What you've learned

Article 022 is `intro-exempt`. By the end of this prompt you can see, in tokens, the price of expressing the same instruction two different ways — and you have a synthetic experiment you can re-run with your own preferences before Article 037 asks you to refactor your real memory files.

Subscribe so you don't miss Article 023, where you measure your real baseline.
