# 112-the-experiment-that-changed-its-mind-mid-sentence — Prompt 1 (silent-fallback audit)

```text
You are auditing a data or evaluation pipeline for SILENT-FALLBACK paths --
places where the pipeline can quietly switch to a degraded strategy, skip
work, or fill in missing data, and KEEP GOING as if nothing changed. You
have read access to the code and logs. You are not fixing anything yet; you
are producing an inventory of every place you can find where the pipeline
is allowed to cope instead of stop -- a static-analysis pass, not a proof
of completeness; note if the codebase has entry points (plugins, remote
services, config-driven branches) you couldn't fully trace by reading.

1. FIND THE FALLBACKS. Search the code for every place a failure is caught
   and handled without aborting: try/except that continues, retries, "or
   default" reads (.get(key, 0), || fallback), degraded/cheaper alternate
   code paths, and any log line containing fall back / fallback / degraded /
   retry / skipped / timeout / default. For each, record: what fails, what
   it falls back TO, and whether anything downstream can tell the difference.

2. FIND THE FALSE COMPLETIONS. Locate every place the pipeline decides a unit
   of work is "done." Flag any that accept PRESENCE as proof of completion --
   "file exists," "output non-empty," "no exception thrown" -- rather than
   checking that the expected quantity of real results is actually there.
   A partial or fallen-back run that still produces output is the exact
   failure this step exists to catch.

3. FIND THE SILENT ZEROS. Search for anywhere missing, null, or unscored data
   is coerced into a valid-looking value (zeros, empty string, "unknown",
   defaults) before aggregation. These turn absence-of-result into a
   plausible bad result that pools into your averages invisibly.

4. CLASSIFY EACH: COPE OR DIE. For every path found in 1-3, decide whether,
   in THIS pipeline's purpose, it should be allowed to degrade-and-continue
   (fine for a production service) or must ABORT (mandatory for anything that
   produces a measurement, an average, or a number you report). If the
   pipeline's output feeds an average or a published figure, the default is
   DIE: a run that changed strategy mid-flight must not survive as a data
   point.

5. CHECK THE EVIDENCE TRAIL. Determine whether a fallback, a partial run, or
   a skipped unit would leave a LOUD, one-place record -- an event or
   lifecycle log answering "what strategy did each unit actually use, and how
   many items did it really complete." If the only trace is a line buried in
   a per-stage debug log nobody reads, flag it: the event that invalidates a
   run must be the easiest thing to find, not the hardest.

6. REPORT. A table: each silent-fallback / false-completion / silent-zero
   path, what it hides, your COPE-or-DIE verdict, and the specific change
   that would make a forbidden degradation ABORT instead of average. Name
   the single highest-risk path -- the one most likely to pool corrupted data
   into a real number without anyone seeing it.
```

## Undo

Read-only audit. It reads code and logs and writes only its report; nothing in the pipeline is modified. Delete the report file when you're done with it.
