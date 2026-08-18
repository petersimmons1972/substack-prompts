# 114-the-auditor-graded-a-blank-exam — Prompt 1 (prove your tests ran)

```text
You are auditing a test suite for silent skips -- tests that report success
without executing. A skipped test is not a passing test; it renders green and
proves nothing. Your job is to make the suite prove it RAN. You have shell
access. Change no test logic.

1. COUNT WHAT RAN, NOT WHAT PASSED. Identify the test framework and enable
   its full skip/collection reporting (verbose mode, reason strings) before
   trusting the default summary -- many runners hide reasons unless asked.
   Run the suite and capture the full output. Record these separately:
   passed, failed, and skipped -- and separately again, note any xfail,
   deselected, cancelled, or "zero tests collected" results, since those are
   different failure modes with different causes, not one bucket. If skipped
   > 0, list every skipped test and its reason string. A skip on a test the
   environment was actually supposed to be able to run is a finding; a
   documented, expected skip (a platform guard, a feature flag genuinely off)
   is not -- distinguish the two before flagging.

2. HUNT THE ENV GATES. Grep the suite AND its runner/CI config for
   conditional skips tied to the environment: skip markers or guards keyed on
   env vars, database or service URLs, credentials, feature flags, or network
   reachability (skipif, skip_unless, "not set", getenv, os.environ,
   required_env), plus CI-level test-selection flags, build tags, and
   fixtures/hooks that can silently exclude tests outside the source text
   itself. For each, record what makes it skip. These are the tests most
   likely to disappear silently in an environment that lacks the dependency
   -- exactly where you most need them to run.

3. TIME EVERY TEST; DISTRUST THE IMPLAUSIBLE ONES. Re-run with per-test
   durations. A test whose runtime is implausible for what it claims to do
   (a claimed real network round-trip or disk I/O finishing in a fraction of
   a millisecond, with no local cache or in-memory backend that would explain
   it) likely did not do the thing. Establish what a real pass costs first --
   don't apply a fixed threshold blind to the environment -- then flag
   outliers against that baseline, and confirm with execution evidence
   (logs, trace, a side effect you can independently check), not runtime
   alone.

4. FORCE THE DEPENDENCIES ON, IN A DISPOSABLE ENVIRONMENT. Re-run the suite
   with the gated dependencies actually present -- but only against a
   throwaway or already-sanctioned test instance, never a production
   database, queue, or credential. If you cannot provision the dependency
   safely, STOP and report the suite as unverifiable rather than skip this
   step or fabricate a mock that changes what's being tested. Compare
   passed / failed / skipped against the first run. Any test that was
   green-by-skip and now executes is a test whose result you never actually
   had. If any now fail, the earlier green was hollow.

5. REPORT. A table: total, passed, failed, skipped (split into
   expected/documented vs. unexpected), and the count of tests whose runtime
   was implausible for what they claim to touch. State the delta between the
   gated run and the dependencies-on run. If the suite reported green while
   skipping tests it was built to run, say so plainly -- that is the
   finding. A green that touched no dependency, on a test built to touch one,
   is not a result.
```

## Undo

The timing pass is read-only. Step 4 is not: it stands up a real dependency and lets tests write to it, so use a disposable instance and tear it down afterward (drop the container/database, revoke any throwaway credentials). If you provisioned nothing beyond a local disposable container, there is nothing left to revert once it's torn down.
