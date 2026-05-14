# Prompting Fundamentals Prompt — XML Restructure A/B

**Article:** 026 — Prompting fundamentals you skipped (Prompt 1 of 2).
**Surfaces:** any surface where you can re-send a prompt; replay step needs API access (Anthropic or OpenAI) for fair token measurement.
**Run mode:** writes only to a dated scratch directory; reads only operator-supplied prompt content.

---

## What this prompt does

Takes one of your recent verbose prompts, restructures it with XML tags and explicit role framing per Anthropic's prompt-engineering guidance, sends both versions to the same model, and reports the token delta and the quality delta side by side. The goal is to put a number on a frequently-cargo-culted technique. If XML structuring earns its keep on your task, you'll see it in the metrics; if it doesn't, you'll see that too. Either result corrects a common assumption.

## Run this prompt

> You are a prompt-restructuring analyst. You are read-only against my home directory except for the scratch directory created in Step 1. You may not exfiltrate file contents to any network endpoint *except* the model API endpoint required to run the comparison, and only with the prompt I have explicitly authorized. You may not read files matching `*.env`, `*credentials*`, `*token*`, `*.key`, `*.pem`, `id_rsa*`, `id_ed25519*`, or any path containing `/.ssh/` or `/.gnupg/`. You may not modify `~/.claude/settings.json`, `~/CLAUDE.md`, `~/.claude/CLAUDE.md`, `~/.claude/projects/-home-psimmons/memory/MEMORY.md`, `~/AGENTS.md`, install MCP servers, change hook configuration, or alter file permissions. API credentials are read from environment variables and never echoed.
>
> **Step 1 — create scratch directory.** Run:
>
> ```bash
> SCRATCH="$HOME/.claude/experiments/$(date +%Y-%m-%d)-026-xml-ab"
> mkdir -p "$SCRATCH"
> echo "scratch=$SCRATCH"
> ```
>
> **Step 2 — capture the verbose original.** Ask me to paste a recent prompt I have used at least once that is over 200 words and contains multiple distinct sections (instructions, examples, content to process, output requirements) jumbled into prose. If I cannot supply one, generate a representative example you label `SYNTHETIC` and flag P0 — operator does not yet have a verbose prompt on hand to refactor; the article should be re-read after a week of normal usage.
>
> Save the original to `$SCRATCH/01-original.txt` verbatim. Strip any client/proprietary identifiers and replace with placeholders (`<CLIENT>`, `<PROJECT>`); record the substitutions in `$SCRATCH/01-redactions.md`.
>
> **Step 3 — restructure with XML.** Produce `$SCRATCH/02-restructured.txt` applying these rules per Anthropic's prompt-engineering guide:
>
> - Wrap the role/persona framing in `<role>...</role>`.
> - Wrap any input content the model should process in `<input>...</input>` (or task-named tags like `<source_text>`, `<diff>`).
> - Wrap examples (if any) in `<example>...</example>` with sub-tags `<input>` and `<output>`.
> - Wrap the explicit task instruction in `<task>...</task>`.
> - Wrap the output requirements in `<output_format>...</output_format>`.
> - Move all instructions to the top, content to the middle, output requirements last.
>
> The restructured prompt must preserve the original semantic intent. Do not add new content; do not remove content beyond redundant connective phrases that XML structure makes unnecessary.
>
> **Step 4 — token-count both.** Estimate tokens for both versions. Use `tiktoken cl100k_base` if available; otherwise `ceil(words / 0.75)`. Write to `$SCRATCH/03-counts.md`: original tokens, restructured tokens, delta (often negative — XML usually saves tokens by replacing prose framing with brief tags).
>
> **Step 5 — send both to the same model.** Default model: Claude Haiku 4.5 (cheap, deterministic enough for an A/B). Send the original prompt; save response to `$SCRATCH/04-original-response.txt` with token count and latency. Send the restructured prompt; save response to `$SCRATCH/05-restructured-response.txt` with token count and latency. Use temperature 0 for both. Use the same system prompt (none, unless the original prompt requires one).
>
> If the API call fails, record the error and continue to Step 6 with the comparison limited to input tokens only.
>
> **Step 6 — score both responses.** Apply the same four-criterion rubric used in Article 024 Prompt 2 (correctness, completeness, format fidelity, brevity), 1–5 each. Note which criteria are objective vs subjective. Write `$SCRATCH/06-rubric.md`.
>
> **Step 7 — produce the verdict.** Write `$SCRATCH/00-AB.md` with: original input tokens, restructured input tokens, input delta, original output tokens, restructured output tokens, original score total, restructured score total, score delta, and a one-sentence verdict — `XML_EARNS_KEEP` if score delta ≥ 0 and either input or output tokens decreased; `XML_NEUTRAL` if score delta = 0 and tokens unchanged within 5%; `XML_OVERHEAD` if tokens increased without a quality improvement. Print to stdout.

## Undo

```bash
rm -rf "$HOME/.claude/experiments/$(date +%Y-%m-%d)-026-xml-ab"
```

That is the entire revert. The prompt makes API calls but writes only inside the scratch directory.

## What you should now see

- Your original verbose prompt and an XML-restructured equivalent in scratch.
- Input token counts for both, usually showing the XML version is shorter.
- Two responses from the same model on the same task.
- A four-criterion rubric scoring both responses.
- A verdict file that names whether XML structure earned its keep on this task.

## How to confirm the win

Article 026 is value-tagged `context-savings`. The win is realized when `XML_EARNS_KEEP` fires. Anthropic's published guidance shows XML structuring helps most on tasks with multiple distinct content blocks (instruction + reference text + examples); it helps less on single-concern prompts. If your verdict comes back `XML_NEUTRAL` or `XML_OVERHEAD`, the prompt was already structured enough that XML did not add signal, or the task did not have enough distinct content blocks. Both results are useful: keep the verdict file as evidence the next time someone tells you to add XML tags reflexively. The cost-savings number to remember: typical operators see 5–20% input-token reduction on multi-block prompts after restructuring.

Subscribe so you don't miss Article 027, where the discipline of *how* to run prompts safely is locked in.
