Copy the prompt below and paste it into Claude, ChatGPT, or your model of choice. The article linked from this directory's README explains what to expect.

````text
You are a memory library tagger. You operate read-only against the operator's home directory and project working directories. You may write only inside the scratch directory created in Step 1. You may not modify any live file, install MCP servers, exfiltrate file contents, or read `*.env`, `*credentials*`, `*token*`, `*.key`, `*.pem`, `id_rsa*`, `id_ed25519*`, `/.ssh/`, or `/.gnupg/` paths.

**Step 1 — create scratch directory.** Run:

```bash
SCRATCH="$HOME/.claude/experiments/$(date +%Y-%m-%d)-058-library"
mkdir -p "$SCRATCH"
```

**Step 2 — enumerate memory files across projects.** Inventory `~/CLAUDE.md`, `~/.claude/CLAUDE.md`, `~/AGENTS.md`, every `MEMORY.md` under `~/.claude/projects/*/memory/`, and every `CLAUDE.md`/`AGENTS.md` under `~/projects/*/` (recursive depth 2). Record path, line count, byte size, and the project the file belongs to (if any). Write to `$SCRATCH/00-files.md`.

**Step 3 — extract entries.** Walk each file and produce `$SCRATCH/01-entries.md` with one row per entry: `entry_id` (file:line), `text` (≤120 chars), `category` (`security`, `process`, `tool-pref`, `style`, `art`, `priority`, `other`), and `source_file`.

**Step 4 — apply tagging signatures.** For each entry, evaluate against the signature set:

| indicator | suggests | strength |
|---|---|---|
| references a specific repo, namespace, or product name | PROJECT-SPECIFIC | strong |
| references a generic tool or workflow (e.g., "use xh for HTTP", "edit-not-sed") | GENERAL | strong |
| references a specific deploy target, port, or service | PROJECT-SPECIFIC | strong |
| references a generic security or hygiene rule | GENERAL | strong |
| references operator's name, identity, or personal preference | GENERAL (personal layer) | medium |
| references a one-off project file path | PROJECT-SPECIFIC | strong |
| references a workflow that recurs across projects (commit hygiene, test cadence) | GENERAL | medium |

Apply tags. Edge cases (rule applies to a project but is generically reusable) tag as both with a justification. Write to `$SCRATCH/02-tags.md`.

**Step 5 — score per file.** For each memory file, compute the GENERAL-share (% of entries tagged GENERAL) and PROJECT-SPECIFIC-share. Write to `$SCRATCH/03-scores.md`. Files with high GENERAL share are candidates for migration to the library; files with high PROJECT-SPECIFIC share stay in the project's repo. Mixed files need splitting.

**Step 6 — surface duplicates.** Identify entries that appear (verbatim or near-verbatim) in multiple memory files. Each duplicate is either a candidate for the library (single source of truth, referenced by name) or evidence of drift (the same rule has slightly different wording in different files). Write to `$SCRATCH/04-duplicates.md`.

**Step 7 — produce the inventory report.** Write `$SCRATCH/00-INVENTORY.md` with: total entries, count per tag, per-file GENERAL share, top duplicates, and a recommendation for which files migrate, split, or stay. Print to stdout.
````
