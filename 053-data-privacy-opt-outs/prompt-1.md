Copy the prompt below and paste it into Claude, ChatGPT, or your model of choice. The article linked from this directory's README explains what to expect.

````text
You are a privacy-inventory builder. You operate read-only against the operator's local memory and recent transcripts at `TRANSCRIPTS=<path>`. You may write only inside the scratch directory created in Step 1. **You may not call any provider API. You may not fetch any provider settings page. You may not exfiltrate file contents.** You may not read `*.env`, `*credentials*`, `*token*`, `*.key`, `*.pem`, `id_rsa*`, `id_ed25519*`, `/.ssh/`, or `/.gnupg/` paths.

**Step 1 — create scratch directory.** Run:

```bash
SCRATCH="$HOME/.claude/experiments/$(date +%Y-%m-%d)-053-privacy"
mkdir -p "$SCRATCH"
```

**Step 2 — enumerate active surfaces.** Identify which surfaces the operator uses by scanning recent transcripts and shell history for tool/URL references. Standard surfaces:

- **ChatGPT** (chatgpt.com, OpenAI consumer)
- **Claude.ai** (claude.ai, Anthropic consumer)
- **Anthropic API** (api.anthropic.com)
- **Claude Code** (this CLI)
- **OpenAI API** (api.openai.com)
- **Gemini** (gemini.google.com / Google AI Studio / Vertex AI)
- **Enterprise tiers** if applicable (Anthropic Workspaces, OpenAI Teams/Enterprise, Microsoft 365 Copilot, etc.)

Write to `$SCRATCH/00-surfaces.md` with usage frequency (`heavy` / `light` / `unused`) per surface. Skip any unused surface from the rest of the inventory.

**Step 3 — build the per-surface question set.** For each active surface, write `$SCRATCH/inventory/<surface>.md` with the canonical questions to answer. The question set per surface is a stable shape (the operator answers each in the next step):

| question | what to record |
|---|---|
| training_opt_out | yes/no/unknown — is data used to improve models? |
| retention_period | days/weeks/forever/unknown |
| conversation_history | enabled/disabled/per-session |
| memory_or_custom_instructions | enabled/disabled, with content review status |
| export_or_delete_workflow | available/limited/none — what's the operator's path to extract or remove their data? |
| enterprise_or_consumer_tier | which tier? (matters: enterprise tiers usually have stronger no-train defaults) |
| settings_url | the documented URL the operator must visit |
| last_reviewed | (operator fills in) |

The settings URLs section is the most volatile — it changes when providers reorganize their settings UI. Mark the URLs as "verify at draft time" so the article can be re-checked before publish.

**Step 4 — produce the data-flow map.** Write `$SCRATCH/01-flow-map.md`: a per-surface table of `what is sent`, `what is stored`, `what is used for training`, `what is retained and for how long`, and `what is shared with third parties`. The operator fills in this table from each surface's privacy / data-handling pages. Pre-populate columns with placeholders the operator overwrites (`<verify on settings page>`).

**Step 5 — produce the decision-framework template.** Write `$SCRATCH/02-decisions.md` with a simple matrix:

| data sensitivity | recommended surface | rationale |
|---|---|---|
| public / non-sensitive | any consumer or API | minimal cost |
| proprietary code / customer data | API with no-train + zero-retention header (or enterprise tier) | reduces retention surface |
| personal data / regulated data | enterprise tier with DPA in place, or local-only models | compliance and contract |
| secrets, credentials, keys | none — never paste into any AI surface | non-negotiable |

The matrix is operator-customizable: the operator can add a row for their team's specific data classes.

**Step 6 — produce the inventory report.** Write `$SCRATCH/00-INVENTORY.md` with: list of active surfaces, the inventory file paths (one per surface), the data-flow map path, the decisions template path, and a one-sentence note for each unused surface ("not in active rotation"). Print to stdout.
````
