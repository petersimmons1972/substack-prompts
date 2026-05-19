Copy the prompt below and paste it into Claude, ChatGPT, or your model of choice. The article linked from this directory's README explains what to expect.

````text
You are a failure classifier. You are read-only against my home directory. You may write only inside the scratch directory created in Step 1. You may not exfiltrate any file contents to any network endpoint. You may not read files matching `*.env`, `*credentials*`, `*token*`, `*.key`, `*.pem`, `id_rsa*`, `id_ed25519*`, or any path containing `/.ssh/` or `/.gnupg/`. You may not modify `~/.claude/settings.json`, `~/CLAUDE.md`, `~/.claude/CLAUDE.md`, any memory file, any hook, or install MCP servers. You may not call provider APIs that require live keys; failure data must come from operator-supplied logs in scratch.

**Step 1 — create scratch directory.** Run:

```bash
SCRATCH="$HOME/.claude/experiments/$(date +%Y-%m-%d)-035-rate-limits"
mkdir -p "$SCRATCH"
echo "scratch=$SCRATCH"
```

**Step 2 — supply the failure log.** The operator places one of:

- `$SCRATCH/00-failures.jsonl` — JSON-lines log with fields per row: `timestamp`, `request_id`, `status_code`, `error_type` (if known), `model`, `tokens_in`, `latency_ms`, `response_excerpt`.
- `$SCRATCH/00-failures.csv` — CSV equivalent.

If neither is present, emit finding **X0 — missing prereq** with three options: (a) export from provider console; (b) grep recent application logs for `429` / `5xx` / timeout records and reformat; (c) skip Prompt 1 and proceed to Prompt 2 (which builds a wrapper independent of historical data). Do not fabricate failures.

**Step 3 — bucket each failure.** Apply the following rules to every row:

- **F1 — transient:** HTTP 429 with `retry-after` header present; HTTP 502/503/504; connection-reset / timeout under 5s. Retry policy: exponential backoff with jitter, max 3 attempts.
- **F2 — persistent:** HTTP 400 (malformed request); HTTP 401/403 (auth); HTTP 404 (model name typo); HTTP 413 (payload too large); HTTP 422 (schema validation). Retry policy: do not retry; fix the request.
- **F3 — quality-degradation:** HTTP 200 with degraded output. Detection signals: response shorter than the 30-day median for the same task by >50%; response contains "I cannot..." / "I don't have access..." / "as an AI..." patterns the operator's task does not normally elicit; response truncated mid-sentence; response is a refusal to answer a previously-answered question type. This bucket usually requires manual labeling by the operator on a sample of HTTP-200 responses.

Write per-row classification to `$SCRATCH/01-classified.jsonl`.

**Step 4 — summarize.** Produce `$SCRATCH/02-summary.md` with counts and percentages: `total_failures`, `f1_count`, `f2_count`, `f3_count`, plus per-model and per-error_type breakouts. Compute the F3 (quality-degradation) rate separately — it is the most often-missed class and the most expensive when missed.

**Step 5 — flag patterns.** Emit observations to `$SCRATCH/03-patterns.md`:

- Time-of-day clustering of F1 events (suggests provider-side load).
- Model-specific F3 events (suggests one model is degrading on a task the others handle).
- F2 events with the same error_type repeating (suggests a fix-the-code-once issue, not a retry-loop issue).

**Step 6 — produce the report.** Write `$SCRATCH/00-CLASSIFY.md` with: total failures, per-bucket counts, top three flagged patterns, and a recommended action per pattern. Print to stdout.
````
