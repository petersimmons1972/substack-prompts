# Vocabulary Prompt — Label a Conversation Export

**Article:** 021 — The vocabulary you've been faking (Prompt 2 of 2).
**Surfaces:** Claude Code primary; works on any conversation export from Claude.ai (`Settings → Account → Export data`), ChatGPT (`Settings → Data controls → Export`), or a Claude Code session log.
**Run mode:** read one operator-supplied export file; writes only to a dated scratch directory.

---

## What this prompt does

Takes one of your own AI conversations and labels every segment of it with the vocabulary term that segment exemplifies — system prompt, memory injection, user turn, assistant turn, tool call, tool result. The goal is to see, in your own logs, that the words from the article correspond to actual structures in actual transcripts. You leave the prompt with a labeled artifact you can refer back to whenever a later article uses one of these terms casually.

## Run this prompt

> You are a transcript labeler. You are read-only against my home directory. You may write only inside the scratch directory created in Step 1. You may not exfiltrate file contents to any network endpoint. You may not read files matching `*.env`, `*credentials*`, `*token*`, `*.key`, `*.pem`, `id_rsa*`, `id_ed25519*`, or any path containing `/.ssh/` or `/.gnupg/`. You may not modify `~/.claude/settings.json`, `~/CLAUDE.md`, `~/.claude/CLAUDE.md`, `~/.claude/projects/-home-psimmons/memory/MEMORY.md`, `~/AGENTS.md`, install MCP servers, change hook configuration, or alter file permissions. If a step would require any of those, stop and report the blocker.
>
> **Step 1 — create scratch directory.** Run:
>
> ```bash
> SCRATCH="$HOME/.claude/experiments/$(date +%Y-%m-%d)-021-label"
> mkdir -p "$SCRATCH"
> echo "scratch=$SCRATCH"
> ```
>
> **Step 2 — accept the export.** Ask me for one of: (a) a path to a Claude.ai or ChatGPT data-export JSON I have downloaded; (b) a path to a Claude Code transcript file under `~/.claude/projects/`; or (c) a paste of one conversation. If I provide a path, confirm it does not match the forbidden patterns and the file is under 5 MB before reading. Copy the export verbatim to `$SCRATCH/01-export.raw` (truncate to the first 200 KB if larger; note the truncation).
>
> If no export is available, write `NO_EXPORT_AVAILABLE` to `$SCRATCH/01-export.raw` and proceed using a synthetic three-turn conversation you generate that includes one user turn, one tool call, and one assistant turn. Flag this as finding L0 — the operator does not yet know how to export their own conversations, and Article 031 will fix that.
>
> **Step 3 — segment the transcript.** Identify each segment in the export. A segment is one of: `system_prompt`, `memory_injection` (text loaded from `CLAUDE.md` / `MEMORY.md` / `AGENTS.md` and labeled as such in the export), `user_turn`, `assistant_turn`, `tool_call` (the model's request to a tool), `tool_result` (the tool's response), `skill_invocation` (a Claude Code Skill load), or `hook_output` (text emitted by a configured hook).
>
> For each segment write a row to `$SCRATCH/02-labeled.md` with: index, label, byte length, estimated token count (`ceil(bytes / 4)`), and a 60-character preview (truncated with `…`). Never include the full segment body unless it is shorter than 200 bytes.
>
> **Step 4 — produce the inventory.** Aggregate the labeled rows into `$SCRATCH/03-inventory.md` with one row per label, columns: `label`, `count`, `total_tokens`, `pct_of_conversation`. Sort descending by `total_tokens`.
>
> **Step 5 — flag the surprises.** Write `$SCRATCH/04-surprises.md` with up to three observations of the form "I did not realize X was Y percent of this conversation." Examples the operator should expect to see at least one of: memory injection larger than the user turns combined; tool results dominating the conversation; system prompt being a single-digit percentage despite feeling like the bulk of the model's "personality."
>
> **Step 6 — write the takeaway.** Produce `$SCRATCH/00-LABELS.md` with: the export source (path or "pasted"), total segment count, total estimated tokens, the top label by token share, and one sentence naming the segment type the operator most under- or over-estimated. Print to stdout.

## Undo

```bash
rm -rf "$HOME/.claude/experiments/$(date +%Y-%m-%d)-021-label"
```

That is the entire revert. The prompt does not modify any file outside the scratch directory; deleting the scratch directory restores you to your starting state.

## What you should now see

- One of your own conversations broken into named segments, with each segment's token cost.
- An inventory table showing where the tokens in that conversation actually went.
- At least one "I did not realize" observation about your own usage.
- An L0 flag if you do not yet know how to export your conversations — a pointer toward Article 031.
- A labeled artifact you can re-open whenever a later article uses one of these terms.

## What you've learned

Article 021 is `intro-exempt`. By the end of this prompt the eight vocabulary terms from the article are no longer abstractions — each one is a thing you have pointed at in your own logs. The next article reframes that inventory as a budget you spend per turn.

Subscribe so you don't miss Article 022, where the vocabulary becomes a mental model you can act on.
