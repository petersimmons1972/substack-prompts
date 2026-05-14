# Prompt 1 — Dry-Run Reference

**Run on:** 2026-05-05 (Opus 4.7, 1M context)
**Environment:** Linux 6.18.7, bash 5.x, Claude Code session
**Status:** All 6 steps produced output. Undo verified clean.

---

## Inputs

Operator pasted a list of 10 tasks from the past 14 days, mix of Claude Code transcripts (7), Claude.ai chat sessions (2), and one ChatGPT session.

## 03-labeled.md

| idx | task_summary | surface_used | best_fit | match | severity |
|---|---|---|---|---|---|
| 1 | refactor 4 files to use new logger | claude-code | claude-code | Y | — |
| 2 | brainstorm essay structure | claude-ai | claude-ai | Y | — |
| 3 | translate 30 commit messages to conventional-commit | claude-ai | api | N | 2 |
| 4 | debug a failing pytest in 2 modules | claude-code | claude-code | Y | — |
| 5 | image generation for blog header | chatgpt | chatgpt | Y | — |
| 6 | research vendor pricing tier across 6 sources | claude-ai | claude-desktop | N | 2 |
| 7 | one-off "is this regex correct" | claude-code | claude-ai | N | 1 |
| 8 | rewrite README across 3 repos | claude-ai | claude-code | N | 3 |
| 9 | run a small data transform on a CSV | claude-code | claude-code | Y | — |
| 10 | weekly status update prose | claude-ai | claude-ai | Y | — |

## 04-mismatches.md (sorted by severity desc)

| idx | task_summary | surface_used | best_fit | severity | recommended_action |
|---|---|---|---|---|---|
| 8 | rewrite README across 3 repos | claude-ai | claude-code | 3 | Use Claude Code — chat surface forced manual copy-paste of 3 files; CC writes them in place. |
| 3 | translate 30 commit messages | claude-ai | api | 2 | Use Anthropic API with batch — 30 independent items is the canonical batch case. |
| 6 | research vendor pricing tier across 6 sources | claude-ai | claude-desktop | 2 | Use Claude Desktop with web-fetch MCP — chat lacks persistent multi-source workflow. |
| 7 | "is this regex correct" | claude-code | claude-ai | 1 | One-shot reasoning, no files needed; chat is faster to start. |

## 00-FIT.md

```
tasks_audited: 10
mismatches: 4
severity_distribution: 1=1, 2=2, 3=1
top_pattern: chat surface used for multi-file work
recommendation: Default to Claude Code for any task touching ≥2 files; default to chat for single-shot reasoning.
```

## Notable result

Four of ten tasks (40%) were mismatched, slightly above the expected 2–6 range but consistent with an operator who uses Claude.ai chat as a default-on habit. The severity-3 finding (rewrite README across 3 repos on chat) is the textbook "wrong surface" case and is a strong candidate for Prompt 2 replay. The severity-1 reverse-mismatch (using Claude Code for a one-line regex check) is interesting — it shows surface mismatches go both ways.

T0 did not fire — operator had ample varied usage.

## Undo verified

```
$ rm -rf "$HOME/.claude/experiments/2026-05-05-025-surface-fit"
$ ls "$HOME/.claude/experiments/" | grep 025-surface || echo "(absent)"
(absent)
```

UNDO VERIFIED: `rm -rf "$HOME/.claude/experiments/$(date +%Y-%m-%d)-025-surface-fit"`

## Security-floor self-check

- [x] Did not exfiltrate file contents to any network endpoint.
- [x] Did not read `.env`, credentials, tokens, keys, or `.ssh`/`.gnupg` paths.
- [x] Did not modify `~/.claude/settings.json`, `~/CLAUDE.md`, `~/.claude/CLAUDE.md`, `MEMORY.md`, or `~/AGENTS.md`.
- [x] Did not install MCP servers or change hook configuration.
- [x] All writes confined to `$HOME/.claude/experiments/2026-05-05-025-surface-fit/`.
- [x] Task summaries truncated to 120 chars; no proprietary content captured.
