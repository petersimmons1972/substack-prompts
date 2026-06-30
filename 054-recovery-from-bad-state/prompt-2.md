Copy the prompt below and paste it into Claude, ChatGPT, or your model of choice. The article linked from this directory's README explains what to expect.

````text
You are a recovery-drill runner. You operate read-only against the operator's live environment for the *initial copy* into scratch. After that, all damage and all recovery happens inside the scratch directory used by Prompt 1. **You may not corrupt, modify, or remove any live file. You may not disable any live hook. The drill is sandboxed; the operator's working environment is unchanged at every step.** You may not exfiltrate file contents, install MCP servers, or read `*.env`, `*credentials*`, `*token*`, `*.key`, `*.pem`, `id_rsa*`, `id_ed25519*`, `/.ssh/`, or `/.gnupg/` paths.

**Step 1 — locate scratch and copy a baseline.** Run:

```bash
SCRATCH="$HOME/.claude/experiments/$(date +%Y-%m-%d)-054-recovery"
test -f "$SCRATCH/00-RECOVERY.md" || { echo "ERROR: run prompt-1 first"; exit 1; }
mkdir -p "$SCRATCH/drill/baseline" "$SCRATCH/drill/damaged" "$SCRATCH/drill/recovered"
cp -p "$HOME/CLAUDE.md" "$SCRATCH/drill/baseline/"
cp -p "$HOME/.claude/projects/-home-psimmons/memory/MEMORY.md" "$SCRATCH/drill/baseline/" 2>/dev/null || true
# Copy hook bodies as plain files (do not run them):
cp -p "$HOME/.claude/hooks/"*.sh "$SCRATCH/drill/baseline/" 2>/dev/null || true
```

**Step 2 — drill 1: simulated memory contamination.** Copy the baseline files into `damaged/`. Damage the copy by inserting three plausible-looking but stale claims into `damaged/MEMORY.md` (e.g., "the cluster has 12 nodes" when the live count is different; "the deploy script is `~/bin/old-deploy.sh`" pointing at a non-existent path). Each insertion is annotated with an HTML comment naming it as a drill artifact.

Run Prompt 1's `02-memory-recovery.md` procedure against `damaged/MEMORY.md`:

- Steps 1–2: detect and audit using the Article 036 drift-detection logic adapted to the scratch fixture.
- Step 3: stage corrections in `recovered/MEMORY.md`.
- Steps 4–5: apply (in scratch) and verify.

Record results in `$SCRATCH/drill/10-drill1-results.md`: time elapsed, claims caught, claims missed, false-positives caught, recovery successful (yes/no).

**Step 3 — drill 2: simulated conversation loop.** No file mutation needed; this drill is procedural. Compose a plausible "loop transcript" at `$SCRATCH/drill/loop-transcript.md` (5 turns of repeated near-identical model output on a stuck task). Run Prompt 1's `01-loop-recovery.md` procedure: produce a handoff document at `$SCRATCH/drill/handoff.md` capturing the task, what was tried, and what to do next. Record the handoff size, time elapsed, and operator-readability score (subjective, 1–5). Write to `$SCRATCH/drill/11-drill2-results.md`.

**Step 4 — drill 3: simulated hook misbehavior.** Pick one of the operator's actual hooks (the smallest one — usually a SessionStart hook). Copy it into `damaged/` and apply a deliberate breakage (e.g., a syntax error in a comment) — *only on the scratch copy*, never on the live hook.

Run Prompt 1's `03-hook-recovery.md` procedure against the scratch copy:

- Detect the breakage by reading the file (do not execute it).
- Diagnose: trace the syntax error to its line.
- Fix in `recovered/`.
- Re-verify by re-reading; do not run the hook in scratch.

Record results in `$SCRATCH/drill/12-drill3-results.md`.

**Step 5 — produce the drill report.** Write `$SCRATCH/00-DRILL.md` with: per-drill outcome, time-to-recover, gaps in the checklist that the drill exposed, and one or two recommendations for tightening Prompt 1's procedures. Print to stdout.

**Step 6 — verify nothing live was touched.** Run a quick sanity check:

```bash
diff -q "$HOME/CLAUDE.md" "$SCRATCH/drill/baseline/CLAUDE.md" && echo "live CLAUDE.md unchanged"
diff -q "$HOME/.claude/projects/-home-psimmons/memory/MEMORY.md" \
        "$SCRATCH/drill/baseline/MEMORY.md" 2>/dev/null && echo "live MEMORY.md unchanged"
# for each hook:
for h in "$SCRATCH/drill/baseline/"*.sh; do
  live="$HOME/.claude/hooks/$(basename "$h")"
  diff -q "$live" "$h" 2>/dev/null && echo "live hook $(basename "$h") unchanged"
done
```

Record verification in `$SCRATCH/drill/13-live-unchanged.md`.
````
