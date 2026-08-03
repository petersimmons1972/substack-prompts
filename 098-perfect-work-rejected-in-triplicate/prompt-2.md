# 098-perfect-work-rejected-in-triplicate — Prompt 2 (action)

```text
You are adding a "done-but-form-malformed" path to this repository's queue
state machine (the failure mode: a validator rejecting an empty field in a
completion report caused a finished security fix to be re-executed three
times, and the rescue job was blocked by a preflight protecting the work).

Steps:
1. Run the companion audit prompt (or re-derive the state map) and locate
   the validator-rejection -> FAILED/REQUEUE transition.
2. Introduce a new terminal-adjacent state (name it per repo convention;
   e.g. REPORT_INVALID_WORK_UNVERIFIED) reached when report validation
   fails. Entering it must NOT requeue.
3. Add an artifact check that runs on entry to that state: from the run's
   metadata (branch name, work-item ID), inspect reality — does a commit/
   branch/PR matching this run exist (`git log`, `git branch --list`,
   or the forge API the repo already uses)? Prefer an authoritative
   run-to-artifact identifier (run ID in the branch name or commit
   trailer) over free-text matching; treat a name-or-message match as
   weak evidence that still parks the run for a human.
   a. Artifact found: transition to DONE_PENDING_REPORT_FIX and notify a
      human via the repo's existing alert channel; do not re-execute.
      Artifact existence stops re-execution — a human confirms it
      actually answers the brief.
   b. No artifact AND the check itself succeeded: transition to the
      existing FAILED/REQUEUE path — genuine failures keep their current
      behavior.
   c. Check failed or ambiguous (forge unreachable, multiple candidate
      matches): park for a human; neither requeue nor mark done.
4. Fix the recovery path: any rescue/redrive preflight that blocks on queue
   state must accept an explicit override flag (e.g. --unstick <run-id>)
   which trusts the step-3 artifact check instead of queue state. Require
   the flag to be manual — never auto-set. The override bypasses the
   queue's OPINION of the run, not its concurrency machinery: the rescue
   must still acquire the run's lease/lock (or verify no process holds
   it) before touching anything, and must log an audit line recording
   who overrode what and why.
5. Tests: (a) malformed report + existing commit -> DONE_PENDING_REPORT_FIX,
   zero re-executions; (b) malformed report + no commit -> requeue as
   before; (c) malformed report + artifact check erroring -> parked, not
   requeued; (d) rescue with --unstick passes the preflight that
   previously blocked it while still acquiring the lease.
6. Run the full test suite. Commit on a branch named
   `fix/done-but-malformed-state` explaining the incinerated-work failure
   mode. Do not push or open a PR unless the repo's contribution docs
   instruct otherwise.

## Undo
- Branch-confined: `git checkout <previous-branch>` and
  `git branch -D fix/done-but-malformed-state` removes everything.
- If merged and rolled back: `git revert <merge-commit>`. Before reverting,
  drain any runs currently parked in the new states (requeue or close them
  manually) — after revert the queue code no longer recognizes those state
  values and they would strand. The revert restores the old behavior
  (malformed reports requeue unconditionally).
```

**Ground truth — tested 2026-07-10 (harness-agnostic wording, run without modification).** Codex CLI ✅ (fixture: the claude-codex repo; full transcript in project records). Claude Code and Grok legs: pending.
