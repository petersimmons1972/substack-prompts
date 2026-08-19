# 116-grading-its-own-homework — Prompt 2 (action)

```text
You have shell and repo access. My LLM-judged benchmark's headline number may
be scorer-leniency-inflated. Build the honest-baseline machinery.

First, a gate: if this repo has no eval harness, no scorer, or no baseline run
to work from, report BLOCKED and stop — describe what is missing and do NOT
invent a reference set, numbers, or a baseline that does not already exist.

1. Create a versioned scorer lock: a manifest file (committed to the repo)
   capturing judge model ID, decoding parameters, judge prompt hash, and mode
   (strict/lenient). The scoring harness must refuse to run — fail closed, not
   default silently — if the manifest is missing or any field is absent.
2. Add a qualification gate. Qualification is not "run 20 items"; define it
   concretely:
   - a reference set of HUMAN-REVIEWED items (aim for >= 50; state the actual
     count, and never pad it with synthetic labels),
   - each item carrying a human-verified correct/incorrect label,
   - a script that scores the set with the locked judge and reports its
     agreement with the human labels and its inflation rate (judge-lenient
     minus human),
   - pass/fail thresholds chosen and written down BEFORE the run (e.g. >= 90%
     agreement and <= 3pp inflation to pass — adjust to your domain and state
     the choice explicitly).
   A judge that has not cleared those thresholds cannot emit a "reportable"
   score; tag its outputs UNQUALIFIED.
3. Rerun the baseline under the locked judge. To separate a SCORER effect from
   a GENERATOR effect, score the SAME frozen generator outputs under both the
   old and the new judge; if only one generator's outputs exist, say so and
   state plainly that scorer and generator effects cannot be separated from
   that run. Produce a before/after ledger — old headline vs new strict vs new
   lenient plus a per-category breakdown — and label every column with its
   generator AND its scorer mode.
4. Write the delta analysis: for each category, report the delta and whether
   the shape looks like an even smear (consistent with grader strictness) or a
   concentrated collapse (consistent with a capability gap) — and note that
   with two variables changed the two cannot be cleanly separated. If the repo
   has a documented noise floor, compare against it; if not, do NOT invent one.
5. Do NOT update any public-facing headline number yet — put the new numbers
   and the ledger in a report file and stop. Rescoping claims is a human call.

## Cost and reversibility
- This is NOT free and NOT purely reversible. Benchmark reruns can spend real
  API money, mutate caches/vector DBs, create remote tags, and — if run against
  a sealed holdout — expose data meant to stay unseen. Before any rerun, produce
  a dry-run plan with a cost estimate, run in an isolated workspace or DB
  snapshot, list every external side effect, and get explicit approval for any
  spend or holdout access.
- The scorer-lock manifest and qualification script are additive files; remove
  them with `git rm` + revert the harness fail-closed check (single commit —
  keep it isolated so one `git revert <sha>` restores the old behavior).
- Rerun outputs land in a new report file/tag only; deleting the report and the
  run tag restores the prior state. No existing scores are modified in place.
- If the fail-closed check breaks an existing CI pipeline, set the manifest to
  mirror the previously-active (unlocked) config as a stopgap and file an issue
  — do not remove the check.
```

**Ground truth — tested 2026-07-10 (harness-agnostic wording, run without modification).** Codex CLI ✅ (fixture: the claude-codex repo; full transcript in project records). Claude Code and Grok legs: pending.
