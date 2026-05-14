Copy the prompt below and paste it into Claude, ChatGPT, or your model of choice. The article linked from this directory's README explains what to expect.

````text
You are a transcript labeler. You are read-only against my home directory. You may write only inside the scratch directory created in Step 1. You may not exfiltrate file contents to any network endpoint. You may not read files matching `*.env`, `*credentials*`, `*token*`, `*.key`, `*.pem`, `id_rsa*`, `id_ed25519*`, or any path containing `/.ssh/` or `/.gnupg/`. You may not modify `~/.claude/settings.json`, `~/CLAUDE.md`, `~/.claude/CLAUDE.md`, `~/.claude/projects/-home-psimmons/memory/MEMORY.md`, `~/AGENTS.md`, install MCP servers, change hook configuration, or alter file permissions. If a step would require any of those, stop and report the blocker.

**Step 1 — create scratch directory.** Run:

```bash
SCRATCH="$HOME/.claude/experiments/$(date +%Y-%m-%d)-021-label"
mkdir -p "$SCRATCH"
echo "scratch=$SCRATCH"
```

**Step 2 — accept the export.** Ask me for one of: (a) a path to a Claude.ai or ChatGPT data-export JSON I have downloaded; (b) a path to a Claude Code transcript file under `~/.claude/projects/`; or (c) a paste of one conversation. If I provide a path, confirm it does not match the forbidden patterns and the file is under 5 MB before reading. Copy the export verbatim to `$SCRATCH/01-export.raw` (truncate to the first 200 KB if larger; note the truncation).

If no export is available, write `NO_EXPORT_AVAILABLE` to `$SCRATCH/01-export.raw` and proceed using a synthetic three-turn conversation you generate that includes one user turn, one tool call, and one assistant turn. Flag this as finding L0 — the operator does not yet know how to export their own conversations, and Article 031 will fix that.

**Step 3 — segment the transcript.** Identify each segment in the export. A segment is one of: `system_prompt`, `memory_injection` (text loaded from `CLAUDE.md` / `MEMORY.md` / `AGENTS.md` and labeled as such in the export), `user_turn`, `assistant_turn`, `tool_call` (the model's request to a tool), `tool_result` (the tool's response), `skill_invocation` (a Claude Code Skill load), or `hook_output` (text emitted by a configured hook).

For each segment write a row to `$SCRATCH/02-labeled.md` with: index, label, byte length, estimated token count (`ceil(bytes / 4)`), and a 60-character preview (truncated with `…`). Never include the full segment body unless it is shorter than 200 bytes.

**Step 4 — produce the inventory.** Aggregate the labeled rows into `$SCRATCH/03-inventory.md` with one row per label, columns: `label`, `count`, `total_tokens`, `pct_of_conversation`. Sort descending by `total_tokens`.

**Step 5 — flag the surprises.** Write `$SCRATCH/04-surprises.md` with up to three observations of the form "I did not realize X was Y percent of this conversation." Examples the operator should expect to see at least one of: memory injection larger than the user turns combined; tool results dominating the conversation; system prompt being a single-digit percentage despite feeling like the bulk of the model's "personality."

**Step 6 — write the takeaway.** Produce `$SCRATCH/00-LABELS.md` with: the export source (path or "pasted"), total segment count, total estimated tokens, the top label by token share, and one sentence naming the segment type the operator most under- or over-estimated. Print to stdout.
````
