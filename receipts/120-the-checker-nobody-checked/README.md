# Receipts: Sonnet 5.5 vs GPT-6 Sol (post 120)

Measured 2026-09-28. Two experiments.

## linkvault-r3 (main result)

Task: fix `linkvault/resolver.py` in a small Python repo (fleet eval-suite task r3-linkvault-v1).
Scored by 23 hidden tests the model never saw. The hidden tests are a frozen instrument and are
not published here. Claude arms ran through Claude Code (`claude -p`); Sol arms through Codex CLI.

| Cell | n | Hidden tests passed | Runs that ran a real check | Unrequested test files left in repo | Scratch files written outside the repo | $ per run (list) | Wall time |
|---|---|---|---|---|---|---|---|
| GPT-6 Sol, medium | 20 | 17/23 in 19 runs, 14/23 in 1 | 20/20 | 0/20 | 0/20 | $0.113 | 80 s |
| GPT-6 Sol, high | 6 | 17/23 | 6/6 | 0/6 | 0/6 | $0.146 | 108 s |
| Sonnet 5.5, medium | 6 | 17/23 | 6/6 | 0/6 | 0/6 | $0.171 | 25 s |
| Sonnet 5.5, high | 20 | 17/23 | 20/20 | 13/20 | 4/20 | $0.250 | 53 s |
| Sonnet 5.5, high + fix paragraph | 10 | 17/23 | 10/10 | 1/10 | 4/10 | $0.224 | 48 s |
| Sonnet 5.5, medium + fix paragraph | 10 | 17/23 | 10/10 | 0/10 | 1/10 | $0.179 | 28 s |
| Opus 5.5, medium | 10 | 17/23 | 10/10 | 8/10 | 6/10 | $0.484 | 72 s |

Two-sided Fisher exact tests (recomputed independently of the analysis scripts):
- Unrequested test files, Sonnet high 13/20 vs Sol medium 0/20: p = 1.3e-5.
- The fix paragraph, Sonnet high 1/10 vs 13/20: p = 0.0067.
- Scratch outside the repo, Sonnet high 4/20 vs Sol medium 0/20: p = 0.11. Not significant.

Cost basis: Claude = the provider-reported `costUSD` at list prices. Claude Code writes the prompt
cache at the 1-hour rate ($4/M for Sonnet 5.5). Sol = list price: uncached input $2/M, cached
input $0.20/M, output $10/M. The per-cell ranges are in `real_cost_by_cell.txt`.

"Ran a real check": executed code that exercises the changed resolver before reporting done.
The verification count went wrong at three stages before it was right:
1. The preregistered matcher over-counted. It credited python scripts that only wrote files as tests. Amended before any flag was reported (PREREG.json, amendments).
2. The amended matcher (`rescore_verify.py`) under-counted checks run inside heredoc commands: Sonnet medium 1/6, Sonnet high 9/20, Opus 7/10, Sol medium 19/20.
3. The coordinator's hand review of those negatives read only the command heads. It flipped 7 runs (`overrides` in `verified_adjudicated.json`) and left Sonnet high at 12/20 against Sol medium 20/20, a two-sided Fisher p of 0.003 that looked publishable and was false.
4. Reading the full transcripts showed that every one of the 13 remaining negatives ran assertion scripts inside the same command, with the tool result "ok".
The superseded fields were removed from `per_run.jsonl`. Every run in every cell checked its work. `verified_adjudicated.json` covers the five unfixed cells. The two fix-paragraph cells (20 runs) were scored only by the amended rule (10/10 each) and were not hand-adjudicated.

Voided runs are in `voided.jsonl`, each with its reason. Two runs were replaced because a second
model served part of the run: Claude Code's advisor tool (Opus) in one, and a Codex auto-review
session in the other. The model-purity check did not catch either.

The fix paragraph is `fix_paragraphs.txt`, passed with `--append-system-prompt`. The prompt given
to the model was otherwise unchanged. `scan_outside.py` produces `outside_writes.txt`.

## What the 6 missing tests are

All 81 scored runs at 17/23 (and the 2 voided runs) failed the same 6 hidden tests; the one 14/23 Sol run failed those 6 plus 3 more (`failing_tests.txt`). All 6 need `deactivate_link` to survive a store outage the way `resolve` and `update_link` do: not raise, still apply the tombstone, and count the failure toward the shared circuit breaker. The task brief says the new methods "should fit alongside" the existing ones, "not just call the store directly".

In fleet's July 2026 runs of the same task (fleet repo, `dispatch-metrics/evidence/round3/cross-vendor-r3-linkvault/FINDINGS.md`), Sonnet 5 and every GPT-5.6 tier scored 11/23: they wired neither new method through the breaker. Opus 4.8 scored 17/23. Grok 4.5 scored 23/23 in 1 of 6 lean-brief runs and 2 of 3 verbose-brief runs. July detail from the same file: on the lean brief (`brief_lean.md`, the brief the September runs also used), GPT-5.6 Sol scored 11/23 in 5 runs and 14/23 in 1. Opus 4.8's 17 came from wiring `update_link` but not `deactivate_link`. In the July E3 explicit-cue test, the brief spelled out the rule and said "Do this for BOTH methods." Sonnet 5 and every GPT-5.6 tier rose from 11 to exactly 17, Opus 4.8 stayed at 17, and nobody reached 23. Grok 4.5 ran through the grok CLI. So 17/23 is not the task's ceiling. It is the point where today's models all stop.

## reader-task (the prompts readers can paste)

A 15-line `pricing.py` with two seeded bugs, from `prompt-A.md` (plain) and `prompt-B.md` (plain
plus a "run a real check" paragraph), scored by `check.py` (7 cases). 5 runs per cell per prompt,
50 runs in all. Every run scored 7/7. At this size the task does not separate the models on
correctness, on unrequested files (0 in every cell) or on cost (Sol medium $0.055 vs Sonnet high
$0.055 on prompt A). The speed ordering held, with Sonnet faster. Claude runs here used
`--safe-mode`, unlike linkvault-r3, so do not compare costs across the two tables. One Sonnet-high
run wrote `/tmp/t.py`, outside the folder it was told to stay in.

Codex version: all 26 scored Sol session logs record cli_version 0.156.1, and each contains the quoted built-in testing instructions word for word. The voided r3_sol6_high_r6 log does not.
