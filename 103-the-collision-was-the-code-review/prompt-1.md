# 103-the-collision-was-the-code-review — Prompt 1 (audit)

```text
You are auditing this repository for (1) unenforced uniqueness in
sequential artifacts and (2) discarded convergent work — cases where two
contributors independently solved the same problem and one answer was
thrown away without being diffed against the other.

Part 1 — collision surfaces:
1. Find sequentially-numbered artifact families: migrations, schema
   versions, numbered docs/ADRs, fixture IDs (glob for zero-padded numeric
   filename prefixes and grep for sequence allocation in code).
2. For each family, determine whether uniqueness is ENFORCED (a CI check,
   a lint, an allocation lock) or CONVENTIONAL (contributors pick the next
   number and hope). Cite the enforcing check or its absence.
3. Check history for past collisions: `git log --diff-filter=A` on each
   family's directory; flag any point where two files sharing a sequence
   number required a rename to resolve. This only sees collisions
   preserved in retained history on branches you can still reach — fetch
   all remotes first (`git fetch --all`); collisions resolved on deleted
   branches or in force-pushed history will not appear. Say so in the
   report rather than implying completeness.

Part 2 — discarded convergence:
4. Search closed PRs and issues for duplicate-resolution language, using
   `gh`'s search flag rather than listing and eyeballing (`gh search
   prs --repo <owner/repo> --state closed "duplicate OR superseded OR
   \"already fixed\" OR \"dup of\""`, similarly for `gh search issues`).
   Note the result count against whatever cap you queried for — a search
   that returns exactly its page limit is a search that's still
   incomplete, not a search that found everything.
5. For up to 5 recent cases where one of two convergent fixes was
   discarded, check whether any recorded comparison happened before
   discarding (`gh pr view <n> --comments` and check both PRs' file
   diffs). Classify each: DIFFED-THEN-DISCARDED or DISCARDED-UNEXAMINED,
   or INSUFFICIENT-EVIDENCE if the discarded branch/commits are gone.
6. Read-only. Modify nothing.

Output a markdown report:
- Family table: artifact family | uniqueness ENFORCED/CONVENTIONAL |
  enforcing check (or none) | past collisions found.
- Convergence table: case (PR/issue refs) | classification | what the
  discarded version contained that the kept one lacked (if determinable).
- Two verdict lines: the collision surface most likely to bite next, and
  whether this repo's culture diffs or discards convergent work.
```

## Undo

Read-only — nothing to undo.

**Ground truth — tested 2026-07-10 (harness-agnostic wording, run without modification).** Codex CLI ✅ (local codex exec, read-only sandbox; fixture: the claude-codex repo). Claude Code and Grok legs: pending.
