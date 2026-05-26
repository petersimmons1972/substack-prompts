Copy the prompt below and paste it into Claude, ChatGPT, or your model of choice. The article linked from this directory's README explains what to expect.

````text
You are an auditor inspecting installed skills for break-even efficiency. You are read-only against my `~/.claude/skills/` directory. You may write only inside the scratch directory created in Step 1. You may not exfiltrate any file contents to any network endpoint. You may not read files matching `*.env`, `*credentials*`, `*token*`, `*.key`, `*.pem`, `id_rsa*`, `id_ed25519*`, or any path containing `/.ssh/` or `/.gnupg/`. You may not modify `~/.claude/settings.json`, install MCP servers, change hook configuration, or alter file permissions.

**Step 1 — create scratch directory.** Run:

```bash
SCRATCH="$HOME/.claude/experiments/$(date +%Y-%m-%d)-040-skill-breakeven"
mkdir -p "$SCRATCH"
echo "scratch=$SCRATCH"
```

**Step 2 — enumerate skills.** List directories under `~/.claude/skills/` (and any plugin-namespaced subdirectories one level deeper, e.g., `superpowers/`). Exclude `bench/` — benched skills are inactive and should not count. For each skill, identify its `SKILL.md` and any other body files (e.g., `INSTRUCTIONS.md`, included markdowns referenced from the front matter). Record skill name, plugin namespace if any, primary file path, and any referenced body file paths. Write to `$SCRATCH/01-skills.md`. If `~/.claude/skills/` does not exist, write `NO_SKILLS_DIR_FOUND` and stop with a missing-prereq finding.

**Step 3 — extract description and body sizes.** For each skill:

- **Description tokens:** parse the `SKILL.md` front matter and read only the `description:` field (and any other front-matter fields the harness loads into context — typically `name`, `description`, sometimes a short trigger list). Estimate `desc_tokens = ceil(words / 0.75)`.
- **Body tokens:** count words in the `SKILL.md` body (everything after the front-matter close) plus every referenced body file. Estimate `body_tokens = ceil(words / 0.75)`.
- **Total surface:** record the sum.

Write `$SCRATCH/02-sizes.md` as a table with columns: skill, desc_tokens, body_tokens, total_tokens. Sort descending by desc_tokens.

**Step 4 — compute break-even.** For each skill, compute `breakeven_invocations = ceil(body_tokens / desc_tokens)`. The intuition: the description costs `desc_tokens` per session whether or not the skill fires; if the skill fires once and loads the body, that one invocation cost `desc_tokens + body_tokens`. After N invocations the skill has cost `N * desc_tokens + body_tokens` in total context-loaded tokens. Inlining the body N times would cost `N * body_tokens`. The skill becomes cheaper when `N * desc_tokens + body_tokens < N * body_tokens`, i.e., when `N > body_tokens / (body_tokens - desc_tokens)`. For skills where `desc_tokens >= body_tokens`, the skill never wins on context grounds alone — flag those.

Write `$SCRATCH/03-breakeven.md` with columns: skill, desc_tokens, body_tokens, breakeven_invocations, classification (`HEALTHY` if breakeven ≤5; `MARGINAL` if 6–20; `EXPENSIVE` if 21–100; `INVERTED` if desc ≥ body; `OVERSIZED` if desc_tokens > 1000).

**Step 5 — flag the failures.** Produce `$SCRATCH/04-failures.md` listing every skill classified `EXPENSIVE`, `INVERTED`, or `OVERSIZED`. For each, name the skill, the failure type, and the reason the math does not work (one sentence — paraphrase, do not paste skill body content).

**Step 6 — write the summary.** Produce `$SCRATCH/00-SUMMARY.md` with: total skills, total description tokens loaded per session, count by classification, and a verdict (`COMPRESSION-WORKING` if ≥80% are HEALTHY/MARGINAL; `MIXED` if 50–80%; `COMPRESSION-FAILING` if <50%). Print to stdout.
````
