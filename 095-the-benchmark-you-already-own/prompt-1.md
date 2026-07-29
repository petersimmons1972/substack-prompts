# 095-the-benchmark-you-already-own — Prompt 1 (audit)

```text
You are auditing an agent operation to determine what model-evaluation
capability it ALREADY possesses in its operational records — before anyone
builds or buys a benchmark. You have shell access to this repo/system.
Read-only; change nothing.

1. Find the operational record: ledgers, scorecards, PR/issue history, review
   logs — anywhere per-task outcomes are recorded with (or attributable to)
   the model or agent that produced them.
2. Determine which benchmark-grade metrics are ALREADY derivable from those
   records, and compute each one that is, per model/agent, over the available
   history:
   a. first-pass rate (tasks accepted without a revision round)
   b. laps-to-merge (revision rounds per task, distribution not just mean)
   c. defect classes (categorize reviewer findings: correctness, security/
      credentials, style, spec-miss; count per class)
3. Assess comparability: for any two models/agents present in the records,
   state whether their task mixes are similar enough to compare (same repo?
   same brief template? same review process? same effort settings?). List
   the uncontrolled variables.
4. Find candidate sting tasks: search the history for documented failures
   with a clear mechanism (e.g., a credential exposure, a data-loss bug, a
   spec violation) that could be repeated as a same-shape task. List up to 3,
   each with: the original failure, the task shape, and what review lane
   caught it (if any).
5. Report: metrics table per model; comparability assessment; sting-candidate
   list. If the records cannot support per-model attribution, say so plainly
   — that is the finding.
```

## Undo

Read-only — nothing to undo.

**Ground truth — tested 2026-07-10 (harness-agnostic wording, run without modification).** Codex CLI ✅ (fixture: the claude-codex repo; full transcript in project records). Claude Code and Grok legs: pending.
