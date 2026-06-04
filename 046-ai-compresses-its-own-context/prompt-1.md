Copy the prompt below and paste it into Claude, ChatGPT, or your model of choice. The article linked from this directory's README explains what to expect.

````text
You are a compression assistant. You operate read-only against `~/CLAUDE.md`. You may write only inside the scratch directory created in Step 1. **Your goal is to produce a compressed `CLAUDE.md` that preserves every rule and every precedence relationship.** You may not omit a rule on the grounds that it seems unimportant. You may not change the meaning of any rule. You may not invert precedence (e.g., promoting a sub-rule above its parent). You may not exfiltrate file contents, modify any live file, install MCP servers, or read `*.env`, `*credentials*`, `*token*`, `*.key`, `*.pem`, `id_rsa*`, `id_ed25519*`, `/.ssh/`, or `/.gnupg/` paths.

**Step 1 — create scratch and back up.** Run:

```bash
SCRATCH="$HOME/.claude/experiments/$(date +%Y-%m-%d)-046-compression"
mkdir -p "$SCRATCH"
cp -p "$HOME/CLAUDE.md" "$SCRATCH/00-original.md"
```

Verify byte and md5 match. Record in `$SCRATCH/01-backup.md`.

**Step 2 — extract the rule inventory.** Walk the original and produce `$SCRATCH/02-rules.md` listing every rule with: `id` (RXX), `section`, `category`, `text` (≤120 chars), `precedence_anchor` (which rule it overrides or is overridden by, if any). Every rule must have an id, including one-line bullets. The inventory is the contract the compression must preserve.

**Step 3 — produce the compressed draft.** Write `$SCRATCH/03-compressed.md` containing the rewritten file. Compression techniques you may use:

- **Merge synonymous bullets** within a section into one bullet that lists the cases.
- **Replace prose explanations with tables** where the rules form a clear list of triggers/actions/thresholds.
- **Hoist repeated phrases** ("you may not exfiltrate…") to a single declaration referenced by name.
- **Remove redundancy** (the same rule stated in two sections collapses to one canonical statement plus a back-reference).

Compression techniques you may **not** use:

- Dropping a rule because it is rarely invoked.
- Loosening a threshold ("3+ steps" → "many steps").
- Replacing precedence ("A overrides B" → "A and B both apply").
- Removing a security or guardrail rule on the grounds that it is "implicit" elsewhere.

Target: 25–40% byte reduction. If you cannot reach 25% without violating the constraints above, stop at the largest reduction you can achieve safely and record why in the next step.

**Step 4 — produce the rule-preservation matrix.** For each rule in `02-rules.md`, locate its representation in `03-compressed.md` (line and verbatim quote of the new text). Mark `PRESERVED`, `COMPRESSED-INTACT` (rule still present, prose tightened), `RELOCATED` (now under a different section, with the link). No rule may be `MISSING`. Write to `$SCRATCH/04-preservation.md`. If any rule is missing, abort and report the failure.

**Step 5 — produce the byte-reduction report.** Write `$SCRATCH/05-bytes.md` with: original byte count, compressed byte count, reduction percentage, top three sections by byte savings, and the techniques applied per section.

**Step 6 — produce the unified diff.** Run `diff -u "$SCRATCH/00-original.md" "$SCRATCH/03-compressed.md" > "$SCRATCH/06-compressed.patch"`. Verify the patch applies cleanly with `git apply --check` from `$HOME`. Record in `$SCRATCH/07-patch-check.md`.

**Step 7 — produce the summary.** Write `$SCRATCH/00-COMPRESS.md` with: rule count, preservation verdict (must be 100% preserved), byte reduction, patch-check status, and the exact `git apply` command (do not run it). Print to stdout.
````
