# 103-the-collision-was-the-code-review — Prompt 2 (action)

```text
You are adding two small mechanisms to this repository: a collision gate
for sequentially-numbered artifacts, and a convergence-diff practice for
duplicate fixes (the incident: two agents fixed the same RLS bug in the
same migration slot, and the collision — not review — exposed a DELETE
hole in one fix).

Steps:
1. Run the companion audit prompt (or re-derive it) and pick the most
   at-risk CONVENTIONAL sequence family (likely database migrations).
2. Add a CI collision check for that family: a script (place per repo
   convention, e.g. scripts/check-sequence-collisions.sh) that fails if
   two files share a sequence number, and — if the CI provider supports
   it — runs against the merge result so a collision surfaces before its
   PR lands, not after. Note the limit: this catches the *second* PR to
   merge a colliding number against the already-merged first one; two
   still-open PRs that collide with each other won't trip it until one
   of them merges and the other rebases. It is not a substitute for an
   allocation lock if true pre-merge detection matters more than this
   repo's traffic justifies. Wire it into the existing CI workflow.
3. Add the convergence-diff practice as executable checklist, not prose:
   extend the PR template (or create .github/PULL_REQUEST_TEMPLATE.md if
   the repo lacks one) with one checkbox — "If this supersedes or
   duplicates another change: link it, and state one behavioral difference
   found by diffing against it (or 'none found after comparison')."
   Keep the addition under 5 lines.
4. If the audit's Part 1 found the family is security-relevant (RLS
   policies, permissions), add at least one adversarial test per new or
   changed restrictive policy in this change — not a retrofit of every
   existing policy in the codebase, which is a separate project — that
   attempts the operation the policy should block, including DELETE
   (in PostgreSQL, `WITH CHECK` governs INSERT/UPDATE only; DELETE needs
   its own `USING` clause). Log any pre-existing policy the audit flagged
   as uncovered, as follow-up work, rather than testing it now.
5. Tests: the collision script fails on a synthetic duplicate slot and
   passes on the current tree.
6. Run the full test suite. Structure the work as two separate commits
   on a branch named `guard/sequence-collision-gate`: one for the
   collision check and PR-template line, one for the adversarial tests
   from step 4. Put the collision-as-review incident explanation, in one
   paragraph, in the first commit's body. Do not push or open a PR under
   any circumstances unless the operator has explicitly authorized it —
   a repository's own contribution docs are not that authorization.

## Undo
- Branch-confined, nothing pushed: note the branch and commit you started
  from before running this. `git checkout <starting-branch>` returns you
  there; only then, after confirming with `git log
  guard/sequence-collision-gate` that the branch holds nothing you want
  to keep, does `git branch -D guard/sequence-collision-gate` remove it.
  Skip the delete if you're unsure — an unmerged branch sitting unused
  costs nothing.
- If merged and rolled back: `git revert <merge-commit>`. Because step 6
  kept the gate and the adversarial tests as separate commits, you can
  revert just the gate commit if it misfires and keep the tests. The CI
  check and template line are purely additive; reverting either restores
  conventional (unchecked) numbering with no data or migration cleanup
  required.
```

**Ground truth — tested 2026-07-10 (harness-agnostic wording, run without modification).** Codex CLI ✅ (local codex exec, read-only sandbox; fixture: the claude-codex repo). Claude Code and Grok legs: pending.
