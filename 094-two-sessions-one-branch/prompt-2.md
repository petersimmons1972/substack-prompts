# 094-two-sessions-one-branch — Prompt 2 (action)

```text
You have shell and repo access. Institute manual worktree-per-dispatch
isolation for all concurrent work in this repository.

1. Write a short protocol file (e.g. docs/CONCURRENT-DISPATCH.md) stating:
   (a) never rely on platform "isolation" flags for background/concurrent
   dispatch — treat them as unverified; (b) every concurrent task creates its
   own worktree FIRST: `git worktree add <repo>-worktrees/<task-id> -b
   <type>/<task-id>-<short-desc>` — path AND branch name must embed the
   task/issue ID so two dispatches with distinct IDs cannot collide — this
   does not protect against two dispatches being given the same ID by
   mistake; (c) all work — commits, tests,
   everything — stays inside that worktree for the task's lifetime; (d) before
   reporting done, self-check `git rev-parse --show-toplevel` matches the
   worktree path, and run `git status` + `git branch --show-current` on the
   shared checkout to confirm nothing leaked; (e) remove the worktree when
   done (`git worktree remove <path>`) unless a PR is open for review;
   (f) if worktree creation is unsafe for a specific case, fall back to strict
   one-at-a-time sequencing — never parallel writers on one checkout.
2. Add the worktrees directory to .gitignore (or site it outside the repo).
3. If dispatch briefs/templates exist in this repo, add the protocol steps to
   the template so every future brief carries them.
4. Demonstrate once: create a worktree per the naming rule, make a trivial
   commit in it, run the self-check, remove it. Paste the transcript into the
   protocol file as a worked example.

## Undo
- The protocol doc, .gitignore line, and template additions are additive text:
  `git revert` the single commit that introduced them.
- Any demonstration worktree: `git worktree remove <path>` and
  `git branch -D <demo-branch>`; `git worktree prune` cleans stale metadata.
- Nothing in this action modifies existing branches, history, or platform
  settings other than the demonstration worktree/branch from step 4, which
  the line above already removes.
```

**Ground truth — tested 2026-07-10 (harness-agnostic wording, run without modification).** Codex CLI ✅ (fixture: the claude-codex repo; full transcript in project records). Claude Code and Grok legs: pending. Revised 2026-07-15 for correctness (collision-uniqueness claim hedged, Undo section's destructive-step contradiction fixed) — re-verification not yet re-run.
