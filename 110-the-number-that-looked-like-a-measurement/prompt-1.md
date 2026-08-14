# 110-the-number-that-looked-like-a-measurement — Prompt 1 (name your estimand)

```text
You are auditing a benchmark / eval report for UNNAMED ESTIMANDS. An
estimand is the real-world quantity a number is meant to estimate, defined
WITHOUT reference to the measuring procedure. A number with no named
estimand gets read as whatever is most impressive; your job is to force
each headline number to name what it is a measurement OF, or be flagged.

You have the report (and, if available, the harness that produced it).

1. LIST THE HEADLINE NUMBERS. Extract every quantitative claim the report
   leans on -- accuracy, deltas, rates, "noise floor", "X% improvement",
   any number a reader would repeat. For each, quote it verbatim with its
   surrounding sentence.

2. DEMAND THE ESTIMAND. For each number, try to complete this sentence
   from the report's own text, no charity:
     "Out in the world there is a quantity Q = ____ , and this number is an
      estimate of Q." Q must name: the POPULATION (over what items/units),
      the OPERATION (what is compared or aggregated, in what units), what is
      HELD FIXED, and whether Q is a property of the SYSTEM or of the
      MEASUREMENT PROCEDURE (scorer, run count, sample size).
   If you cannot fill Q from the report alone, mark the number UNNAMED.

3. HUNT TWO SPECIFIC COUNTERFEITS.
   a. CONFLATION: is any number the sum/blend of two different estimands
      (e.g. a per-item churn rate added to an aggregate band), even if both
      happen to be expressed as percentages? Adding them yields a number
      with NO referent. Flag it.
   b. PROCEDURE-AS-WORLD: does any number move when you change only the
      instrument (a more/less lenient scorer, more runs, a different sample)?
      If a rerun or sensitivity check is available and shows movement, it
      measures your procedure, not the system -- flag it and name which knob
      moves it. If no rerun is possible from the report alone, flag the
      number as procedure-conditional by construction (its definition
      depends on the scorer/run-count/sample) rather than claiming observed
      movement you haven't tested.

4. RESTATE OR RETRACT. For each surviving number, write the one sentence
   that names its estimand explicitly. For each UNNAMED or counterfeit
   number, state plainly that it cannot be reported as a measurement until
   its estimand is named or the conflation is separated.

5. REPORT. A table: number | quoted claim | estimand (or UNNAMED) |
   property of system or procedure | verdict (keep-as-restated / separate /
   retract). End with the count of headline numbers that could not name
   what they measure.
```

## Undo

Read-only audit. It reads a report and writes findings; it changes no data and runs no evaluation. Nothing to revert except any notes file it produces.
