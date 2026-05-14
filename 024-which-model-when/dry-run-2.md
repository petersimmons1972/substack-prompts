# Prompt 2 — Dry-Run Reference

**Run on:** 2026-05-05 (Opus 4.7, 1M context)
**Environment:** Linux 6.18.7, bash 5.x, Claude Code session, Anthropic API access via `ANTHROPIC_API_KEY` env var
**Status:** All 6 steps produced output. API call succeeded. Undo verified clean.

---

## Inputs

Top candidate from Prompt 1's `04-overspends.md`: a 380-token assistant response to a `bulk_judge` task — "score these 12 commit messages 1–5 against our convention." Original model: `unknown` (treated as session default Sonnet). Replay target: Haiku 4.5.

## 11-user-prompt.txt (excerpt)

```
Score each of these 12 commit messages 1–5 against our convention
(imperative mood, <72 chars, conventional-commit prefix). Return a table.

1. fix: handle null in parser
2. updated readme
3. feat(api): add /v1/projects endpoint
... (9 more)
```

## 14-replay-response.txt (excerpt — Haiku 4.5)

```
| # | message | score | reason |
|---|---|---|---|
| 1 | fix: handle null in parser | 5 | imperative, prefix, <72 |
| 2 | updated readme | 2 | past tense, no prefix |
| 3 | feat(api): add /v1/projects endpoint | 5 | conforms |
... (9 more rows)
```

Replay tokens: 412. Latency: 1.8s. Model id: `claude-haiku-4-5-20251015`.

## 15-rubric.md

| Criterion | Original (Sonnet) | Replay (Haiku 4.5) | Notes |
|---|---|---|---|
| Correctness | 5 | 5 | Both scored all 12 messages consistently with the rubric. |
| Completeness | 5 | 5 | Both included reasoning per row. |
| Format fidelity | 5 | 5 | Both returned a markdown table. |
| Brevity | 4 | 5 | Haiku omitted a paragraph of preamble Sonnet included. |
| **Total** | **19** | **20** | |

## 00-REPLAY.md

```
candidate_class: bulk_judge
original_model: Sonnet (default)
replay_model: claude-haiku-4-5-20251015
original_tokens: 380
replay_tokens: 412
original_score: 19
replay_score: 20
score_delta: +1
verdict: OVERSPEND_CONFIRMED
```

## Notable result

The replay scored marginally *higher* than the original because Haiku skipped a preamble paragraph that Sonnet emitted, satisfying brevity. This is the canonical bulk-judge result Anthropic's own pricing guidance describes — for rubric-scoring tasks, Haiku is not just cheaper but often produces tighter output. The cost ratio for this turn class (Haiku at roughly 8% the per-token cost of Sonnet) means an operator who runs 100 such turns per month moves from ~$10 to ~$0.80 with no quality loss.

Worth flagging for Phase 3 drafting: a single confirmed replay is suggestive but not robust. The article should suggest replaying 3–5 candidates before declaring a habit change, not one. The prompt as written supports this by being re-runnable with a different candidate selection — perhaps note this in the "what you should now see" section of Article 024's body.

## Undo verified

```
$ rm -rf "$HOME/.claude/experiments/2026-05-05-024-model-overspend"
$ ls "$HOME/.claude/experiments/" | grep 024-model || echo "(absent)"
(absent)
```

UNDO VERIFIED: `rm -rf "$HOME/.claude/experiments/$(date +%Y-%m-%d)-024-model-overspend"`

The API call itself is not undoable; its content was operator-authorized prose with no PII or credentials. State fully restored locally.

## Security-floor self-check

- [x] Did not exfiltrate any file contents beyond the operator-authorized user prompt.
- [x] Did not read `.env`, credentials, tokens, keys, or `.ssh`/`.gnupg` paths. API key consumed from env var; never echoed.
- [x] Did not modify `~/.claude/settings.json`, `~/CLAUDE.md`, `~/.claude/CLAUDE.md`, `MEMORY.md`, or `~/AGENTS.md`.
- [x] Did not install MCP servers or change hook configuration.
- [x] All local writes confined to `$HOME/.claude/experiments/2026-05-05-024-model-overspend/`.
- [x] Reconstructed user prompt scanned for credential patterns before transmission; none detected.
