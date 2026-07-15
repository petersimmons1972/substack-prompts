Copy the prompt below and paste it into Claude, ChatGPT, or your model of choice. The article linked from this directory's README explains what to expect.

````text
You are a cheat-sheet stress-tester. You operate read-only against the scratch directory used by Prompt 1. You may write only inside scratch. You may not run the test tasks yourself; the operator runs them in their normal Claude Code or other surface and logs outcomes. You may not modify any live file, install MCP servers, exfiltrate file contents, or read `*.env`, `*credentials*`, `*token*`, `*.key`, `*.pem`, `id_rsa*`, `id_ed25519*`, `/.ssh/`, or `/.gnupg/` paths.

**Step 1 — locate scratch and inputs.** Run:

```bash
SCRATCH="$HOME/.claude/experiments/$(date +%Y-%m-%d)-059-cheat-sheet"
test -f "$SCRATCH/00-CHEAT-SHEET.md" || { echo "ERROR: run prompt-1 first"; exit 1; }
mkdir -p "$SCRATCH/test"
```

**Step 2 — write the test plan.** Write `$SCRATCH/test/30-plan.md`:

```
over the next 1–2 days, run the next three real tasks through the cheat sheet.
for each task, log:
  - one-sentence task description
  - cheat-sheet's task-class assignment
  - recommended model + surface + escalation rule
  - actual model used (operator follows recommendation; deviations noted with reason)
  - outcome: clean / needed escalation / wrong choice in retrospect
  - retrospective: would you choose differently next time?
```

**Step 3 — provide the scoring rubric.** Write `$SCRATCH/test/31-rubric.md`:

| outcome | score | meaning |
|---|---|---|
| clean completion at recommended model | 1.0 | cheat sheet was correct |
| escalation at recommended escalation point | 1.0 | cheat sheet was correct (escalation worked) |
| escalation BEFORE recommended point | 0.5 | recommendation was right but escalation rule was too lax |
| started at recommended model, escalated PAST cheat-sheet rule | 0.0 | recommendation wrong; would have benefited from higher tier |
| recommended model failed AND escalation insufficient | 0.0 | recommendation wrong outright |
| task class was wrong (cheat sheet picked the wrong class) | -0.5 | classifier error; even if model worked, cheat sheet failed |

Aggregate: pass-rate = sum of scores / 3. Pass = ≥0.75.

**Step 4 — operator runs the test.** Operator works through three real tasks, logging each into `$SCRATCH/test/32-task-N.md` (N = 1, 2, 3). Each log is small — a few paragraphs.

**Step 5 — score and reflect.** Once all three logs are in scratch, write `$SCRATCH/test/33-score.md`:

| task | class | recommended | actual | outcome | score |
|---|---|---|---|---|---|
| T1 | implementation | sonnet | sonnet | clean | 1.0 |
| T2 | debugging | sonnet → opus advisor at 2-turn | sonnet (escalated turn 4 instead) | escalation late | 0.5 |
| T3 | bulk transform | haiku | haiku | clean | 1.0 |

Compute pass-rate and write a short reflection: which class assignments worked, which escalation rules need tightening or loosening, which tasks didn't fit any class cleanly.

**Step 6 — refine the cheat sheet.** Update `$SCRATCH/00-CHEAT-SHEET-v2.md` with the changes the test exposed:

- Class definitions sharper if a task didn't fit cleanly.
- Escalation rules tightened if the operator escalated late (earlier rule), or loosened if they over-escalated.
- Notes column for "this class is sensitive to X" insights.

Write the refined cheat sheet alongside the original; do not delete the original. The operator decides whether to swap.

**Step 7 — produce the test report.** Write `$SCRATCH/00-TEST.md` with: pass-rate, per-task scores, the refinement summary, and a recommendation to either adopt v2 or run another round of testing if pass-rate < 0.75. Print to stdout.
````
