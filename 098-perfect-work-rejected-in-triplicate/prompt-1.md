# 098-perfect-work-rejected-in-triplicate — Prompt 1 (audit)

```text
You are auditing this repository's job/queue/dispatch system for
"paperwork-over-work" failure modes: paths where a malformed status report
re-executes, strands, or fails to promote completed work.

Steps:
1. Map the state machine. Find the queue/dispatch/runner code (grep for:
   "requeue", "retry", "validator", "validate", "needs-input" or
   "needs_input", "dead-letter"/"dead_letter", "terminal", "status",
   "preflight"). Enumerate every state a run can be in and every transition,
   citing file:line for each transition.
2. Find the validators. For each validation applied to a run's REPORT
   (completion message, status payload, required fields), record:
   a. What it checks (form: schema/fields) vs what it verifies (substance:
      does the claimed artifact — commit, PR, file — actually exist?).
   b. What happens on rejection: is there ANY path other than
      FAILED/REQUEUE? Specifically, is there a state meaning "work may be
      complete; report malformed"?
3. Trace the re-execution cost. For each rejection->requeue path, determine
   whether requeued runs redo work from scratch or resume; note whether
   anything checks for existing artifacts (prior commits/branches) before
   re-executing.
4. Audit the recovery tooling. Find any rescue/recovery/redrive mechanism
   and list every preflight/guard it must pass. Flag any guard that reads
   queue STATE rather than repository REALITY and offers no reconciliation
   path — these will block recovery of exactly the work they protect.
   Guards that exist for concurrency control (leases, ownership,
   cancellation) are legitimate; flag them only if they cannot be
   reconciled against reality.
5. Read-only. Modify nothing.

Output a markdown report:
- The state diagram as a list of transitions (state -> state, trigger,
  file:line).
- Validator table: check | form-or-substance | rejection outcome |
  "done-but-malformed" path exists yes/no.
- Re-execution findings: which paths burn completed work, worst-case cost.
- Recovery findings: guards that would block rescue of stranded-but-done
  work, with file:line.
- Verdict: the single transition most likely to incinerate finished value.
```

## Undo

Read-only — nothing to undo.

**Ground truth — tested 2026-07-10 (harness-agnostic wording, run without modification).** Codex CLI ✅ (fixture: the claude-codex repo; full transcript in project records). Claude Code and Grok legs: pending.
