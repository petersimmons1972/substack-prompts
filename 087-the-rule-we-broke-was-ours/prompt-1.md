# 087-the-rule-we-broke-was-ours — Prompt 1 (audit your own standard)

Excerpted from the series' reader-prompt artifacts (lead author: Codex/GPT-5.6 family,
per founder ruling 2026-07-16 — the model family these target authors its own prompts).
The full pair publishes with article 04.

## 1. For Codex users — the agentic coding brief

Replace everything in brackets. Keep the brief lean: describe the outcome, relevant evidence, authority, and success criteria—not a script for every step.

```text
GOAL
[One sentence describing the user-visible or operational result you
want—not the implementation steps.]

SUCCESS CRITERIA
- [Observable behavior that must work.]
- [Regression or invariant that must remain true.]
- [Required test, build, type-check, benchmark, or manual check.]

CONTEXT
- Repo/paths: [Relevant files or modules, or “unknown—locate them.”]
- Current behavior: [Exact reproduction command or steps, expected
  result, and actual result.]
- Relevant prior art: [Existing pattern, test, API, or convention to
  follow. Omit if none.]
- Environment facts: [Known tool, dependency, network, sandbox, or
  platform constraints. State facts, not guesses.]

AUTHORITY AND BOUNDARIES
- You may inspect the repository, edit files needed for this goal, and
  run relevant non-destructive checks without asking first.
- Do not change: [Protected files, public behavior, dependencies, or
  unrelated code.]
- Get confirmation before: [External writes, destructive actions,
  deployments, purchases, or material expansion of scope.]
- For reversible, in-scope details, make a reasonable assumption and
  record it. Ask only when an ambiguity would materially change the
  result or require a risky action.
- If instructions, code, tests, or documentation conflict, stop that
  part of the work and report the specific conflict with references.

IMPLEMENTATION EXCEPTION (delete if unused)
I require this implementation detail: [specific prescription].
Reason: it prevents this named trap: [plausible wrong implementation,
compatibility failure, security risk, or false-positive test result].
Honor this constraint for that part; choose the simplest
repo-consistent implementation elsewhere.

VERIFICATION — SAVED EVIDENCE REQUIRED
Use [artifact directory, preferably an existing ignored directory or
an absolute temporary path]. Do not overwrite evidence from another
run.

1. Before editing, run the reproduction when it is runnable. Save the
   exact command, exit status, stdout, and stderr as before.txt.
2. If the reproduction cannot run, save the attempted command and the
   concrete blocker as before.txt.
3. After editing, rerun the same reproduction and save the same fields
   as after.txt.
4. Run [test/build/type-check/benchmark command] and save the command,
   exit status, stdout, and stderr as tests.txt.
5. Run any additional check needed by the SUCCESS CRITERIA and save it
   under a descriptive filename.
6. Inspect the final diff. Do not claim success for a criterion that
   was not checked or for a command that failed.

OUTPUT
- Complete the in-scope change; do not stop after producing a plan.
- Keep the diff scoped to the GOAL; avoid unrelated refactors.
- Report: what changed, each success criterion and the artifact that
  supports it, assumptions made, anything not verified, and any
  remaining blocker or conflict.
- For every success claim, cite the artifact path and the key result
  or exit status. Treat claims without saved evidence as unverified.
```

---
