# 115-no-safe-single-run — Prompt 1 (find your flip set)

```text
You are auditing a benchmark or eval to find its FLIP SET: the specific
items whose pass/fail verdict is not stable across runs under IDENTICAL
configuration -- same model, same weights, same decoding params (temperature
0 included), same prompts, same scorer, same seed if one exists. You have
shell access. Change no configuration between runs.

1. PIN AND RUN k TIMES. Record every knob that could vary (model + revision,
   decoding params, batch size / concurrency, endpoint or provider region,
   scorer version, retrieval or context assembly, RNG seed) to
   run-config.txt. Then run the SAME evaluation k>=5 times, writing per-item
   outcomes (item id, pass/fail) to run-<n>.jsonl. Change nothing between
   runs. If the harness ever falls back to a different code path mid-run
   (slower retrieval, a retry, a degraded scorer), that run is contaminated:
   ABORT it and discard it, do not let it finish and get pooled with the
   clean ones. Grep the logs for fallback/retry/degraded as a floor, not a
   substitute for watching the run.

2. BUILD THE FLIP SET. An item is in the flip set if its verdict is not
   identical across all k runs. List every flip-set item with its id and its
   per-run correctness fraction (how often it passed out of k). Report the
   flip set as a list, not just a count -- the members are the deliverable.

3. REPORT THREE NUMBERS, NOT ONE. Compute per-run accuracy (mean and
   standard deviation across the k runs). Give the mean pairwise per-item
   disagreement (over all run pairs, the fraction of items whose verdict
   differs) as the k-invariant headline. Report the raw "fraction of items
   that ever flipped" ONLY with an explicit note that it grows with k
   (P = 1 - p^k - (1-p)^k, where p is that item's own per-run pass
   probability -- this is a per-item formula, not a single field-wide
   constant) and is a property of how many times you looked, not of the
   system.

4. DO NOT TRIAGE BY ITEM FEATURES. You will be tempted to find a rule --
   "long questions flip," "numeric answers are stable" -- so you can run only
   the fragile items repeatedly. If you test features against flipping, hold
   out a second independent block of runs and require the association to
   replicate there before you believe it. State plainly that any single-block
   signal is suggestive-only and MUST NOT be used to single-run a subset.
   Assume there is no safe subset until replication proves one exists.

5. CHECK RETRIEVAL BEFORE BLAMING IT. For flip-set items, verify whether the
   gold/correct evidence was present in context on every run. If it was
   always present and the answer flipped anyway, the fragility is in
   generation/scoring, not retrieval -- report that, because it changes the
   fix. If retrieval varied, separate that source before reporting.

6. STATE THE RULE. Put the accuracy SD and the mean pairwise disagreement
   next to the smallest margin your work reports as a result. Treat the SD
   as a floor, not a significance test: a headline margin inside roughly one
   SD has not been established without a proper interval or replication, so
   label it not-yet-distinguishable and report the flip set as the reason.
   Say plainly: no single-run margin under the noise floor is a result.
```

## Undo

This prompt only reads and scores; it does not modify your system under test. It is not free, though -- repeated evaluation runs can burn API spend, hit rate limits, or write to shared caches/databases depending on your harness, so budget for that before running k of them. To clean up its own output, create a dedicated run directory first (e.g. `mkdir flip-set-audit-$(date +%s)`) and write `run-config.txt` / `run-*.jsonl` there, then `rm -r` that one directory when you're done reading them -- not a bare glob against your working directory.
