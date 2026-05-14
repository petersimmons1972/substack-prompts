# Prompt 2 — Dry-Run Reference

**Run on:** 2026-05-05 (Opus 4.7, 1M context)
**Environment:** Linux 6.18.7, bash 5.x, Claude Code session
**Status:** All 7 steps produced output. Replay completed by operator. Undo verified clean.

---

## Inputs

Top candidate from Prompt 1: idx 8 — "rewrite README across 3 repos" (severity 3, originally run on Claude.ai chat). Replay surface: Claude Code.

## 11-original-metrics.md

```
turns: 18
tokens_est: 21,400
elapsed_time: 47 min (operator estimate; chat surface does not record)
quality_note: 4/5 — final READMEs were good after manual stitching, but the stitching was the bottleneck.
```

## 12-runbook.md (excerpt)

```
1. Open Claude Code in the parent directory of the three repos.
2. Start a fresh session.
3. First user prompt:
   "Read the existing README.md in repos A, B, C. Each is a small open-source
    library. Rewrite each so they share a consistent structure: H1 title,
    one-paragraph summary, install, quickstart, links. Preserve existing
    examples. Show me a diff per file before writing."
4. Expected output: three diffs, then on approval, three Write calls.
5. Record after completion: turns, tokens (Claude Code status line), elapsed time.
6. Use generic test repos with no proprietary content.
```

## 13-replay-metrics.md (operator-supplied after replay)

```
turns: 5
tokens_est: 8,200
elapsed_time: 11 min
quality_note: 5/5 — Claude Code wrote all three diffs in one turn, applied after one round of edits.
```

## 14-comparison.md

| metric | original (chat) | replay (Claude Code) | delta | delta_pct |
|---|---|---|---|---|
| turns | 18 | 5 | -13 | -72% |
| tokens_est | 21,400 | 8,200 | -13,200 | -62% |
| elapsed_time | 47 min | 11 min | -36 min | -77% |
| quality | 4 | 5 | +1 | — |

## 00-DELTA.md

```
candidate: idx 8 — rewrite README across 3 repos
original_surface: claude-ai (chat)
replay_surface: claude-code
turns_delta: -13 (-72%)
tokens_delta: -13,200 (-62%)
time_delta: -36 min (-77%)
quality_delta: +1
verdict: BETTER_FIT_CONFIRMED
```

## Notable result

The 72% turn reduction is at the upper end of the predicted 50–80% range for severity-3 mismatches; quality also improved by one point because the diff-then-write workflow caught a structural inconsistency the chat-paste approach had let through. The operator now has a single concrete artifact ($SCRATCH/14-comparison.md) showing a 62% token reduction on a real task — the kind of evidence that changes a habit.

Worth flagging for Phase 3: the runbook in this dry-run was generic enough to serve readers; Phase 3 drafting should make sure the article body emphasizes that the replay should use a *test* equivalent, not the original proprietary content. The prompt covers this in Step 3 but the article body should reinforce it.

## Undo verified

```
$ rm -rf "$HOME/.claude/experiments/2026-05-05-025-surface-fit"
$ ls "$HOME/.claude/experiments/" | grep 025-surface || echo "(absent)"
(absent)
```

UNDO VERIFIED: `rm -rf "$HOME/.claude/experiments/$(date +%Y-%m-%d)-025-surface-fit"`

The replay itself was operator-driven on Claude Code against test repos — no live file in `~/CLAUDE.md`, settings, or memory family was touched.

## Security-floor self-check

- [x] Did not exfiltrate file contents to any network endpoint.
- [x] Did not read `.env`, credentials, tokens, keys, or `.ssh`/`.gnupg` paths.
- [x] Did not modify `~/.claude/settings.json`, `~/CLAUDE.md`, `~/.claude/CLAUDE.md`, `MEMORY.md`, or `~/AGENTS.md`.
- [x] Did not install MCP servers or change hook configuration.
- [x] All writes confined to `$HOME/.claude/experiments/2026-05-05-025-surface-fit/`.
- [x] Replay used generic test repos; no proprietary content was rewritten.
