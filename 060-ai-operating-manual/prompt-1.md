Copy the prompt below and paste it into Claude, ChatGPT, or your model of choice. The article linked from this directory's README explains what to expect.

````text
You are a manual assembler. You operate read-only against the operator's home directory and the scratch directories from prior articles in the series. You may write only inside the scratch directory created in Step 1. You may not modify any live file, install MCP servers, exfiltrate file contents, or read `*.env`, `*credentials*`, `*token*`, `*.key`, `*.pem`, `id_rsa*`, `id_ed25519*`, `/.ssh/`, or `/.gnupg/` paths.

**Step 1 — create scratch directory.** Run:

```bash
SCRATCH="$HOME/.claude/experiments/$(date +%Y-%m-%d)-060-manual"
mkdir -p "$SCRATCH/manual"
```

**Step 2 — collect the source artifacts.** Locate the following from prior series scratch directories and operator's environment. Each is required; missing artifacts are flagged and the manual is assembled with placeholders + a TODO file naming the gaps.

| artifact | source | required |
|---|---|---|
| tuned `~/CLAUDE.md` | live ~/CLAUDE.md (post-Article 046 compression and 047 cleanup) | yes |
| tuned `~/AGENTS.md` | live ~/AGENTS.md (post-Article 043 split, 049 contract review) | yes |
| Article 023 baseline measurement script | $HOME/.claude/experiments/baseline-original.md or operator-stored copy | yes |
| permission baseline (post-Article 050) | live ~/.claude/settings.json | yes |
| selection cheat sheet (Article 059) | $HOME/.claude/experiments/<date>-059-cheat-sheet/00-CHEAT-SHEET.md | yes |
| personal CLAUDE.md library (Article 058) | $HOME/library/ if migrated, else $SCRATCH (058)/library/ | yes (or note migration pending) |
| convention-loop template (Article 048) | derived from Article 048 prompts | suggested |
| recovery card (Article 054) | $HOME/.claude/experiments/<date>-054-recovery/00-RECOVERY.md | suggested |
| injection-mitigation checklist (Article 052) | the 6-item checklist or its install location in CLAUDE.md | suggested |
| privacy posture (Article 053) | $SCRATCH (053)/00-CHANGES.md (per-surface change-list with current state) | suggested |

Record the inventory in `$SCRATCH/00-sources.md` with location and presence verdict.

**Step 3 — assemble the manual structure.** Create the manual directory layout:

```
manual/
├── README.md                  — overview, version, how to use
├── 00-claude-md.md             — tuned ~/CLAUDE.md (canonical version)
├── 01-agents-md.md             — tuned ~/AGENTS.md (canonical version)
├── 02-library/                  — personal CLAUDE.md library (from Article 058)
│   ├── 01-defaults.md
│   ├── 02-tools.md
│   ├── 03-security.md
│   ├── 04-pre-flight.md
│   ├── 05-engram-or-memory.md
│   ├── 06-cost-guardrails.md
│   └── 07-personal.md
├── 03-baseline.md              — Article 023 baseline measurement script + last results
├── 04-permission-baseline.json — sanitized permissions snapshot (no secrets)
├── 05-cheat-sheet.md           — Article 059 cheat sheet
├── 06-recovery-card.md         — Article 054 one-page recovery
├── 07-injection-checklist.md   — Article 052 mitigation checklist
├── 08-privacy-posture.md       — Article 053 per-surface posture record
├── 09-convention-loop.md       — Article 048 template for adding new rules
└── 99-revision-log.md          — version history of this manual
```

Copy each source artifact into its location. Sanitize `04-permission-baseline.json` (remove any per-machine local paths or operator-identifying entries that are not portable; replace with `<USER>`-style placeholders).

**Step 4 — write `manual/README.md`.** A short overview, ≤500 words, covering:

- What this manual is (the operator's personal AI operating system).
- How to use it on a new machine (clone repo, symlink relevant files into `~/`).
- How to maintain it (re-run the series prompts quarterly; revise the relevant sections).
- What is *not* in the manual (project-specific memory files; those stay per-repo).

**Step 5 — produce the gap report.** If any required source artifact was missing or partial in Step 2, list the gaps in `$SCRATCH/01-gaps.md`. The manual is still assembled with placeholders for the missing pieces; the gap report is the operator's TODO list.

**Step 6 — produce the assembly report.** Write `$SCRATCH/00-MANUAL.md` with: the manual directory listing, source inventory, gaps (if any), total bytes/lines, and a one-paragraph "ready to version" note. Print to stdout. Do not initialize a git repo or copy the manual outside scratch.
````
