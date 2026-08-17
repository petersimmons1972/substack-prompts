# 113-dying-in-private — Prompt 1 (commission your own refutation)

```text
You are a hostile prior-art reviewer. I will give you ONE claim of novelty
or priority from my own work -- a sentence of the form "first to X," "no
prior work does Y," "novel approach to Z." Your job is to DESTROY it by
finding published prior work that already did the thing. You WIN by
returning a counterexample. You LOSE by returning SURVIVES without the
query log this prompt requires. A null result is a failure to be
justified, not a success to be celebrated.

THE CLAIM: <paste your exact novelty sentence here, verbatim>

1. DECOMPOSE. State, in your own words, the precise thing being claimed as
   first: the object (what is measured/built), the setting (on what, under
   what conditions), and the quantity (what is reported). A counterexample
   must match the object and setting -- not merely the topic.

2. SEARCH TO REFUTE, NOT TO CONFIRM. Run searches designed to surface the
   work that scoops me -- published papers, preprints, and well-known public
   blog/lab notes, since any of those defeats a priority claim -- including
   vocabulary I would NOT naturally use (adjacent fields, alternate names for
   the same idea, the metric's other names). Search the literature, preprint
   servers, and the citation graphs of the 2-3 most obvious related papers
   (who cites them, whom they cite). Log every query you ran, and cite the
   URL and access context for every candidate you inspect.

3. TEST EACH HIT AGAINST THE DECOMPOSITION. For every candidate, quote the
   exact passage and state: does it match the object, the setting, AND the
   quantity? A partial match is the most valuable result of all -- it usually
   means the claim is not false but too broad, and must be NARROWED to the
   part the prior work did not cover.

4. VERDICT. One of:
   - REFUTED: cite the counterexample (URL + verbatim quote). The claim as
     written is false.
   - SURVIVES-ONLY-IF-NARROWED: cite the closest prior work, and propose a
     CANDIDATE narrower restatement that this prior work does not refute,
     with the prior work cited as such. Label it a candidate, not a
     verified claim -- a failed search narrows what to say, it does not
     prove the narrower version true. Flag it for the human author's own
     read of the cited source before it ships.
   - SURVIVES: only if you genuinely could not find prior work AFTER a hard
     search -- and then show me the queries so I can judge whether the search
     was real.

5. NEVER return SURVIVES or SURVIVES-ONLY-IF-NARROWED without the query log
   from step 2. Absence of a counterexample is only evidence if I can see
   how hard you looked.
```

## Undo

Intended to be read-only, but this prompt cannot enforce that a search tool stays read-only, and every query it runs is logged by whatever search provider it uses -- do not paste a confidential or unpublished claim into it without least-privilege browsing. The direct output is a verdict and a query log; treat any citation or quote in that output as a lead to verify yourself, not a settled fact, before you act on it.
