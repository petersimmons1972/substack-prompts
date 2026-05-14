# Prompt 2 — Dry-Run Reference

**Run on:** 2026-05-05 (Opus 4.7, 1M context)
**Environment:** Linux 6.18.7, bash 5.x, Claude Code session
**Status:** All 5 steps produced output. Diff confirmed single-field delta. Undo verified clean. Live `~/CLAUDE.md` md5 unchanged across the entire dry-run.

---

## Inputs

`~/CLAUDE.md` cloned into `$SCRATCH/clean/CLAUDE.md` (13,531 bytes, 137 lines, 1,912 words). The bloated copy is the clean clone plus the 412-word "Notes on consistency and craft" paragraph from Step 2.

## diff between clean and bloated

```
$ diff -q $SCRATCH/clean/CLAUDE.md $SCRATCH/bloated/CLAUDE.md
Files differ
$ wc -l $SCRATCH/clean/CLAUDE.md $SCRATCH/bloated/CLAUDE.md
  137 .../clean/CLAUDE.md
  140 .../bloated/CLAUDE.md
$ wc -w $SCRATCH/clean/CLAUDE.md $SCRATCH/bloated/CLAUDE.md
 1912 .../clean/CLAUDE.md
 2324 .../bloated/CLAUDE.md
```

Word delta: **+412**. Line delta: **+3** (heading + blank + paragraph).

## clean/00-BASELINE.md

```
baseline_date: 2026-05-05
memory_files_total_tokens: 3243
memory_files_count: 4
skills_count: 24
hooks_count: 11
allow_rules: 29
broad_wildcard_rules: 10
secrets_indicator_hits: 0
```

## bloated/00-BASELINE.md

```
baseline_date: 2026-05-05
memory_files_total_tokens: 3793
memory_files_count: 4
skills_count: 24
hooks_count: 11
allow_rules: 29
broad_wildcard_rules: 10
secrets_indicator_hits: 0
```

## 00-DELTA.md

| field | clean | bloated | delta |
|---|---|---|---|
| memory_files_total_tokens | 3,243 | 3,793 | **+550** |
| memory_files_count | 4 | 4 | 0 |
| skills_count | 24 | 24 | 0 |
| hooks_count | 11 | 11 | 0 |
| allow_rules | 29 | 29 | 0 |
| broad_wildcard_rules | 10 | 10 | 0 |
| secrets_indicator_hits | 0 | 0 | 0 |

Expected delta from Article 021's words/0.75 ratio: `ceil(412/0.75)` = **550**. Observed: **550**. The estimate is consistent; the baseline measures what it claims to measure.

## Notable result

Exactly one field moved, by exactly the predicted amount. This is the proof of correctness for the baseline: it is content-derived, deterministic, and scoped to the file inputs. Any later article that claims a context-savings win should produce a corresponding decrease in `memory_files_total_tokens` of similar magnitude per word removed. The B0 flag was not raised; the operator already has `~/CLAUDE.md` in place.

## Undo verified

```
$ md5sum $HOME/CLAUDE.md   # before
<hash-A>  /home/psimmons/CLAUDE.md
$ rm -rf "$HOME/.claude/experiments/2026-05-05-023-bloat-delta"
$ md5sum $HOME/CLAUDE.md   # after
<hash-A>  /home/psimmons/CLAUDE.md
$ ls "$HOME/.claude/experiments/" | grep 023-bloat || echo "(absent)"
(absent)
```

UNDO VERIFIED: `rm -rf "$HOME/.claude/experiments/$(date +%Y-%m-%d)-023-bloat-delta"` — live `~/CLAUDE.md` md5 identical before and after.

## Security-floor self-check

- [x] Did not exfiltrate file contents to any network endpoint.
- [x] Did not read `.env`, credentials, tokens, keys, or `.ssh`/`.gnupg` paths.
- [x] Read `~/CLAUDE.md` only to copy it into scratch; never wrote to the original.
- [x] Did not modify `~/.claude/settings.json`, `~/.claude/CLAUDE.md`, `MEMORY.md`, or `~/AGENTS.md`.
- [x] Did not install MCP servers or change hook configuration.
- [x] All writes confined to `$HOME/.claude/experiments/2026-05-05-023-bloat-delta/`.
- [x] Secrets-indicator scan output: 0 hits in both runs (consistent with baseline-prompt's behavior).
