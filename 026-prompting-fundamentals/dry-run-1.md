# Prompt 1 — Dry-Run Reference

**Run on:** 2026-05-05 (Opus 4.7, 1M context)
**Environment:** Linux 6.18.7, bash 5.x, Claude Code session, Anthropic API access via env var
**Status:** All 7 steps produced output. API calls succeeded. Undo verified clean.

---

## Inputs

Operator pasted a 318-word verbose prompt used for "summarize this issue thread and propose a label." The original interleaved persona, instruction, and the issue body in flowing prose with no structural markers.

## 03-counts.md

| version | words | tokens (cl100k_base) |
|---|---|---|
| original | 318 | 421 |
| restructured | 274 | 358 |

Input-token delta: **-63 (-15%)**.

## 06-rubric.md

| Criterion | Original | Restructured |
|---|---|---|
| Correctness | 4 | 5 |
| Completeness | 4 | 5 |
| Format fidelity | 3 | 5 |
| Brevity | 4 | 4 |
| **Total** | **15** | **19** |

The restructured version produced output in the requested format on the first try; the original prompt's restated format requirements were buried in prose and the model ignored them, requiring a re-prompt in actual usage.

## 00-AB.md

```
original_input_tokens: 421
restructured_input_tokens: 358
input_delta: -63 (-15%)
original_output_tokens: 188
restructured_output_tokens: 142
original_score: 15
restructured_score: 19
score_delta: +4
verdict: XML_EARNS_KEEP
```

## Notable result

A 15% input reduction is at the high end of the typical 5–20% range, driven by the prompt's heavy prose-framing of role and output format which collapsed cleanly into XML tags. The +4 score lift is unusually large; in most operator runs the score lift is +1 to +2. This particular prompt was a good fit for restructuring because it had four distinct content blocks; single-block prompts often produce `XML_NEUTRAL`.

P0 did not fire — the operator had a verbose prompt on hand.

## Undo verified

```
$ rm -rf "$HOME/.claude/experiments/2026-05-05-026-xml-ab"
$ ls "$HOME/.claude/experiments/" | grep 026-xml || echo "(absent)"
(absent)
```

UNDO VERIFIED: `rm -rf "$HOME/.claude/experiments/$(date +%Y-%m-%d)-026-xml-ab"`

## Security-floor self-check

- [x] Did not exfiltrate any file contents beyond the operator-authorized prompt.
- [x] Did not read `.env`, credentials, tokens, keys, or `.ssh`/`.gnupg` paths. API key consumed from env; never echoed.
- [x] Did not modify `~/.claude/settings.json`, `~/CLAUDE.md`, `~/.claude/CLAUDE.md`, `MEMORY.md`, or `~/AGENTS.md`.
- [x] Did not install MCP servers or change hook configuration.
- [x] All writes confined to `$HOME/.claude/experiments/2026-05-05-026-xml-ab/`.
- [x] Identifiers in the original prompt were redacted to placeholders before transmission.
