# 092-my-agent-doesnt-know-me — Prompt 1 (audit)

```text
You are auditing this repository for "session amnesia debt": how much
operating knowledge exists only in conversation history and would be lost
the moment a fresh agent session starts.

Using only shell and repository access:

1. Inventory durable agent context — what a newborn session would actually
   receive:
   - `ls -la CLAUDE.md AGENTS.md .cursorrules .github/copilot-instructions.md 2>/dev/null`
   - `find .claude -type f 2>/dev/null` (list files individually — it is a
     directory, not a file; do not `wc -l` the directory itself).
   - For each file found: `wc -l` and note the last-modified date
     (`git log -1 --format='%ci' -- <file>` where tracked).
2. Probe for orphaned decisions — knowledge referenced but not recorded:
   - `git log --oneline -30` and flag commit messages that reference
     decisions/discussions with no recorded home ("as discussed",
     "per review", "as agreed"):
     `git log --format='%h %s' -100 | grep -iE 'as discussed|as agreed|per (our|the) (chat|conversation|discussion|review)'`
   - Treat matches as candidates, not proof — check whether an issue, PR
     description, or ADR actually records the decision before calling it
     orphaned.
3. Staleness check: for each context file from step 1 that is tracked,
   count commits to the repo since that file last changed:
   `git rev-list --count $(git log -1 --format=%H -- <file>)..HEAD`
   — high counts mean the briefing is due for review, not necessarily wrong.
   If `git log -1 --format=%H -- <file>` returns nothing (untracked or
   never committed), report that file as UNTRACKED and skip the rev-list.
4. Coverage check: do the context files answer a newborn's first four
   questions? Run one targeted grep per topic rather than a single blended
   count — `grep -ciE 'pytest|npm test|go test' <file>` for tests,
   `grep -ciE 'npm run|make |docker build' <file>` for build/run,
   `grep -ciE 'branch|pull request|PR convention' <file>` for conventions,
   `grep -ciE 'do not|never |must not' <file>` for constraints. Record
   present/absent per topic from its own pattern, not a shared count.

Output format:
## Durable context inventory
- <file>: <lines> lines, last touched <date>, <N> commits stale (or UNTRACKED)
## Orphaned decisions
- <commit>: <message> (candidate — no recorded home found in issues/PRs/ADRs)
## Newborn briefing coverage
tests: PRESENT/ABSENT · run: PRESENT/ABSENT · conventions: PRESENT/ABSENT ·
constraints: PRESENT/ABSENT
## Verdict
One sentence: given only what step 1-4 found on disk, how much of a fresh
session's working agreements are documented, and where the rest likely lives.
```

## Undo

Read-only — nothing to undo.

**Ground truth — tested 2026-07-10 (harness-agnostic wording, run without modification).** Codex CLI ✅ (fixture: the claude-codex repo; full transcript in project records). Claude Code and Grok legs: pending. Revised 2026-07-15 for correctness (directory-vs-file inventory bug, untracked-file staleness crash, blended-count false positives in the coverage check) — re-verification against the fixture not yet re-run.
