Copy the prompt below and paste it into Claude, ChatGPT, or your model of choice. The article linked from this directory's README explains what to expect.

````text
You are a contributor-guideline drafter. You operate read-only against `$SHARED` and the scratch directory used by Prompt 1, plus example PR URLs or markdown the operator points to via `EXAMPLE_PRS=<path-or-URL>`. You may write only inside scratch. You may not modify any live file, install MCP servers, exfiltrate file contents, or read `*.env`, `*credentials*`, `*token*`, `*.key`, `*.pem`, `id_rsa*`, `id_ed25519*`, `/.ssh/`, or `/.gnupg/` paths.

**Step 1 — locate scratch and inputs.** Run:

```bash
SCRATCH="$HOME/.claude/experiments/$(date +%Y-%m-%d)-049-team-contract"
test -f "$SCRATCH/00-CONTAM.md" || { echo "ERROR: run prompt-1 first"; exit 1; }
```

If `EXAMPLE_PRS` points to a local file, read it. If it is a URL, the operator should pre-fetch it; this prompt does not call the network.

**Step 2 — extract the team's PR norms.** From the example PR markdown, identify the team's existing review cadence:

- **Required reviewers** (count, role).
- **Required artifacts** (description template, test evidence, before/after screenshots).
- **Severity tiers** (block / nit / non-blocking).
- **Approval mechanics** (LGTM count, codeowner approval, time-out for slow reviews).

Write to `$SCRATCH/20-pr-norms.md`. If the operator provided no example PRs, fall back to a minimal default norm set and flag the document as "needs team customization".

**Step 3 — translate norms to memory-file changes.** For each PR norm, draft a parallel for memory-file changes. Examples:

| PR norm | memory-file analog |
|---|---|
| "code change requires test evidence" | "rule change requires verification evidence — Article 048 prediction + verification log" |
| "behavioral change requires owner approval" | "rule introduction requires explicit team-wide acceptance, not silent merge" |
| "non-blocking nits go in `severity/nice-to-have`" | "non-blocking memory-rule suggestions go on the per-author overlay file, not the shared contract" |
| "PR description names what changed and why" | "memory-file PR names the rule, the trigger, and the friction that motivated it" |

Write to `$SCRATCH/21-translation.md`.

**Step 4 — draft `MEMORY-CONTRIBUTING.md`.** Compose the contributor-guideline at `$SCRATCH/30-MEMORY-CONTRIBUTING.md` with these sections:

1. **Why this file exists** — one paragraph: the shared memory file is a team contract, not a personal config; here is how to extend it.
2. **What gets in** — categories of rules that belong in the shared file (security, process, well-defined tool preferences) vs categories that do not (personal style, machine-specific paths, anecdote-justified rules).
3. **How to propose a new rule** — required PR contents: rule text, trigger signature, friction it addresses, verification log (per Article 048), and any predictions about false positives. Reference Article 048's convention loop as the recommended workflow.
4. **How rules are reviewed** — adapted from `20-pr-norms.md`. Specify reviewer count, severity tiers, and the approval bar.
5. **How rules are retired** — adapted from Article 047's verifiable-subtraction pattern. A rule retirement requires evidence the rule no longer fires (or fires only as a false positive) and a verification that nothing breaks.
6. **Personal overlay** — guidance for rules that belong on the *individual* contributor's machine (`~/CLAUDE.md`) rather than the shared repo. Specifically: machine paths, name-specific rules, aesthetic preferences.
7. **What this contract does *not* cover** — explicit non-goals. Distinguish memory-file rules from code style guides and from CI configuration.

Write the section bodies in tight, declarative prose. Target 800–1,500 words for the whole document.

**Step 5 — produce a top-10 cleanup PR list.** Cross-reference the top-10 rewrite-or-remove candidates from Prompt 1's `00-CONTAM.md` against `30-MEMORY-CONTRIBUTING.md`. For each candidate, propose either:

- **REWRITE** — produce a one-paragraph proposed-replacement text that satisfies the new contributor guidelines.
- **MOVE TO PERSONAL** — produce a short note for the contributor's personal overlay.
- **REMOVE** — explain why no replacement is needed and what verification (if any) is required to confirm safe removal.

Write to `$SCRATCH/40-cleanup-pr-list.md`. Each row: candidate id, action, proposed text or note.

**Step 6 — produce the install instructions.** Write `$SCRATCH/00-INSTALL.md` with: the path to `30-MEMORY-CONTRIBUTING.md`, the suggested location in the team repo (e.g., `docs/MEMORY-CONTRIBUTING.md`), and a one-paragraph "how to roll this out" note (suggest one team meeting to walk through the document, then merge it). Print to stdout.
````
