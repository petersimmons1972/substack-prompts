# 086-reviewed-a-ghost — Prompt 2 (action)

```text
Add a "review freshness" guard that surfaces approvals which have drifted off
the current head. Note up front: GitHub already offers native "dismiss stale
pull request approvals when new commits are pushed" in branch protection —
available on public repos on any plan, and on private repos on an eligible
plan. If you can enable that setting, do so; it is stronger than a workflow.
This guard is for when you also want the drift to show up as a status check,
or cannot configure branch protection.

1. Create `.github/workflows/review-freshness.yml` with a workflow that runs
   on `pull_request` (types: [opened, reopened, synchronize]) and on
   `pull_request_review` (types: [submitted, dismissed]) so it re-evaluates
   after a new approval too. The job reads the PR's reviews (via the GitHub
   API with the built-in GITHUB_TOKEN), takes the latest APPROVED review, and
   compares its `commit.oid` against the current head SHA. It fails with
   "Approval is for <old-sha>; head is now <new-sha> — re-review required"
   when they differ, and passes when there is no APPROVED review yet (nothing
   to go stale). Name the job `review-matches-head`. This only blocks a merge
   if you add `review-matches-head` as a REQUIRED status check in branch
   protection; otherwise it surfaces drift without enforcing it.
2. Add one line to CONTRIBUTING.md (create it if absent) under a "Reviews"
   heading: "A review verdict refers to an exact commit SHA. An approval of
   commit A says nothing about commit B."
3. Commit on a new branch `ci/review-freshness` with message
   "ci: fail when approval SHA differs from head SHA". Do not push or open
   a PR unless the operator asks.

## Undo
- `git checkout -` then `git branch -D ci/review-freshness` removes the
  workflow and the CONTRIBUTING line entirely; nothing touched the default
  branch.
- If the branch was pushed before undo was requested:
  `git push origin --delete ci/review-freshness`.
- No repository settings, branch protections, or existing workflows were
  modified, so there is nothing else to restore.
```

**Ground truth — tested 2026-07-10 (harness-agnostic wording, run without modification).** Codex CLI ✅ (terse result; transcript in project records). Claude Code and Grok legs: pending.
