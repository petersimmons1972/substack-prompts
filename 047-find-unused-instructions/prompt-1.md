Copy the prompt below and paste it into Claude, ChatGPT, or your model of choice. The article linked from this directory's README explains what to expect.

````text
You are an unused-rule auditor. You operate read-only against `~/CLAUDE.md` and the operator's session transcripts at the path supplied via `TRANSCRIPTS=<path>` (defaults to `~/.claude/projects/-home-psimmons/transcripts/` if present, otherwise `~/.claude/logs/`). You may write only inside the scratch directory created in Step 1. You may not exfiltrate file contents, modify any live file, install MCP servers, or read `*.env`, `*credentials*`, `*token*`, `*.key`, `*.pem`, `id_rsa*`, `id_ed25519*`, `/.ssh/`, or `/.gnupg/` paths.

**Step 1 — create scratch directory.** Run:

```bash
SCRATCH="$HOME/.claude/experiments/$(date +%Y-%m-%d)-047-unused"
mkdir -p "$SCRATCH"
```

**Step 2 — extract the rule inventory.** Walk `~/CLAUDE.md` and produce `$SCRATCH/01-rules.md` with one row per rule: `id`, `text` (≤120 chars), `category`, `trigger_signature`. The trigger signature is one or more grep-able patterns that should appear in a session transcript when the rule fires. Examples:

| rule | trigger_signature |
|---|---|
| "use xh not curl" | `xh ` or `curl ` in a tool call |
| "engram recall at start" | `memory_recall` MCP call near session start |
| "git status before write op" | `git status` followed by an Edit/Write within 5 turns |
| "filed Issue on bug discovery" | `gh issue create` after a discovered defect mention |

If a rule's trigger signature cannot be expressed in a small set of grep patterns, mark `signature=heuristic` and supply a textual description; the cross-check will be best-effort for those rules.

**Step 3 — collect transcripts.** List `$TRANSCRIPTS/*.jsonl` (or whatever extension matches), filter to the last 30 days. Record paths, byte sizes, and approximate turn counts. Write to `$SCRATCH/02-transcripts.md`. If no transcripts exist, fall back to scanning `~/.claude/projects/*/memory/*.md` for traces of past runs and warn the operator that confidence will be lower.

**Step 4 — match rules to transcript firings.** For each rule, run its grep patterns over the transcript set. Record `firings` (how many distinct sessions matched the trigger). Write to `$SCRATCH/03-firings.md`: `rule_id`, `signature`, `firings`, `last_fired_session`, `verdict`.

Verdicts:

- **ACTIVE** — fired ≥ 3 times in the last 30 days.
- **INFREQUENT** — fired 1–2 times in the last 30 days.
- **UNUSED-CANDIDATE** — fired 0 times in the last 30 days **and** the trigger signature is not heuristic. (Heuristic-trigger rules with 0 firings are kept and tagged `UNVERIFIABLE` instead.)
- **UNVERIFIABLE** — trigger signature is heuristic or transcripts are missing; cannot be assessed.

**Step 5 — surface the false-positive guard.** For each `UNUSED-CANDIDATE`, scan `~/CLAUDE.md` itself for cross-references *to* the rule (e.g., another rule says "see X" pointing at this rule). Cross-referenced rules are recorded as `UNUSED-CANDIDATE-CROSSREF` and downgraded to `INFREQUENT` for review purposes — they may not fire directly but they support other rules.

**Step 6 — produce the unused-rule report.** Write `$SCRATCH/00-UNUSED.md` with: total rules, count per verdict, top 10 unused candidates ranked by byte cost (longer rules cost more to retain), and per-candidate notes. Print to stdout. The report does not propose removals — Prompt 2 stages those after a behavioral verification step.
````
