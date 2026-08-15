# 111-the-statistic-that-grew-when-you-looked — Prompt 1 (k-invariance check)

```text
You are auditing a single reported statistic for k-invariance -- whether its
value depends on how many repeated observations (runs, trials, samples) were
collected, rather than on the system being measured. You have the per-run
data and shell access.

INPUT. A reported statistic S computed from k repeated observations of a
fixed system (e.g. "21% of items flipped", "score is 51 +/- 4", "max latency
was 900ms"), plus the raw per-run data it was computed from.

1. CLASSIFY THE ESTIMAND. Decide whether S is one of the growth-by-looking
   family: any "has X ever happened", "the most/least X observed", or
   "the min-to-max spread" quantity. These can only move one direction as k
   increases (ever-happened and max climb; min falls; range widens). If S is
   one of these, it is NOT k-invariant -- flag it now, before recomputing.

2. RECOMPUTE ACROSS k. Recompute S at k = 2, 3, 4, ... up to the full count.
   If the observations have a meaningful order (they were collected
   sequentially), use the growing prefix (first k). If order is arbitrary,
   instead draw several random subsets of each size k and average S over
   them. Plot or print S as a function of k.

3. READ THE CURVE. If S trends monotonically with the number of observations
   and has not visibly leveled off, S is a property of your sample size, not
   the system. Report the value ONLY with its k attached ("21.8% at k=7"),
   never as a bare rate, and state which direction it would move if rerun
   longer.

4. SUBSTITUTE A k-INVARIANT ESTIMAND. Replace the growth quantity with one
   that estimates a fixed property and tightens (not drifts) as k grows:
     - for "ever flipped" -> mean pairwise per-item disagreement across all
       run pairs;
     - for "min-to-max spread" -> standard deviation across runs;
     - for "worst observed" -> a high quantile (e.g. p95 or p99) reported
       together with the sample size it was computed from, not the raw
       extreme and not a fabricated confidence interval.
   Report the invariant number as the headline; keep the growth number only
   as a labelled, k-tagged aside if at all.

5. REPORT. One table: S at each k, the direction it trends, and the
   k-invariant substitute with its value. State plainly whether the
   originally-reported statistic was describing the system or the experiment.
```

## Undo

Read-only analysis. It computes on data you already have and writes only whatever table or plot you direct it to; delete those when you're done.
