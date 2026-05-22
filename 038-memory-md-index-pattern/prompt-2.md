Copy the prompt below and paste it into Claude, ChatGPT, or your model of choice. The article linked from this directory's README explains what to expect.

````text
You are a remediation planner. You operate read-only against my live `MEMORY.md`. You may write only inside the scratch directory used by Prompt 1. You may not exfiltrate file contents. You may not read `*.env`, `*credentials*`, `*token*`, `*.key`, `*.pem`, `id_rsa*`, `id_ed25519*`, `/.ssh/`, or `/.gnupg/` paths. You may not modify the live `MEMORY.md`, `~/.claude/settings.json`, `~/CLAUDE.md`, or any file outside the scratch directory. You may not install MCP servers, change hook configuration, or alter permissions. You stage a fix; the human applies it.

**Step 1 — locate scratch and classification.** Run:

```bash
SCRATCH="$HOME/.claude/experiments/$(date +%Y-%m-%d)-038-memory-index"
test -f "$SCRATCH/02-classified.md" || { echo "ERROR: run prompt-1 first"; exit 1; }
```

Read `$SCRATCH/00-target.md` and `$SCRATCH/02-classified.md`. If `00-target.md` contains `NO_MEMORY_MD_FOUND`, stop with a missing-prereq finding.

**Step 2 — back up the target.** Copy the live `MEMORY.md` to scratch with a timestamped name:

```bash
TARGET="<path from 00-target.md>"
TS="$(date +%Y%m%d-%H%M%S)"
cp -p "$TARGET" "$SCRATCH/backup-${TS}-MEMORY.md"
```

Verify byte-count and md5 match. Record in `$SCRATCH/11-backup-verified.md`.

**Step 3 — extract payloads.** Make `$SCRATCH/payloads/`. For each entry classified `PAYLOAD` or `MIXED-thin-payload`, write its body to `$SCRATCH/payloads/<topic-slug>.md`. The slug is derived from the entry's topic summary (lowercase, hyphenated, ≤40 chars). Record the mapping (entry number → slug → byte count) in `$SCRATCH/12-payload-map.md`. Do not echo payload bodies into the map.

**Step 4 — produce the staged `MEMORY.md`.** Write `$SCRATCH/13-proposed-MEMORY.md` containing only:

- The original file's preamble and section headings.
- For each `KEEP` entry from Prompt 1: the original line, unchanged.
- For each extracted payload: a one-line pointer in the form `- <Topic>: see ~/.claude/memory/payloads/<slug>.md`. (The path under `~/.claude/memory/payloads/` is the proposed *future* location; the file lives in scratch until the human applies the change.)
- For each `BARE-TOPIC` entry: either expand into a pointer (if the topic maps to an existing payload) or drop with a note in `14-decisions.md`.
- Drop entries marked `DELETE` in Prompt 1.
- Add a single comment at the top: `<!-- restructured 2026-MM-DD via article 038; payloads in ~/.claude/memory/payloads/ -->`.

**Step 5 — measure the delta.** Compute byte size, line count, word count, and estimated tokens for both files. Write `$SCRATCH/14-delta.md` with two rows and a `tokens_saved_in_context` field (the live file's tokens minus the staged file's tokens). Note that the on-disk total grows by the payload directory size — payloads are not deleted, only externalized.

**Step 6 — produce apply and undo.** Write `$SCRATCH/15-apply.sh` containing the two operations the human will run:

```bash
mkdir -p "$HOME/.claude/memory/payloads"
cp -p "$SCRATCH/payloads/"*.md "$HOME/.claude/memory/payloads/"
cp -p "$SCRATCH/13-proposed-MEMORY.md" "$TARGET"
```

And `$SCRATCH/16-undo.sh` containing:

```bash
cp -p "$SCRATCH/backup-${TS}-MEMORY.md" "$TARGET"
rm -rf "$HOME/.claude/memory/payloads"
```

The undo restores `MEMORY.md` and removes the payload directory the apply created. Make both scripts executable. Print `14-delta.md` and `12-payload-map.md` to stdout.
````
