# 086-reviewed-a-ghost — Prompt 1 (audit)

```text
You are auditing this repository for "ghost review" exposure: reviews or CI
verdicts that may have been rendered against code other than what shipped.

Using only shell and repository access:

1. Establish the default-branch tip: `git fetch --all --prune`, then record
   `git rev-parse origin/HEAD` (or origin/main) as DEFAULT_BRANCH_SHA. Note:
   this is the branch tip, not necessarily what is deployed — if a release
   tag or deployment record exists, prefer its SHA as the "what shipped"
   reference.
2. Find stale review surfaces:
   a. Local branches behind their upstream (report the behind count and last
      commit date; treat a large lag as suspect):
      `git for-each-ref --format='%(refname:short) %(upstream:track) %(committerdate:iso)' refs/heads`
   b. Worktrees pinned to old refs: `git worktree list`
   c. If `gh` is available: open PRs whose approval no longer matches the head:
      `gh pr list --json number,reviews,headRefOid --limit 50`
      — for each PR, take the latest APPROVED review and flag it when
      `review.commit.oid != headRefOid`. (The `gh --json reviews` schema
      exposes `commit.oid`; the field is named `commit_id` only on the REST
      reviews endpoint via `gh api`.)
3. For each flagged item, compute the drift on both sides:
   - PR: approved oid vs head — `git rev-list --left-right --count <approved-oid>...<headRefOid>`
   - stale ref: ref vs default tip — `git rev-list --left-right --count <stale-sha>...DEFAULT_BRANCH_SHA`
   then `git diff --stat <sha-a> <sha-b> | tail -1` for the file count.
4. Check for a semantic freshness rule, not incidental strings. Look for
   branch protection / rulesets that dismiss stale approvals on new commits,
   and for CONTRIBUTING or review-template language requiring re-review when
   the head moves:
   `grep -riE 'dismiss stale|re-?review|exact (commit|sha)' CONTRIBUTING* .github/ 2>/dev/null`
   Treat an incidental `sha` in a checkout step as non-evidence.

Output format:
## Ghosts found
- <ref or PR>: verdict at <sha>, current head/tip is <sha>,
  drift: <A behind / B ahead commits, M files>
## Pinning discipline
PRESENT | ABSENT — cite the freshness rule or its absence.
## Verdict
One sentence: can a review in this repo currently be trusted to describe the
code being shipped, and why or why not.
```

## Undo

Read-only — nothing to undo.

**Ground truth — tested 2026-07-10 (harness-agnostic wording, run without modification).** Codex CLI ✅ (fixture: the claude-codex repo; full transcript in project records). Claude Code and Grok legs: pending.
