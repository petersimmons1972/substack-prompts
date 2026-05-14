# Prompt 1 — Dry-Run Reference

**Run on:** 2026-05-05 (Opus 4.7, 1M context)
**Environment:** Linux 6.18.7, bash 5.x, Claude Code session, cwd=`~/projects/substack`
**Status:** All 8 steps produced output. Undo verified clean.

This is the worked example for Article 028 Prompt 1. Numbers describe the operator's environment on the date above; they are illustrative.

---

## 00-FINDINGS.md (final ranked table)

| id | anti_pattern | present | blast_radius | ease_of_fix | score | evidence_file |
|---|---|---|---|---|---|---|
| A4 | wildcard permissions | Y | 4 | 4 | 16 | A4-permissions.md |
| A1 | bloated memory files | Y | 3 | 5 | 15 | A1-bloat.md |
| A0 | baseline missing | Y | 2 | 5 | 10 | 00-baseline-snapshot.md |
| A2 | secrets in memory files | N | 5 | 3 | 0 | A2-secrets.md |
| A3 | undo discipline | N | 3 | 4 | 0 | A3-undo.md |
| A5 | model selection | N | 2 | 4 | 0 | A5-model-selection.md |

## A1 — Bloat (excerpt)

| Path | Bytes | Lines | Words | ~Tokens |
|---|---|---|---|---|
| ~/CLAUDE.md | 13531 | 137 | 1912 | 2549 |
| ~/.claude/CLAUDE.md | (absent) | - | - | - |
| ~/.claude/projects/-home-psimmons/memory/MEMORY.md | 1912 | 53 | 236 | 314 |
| ~/AGENTS.md | 2035 | 14 | 285 | 380 |

Total memory-file tokens: **3243**. Single flag: `~/CLAUDE.md` exceeds the 2,500-token threshold (~2,549).

## A2 — Secrets

Zero indicator hits across the four memory files. Operator memory is clean.

## A3 — Undo discipline

`~/CLAUDE.md`: 4 undo-keywords against 15 imperatives — within tolerance, no flag.
`MEMORY.md`: 1 undo-keyword, 0 imperatives — informational file, no flag.
`AGENTS.md`: 2 undo-keywords, 5 imperatives — borderline, no flag.

## A4 — Permission surface

- allow rules: 29
- deny rules: 19
- ask rules: 0
- wildcard rules (ending `*`): 10
- `Bash(*)` shell-wide grants: 0
- configured hook keys: 6
- **FLAG:** high wildcard count (10).

## A5 — Model selection

`~/CLAUDE.md` contains 9 model/tier references (Haiku/Sonnet/Opus tier rules in the Advisory Protocol section). A5 absent — this operator already encodes model-selection discipline.

## Notable result

The top finding is **A4 wildcard permissions** at score 16 — ten allow-rules ending in `*` against a clean secrets surface and present-but-bounded bloat. The audit correctly identifies the highest-leverage fix: tighten broad permission grants. This is the kind of insight the reader cannot get from documentation alone — it requires inspecting their own `settings.json`.

## Undo verified

```
$ rm -rf "$HOME/.claude/experiments/2026-05-05-028-smoke"
$ ls "$HOME/.claude/experiments/"
(empty)
```

UNDO VERIFIED: `rm -rf "$HOME/.claude/experiments/$(date +%Y-%m-%d)-028-anti-patterns"`

State fully restored. No file outside the scratch directory was modified.

## Security-floor self-check

- [x] Did not exfiltrate file contents to any network endpoint.
- [x] Did not read `.env`, credentials, tokens, keys, or `.ssh`/`.gnupg` paths.
- [x] Did not modify `~/.claude/settings.json` (read-only via `jq`).
- [x] Did not modify `~/CLAUDE.md`, `~/.claude/CLAUDE.md`, `MEMORY.md`, or `~/AGENTS.md`.
- [x] Did not install MCP servers or change hook configuration.
- [x] All writes confined to `$HOME/.claude/experiments/2026-05-05-028-smoke/`.
- [x] Secrets scan output contained redacted previews only — no full matches displayed (and zero hits in this environment).
