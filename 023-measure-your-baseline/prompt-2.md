Copy the prompt below and paste it into Claude, ChatGPT, or your model of choice. The article linked from this directory's README explains what to expect.

````text
You are a baseline-comparison auditor. You are read-only against my home directory. You may write only inside the scratch directory created in Step 1. You may not exfiltrate file contents to any network endpoint. You may not read files matching `*.env`, `*credentials*`, `*token*`, `*.key`, `*.pem`, `id_rsa*`, `id_ed25519*`, or any path containing `/.ssh/` or `/.gnupg/`. You may not modify `~/.claude/settings.json`, `~/CLAUDE.md`, `~/.claude/CLAUDE.md`, `~/.claude/projects/-home-psimmons/memory/MEMORY.md`, `~/AGENTS.md`, install MCP servers, change hook configuration, or alter file permissions. You may read `~/CLAUDE.md` for the purpose of copying it into scratch; you may not write to the original.

**Step 1 — create scratch directory and clone CLAUDE.md.** Run:

```bash
SCRATCH="$HOME/.claude/experiments/$(date +%Y-%m-%d)-023-bloat-delta"
mkdir -p "$SCRATCH/clean" "$SCRATCH/bloated"
if [ -f "$HOME/CLAUDE.md" ]; then
  cp -p "$HOME/CLAUDE.md" "$SCRATCH/clean/CLAUDE.md"
else
  echo "NO_CLAUDE_MD_FOUND" > "$SCRATCH/clean/CLAUDE.md"
fi
cp -p "$SCRATCH/clean/CLAUDE.md" "$SCRATCH/bloated/CLAUDE.md"
echo "scratch=$SCRATCH"
```

If `~/CLAUDE.md` does not exist, flag this as finding B0 — the operator has not yet placed a project-level memory file at home; later articles assume one. The dry-run should still succeed using the placeholder file.

**Step 2 — append a useless paragraph to the bloated copy.** Append exactly the following 412-word paragraph (verbatim) to `$SCRATCH/bloated/CLAUDE.md`. The paragraph is intentionally generic, non-identifying, and adds zero operational signal:

```
## Notes on consistency and craft

Consistency is the mother of mastery, and mastery the parent of consistency. In every domain — woodworking, prose, software, dressage — the practitioner returns daily to the same small set of motions, varying only what the day's material demands. The lathe receives a fresh blank; the page receives a fresh sentence; the function receives a fresh test. Across these returns the practitioner accumulates not knowledge of new techniques but a deeper acquaintance with the techniques already chosen. This deeper acquaintance is sometimes called taste, sometimes called intuition, sometimes called experience; the words are different doors into the same room. The room is small, and its furniture is the few habits the practitioner has decided are worth keeping. To walk into the room each morning is to choose, again, that those few habits matter more than the day's distractions. The choice is rarely dramatic. It usually looks like making coffee, opening the editor, and writing the first sentence before the inbox has been opened. It looks like running the test before the implementation, and writing the implementation before the next test. It looks like backing up the file before the edit, and committing the edit before the next experiment. None of these motions is interesting in isolation. Each is, in fact, almost insultingly small. The interest lies in the accumulation — the discovery, twenty years later, that the small motions have built a body of work that the dramatic gestures of more talented but less consistent practitioners have not. Memory files are subject to the same logic. The line you add today will be read tomorrow, and the day after, and the day after that. Adding it is cheap. Reading it, every turn, for the rest of the project, is the actual cost. So the discipline is not to add what is interesting but to add only what is repeatable, what is true on the worst day as well as the best, what survives the kind of audit you would conduct if you knew you were going to be cross-examined about it next year. The rest is decoration, and decoration in a memory file is a tax on every conversation that follows.
```

Confirm the bloated copy is exactly the clean copy plus this paragraph (use `diff` and report the line and word delta).

**Step 3 — run the baseline against the clean copy.** Use the Article 023 baseline prompt logic (from `posts/free/023-measure-your-baseline/prompts/baseline.md`) but operate on `$SCRATCH/clean/CLAUDE.md` in place of `~/CLAUDE.md` for memory-file inventory and token estimation. All other inputs (`~/.claude/CLAUDE.md`, `MEMORY.md`, `AGENTS.md`, `settings.json`) read live as usual. Write the eight-line summary to `$SCRATCH/clean/00-BASELINE.md`.

**Step 4 — run the baseline against the bloated copy.** Repeat Step 3 with `$SCRATCH/bloated/CLAUDE.md`. Write to `$SCRATCH/bloated/00-BASELINE.md`.

**Step 5 — diff and report.** Produce `$SCRATCH/00-DELTA.md` showing the side-by-side of the two `00-BASELINE.md` files and the per-line delta. Highlight `memory_files_total_tokens`. Print the delta file to stdout.
````
