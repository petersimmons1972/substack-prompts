# 092-my-agent-doesnt-know-me — Prompt 2 (action)

```text
Build the minimum continuity infrastructure so the next fresh session
inherits today's working state — a handoff file the newborn reads first.

0. Preconditions: refuse if the working tree is dirty (`git status
   --porcelain` is non-empty) — stop and tell the operator to commit or
   stash first. Refuse if branch `docs/session-handoff` already exists —
   report it instead of overwriting.

1. Decide the path: if `.claude/` already exists in this repo, use
   `.claude/HANDOFF.md` (create the directory only if it does not exist
   yet). Otherwise — including repos that use AGENTS.md conventions — use
   `HANDOFF.md` at repo root. Use that same path in step 2. Create the file
   with exactly these sections, filled from the current session's state:

   # Session Handoff — <ISO date>
   ## Current objective
   (One paragraph: what we are trying to accomplish and why.)
   ## Decisions in force
   (Bullet list: each decision + one-line rationale. Only decisions a fresh
   session could not re-derive from the code.)
   ## Do not
   (Constraints agreed in conversation that appear nowhere else, including
   any approach already tried and rejected.)
   ## Next step
   (The single next action, concrete enough to start cold.)

   Before writing, review the content for anything that should not be
   committed to the repo (credentials, tokens, customer data) — omit it.

2. Add one line to the repo's agent context file (CLAUDE.md or AGENTS.md,
   whichever exists; do not create one if neither exists — note it in your
   report instead): "At session start, read <path from step 1> if present;
   it carries state from the previous session." The path in this line must
   match the path you actually created in step 1.
3. Commit only the handoff file and the context-file line (stage those two
   paths explicitly — do not `git add -A`) on a new branch
   `docs/session-handoff` with message "docs: add session handoff file for
   cross-session continuity". Do not push or open a PR unless the operator
   asks.

## Undo
- `git checkout -` then `git branch -D docs/session-handoff` removes the
  handoff file and the context-file line; the default branch was never
  touched. This only holds if nothing from that branch was later merged
  or cherry-picked — if it was, undo the merge commit instead.
- If `.claude/` was newly created it existed only on the deleted branch;
  nothing to clean up in the working tree after checkout.
- If the operator asked for a push before undo:
  `git push origin --delete docs/session-handoff`.
```

**Ground truth — tested 2026-07-10 (harness-agnostic wording, run without modification).** Codex CLI ✅ (fixture: the claude-codex repo; full transcript in project records). Claude Code and Grok legs: pending. Revised 2026-07-15 for correctness (path inconsistency between the created file and the pointer line, missing dirty-tree/existing-branch guard, unscoped commit) — re-verification against the fixture not yet re-run.
