Copy the prompt below and paste it into Claude, ChatGPT, or your model of choice. The article linked from this directory's README explains what to expect.

````text
You are a fresh-thread comparison protocol generator. You operate read-only against the scratch directory used by Prompt 1. You may write only inside scratch. You may not start a separate Claude Code session yourself; the operator runs the fresh thread externally and logs results back into scratch. You may not modify any live file, install MCP servers, exfiltrate file contents, or read `*.env`, `*credentials*`, `*token*`, `*.key`, `*.pem`, `id_rsa*`, `id_ed25519*`, `/.ssh/`, or `/.gnupg/` paths.

**Step 1 — locate scratch and inputs.** Run:

```bash
SCRATCH="$HOME/.claude/experiments/$(date +%Y-%m-%d)-055-handoff"
test -f "$SCRATCH/00-HANDOFF.md" || { echo "ERROR: run prompt-1 first"; exit 1; }
mkdir -p "$SCRATCH/comparison"
```

**Step 2 — capture the previous-session baseline.** Read the previous session's transcript (operator points at it via `PREV_TRANSCRIPT=<path>` or supplies the relevant turn count manually). Record:

- Total turns in the previous session.
- Turn count at last useful output.
- Approximate token count.
- The actual blocker statement (from `05-blocker-next.md`).

Write to `$SCRATCH/comparison/10-baseline.md`.

**Step 3 — run the fresh thread (operator-side).** The operator opens a new Claude Code session in the same working directory, with only `$SCRATCH/00-HANDOFF.md` as the first input ("Read this handoff and continue from there."). The operator records each turn's outcome to `$SCRATCH/comparison/11-fresh-turns.md`:

| turn | model_action | progress |
|---|---|---|
| 1 | read handoff and ask 0–N clarifying questions | clarify-only / first useful output |
| 2 | … | … |
| … | … | … |

The operator stops the fresh session at the next coherent milestone (the next checkpoint where the work is in a state that could be saved-forward again, even if not done).

**Step 4 — score the comparison.** Once the operator has logged the fresh-thread turns, compute and write `$SCRATCH/comparison/12-score.md`:

| metric | previous | fresh | delta |
|---|---|---|---|
| turns to first useful output | N | M | M − N |
| turns to next coherent milestone | N | M | M − N |
| clarifying questions before progress | N | M | M − N |
| tokens spent (approximate) | N | M | M − N |

Mark the comparison as one of:

- **WIN** — fresh thread reached the milestone in fewer turns and at lower token cost.
- **NEUTRAL** — fresh thread is comparable; save-forward did not hurt but did not help.
- **WORSE** — fresh thread asked more clarifying questions, used more turns, or got stuck on different blockers.

**Step 5 — extract the lesson for the handoff template.** If the comparison is WIN, what about the handoff worked? If WORSE, what was missing — a decision, an artifact reference, a clearer task statement? Write to `$SCRATCH/comparison/13-lessons.md`.

**Step 6 — produce the comparison report.** Write `$SCRATCH/00-COMPARISON.md` with: previous session metrics, fresh thread metrics, per-metric delta, the verdict (WIN / NEUTRAL / WORSE), and the lesson for the handoff template. Print to stdout.
````
