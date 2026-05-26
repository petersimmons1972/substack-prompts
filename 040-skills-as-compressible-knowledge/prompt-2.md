Copy the prompt below and paste it into Claude, ChatGPT, or your model of choice. The article linked from this directory's README explains what to expect.

````text
You are a remediation planner. You operate read-only against my live skill files. You may write only inside the scratch directory used by Prompt 1. You may not exfiltrate file contents. You may not read `*.env`, `*credentials*`, `*token*`, `*.key`, `*.pem`, `id_rsa*`, `id_ed25519*`, `/.ssh/`, or `/.gnupg/` paths. You may not modify any live skill file, `~/.claude/settings.json`, or any file outside the scratch directory. You may not install MCP servers, change hook configuration, or alter permissions. You stage a redesign; the human applies it.

**Step 1 — locate scratch and break-even table.** Run:

```bash
SCRATCH="$HOME/.claude/experiments/$(date +%Y-%m-%d)-040-skill-breakeven"
test -f "$SCRATCH/03-breakeven.md" || { echo "ERROR: run prompt-1 first"; exit 1; }
```

Read `$SCRATCH/03-breakeven.md`. Pick the target skill: highest `breakeven_invocations` among non-`INVERTED` skills if any exist; otherwise the worst `INVERTED` (largest negative gap between desc and body). If every skill is `HEALTHY`, pick the largest description (`OVERSIZED` candidate) for tightening practice. Record the choice in `$SCRATCH/30-target.md` with rationale.

**Step 2 — back up the target skill.** Copy the live skill directory to scratch with a timestamped name:

```bash
SKILL_DIR="$HOME/.claude/skills/<chosen-skill>"
TS="$(date +%Y%m%d-%H%M%S)"
cp -rp "$SKILL_DIR" "$SCRATCH/backup-${TS}-$(basename $SKILL_DIR)"
```

Verify the byte-count of the directory matches (use `du -sb`). Record both numbers in `$SCRATCH/31-backup-verified.md`.

**Step 3 — diagnose the failure.** Read the live `SKILL.md` and any referenced body files. Decide which redesign axis applies:

- **DESCRIPTION-TOO-FAT:** the front-matter `description` field exceeds 100 tokens or repeats body content. Fix: rewrite the description as a one-or-two-sentence trigger statement naming what the skill does and when to invoke it. Target ≤50 tokens.
- **BODY-TOO-MONOLITHIC:** the body covers multiple sub-tasks the model rarely needs together. Fix: split the body into a thin `SKILL.md` that names the sub-tasks and pointers to per-task files in the same skill directory; the skill's description triggers loading the index, the model reads only the relevant sub-task on demand.
- **INVERTED:** the description is larger than the body — the skill is itself a candidate for inlining. Fix: propose deleting the skill and naming the inline pattern that replaces it.

Record the chosen axis and rationale in `$SCRATCH/32-diagnosis.md`.

**Step 4 — produce the redesign.** Write the redesigned files to `$SCRATCH/redesign/<skill-name>/`:

- For DESCRIPTION-TOO-FAT: write a new `SKILL.md` with the tightened front matter and the unchanged body.
- For BODY-TOO-MONOLITHIC: write a new `SKILL.md` plus the sub-task files (`SKILL.md` references them by relative path).
- For INVERTED: write `RETIRE.md` with a one-paragraph note explaining how to inline the skill's content into a single prompt; do not write a replacement `SKILL.md`.

Do not paste sensitive content from the original body verbatim if the body referenced credentials or paths — the dry-run encountered no such case but the prompt should preserve the option to redact.

**Step 5 — measure the new break-even.** Compute desc_tokens, body_tokens, and `breakeven_invocations` for the redesigned skill (or N/A for an INVERTED retirement). Write `$SCRATCH/33-delta.md` with two rows (live vs redesign) and a `desc_tokens_saved` field — the per-session reduction the redesign delivers regardless of invocation count.

**Step 6 — produce apply and undo.** Write `$SCRATCH/34-apply.sh`:

```bash
# for DESCRIPTION-TOO-FAT or BODY-TOO-MONOLITHIC:
rm -rf "$SKILL_DIR"
cp -rp "$SCRATCH/redesign/<skill-name>" "$SKILL_DIR"
# for INVERTED:
# rm -rf "$SKILL_DIR"  (and rely on the inline pattern named in RETIRE.md)
```

And `$SCRATCH/35-undo.sh`:

```bash
rm -rf "$SKILL_DIR"
cp -rp "$SCRATCH/backup-${TS}-<skill-name>" "$SKILL_DIR"
```

Make both executable. Print `33-delta.md` and the redesigned `SKILL.md` to stdout.
````
