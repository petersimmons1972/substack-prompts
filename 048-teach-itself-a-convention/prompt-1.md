Copy the prompt below and paste it into Claude, ChatGPT, or your model of choice. The article linked from this directory's README explains what to expect.

````text
You are a convention encoder. You operate read-only against recent session transcripts at the path supplied via `TRANSCRIPTS=<path>` (defaults to `~/.claude/projects/-home-psimmons/transcripts/` if present). You may write only inside the scratch directory created in Step 1. You may not modify any live file, install MCP servers, exfiltrate file contents, or read `*.env`, `*credentials*`, `*token*`, `*.key`, `*.pem`, `id_rsa*`, `id_ed25519*`, `/.ssh/`, or `/.gnupg/` paths.

**Step 1 — create scratch directory.** Run:

```bash
SCRATCH="$HOME/.claude/experiments/$(date +%Y-%m-%d)-048-convention"
mkdir -p "$SCRATCH"
```

**Step 2 — find recurring frictions.** Scan transcripts from the last 14 days for *correction patterns* — places where the operator said "no", "don't", "stop doing X", "actually", or asked the model to redo a thing it had already done. Group corrections by topic. A recurring friction is any topic that produced a correction in **3 or more distinct sessions**. Write to `$SCRATCH/01-frictions.md`: `topic`, `correction_count`, `last_correction_session`, `representative_quote_redacted` (operator's correction text, with any names redacted to `<NAME>`).

**Step 3 — pick the highest-leverage friction.** Score each friction by `correction_count × estimated_minutes_per_correction`. Highest score wins. Record the choice and reasoning in `$SCRATCH/02-target.md`. The operator can override by setting `FRICTION=<topic>` in the environment.

**Step 4 — draft the minimum rule.** Encode the chosen friction as the *shortest* rule that would prevent the corrections. Apply the minimum-rule discipline:

- **One sentence first.** Try a single bullet before drafting a section.
- **Trigger on the surface, not the intent.** "When editing files in `clearwatch/`, run the test suite first" beats "Be careful when editing Clearwatch code" — the first has a grep-able trigger; the second is a vibe.
- **No examples in the rule itself** — examples grow stale. Reference a section number or a file path.
- **No exceptions in the first draft.** Exceptions get added in refinement (Prompt 2) only when verification shows they are needed.

Write the candidate rule to `$SCRATCH/03-rule-draft.md` with: `rule_text`, `proposed_section` (where in `~/CLAUDE.md` it would land), `trigger_signature` (grep pattern that should appear in transcripts when the rule fires).

**Step 5 — predict the rule's behavior.** Write `$SCRATCH/04-prediction.md` with three predictions:

1. **Expected trigger rate** — how often will the rule fire (sessions per week, by extrapolating from the corrections that motivated it).
2. **Expected false-positive shape** — when might the rule fire incorrectly? Name a scenario.
3. **Expected blast radius** — what happens if the rule fires when it should not? (Usually low; if high, redraft.)

Predictions are the article's diagnostic: a rule whose blast radius is "high if wrong" is one whose first encoding should be conservative.

**Step 6 — produce the staging report.** Write `$SCRATCH/00-CONVENTION.md` with: chosen friction, candidate rule (verbatim), predictions, and a one-paragraph "ready for verification" note. Print to stdout. Do not modify `~/CLAUDE.md`.
````
