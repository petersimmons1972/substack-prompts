# Article 028 — Anti-patterns Audit Smoke Test

**Date:** 2026-05-06
**Verdict:** PASS

## PASS criteria check

- Prompt 1 produced `00-FINDINGS.md` with 6 finding rows (2 present, 4 absent). PASS.
- Prompt 2 produced `10-PLAN.md` with target file `/home/psimmons/.claude/settings.json` and expected delta `broad_wildcard_rules: 6 → 5`. PASS.

## Deliverables produced

| Deliverable | Path | Status |
|---|---|:-:|
| Findings table | `00-FINDINGS.md` | OK |
| Bloat table | `A1-bloat.md` | OK |
| Secrets scan | `A2-secrets.md` | OK |
| Undo-discipline audit | `A3-undo.md` | OK |
| Permissions audit | `A4-permissions.md` | OK |
| Model-selection audit | `A5-model-selection.md` | OK |
| Baseline snapshot | `00-baseline-snapshot.md` | OK |
| Remediation target | `10-target.md` | OK |
| Backup verification | `11-backup-verified.md` | OK |
| Proposed replacement | `12-proposed-settings.json` | OK |
| Diff | `13-diff.md` | OK |
| Undo script (executable) | `14-undo.sh` | OK |
| Remediation plan | `10-PLAN.md` | OK |

## Steps failed or skipped

None. All 8 Prompt 1 steps and all 6 Prompt 2 steps completed.

Notes / minor observations:
- `~/.claude/CLAUDE.md` is absent (Prompt 1 Step 3 set covers four files; only three exist). Reported as MISSING in `A1-bloat.md`, not flagged as failure.
- The proposed `12-proposed-settings.json` has two cosmetic regressions vs the live file: a unicode arrow re-encoded as `→` and a missing trailing newline. Called out in `10-PLAN.md` so the human applier can patch them on review. Not load-bearing for the smoke test.
- Live config files were not modified. Backup byte-count verified equal to live.

## 00-FINDINGS.md contents

```
# 00 — Ranked Findings

Score = blast_radius * ease_of_fix. Sorted descending.

| id | anti_pattern | present | blast_radius | ease_of_fix | score | evidence_file |
|---|---|:-:|:-:|:-:|:-:|---|
| A4 | Wildcard / shell-wide permissions (bare `Bash` grant + 10 trailing wildcards) | Y | 5 | 4 | 20 | A4-permissions.md |
| A1 | Bloated memory file (`~/CLAUDE.md` 2550 tokens, >2500 threshold) | Y | 3 | 4 | 12 | A1-bloat.md |
| A0 | Baseline missing | N | 0 | 0 | 0 | (baseline present) |
| A2 | Secrets in memory files | N | 0 | 0 | 0 | A2-secrets.md |
| A3 | Missing undo discipline | N | 0 | 0 | 0 | A3-undo.md |
| A5 | Absent model-selection guidance | N | 0 | 0 | 0 | A5-model-selection.md |

**Top finding: A4 — Wildcard permissions.** Bare `Bash` allow rule grants shell-wide execution authority; pair with 10 trailing-wildcard rules including broad MCP namespace grants. Highest leverage fix.
```

## 10-PLAN.md contents

```
# 10 — Remediation Plan

- **Target file:** `/home/psimmons/.claude/settings.json`
- **Anti-pattern:** A4 — Wildcard / shell-wide permissions
- **Backup:** `backup-20260506-183110-settings.json` (8138 bytes, byte-count verified)
- **Proposal:** `12-proposed-settings.json`
- **Diff:** `13-diff.md`
- **Undo:** `14-undo.sh`

## What changes

The bare `Bash` allow rule grants shell-wide execution authority to every command. The proposal replaces it with five narrowly scoped allowances (`Bash(git status)`, `Bash(git diff *)`, `Bash(git log *)`, `Bash(ls *)`, `Bash(cat *)`) covering the common read-only Bash operations the user actually performs. All other commands fall back to the auto-prompt flow. Trailing-wildcard MCP rules (`mcp__github__*`, etc.) are preserved — they are scoped to a single MCP server's tool surface and not equivalent to `Bash(*)`.

## Apply command (manual review required)

```bash
cp -p "/home/psimmons/.claude/experiments/2026-05-06-028-anti-patterns/12-proposed-settings.json" "/home/psimmons/.claude/settings.json"
```

Review `13-diff.md` first. The diff also shows a unicode escape (`→` becoming `→`) introduced by JSON re-serialization; that is cosmetic but worth a manual edit-back to `→` if preferred. There is also a trailing-newline regression — restore the trailing newline after applying.

## Undo

```bash
/home/psimmons/.claude/experiments/2026-05-06-028-anti-patterns/14-undo.sh
```

## Expected delta in next baseline run

- `broad_wildcard_rules`: drop by 1 (the bare `Bash` rule). Article 023 baseline: 6 → 5.
- `allow_rules`: rises from 29 → 33 (replacing one shell-wide rule with five scoped rules); this is intentional — count goes up, blast radius goes down.
- `memory_files_total_tokens`: unchanged.
- `secrets_indicator_hits`: unchanged.

If `broad_wildcard_rules` does not drop after applying, run `14-undo.sh` and re-investigate.
```
