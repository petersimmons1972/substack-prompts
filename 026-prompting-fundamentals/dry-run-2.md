# Prompt 2 — Dry-Run Reference

**Run on:** 2026-05-05 (Opus 4.7, 1M context)
**Environment:** Linux 6.18.7, bash 5.x, Claude Code session, Anthropic API access
**Status:** All 9 steps produced output. API calls succeeded across 10 calls (5 tests x 2 versions). Undo verified clean.

---

## Inputs

Repeated prompt: "classify this commit message as one of fix/feat/refactor/chore/docs/test." Operator confirmed using it ~30 times per month.

Five test inputs (mix of easy and hard):

```
1. fix: handle null in parser
2. drop debug print
3. add /v1/projects endpoint
4. wip
5. refactor(api): extract auth middleware into shared package
```

## 06-counts.md

| version | tokens (cl100k_base) |
|---|---|
| bare | 38 |
| fewshot (3 examples) | 152 |

Per-call overhead: **+114 tokens**.

## 07-results.md

| test | bare | fewshot | bare_correct | fewshot_correct |
|---|---|---|---|---|
| 1 | fix | fix | Y | Y |
| 2 | chore | refactor | N | Y |
| 3 | feat | feat | Y | Y |
| 4 | chore | chore | ? → Y (operator) | ? → Y (operator) |
| 5 | refactor | refactor | Y | Y |

Bare correct: 4/5. Few-shot correct: 5/5.

## 08-economics.md

```
quality_uplift: +1
tokens_per_call_overhead: 114
total_overhead_5_calls: 570
cost_per_quality_point: 570
```

Interpretation: at 30 calls/month, the per-month overhead is 3,420 tokens for one quality-point uplift across the test set. At Haiku 4.5 pricing this is fractions of a cent per month. The cost-per-quality-point of 570 is just over the 500 threshold for `EXAMPLES_EARN_KEEP`, so the verdict tilts to `EXAMPLES_OVERPRICED` despite the real quality improvement.

## 00-FEWSHOT.md

```
bare_correct: 4/5
fewshot_correct: 5/5
quality_uplift: +1
tokens_per_call_overhead: 114
total_overhead_5_calls: 570
verdict: EXAMPLES_OVERPRICED
```

## Notable result — flag for Phase 3 drafting

The 500-token threshold for `EXAMPLES_EARN_KEEP` was tuned to a typical Haiku call cost; for Sonnet/Opus operators, the threshold should be higher (Opus tokens are ~30x more expensive). The article body should call this out explicitly: the verdict is *cost-per-call sensitive*, and operators using larger models for few-shot have more room to absorb the overhead.

Also worth flagging: the operator's actual usage was 30 calls/month, not the 5 of the test. The quality lift would compound; if examples save the operator from one mis-classification per month that costs 5 minutes to correct, the human-time savings dwarf the token cost. The article should note that token economics is one input to the decision, not the whole decision.

## Undo verified

```
$ rm -rf "$HOME/.claude/experiments/2026-05-05-026-fewshot"
$ ls "$HOME/.claude/experiments/" | grep 026-fewshot || echo "(absent)"
(absent)
```

UNDO VERIFIED: `rm -rf "$HOME/.claude/experiments/$(date +%Y-%m-%d)-026-fewshot"`

## Security-floor self-check

- [x] Did not exfiltrate any file contents beyond the operator-authorized prompt and test inputs.
- [x] Did not read `.env`, credentials, tokens, keys, or `.ssh`/`.gnupg` paths.
- [x] Did not modify `~/.claude/settings.json`, `~/CLAUDE.md`, `~/.claude/CLAUDE.md`, `MEMORY.md`, or `~/AGENTS.md`.
- [x] Did not install MCP servers or change hook configuration.
- [x] All writes confined to `$HOME/.claude/experiments/2026-05-05-026-fewshot/`.
- [x] Test inputs were generic commit-message strings; no proprietary content sent to the API.
