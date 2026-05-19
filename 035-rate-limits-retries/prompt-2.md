Copy the prompt below and paste it into Claude, ChatGPT, or your model of choice. The article linked from this directory's README explains what to expect.

````text
You are a wrapper-and-tester implementer. You operate read-only against my home directory. You may write only inside the scratch directory used by Prompt 1 (or create it if Prompt 1 was skipped). You may not exfiltrate any file contents to any network endpoint. You may not read `*.env`, `*credentials*`, `*token*`, `*.key`, `*.pem`, `id_rsa*`, `id_ed25519*`, `/.ssh/`, or `/.gnupg/` paths. You may not modify `~/.claude/settings.json`, `~/CLAUDE.md`, `~/.claude/CLAUDE.md`, any memory file, any hook, or install MCP servers. You may not install Python packages globally; if a virtualenv is needed, create it inside scratch.

**Step 1 — create or reuse scratch.** Run:

```bash
SCRATCH="$HOME/.claude/experiments/$(date +%Y-%m-%d)-035-rate-limits"
mkdir -p "$SCRATCH"
```

**Step 2 — write the synthetic load generator.** Produce `$SCRATCH/50-fake_provider.py`: a small Python module exposing a `call(payload)` function. Behavior:

- On 60% of calls: return `{"status": 200, "body": "ok"}`.
- On 15% of calls: return `{"status": 429, "retry_after": 1}` (F1 transient).
- On 5% of calls: return `{"status": 503}` (F1 transient).
- On 10% of calls: return `{"status": 400, "body": "bad request"}` (F2 persistent).
- On 10% of calls: return `{"status": 200, "body": "I cannot help with that."}` (F3 quality-degradation).

The function should accept a `seed` parameter so runs are reproducible. No network calls; pure Python `random`.

**Step 3 — write the retry wrapper.** Produce `$SCRATCH/51-wrapper.py`:

```python
# call(provider_callable, payload, max_retries=3) → result
# Class-aware: F1 backs off and retries; F2 raises immediately; F3 surfaces a quality flag without retrying.
```

Required behaviors:

- F1 (429/5xx): exponential backoff with jitter (`base * 2**attempt + random()`), capped at 30s, max 3 attempts. Honor `retry_after` if present.
- F2 (4xx other than 429): raise immediately with the status code in the message. Do not retry.
- F3 (200 with refusal/truncation/short-response patterns): return result with `quality_flag=degraded`. Do not retry by default; let caller decide.
- Log each attempt with `request_id`, `status`, `attempt`, `class`, `latency_ms` to `$SCRATCH/52-wrapper.log`.

Keep total wrapper code under 80 lines.

**Step 4 — write the test harness.** Produce `$SCRATCH/53-load.py`: imports `fake_provider` and `wrapper`, runs 200 calls through the wrapper, collects per-class outcomes. Write a JSONL trace to `$SCRATCH/54-trace.jsonl`.

**Step 5 — run the test.** Execute `python3 "$SCRATCH/53-load.py"` from inside scratch. Verify output.

**Step 6 — measure outcomes.** Read `54-trace.jsonl`. Compute: `success_rate`, `f1_recovered_pct` (F1 calls that ultimately succeeded after retry), `f2_correctly_failed_fast_pct` (F2 calls that did not retry), `f3_flagged_pct` (F3 calls correctly tagged degraded). Write to `$SCRATCH/55-outcomes.md`.

Acceptance criteria:

- `f1_recovered_pct ≥ 80%` (transient retries should mostly succeed).
- `f2_correctly_failed_fast_pct = 100%` (zero wasted retries on F2).
- `f3_flagged_pct ≥ 90%` (degradation pattern detection working).

If any criterion fails, fix the wrapper in scratch and re-run.

**Step 7 — produce the report.** Write `$SCRATCH/50-PLAN.md` with: wrapper code path, test harness path, sample run outcomes, acceptance verdict, and an "adapt to production" note describing the four lines the operator must change to wire the wrapper to their real provider client. Print to stdout.
````
