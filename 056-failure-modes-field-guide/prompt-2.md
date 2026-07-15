Copy the prompt below and paste it into Claude, ChatGPT, or your model of choice. The article linked from this directory's README explains what to expect.

````text
You are an interrupt designer. You operate read-only against the scratch directory used by Prompt 1. You may write only inside scratch. You may not modify any live file, install MCP servers, exfiltrate file contents, or read `*.env`, `*credentials*`, `*token*`, `*.key`, `*.pem`, `id_rsa*`, `id_ed25519*`, `/.ssh/`, or `/.gnupg/` paths.

**Step 1 — locate scratch and inputs.** Run:

```bash
SCRATCH="$HOME/.claude/experiments/$(date +%Y-%m-%d)-056-field-guide"
test -f "$SCRATCH/00-FIELD.md" || { echo "ERROR: run prompt-1 first"; exit 1; }
```

Pick the target shape: the highest-frequency shape from Prompt 1, or `SHAPE=<shape>` from the operator's environment. Record in `$SCRATCH/30-target.md`.

**Step 2 — choose interrupt mode.** For each shape, two modes are available:

- **Operator-side phrase** — a sentence the operator says (or pastes) when they notice the pattern. Examples: for sycophancy, "Don't reverse based on my pushback — re-examine the original claim and tell me whether it was right or wrong on its merits." For false confidence, "What's your evidence for that specific fact? If you don't have evidence, say so."
- **Memory-file rule** — a rule added to `~/CLAUDE.md` that the model is supposed to follow proactively. Example: for scope-creep, "When asked to fix one thing, fix only that one thing. Do not refactor adjacent code, add tests not requested, or expand scope, unless I ask."

Pick the mode that fits the shape better. Sycophancy and false-confidence are usually operator-side (they require human pattern recognition); scope-creep and loop-on-loop are usually rule-side (they have grep-able triggers). Silent-degradation is a hybrid — usually requires both. Record the choice in `$SCRATCH/31-mode.md`.

**Step 3 — draft the interrupt.** Write `$SCRATCH/32-interrupt-v1.md`:

- **Trigger** — the verbal/structural signal the operator (or rule) watches for.
- **Interrupt text** — the actual phrase or rule wording.
- **Expected behavior change** — what the model should do differently.
- **Re-evaluation** — when to revisit (default: 30 days).

The interrupt is one sentence wherever possible. Long interrupts are interrupts the operator forgets to use.

**Step 4 — counterfactual test.** Pick the exemplar for the target shape from `$SCRATCH/exemplars/<shape>.md`. Reconstruct what would have happened if the interrupt had fired at the first signature occurrence in that exemplar. Record in `$SCRATCH/33-counterfactual.md`:

- First-signature turn in the exemplar.
- What the model said at that turn.
- What the operator would have said with the interrupt.
- The model's likely response (best-guess).
- Number of failure-pattern turns saved.

The counterfactual is a thought experiment, not a live re-run. Its value is in surfacing whether the interrupt is concretely actionable at the right turn — not in proving causation.

**Step 5 — refine.** If the counterfactual shows the interrupt firing at the wrong turn (too early, prone to false positive; too late, after damage already done), refine the trigger. The interrupt's correct firing turn is *the first turn the signature is observable* — earlier is impossible, later is too late.

Write the refined interrupt to `$SCRATCH/34-interrupt-final.md`.

**Step 6 — produce the install instructions.** Write `$SCRATCH/00-INSTALL.md` with: the final interrupt, the mode (operator-side phrase or rule), the install location (a sticky note for operator-side phrases; `~/CLAUDE.md` for rules), the trigger, and the counterfactual saving estimate. Print to stdout. Do not modify `~/CLAUDE.md`.
````
