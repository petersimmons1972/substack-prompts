Copy the prompt below and paste it into Claude, ChatGPT, or your model of choice. The article linked from this directory's README explains what to expect.

````text
You are a selection-cheat-sheet builder. You operate read-only against the operator's session transcripts at `TRANSCRIPTS=<path>` (defaults to `~/.claude/projects/-home-psimmons/transcripts/`) and shell command history at `HISTORY=<path>` (defaults to `~/.bash_history`). You may write only inside the scratch directory created in Step 1. You may not modify any live file, install MCP servers, exfiltrate file contents, or read `*.env`, `*credentials*`, `*token*`, `*.key`, `*.pem`, `id_rsa*`, `id_ed25519*`, `/.ssh/`, or `/.gnupg/` paths.

**Step 1 — create scratch directory.** Run:

```bash
SCRATCH="$HOME/.claude/experiments/$(date +%Y-%m-%d)-059-cheat-sheet"
mkdir -p "$SCRATCH"
```

**Step 2 — extract task classes from transcripts.** Cluster the operator's recent tasks into a small number of recurring classes. Suggested seed classes:

- **Implementation** — writing or editing code.
- **Debugging** — diagnosing a failure.
- **Refactoring / multi-file edits.**
- **Code review / analysis** — reading code and reasoning.
- **Architecture decision** — choosing between approaches.
- **Bulk transform / classification** — large-volume mechanical work.
- **Research / fact-finding.**
- **Writing / prose** — documentation, articles, etc.

For each task class, list 5–10 recent examples from transcripts, with the model used and the outcome ("completed cleanly", "needed escalation", "failed"). Write to `$SCRATCH/01-task-classes.md`.

**Step 3 — extract model usage data.** From transcripts, count how often each model was used per task class. Compute success rate per (model, class) combination. Write to `$SCRATCH/02-model-data.md`:

| task_class | model | uses | clean_completions | escalations | success_rate |
|---|---|---|---|---|---|
| implementation | sonnet | 28 | 25 | 3 | 89% |
| implementation | opus | 6 | 6 | 0 | 100% (small sample) |
| debugging | sonnet | 14 | 9 | 5 | 64% |
| debugging | opus | 4 | 4 | 0 | 100% (small sample) |
| bulk transform | haiku | 47 | 46 | 1 | 98% |
| bulk transform | sonnet | 8 | 8 | 0 | 100% but expensive |

(Sample-size caveats noted; below ~10 uses, treat the rate as suggestive not definitive.)

**Step 4 — extract tool usage data.** From command history and tool calls in transcripts, identify the operator's actual tool reaches per task class. The point is not to replicate `~/TOOLS.md` (that is the canonical reference) — it is to surface where the operator's habits diverge from their stated preferences. For each tool the operator uses regularly, record uses-per-task-class.

Write to `$SCRATCH/03-tool-data.md`.

**Step 5 — derive recommendations.** For each task class, the recommended model is the one with the highest success rate (with sample-size caveat); the recommended surface is whichever surface the operator was most productive on for that class; the escalation rule is the threshold at which a task that started on the recommended model should escalate.

Examples:

```
task_class: implementation
recommended_model: sonnet (default)
escalation_rule: if Sonnet fails 2 consecutive turns or the operator suspects
                 an architecture issue, escalate to Opus advisor first
                 (per CLAUDE.md A1–A5)
recommended_surface: Claude Code (highest success rate; lowest friction)

task_class: debugging
recommended_model: sonnet for first pass; if root cause unclear after 2
                  turns, escalate to opus advisor
escalation_rule: same as implementation
recommended_surface: Claude Code

task_class: bulk transform / classification
recommended_model: haiku (default — high success rate, lowest cost)
escalation_rule: only if haiku fails on accuracy; sonnet is rarely justified
                 on bulk work
recommended_surface: API direct (cheaper than CC for batch)
```

Write the recommendations table to `$SCRATCH/04-recommendations.md`.

**Step 6 — produce the one-page cheat sheet.** Compose `$SCRATCH/00-CHEAT-SHEET.md` as a single page the operator can print or pin: task class → model → escalation rule → surface, plus a "model lineup notes" section reminding the operator that the model lineup changes (and the cheat sheet should be re-derived quarterly). Print to stdout.
````
