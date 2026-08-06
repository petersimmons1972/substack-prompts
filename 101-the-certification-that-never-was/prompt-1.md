# 101-the-certification-that-never-was — Prompt 1 (audit)

```text
You have shell and repo access (including `gh` or equivalent, if available).
Audit this project's records of verification — changelogs, plan documents,
deploy logs, handoff briefs, README claims — for certifications that never
were.

1. Find every verification-shaped claim in the project's documents: "audited,"
   "certified," "reviewed," "all tests pass," "verified," "signed off,"
   "zero defects," gate/checklist results. List each with its location.
2. For each claim, find the primary artifact that would prove it: the actual
   PR review comment, CI run ID, audit output file, signed record. Check the
   artifact itself where you have access — count the actual PR comments, read
   the actual CI conclusion — never a summary of it.
3. Classify every claim into exactly four lists:
   - VERIFIED: claim + link to the primary artifact that substantiates it
   - CONTRADICTED: claim + the artifact evidence against it
   - NOT FOUND: no artifact found in the completed search scope; this does not
     prove that no artifact exists
   - INACCESSIBLE/SEARCH INCOMPLETE: access, tooling, or search errors prevented
     a complete check; record the scope attempted and every error
4. Treat NOT FOUND and INACCESSIBLE/SEARCH INCOMPLETE as unverified regardless
   of who asserted the claim. For every non-VERIFIED claim, flag whether it is
   load-bearing:
   does anything downstream (a merge, a deploy, a dependent decision) rest on
   the claim being true?
5. Ordering check: for each verified claim, compare the artifact's timestamp
   against the action it supposedly gated. Flag any "certification" that
   post-dates the thing it certified.
6. Do not assume good faith or bad faith. Authors under handoff or deadline
   pressure write what they expected to be true. Report what the artifacts
   show.
7. A tool or access error is not evidence against a claim. If any load-bearing
   check is incomplete, the overall verdict is INCOMPLETE.

Output shape: the four lists (each entry: claim, location, artifact link or
search scope/error, load-bearing yes/no), the ordering violations, and a
one-paragraph verdict naming the single most dangerous unsubstantiated claim.
```

## Undo

Read-only — nothing to undo.

**Ground truth status — revised 2026-07-27 after adversarial review.** The earlier three-list version passed a Codex CLI fixture on 2026-07-10. The stricter search-error classifications above have not been re-run. Claude Code and Grok legs: pending.
