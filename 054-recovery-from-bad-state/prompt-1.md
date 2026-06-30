Copy the prompt below and paste it into Claude, ChatGPT, or your model of choice. The article linked from this directory's README explains what to expect.

````text
You are a recovery checklist builder. You operate read-only against the operator's home directory. You may write only inside the scratch directory created in Step 1. You may not modify any live file, install MCP servers, exfiltrate file contents, or read `*.env`, `*credentials*`, `*token*`, `*.key`, `*.pem`, `id_rsa*`, `id_ed25519*`, `/.ssh/`, or `/.gnupg/` paths.

**Step 1 — create scratch directory.** Run:

```bash
SCRATCH="$HOME/.claude/experiments/$(date +%Y-%m-%d)-054-recovery"
mkdir -p "$SCRATCH"
```

**Step 2 — inventory the operator's recoverability surface.** Identify:

- **Memory files** — paths, sizes, git-tracked yes/no.
- **Hooks** — files under `~/.claude/hooks/`, `.claude/hooks/`, with one-line descriptions of what each does.
- **Settings** — `~/.claude/settings.json`, `~/.claude/settings.local.json`, project-local equivalents.
- **Scratch directories** — `~/.claude/experiments/` recent contents.
- **Repository state** — any `.git/` near the operator's working directory; whether memory files are in a git repo.
- **Snapshots** — any backup directories, time-machine targets, or other recovery sources the operator has set up.

Write to `$SCRATCH/00-surface.md`.

**Step 3 — produce the loop-recovery procedure.** Conversation loops happen when the model is repeating itself or making no progress; the recovery is to start a fresh thread with a handoff. Write `$SCRATCH/01-loop-recovery.md` with:

1. **Detect** — symptom checklist (same error 3+ times, output unchanged across 5 turns, growing token cost without progress).
2. **Save forward** — produce a handoff document at `$SCRATCH/handoff-<topic>.md` capturing what was attempted, what failed, and what the next session should try (cross-reference Article 055).
3. **End the thread** — exit the current Claude Code session.
4. **Start fresh** — open a new session with the handoff document as the first input.

**Step 4 — produce the memory-contamination recovery procedure.** Memory contamination is when memory files have accumulated wrong facts. Write `$SCRATCH/02-memory-recovery.md` with:

1. **Detect** — symptom checklist (model confidently asserting wrong facts, references to deleted paths, references to retired tools).
2. **Audit** — run Article 036's drift detection prompt to identify stale claims.
3. **Stage corrections** — Article 036 Prompt 2 stages patches in scratch.
4. **Apply** — operator applies the patches by hand after reading the diff.
5. **Roll back path** — git checkout / restore from backup if a patch turns out to be wrong.
6. **Re-recall** — once memory is fixed, run a memory_recall to confirm clean retrieval.

**Step 5 — produce the hook-misbehavior recovery procedure.** Hooks misbehaving show up as session-start failures, weird auto-injected text, or unexpected behavior on tool calls. Write `$SCRATCH/03-hook-recovery.md` with:

1. **Detect** — symptom checklist (session-start hook errors visible in output, unexplained text in MEMORY.md, tool-call hooks producing surprising side effects).
2. **Disable temporarily** — `mv ~/.claude/hooks/<hook>.sh ~/.claude/hooks/<hook>.sh.disabled` (operator's specific path).
3. **Restart session** — confirm symptom resolved.
4. **Diagnose** — read the hook's logs, recent edits, and dependencies.
5. **Fix or replace** — repair the hook or write a stub.
6. **Re-enable** — `mv` back; confirm normal operation.

**Step 6 — produce the consolidated recovery card.** Write `$SCRATCH/00-RECOVERY.md` as a single-page card the operator can print or pin: three failure shapes, three recovery procedures, key commands per procedure, and an "if all else fails" section pointing at scratch backups, git history, and the operator's manual snapshots. Print to stdout.
````
