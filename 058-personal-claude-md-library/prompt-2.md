Copy the prompt below and paste it into Claude, ChatGPT, or your model of choice. The article linked from this directory's README explains what to expect.

````text
You are a library structure planner. You operate read-only against the operator's memory files and the inventory in scratch. You may write only inside the scratch directory used by Prompt 1. You may not modify any live memory file, install MCP servers, exfiltrate file contents, or read `*.env`, `*credentials*`, `*token*`, `*.key`, `*.pem`, `id_rsa*`, `id_ed25519*`, `/.ssh/`, or `/.gnupg/` paths.

**Step 1 — locate scratch and inputs.** Run:

```bash
SCRATCH="$HOME/.claude/experiments/$(date +%Y-%m-%d)-058-library"
test -f "$SCRATCH/00-INVENTORY.md" || { echo "ERROR: run prompt-1 first"; exit 1; }
mkdir -p "$SCRATCH/library" "$SCRATCH/migrations" "$SCRATCH/backups"
```

**Step 2 — design the library structure.** Group GENERAL entries from `02-tags.md` by category. Suggested layout:

- `library/00-readme.md` — overview, versioning notes
- `library/01-defaults.md` — behavioral defaults, decision percentages
- `library/02-tools.md` — tool preferences (xh, stern, semgrep, ast-grep, etc.)
- `library/03-security.md` — security rules and security-floor declarations
- `library/04-pre-flight.md` — pre-flight protocol
- `library/05-engram-or-memory.md` — memory/recall patterns
- `library/06-cost-guardrails.md` — cost guardrails and wake-the-founder triggers
- `library/07-personal.md` — operator's identity-bearing rules (terse responses, name, etc.)

Adjust based on the operator's actual GENERAL inventory; not every category needs a file.

Write each library file to `$SCRATCH/library/<NN>-<topic>.md` containing the GENERAL entries that belong there.

**Step 3 — produce the canonical entry resolution.** For duplicate entries (from `04-duplicates.md`), pick a canonical wording. Each library entry has a stable `id` (e.g., `LIB-TOOLS-001`) so projects can reference it. Write to `$SCRATCH/10-canonical.md`.

**Step 4 — back up affected files.** Copy each project's `CLAUDE.md`/`AGENTS.md` (and `~/CLAUDE.md` if it will be touched) to `$SCRATCH/backups/<file>-<TS>`. Verify byte and md5. Record in `$SCRATCH/11-backup-verified.md`.

**Step 5 — produce per-file migration plans.** For each project file, write `$SCRATCH/migrations/<project>-plan.md` with:

- **Library imports** — list of library files this project includes by reference. Reference syntax (operator chooses): a `<!-- include: ~/library/01-defaults.md -->` comment, a Markdown link, or a per-project frontmatter line. The reference is *documentation*, not auto-loaded — the operator chooses how to honor it.
- **Project-specific retained content** — entries from the original file that stay (PROJECT-SPECIFIC tag).
- **Removed content** — entries removed because they are now sourced from the library, with the library entry id they map to.
- **Migration patch** — a unified diff against the original file showing the new shape.
- **Rollback** — exact `git restore` or `cp -p backup/<file>-<TS>` command.

Order projects by least-active first; the operator migrates one project at a time and verifies the project still works before moving to the next. Active in-flight projects (high commit cadence) are migrated last to minimize blast radius.

**Step 6 — verify patches.** For each migration patch, run `git apply --check` from the relevant project directory. Patches must apply cleanly. Write results to `$SCRATCH/12-patch-check.md`. Patches that fail twice are abandoned and logged with the reason.

**Step 7 — produce the staging report.** Write `$SCRATCH/00-MIGRATION.md` with: library file paths, per-project migration plan paths, patch-check results, the recommended migration order, and a "verify after each project" checklist (run that project's tests, do a representative task, confirm no behavior change). Print to stdout. Do not run any apply.
````
