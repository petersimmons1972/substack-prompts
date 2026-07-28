# 094-two-sessions-one-branch — Prompt 1 (audit)

```text
You have shell and repo access. Audit this repository (and its recent history)
for shared-checkout concurrency contamination — unrelated work interleaved on
the same branch by concurrent writers.

1. For the last 20 merged/closed PRs (or last 50 commits if PR metadata is
   unavailable), compare each PR's stated intent (title/description) against
   its diff stat. Flag any PR whose additions+deletions exceed 10x what its
   description implies (e.g., a "docs:" or "typo" PR with hundreds of
   additions) — as a concrete baseline, a "docs:"/"typo"/"chore" PR touching
   one named file should be flagged if additions exceed 50, or exceed 10x the
   number of files its title names, whichever is larger.
2. For each flagged PR/branch, list its commits with author, co-author
   trailers, and any session/tool identifiers in trailers. Flag branches
   whose commits carry two or more distinct session identities AND whose
   subject matter or touched paths diverge from the branch's stated intent —
   multiple sessions alone is not contamination; multiple sessions plus a
   content mismatch is.
3. Check the working repo for concurrency exposure right now:
   `git worktree list` (are concurrent tasks sharing one checkout?), current
   branch vs the branch named in the active task/dispatch record (if no task
   record is available, state that expectation could not be established
   rather than guessing), and any WIP commits on branches whose names don't
   match the WIP's subject matter.
4. If any orchestration/dispatch config exists in the repo (agent configs,
   CI dispatch, automation settings), identify whether it relies on a
   platform "isolation" flag — and state whether that flag's behavior under
   BACKGROUND/async dispatch is verified anywhere, or merely assumed.

Output shape:
- CONTAMINATED (or suspect) PRs/branches: number, intent vs actual diff stat,
  stranger commits with session evidence
- CURRENT EXPOSURE: shared-checkout concurrent writers yes/no, worktree usage
- ISOLATION ASSUMPTIONS: each platform isolation mechanism found, verified vs
  assumed
- VERDICT: one paragraph — has cross-session contamination happened here, and
  what is the single most exposed workflow today?
```

## Undo

Read-only — nothing to undo.

**Ground truth — tested 2026-07-10 (harness-agnostic wording, run without modification).** Codex CLI ✅ (fixture: the claude-codex repo; full transcript in project records). Claude Code and Grok legs: pending. Revised 2026-07-15 for correctness (10x threshold operationalized, session-identity flag now requires a content/path mismatch, 'expected branch' derivation clarified) — re-verification not yet re-run.
