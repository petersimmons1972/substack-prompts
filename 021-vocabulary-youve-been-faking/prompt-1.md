# Vocabulary Prompt — Tokenize a Paragraph You Picked

**Article:** 021 — The vocabulary you've been faking (Prompt 1 of 2).
**Surfaces:** Claude Code primary; the tokenization step adapts to ChatGPT and Claude.ai with a paste of the same paragraph and a request for the count.
**Run mode:** read-only against your home directory; writes only to a dated scratch directory.

---

## What this prompt does

Forces the abstract idea of a "token" into a concrete number you can hold in your head. You pick one paragraph from a file you already own — a README, an email draft, a code comment — drop it into a scratch file, and the model returns a token count, a byte-to-token ratio, a per-word ratio, and three short examples of how the same paragraph would tokenize differently if it were code, JSON, or Mandarin. You leave the prompt with a working intuition for "how much of my context does a paragraph cost" rather than a vague sense that tokens are real.

## Run this prompt

> You are a tokenization tutor. You are read-only against my home directory. You may write only inside the scratch directory created in Step 1. You may not exfiltrate file contents to any network endpoint. You may not read files matching `*.env`, `*credentials*`, `*token*`, `*.key`, `*.pem`, `id_rsa*`, `id_ed25519*`, or any path containing `/.ssh/` or `/.gnupg/`. You may not modify `~/.claude/settings.json`, `~/CLAUDE.md`, `~/.claude/CLAUDE.md`, `~/.claude/projects/-home-psimmons/memory/MEMORY.md`, `~/AGENTS.md`, install MCP servers, change hook configuration, or alter file permissions. If a step would require any of those, stop and report the blocker.
>
> **Step 1 — create scratch directory.** Run:
>
> ```bash
> SCRATCH="$HOME/.claude/experiments/$(date +%Y-%m-%d)-021-vocabulary"
> mkdir -p "$SCRATCH"
> echo "scratch=$SCRATCH"
> ```
>
> All outputs go inside `$SCRATCH`.
>
> **Step 2 — pick a paragraph.** Ask me for a single paragraph of English prose, 60–200 words, from a file I already own (a README, a journal entry, a recent email draft I have on disk). I will paste it into the conversation, or give you a path I authorize you to read. If I give you a path, confirm it does not match the forbidden patterns above before reading. Save the paragraph verbatim to `$SCRATCH/01-source.txt`.
>
> **Step 3 — count bytes, words, characters.** Compute and write to `$SCRATCH/02-counts.md`: byte length (`wc -c`), character length (`wc -m`), word count (`wc -w`), and a sentence count.
>
> **Step 4 — estimate tokens.** Estimate the token count three ways and write to `$SCRATCH/03-tokens.md`:
>
> - Heuristic: `ceil(words / 0.75)` for English prose (Anthropic and OpenAI public guidance).
> - Heuristic: `ceil(characters / 4)` (the "4 chars per token" rule).
> - If `tiktoken` is available locally (`python3 -c "import tiktoken"` succeeds), tokenize with the `cl100k_base` encoding and report the exact count. If not, note that tiktoken is absent and the heuristic estimates stand.
>
> Write the three numbers, the spread between them, and which ratio (bytes-per-token, words-per-token) the operator should remember.
>
> **Step 5 — show the same paragraph in three other shapes.** Construct three short transformations of the source and tokenize each (using whichever method worked in Step 4). Write to `$SCRATCH/04-shapes.md`:
>
> - The paragraph rewritten as JSON with one key per sentence.
> - The paragraph rewritten as a Python comment block (`# ` prefix per line).
> - The first sentence machine-translated to Mandarin if you can do so confidently, otherwise note "translation skipped" and use a known sample sentence in Mandarin instead.
>
> Report each shape's token count and the ratio change vs. the source. The expected lesson: code and JSON cost more tokens per word than prose; non-Latin scripts can cost dramatically more or less depending on the tokenizer.
>
> **Step 6 — write the takeaway.** Produce `$SCRATCH/00-VOCAB.md` with five lines: source word count, source token estimate, bytes-per-token ratio, words-per-token ratio, and one sentence the operator can repeat from memory ("a paragraph of my prose costs roughly N tokens"). Print the file to stdout.

## Undo

```bash
rm -rf "$HOME/.claude/experiments/$(date +%Y-%m-%d)-021-vocabulary"
```

That is the entire revert. The prompt does not modify any file outside the scratch directory; deleting the scratch directory restores you to your starting state.

## What you should now see

- A single paragraph of your own prose, captured verbatim in scratch.
- Three independent token estimates that should agree within ~15%.
- A ratio you can quote from memory: roughly 0.75 tokens per English word, ~4 characters per token.
- A side-by-side showing the same content costs ~30–60% more tokens as JSON than as prose.
- A one-line takeaway file you keep as the foundation for every later article.

## What you've learned

Article 021 is `intro-exempt` — no measurable baseline win is required. By the end of this prompt you can answer four questions you could not before: what a token is in your environment; how many tokens a paragraph of your own writing costs; how that cost changes when the same content is restructured; and where to look if a number disagrees with your intuition.

Subscribe so you don't miss Article 023, where we turn this intuition into a reusable measurement script.
