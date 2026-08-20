# 118-the-instruction-was-the-absence-of-one — Prompt 2 (action)

```text
You are upgrading an agent pipeline from config-trusted to per-run-verified
model attribution. Target: the record source your audit rated CONFIG-TRUSTED —
substitute its actual path/file for <the CONFIG-TRUSTED record source>
wherever it's referenced below. You have shell access.

1. IDENTIFY the per-run ground truth: find where each run's own output/log
   states the model actually used (a banner line, an API response field, a
   version string). If runs do not currently emit one, add the smallest
   possible change so they do (e.g., the wrapper script echoes the resolved
   model identifier into the run's log at start).
2. VERIFY AT WRITE TIME: modify the component that appends rows to
   <the CONFIG-TRUSTED record source> so that it reads the model identifier
   from the run's own log, not from configuration. If the two disagree, or
   the log line is missing, it must write "model": null,
   "attribution_status": "unverified", and "configured_model_unverified":
   "<config-value>" — never write the unverified guess into the model field
   itself. (A disagreement means one of your two witnesses is wrong and you
   do not yet know which — the log can be stale or truncated just as the
   config can be newer than the run — so flag the row for a human instead
   of auto-picking a winner.) Any analysis or grouping code that aggregates rows by model must
   filter to attribution_status == "verified" first, or it will silently
   create a garbage bucket (or crash) out of the unverified rows.
3. BACKFILL AUDIT FLAG: do not rewrite historical rows. Instead, write a
   one-off report file attribution-audit-<date>.md listing any historical
   rows that fall inside a known config-change ambiguity window, so a human
   can decide.
4. TEST: run one end-to-end job (or a dry-run/mock if the pipeline has one)
   and show that the new row's model field came from the run log. Then force
   a real mismatch to prove the disagreement path works: start a run under
   the real model so its log records the real model name, then — after the
   run has logged its own model but before the ledger write executes —
   change the config to point at a different, fake model name. Show the
   resulting ledger row has "model": null and "attribution_status":
   "unverified" (log said the real model, config said the fake one, so
   neither is trusted alone) rather than silently recording either value.
5. Commit with message: "attribution: verify model per-run from logs; config
   is a claim, not a fact". Print the diff.

Constraints: no changes to historical data; no changes outside the
attribution write path and the run-log emission point.

## Undo
To revert everything this prompt did:
1. `git log --oneline` — identify the single attribution commit above.
2. `git revert <that-commit>` to restore config-trusted behavior. Use
   revert, not a hard reset — a reset can discard unrelated uncommitted
   work sitting in the same tree and has no built-in check that this
   commit is really the sole tip.
3. Delete the report file: `rm attribution-audit-<date>.md` (or revert its
   commit if committed).
4. If step 4's test left a fake model name in any config file, restore the
   real value by re-editing it to the value shown in the pre-change diff.
   (Avoid `git checkout -- <config-file>` — it would also discard any
   unrelated edits sitting in that file.)
```

**Ground truth — tested 2026-07-10 (harness-agnostic wording, run without modification).** Codex CLI ✅ (fixture: the claude-codex repo; full transcript in project records). Claude Code and Grok legs: pending.
