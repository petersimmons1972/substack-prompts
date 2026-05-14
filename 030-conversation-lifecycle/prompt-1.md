You are an analyst measuring the relevance decay of one long conversation. You are read-only against my home directory. You may write only inside the scratch directory created in Step 1. You may not exfiltrate any file contents to any network endpoint. You may not read files matching `*.env`, `*credentials*`, `*token*`, `*.key`, `*.pem`, `id_rsa*`, `id_ed25519*`, or any path containing `/.ssh/` or `/.gnupg/`. You may not modify `~/.claude/settings.json`, `~/CLAUDE.md`, `~/.claude/CLAUDE.md`, any memory file, any hook, or install MCP servers. You may not export the conversation outside scratch.

**Step 1 — create scratch directory.** Run:

```bash
SCRATCH="$HOME/.claude/experiments/$(date +%Y-%m-%d)-030-lifecycle"
mkdir -p "$SCRATCH"
echo "scratch=$SCRATCH"
```

**Step 2 — locate the transcript.** Find the most recent conversation transcript or session log available read-only on the reader's surface. For Claude Code, look under `~/.claude/projects/` for the active project's history file. Record path and turn count to `$SCRATCH/00-source.md`. If no transcript is reachable, emit finding **X0 — missing prereq** and exit cleanly: relevance estimation requires turn-level access.

**Step 3 — define the working topic.** Ask the operator (or, for an automated run, take from a `$SCRATCH/topic.txt` if present) to name the *current* working topic in one sentence. Write it to `$SCRATCH/01-topic.md`. Default if absent: take the last user turn as the topic.

**Step 4 — score relevance per turn.** For each turn (user + assistant pair), produce a 0–5 relevance score against the working topic using these rubrics: 5 = directly references current topic; 3 = related context (file paths, tools, prior decisions still in play); 1 = distant context that occasionally informs phrasing; 0 = unrelated tangent or resolved subtask. Write `$SCRATCH/02-relevance.md` with columns: `turn`, `relevance`, `tokens_est`, `cumulative_tokens`. Do not include turn bodies.

**Step 5 — locate the restart point.** Walk turns from newest to oldest. The restart point is the highest turn number where the cumulative relevance score from that turn forward is ≥ 80% of the total relevance score. Equivalently: the earliest turn that still matters. Record the restart turn in `$SCRATCH/03-restart-point.md`, with the tokens you would shed (cumulative tokens *before* that turn) and the tokens you would carry (cumulative tokens *from* that turn forward).

**Step 6 — render the timeline.** Produce `$SCRATCH/00-LIFECYCLE.md` with: turn count, total tokens, restart turn, tokens shed, tokens carried, and a sparkline of relevance scores rendered as block characters (`▁▂▃▄▅▆▇█`) from oldest to newest. Mark the restart turn with a `|` divider. Print to stdout.
