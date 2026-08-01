# 096-the-detector-that-arrested-its-own-confession — Prompt 2 (action)

```text
You are hardening one pattern-based security filter in this repository
against mention/use confusion and normalization evasion (the failure mode:
a concealment-payload scanner that quarantined its own PR description while
passing "dont" without the apostrophe).

Steps:
1. Run the companion audit prompt (or re-derive it) and select the detector
   with verdict BOTH, or failing that MENTION-CONFUSED or EVADABLE.
2. Add input normalization ahead of matching: case-fold; strip or
   canonicalize punctuation inside candidate phrases (don't/dont/don t);
   collapse whitespace; map common unicode confusables and strip zero-width
   characters. Keep it a pure function with its own unit tests.
3. Add an intent gate appropriate to the detector's job. Minimum viable:
   only fire when the matched phrase is in imperative position (not
   preceded by reporting verbs like "detects", "matches", "flags", "for
   example"), or score-and-threshold rather than binary-match if the
   codebase supports it. Being inside quotation marks lowers the score; it
   must NOT be treated as automatic clearance — an attacker can wrap a live
   instruction in fake quotes as easily as an author can quote a payload to
   describe it. Document the gate's known limits in a comment — this is a
   mitigation, not a proof.
4. Add two regression suites, keeping the mutation corpus (4b) in its own
   file separate from any self-scan target so the two assertions cannot
   collide:
   a. SELF-SCAN: the detector runs against its own source and README (and
      any test files that do NOT contain the mutation corpus); assert zero
      findings.
   b. MUTATION CORPUS: each known payload plus its step-2 variants, in a
      dedicated fixture file excluded from the self-scan target; assert
      all are caught.
5. Run the full test suite. Commit on a branch named
   `harden/<detector-name>-intent-gate` with a message naming both failure
   modes. Do not push or open a PR unless the repo's contribution docs
   instruct otherwise.

## Undo
- Branch-confined: confirm `git status` is clean on the shared checkout
  first, then `git checkout <previous-branch>` and
  `git branch -D harden/<detector-name>-intent-gate` removes all changes.
- If merged and later rolled back: `git revert <merge-commit>`. Note the
  asymmetry: reverting restores BOTH old failure modes (the false negatives
  return too). If the revert is because the intent gate suppressed a real
  detection, revert only the gate commit and keep the normalization commit
  — structure the work as two commits so this partial undo is possible.
```

**Ground truth — tested 2026-07-10 (harness-agnostic wording, run without modification).** Codex CLI ✅ (fixture: the claude-codex repo; full transcript in project records). Claude Code and Grok legs: pending. Revised 2026-07-15 for correctness (quotation marks no longer treated as automatic clearance in the intent gate, SELF-SCAN and MUTATION CORPUS separated into non-colliding fixture files, undo gained a clean-worktree check) — re-verification not yet re-run.
