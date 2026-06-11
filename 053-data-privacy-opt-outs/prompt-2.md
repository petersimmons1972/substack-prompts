Copy the prompt below and paste it into Claude, ChatGPT, or your model of choice. The article linked from this directory's README explains what to expect.

````text
You are a per-surface change-list generator. You operate read-only against the operator's filled-in inventory in scratch. You may write only inside the scratch directory used by Prompt 1. **You may not call any provider API. You may not fetch any provider settings page. You may not exfiltrate file contents.** You may not read `*.env`, `*credentials*`, `*token*`, `*.key`, `*.pem`, `id_rsa*`, `id_ed25519*`, `/.ssh/`, or `/.gnupg/` paths. You may not modify any local file outside scratch.

**Step 1 — locate scratch and inputs.** Run:

```bash
SCRATCH="$HOME/.claude/experiments/$(date +%Y-%m-%d)-053-privacy"
test -f "$SCRATCH/00-INVENTORY.md" || { echo "ERROR: run prompt-1 first"; exit 1; }
```

Verify each per-surface inventory file under `$SCRATCH/inventory/` has been filled in by the operator. If any are still placeholders, list them and stop — the change-list cannot be honest if the starting state is unknown.

**Step 2 — load the recommended posture per data class.** Use the Prompt 1 decision matrix at `$SCRATCH/02-decisions.md` to determine the recommended posture per surface. Record the recommendation and rationale in `$SCRATCH/40-recommendations.md`:

| surface | recommended_posture | rationale |
|---|---|---|
| ChatGPT consumer | training off; conversation history minimum-needed; memory off if proprietary code is ever pasted | training surface for consumer tiers; operator may paste sensitive content |
| Claude.ai consumer | training off (default in many regions); conversation history per session preference | confirm region defaults at settings URL |
| Anthropic API | no-train header on every request; zero-retention header for sensitive batches | the headers are the contract |
| Claude Code | tied to API account; verify settings.json reflects the API account's privacy posture | downstream of the API tier choice |
| OpenAI API | enterprise/Teams tier preferred for proprietary work; consumer API has different defaults | operator decides tier per data class |
| Gemini | check Google account level controls + Workspace if applicable | Workspace shifts defaults |

The recommendation rows are templates — the operator may adjust per their data classes from `02-decisions.md`.

**Step 3 — produce per-surface change rows.** For each active surface, write `$SCRATCH/changes/<surface>.md` with one row per setting that needs to change. Each row has:

- **Setting** — name of the toggle.
- **Settings URL** — the documented URL.
- **Before** — current state (from the inventory).
- **After** — recommended state.
- **Reasoning** — why this change.
- **Undo** — how to revert this specific change in this surface's UI.
- **Verify** — a one-sentence check the operator runs after the change to confirm it took.

If the inventory shows a setting is already at the recommended state, skip it (record as "already-aligned"). The change rows produce a per-surface to-do list the operator can complete in 10–20 minutes.

**Step 4 — produce the snapshot-before script (optional).** Write `$SCRATCH/41-snapshot-script.md` describing how the operator can take a manual screenshot or copy-paste of each surface's privacy settings page *before* changing anything, and where to store the screenshots (suggested: `$SCRATCH/snapshots/before/`). This is the operator's audit trail. The prompt does not take screenshots itself.

**Step 5 — produce the snapshot-after / verify guidance.** Write `$SCRATCH/42-verify.md` with a per-surface verification step the operator runs after applying the changes. Examples: "On Anthropic API, send one test request with the no-train header and confirm response headers reflect compliance"; "On ChatGPT, open settings and confirm 'Improve the model for everyone' is off"; "Save a 'snapshot-after' screenshot to `$SCRATCH/snapshots/after/`."

**Step 6 — produce the change-list report.** Write `$SCRATCH/00-CHANGES.md` with: list of surfaces, per-surface change-row count, links to the per-surface change files, snapshot script reference, verify guidance reference, and an explicit "this is operator-driven, the prompt does not change any setting on your behalf" note. Print to stdout.
````
