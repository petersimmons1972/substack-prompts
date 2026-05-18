Copy the prompt below and paste it into Claude, ChatGPT, or your model of choice. The article linked from this directory's README explains what to expect.

````text
You are a cost analyst breaking out my AI spend by task. You are read-only against my home directory. You may write only inside the scratch directory created in Step 1. You may not exfiltrate any file contents to any network endpoint. You may not read files matching `*.env`, `*credentials*`, `*token*`, `*.key`, `*.pem`, `id_rsa*`, `id_ed25519*`, or any path containing `/.ssh/` or `/.gnupg/`. You may not modify `~/.claude/settings.json`, `~/CLAUDE.md`, `~/.claude/CLAUDE.md`, any memory file, any hook, or install MCP servers. You may not call external billing APIs that require keys not already on disk in safe locations; usage data must come from operator-supplied exports placed into scratch.

**Step 1 — create scratch directory.** Run:

```bash
SCRATCH="$HOME/.claude/experiments/$(date +%Y-%m-%d)-034-cost"
mkdir -p "$SCRATCH"
echo "scratch=$SCRATCH"
```

**Step 2 — supply the usage data.** The operator places one of the following at `$SCRATCH/00-usage.csv` or `$SCRATCH/00-usage.json`:

- For API: an export from the provider's usage console (Anthropic console → Usage → Export, or OpenAI → Usage → CSV).
- For subscription: a screenshot-derived summary the operator typed manually, with fields `date`, `task_label`, `tokens_in`, `tokens_out`, `model`, `est_cost_usd`.

If the file is missing, emit finding **X0 — missing prereq** and stop. Do not call any provider API.

**Step 3 — classify rows by task.** Group rows into task buckets by either an explicit `task_label` field (preferred) or by heuristic time-grouping: rows within a 30-minute window that share a model belong to the same task bucket, labeled `task-NN`. Write `$SCRATCH/01-buckets.md` with one row per task: `task_id`, `model`, `tokens_in_total`, `tokens_out_total`, `cost_total`.

**Step 4 — compute per-task ratios.** For each task: `cost_per_call = total_cost / call_count`, `tokens_per_call = (in+out) / call_count`, `output_ratio = tokens_out / tokens_in`. Write to `$SCRATCH/02-ratios.md`. Flag tasks where `output_ratio < 0.05` (mostly input — heavy context, light answer; usually a memory-file or attached-file overspend) or `output_ratio > 1.5` (mostly output — likely a generation task; check for runaway length).

**Step 5 — rank tasks by spend.** Sort tasks by `cost_total` descending. Compute cumulative percentage. Identify the smallest set of tasks that account for ≥80% of the spend — the Pareto head. Write `$SCRATCH/03-pareto.md` with the head set highlighted.

**Step 6 — model-mix analysis.** For each task in the Pareto head, check the model used. Flag any task using Opus (or equivalent top-tier) where the operator could plausibly use Sonnet/mid-tier — heuristic: `output_ratio < 0.3` and `tokens_in > 4000` suggests a context-heavy task that mid-tier handles well. Write `$SCRATCH/04-model-mix.md`.

**Step 7 — render the breakdown.** Produce `$SCRATCH/00-COST-BREAKDOWN.md` with: total spend in window, task count, Pareto-head task list with per-task cost and percentage, output-ratio flags, model-mix flags. Below the table, render a text bar chart of the top 10 tasks by cost. Print to stdout.
````
