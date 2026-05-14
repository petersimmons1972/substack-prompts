# Baseline Prompt — Dry-Run Reference

**Run on:** 2026-05-05 (Opus 4.7, 1M context)
**Environment:** Linux 6.18.7, bash 5.x, Claude Code session, cwd=`$HOME`
**Status:** ✅ All 7 steps produced output. Undo verified clean.

This is the canonical worked example for Article 023. Use it during Phase 3 drafting as the "what the reader will see" reference. The numbers below describe the operator's environment on the date above; they are illustrative, not generic.

---

## 00-BASELINE.md (final summary)

```
baseline_date: 2026-05-05
memory_files_total_tokens: 2997
memory_files_count: 3
skills_count: 12
hooks_count: 23
allow_rules: 29
broad_wildcard_rules: 6
secrets_indicator_hits: 0
```

## 01-memory-inventory.md (excerpt)

| Path | Bytes | Lines | Words | ~Tokens | Modified |
|---|---|---|---|---|---|
| ~/CLAUDE.md | 13531 | 137 | 1912 | 2549 | 2026-05-04 |
| ~/.claude/projects/-home-psimmons/memory/MEMORY.md | 2721 | 64 | 336 | 448 | 2026-05-05 |
| ~/AGENTS.md | 2035 | 14 | 285 | 380 | 2026-05-05 |
| (cwd) CLAUDE.md | 4239 | 69 | 608 | 811 | 2026-04-27 |

## 02-skill-hook-inventory.md (counts only)

- 12 skills installed (`adversarial-source-check`, `analyzing-companies`, `bench`, `dispatching-parallel-agents`, `github-docs`, `impeccable`, `linkedin-content`, `memory-cleanup`, `status`, `ui-ux-pro-max`, `visual-output-standards`, `write`).
- 23 hook scripts on disk under `~/.claude/hooks/`.

## 03-permission-surface.md

- Allow rules: 29
- Deny rules: 19
- Ask rules: 0
- Wildcard rules: 6
- Configured hooks: PostToolUse, PreCompact, PreToolUse, SessionStart, Stop, UserPromptSubmit

## 04-secrets-indicators.md

Zero hits across `~/CLAUDE.md`, `~/.claude/CLAUDE.md` (absent), `~/.claude/projects/-home-psimmons/memory/MEMORY.md`. Operator memory files are clean.

## 05-context-budget.md

- `~/CLAUDE.md`: 2549 tokens
- `~/.claude/projects/-home-psimmons/memory/MEMORY.md`: 448 tokens
- **Total memory-file tokens at session start: 2997**

## Undo verified

```
$ rm -rf "$HOME/.claude/experiments/$(date +%Y-%m-%d)-baseline"
$ ls -la ~/.claude/experiments/
total 8
drwxrwxr-x  2 psimmons psimmons 4096 May  5 10:51 .
drwx------ 28 psimmons psimmons 4096 May  5 10:50 ..
```

State fully restored.

---

## Refinements identified during dry-run (apply in Phase 2 prompt revision)

1. **Default-load semantics depend on cwd.** The prompt currently says "files that load by default" without specifying the working directory. Phase 2 revision: instruct the model to enumerate which files load given the *current* cwd, since project-scoped `CLAUDE.md` only loads inside that project.
2. **Distinguish active vs inactive skills.** Skills directory may include a `bench/` subdirectory holding inactive skills that don't auto-load. Phase 2 revision: tag `bench/` and similar inactive containers separately in the count.
3. **Distinguish wired vs unwired hooks.** Hook script files on disk are not the same as hooks the harness actually invokes. Phase 2 revision: cross-reference hook scripts against `settings.json` `hooks` keys and report wired-count separately from disk-count.
4. **Wildcard semantics.** Currently counts rules ending in `*`; should also count rules with `**` and rules with mid-string globbing for completeness.

These refinements are quality-of-life, not blockers. The prompt as published produces a usable, comparable baseline today.
