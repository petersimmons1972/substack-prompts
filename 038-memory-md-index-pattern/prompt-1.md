Copy the prompt below and paste it into Claude, ChatGPT, or your model of choice. The article linked from this directory's README explains what to expect.

````text
You are an auditor inspecting my `MEMORY.md` for the index pattern. You are read-only against my home directory. You may write only inside the scratch directory created in Step 1. You may not exfiltrate any file contents to any network endpoint. You may not read files matching `*.env`, `*credentials*`, `*token*`, `*.key`, `*.pem`, `id_rsa*`, `id_ed25519*`, or any path containing `/.ssh/` or `/.gnupg/`. You may not modify `~/.claude/settings.json`, install MCP servers, change hook configuration, or alter file permissions.

**Step 1 — create scratch directory.** Run:

```bash
SCRATCH="$HOME/.claude/experiments/$(date +%Y-%m-%d)-038-memory-index"
mkdir -p "$SCRATCH"
echo "scratch=$SCRATCH"
```

**Step 2 — locate the target file.** Find the loaded `MEMORY.md`. Prefer in this order: `~/.claude/projects/<project-slug>/memory/MEMORY.md` (the Claude Code default), then `~/MEMORY.md`, then `./MEMORY.md`. Record the chosen path and byte size in `$SCRATCH/00-target.md`. If none exist, write `NO_MEMORY_MD_FOUND` and emit a missing-prereq finding rather than aborting.

**Step 3 — segment into entries.** Treat each list item, each `##` or `###` heading-with-body, and each blank-line-separated paragraph as one *entry*. Number them. For each entry, capture: entry number, line range, byte size, word count, estimated tokens (`ceil(words / 0.75)`), and a one-line topic summary (no full quote). Write to `$SCRATCH/01-entries.md`.

**Step 4 — classify each entry.** Apply these tests in order and record `INDEX-WORTHY`, `PAYLOAD`, or `BARE-TOPIC`:

- **INDEX-WORTHY:** ≤25 tokens, names a topic plus a pointer (a path, a tag, or an Engram-recall query), holds no narrative body. Example shape: `Homelab patterns: memory_recall("<topic>", project="homelab")`.
- **PAYLOAD:** >100 tokens, contains narrative text, code blocks, or step-by-step procedures. The model can act on it without retrieval but it costs context every turn.
- **MIXED:** 25–100 tokens. Either a fat index entry or a thin payload. Note in justification.
- **BARE-TOPIC:** ≤10 tokens, names a topic with no pointer. The model has nothing to retrieve and the entry teaches nothing.

Write the classified table to `$SCRATCH/02-classified.md` with columns: entry number, classification, tokens, topic summary, recommended action (`KEEP`, `EXTERNALIZE`, `EXPAND-TO-POINTER`, `DELETE`).

**Step 5 — flag mismatches.** Produce `$SCRATCH/03-mismatches.md` listing:

- **payloads in the index:** entries classified `PAYLOAD` (these should be moved to separate files and replaced with a pointer);
- **dead pointers:** entries that look like `INDEX-WORTHY` but reference a path that does not exist on disk (verify with `test -f`, `test -d`; for `memory_recall` calls, mark as *unverifiable from prompt*);
- **bare topics:** entries with no pointer at all.

Do not paste full payload bodies. Use line ranges and one-line summaries.

**Step 6 — write the summary.** Produce `$SCRATCH/00-SUMMARY.md` with: target path, total entries, tokens by classification, count of mismatches, and a verdict (`INDEX-CLEAN` if PAYLOAD share <10% and no bare topics; `MIXED` if PAYLOAD share 10–40%; `PAYLOAD-HEAVY` if >40%). Print to stdout.
````
