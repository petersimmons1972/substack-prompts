# 109-the-paper-about-measurement-error — Prompt 1 (audit)

```text
You are auditing a benchmark or eval harness for run-to-run variance under
IDENTICAL configuration -- same model, same weights, same decoding params
(temperature 0 included), same prompts, same scorer, same seed if one
exists. You have shell access. Change no configuration between runs.

1. PIN THE CONFIG. Record every knob that could vary: model + revision,
   decoding params, batch size / concurrency, endpoint or provider region,
   scorer version, retrieval or context assembly, and any RNG seed. Write
   them to run-config.txt. If the harness cannot be made to hold all of
   these fixed, STOP and report that -- an unpinnable harness cannot be
   measured for its own noise.

2. RUN IT k TIMES UNCHANGED. Execute the SAME evaluation k>=5 times with the
   pinned config, writing per-item outcomes (item id, pass/fail) for each run
   to run-<n>.jsonl. Do not change anything between runs. If the harness ever
   falls back to a different code path mid-run (a slower retrieval mode, a
   retry, a degraded scorer), that run is contaminated: ABORT the run and
   discard it, do not let it finish and get pooled with the clean ones. Grep
   the run logs for fallback/retry/degraded as a floor, not a substitute for
   watching the run.

3. COMPUTE THE k-INVARIANT NUMBER. Report per-run accuracy (mean and standard
   deviation across the k runs) AND the mean pairwise per-item disagreement:
   over all run pairs, the fraction of items whose pass/fail differs. Report
   the pairwise disagreement, NOT the "fraction of items that ever flipped"
   -- the ever-flipped fraction grows with k (P = 1 - p^k - (1-p)^k, for
   independent runs with a fixed per-item flip probability) and is a
   property of how many times you looked, not of the system.

4. COMPARE TO THE MARGINS YOU PUBLISH. Put the accuracy SD and the mean
   pairwise disagreement next to the smallest margin your work reports as a
   result. Treat the SD as a floor, not a significance test: a headline
   delta inside roughly one SD has not been established without a proper
   interval or replication, so label it not-yet-distinguishable and report
   it with the SD, never as a bare point estimate.

5. REPORT. A table: per-run accuracy, mean, SD, mean pairwise disagreement,
   and the count of runs discarded for fallback. If the SD is not small
   compared to any margin you publish single-run, say so plainly -- that is
   the finding.
```

## Undo

This prompt only reads and scores; it does not modify your system under test. It is not free, though — repeated evaluation runs can burn API spend, hit rate limits, or write to shared caches/databases depending on your harness, so budget for that before running k of them. To clean up its own output, create a dedicated run directory first (e.g. `mkdir noise-audit-$(date +%s)`) and write `run-config.txt` / `run-*.jsonl` there, then `rm -r` that one directory when you're done reading them — not a bare glob against your working directory.
