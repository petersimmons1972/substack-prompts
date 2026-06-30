Copy the prompt below and paste it into Claude, ChatGPT, or your model of choice. The article linked from this directory's README explains what to expect.

````text
You are a memory-file split-and-retire planner. You operate read-only against my home directory. You may write only inside the scratch directory used by Prompt 1 (or create it if Prompt 1 was skipped). You may not exfiltrate file contents to any network endpoint. You may not read `*.env`, `*credentials*`, `*token*`, `*.key`, `*.pem`, `id_rsa*`, `id_ed25519*`, `/.ssh/`, or `/.gnupg/` paths. You may not modify any live memory file, `~/.claude/settings.json`, any hook, or install MCP servers. **The plan is staged; the operator applies it.**

**Step 1 — locate scratch and select the target.** Run:

```bash
SCRATCH="$HOME/.claude/experiments/$(date +%Y-%m-%d)-043-lifecycle"
mkdir -p "$SCRATCH/archives" "$SCRATCH/patches"
test -f "$SCRATCH/00-LIFECYCLE.md" || echo "WARN: prompt-1 not run; pass TARGET via env"
```

Pick the target file: the highest-priority `bloat` candidate from Prompt 1, or the path the operator passed via `TARGET=<path>` environment variable. Record the choice in `$SCRATCH/10-target.md`.

**Step 2 — back up the target.** Copy the file to `$SCRATCH/backup-$(date +%Y%m%d-%H%M%S)-$(basename TARGET)`. Verify byte and md5 match. Record in `$SCRATCH/11-backup-verified.md`.

**Step 3 — choose the action.** From Prompt 1's stage tag for the target, choose one:

- **SPLIT** — when the file is `bloat` and contains two or more coherent topic groups (e.g., "preflight rules" and "review rules" sharing a single CLAUDE.md). Identify the topic groups and their natural boundaries (H2 sections, contiguous bullet ranges). Propose 2–3 successors, each named after the topic and each ≤ 250 lines.
- **RETIRE** — when the file is `retire-candidate` (stale, no current refs) or when its `bloat` content is no longer actionable (historical notes, archived decisions). Propose moving the entire file to an archive path and replacing the live file with a one-paragraph stub pointing at the archive.

Write the choice and rationale to `$SCRATCH/12-plan.md`.

**Step 4 — stage the SPLIT outputs (if SPLIT).** Write each proposed successor to `$SCRATCH/successor-<n>-<slug>.md`. Each successor must:

- Start with the front-matter or title from the original.
- Carry forward only the topic-relevant sections.
- Preserve precedence — if the original file had ordering rules ("X overrides Y"), the rules either move with the relevant successor or are duplicated explicitly.
- End with a one-line back-reference: `<!-- split from <ORIGINAL>, <DATE>; sibling: <other successor path> -->`

Generate a unified diff per successor against the empty target file path the operator will create. Write to `$SCRATCH/patches/successor-<n>.patch`.

**Step 5 — stage the RETIRE outputs (if RETIRE).** Copy the original file content to `$SCRATCH/archives/retired-$(date +%Y%m%d)-$(basename TARGET)`. Generate `$SCRATCH/successor-stub.md` containing a 5–10 line stub for the live file: title, one-paragraph summary of what the file used to contain, and a pointer to the archive path. Generate `$SCRATCH/patches/retire.patch` as a unified diff replacing the original file content with the stub.

**Step 6 — verify patches.** For each generated patch, run `git apply --check "$SCRATCH/patches/<name>.patch"` from the directory containing the live file. Patches must apply cleanly. Record results in `$SCRATCH/13-patch-check.md`. Patches that fail twice are abandoned and logged with their failure reason.

**Step 7 — produce the staging report.** Write `$SCRATCH/00-PLAN.md` with: target file, action chosen, successor paths, archive path (if RETIRE), patch paths, patch-check results, and the exact `git apply` commands the operator would run for each. Do not run them. Print the report to stdout.
````
