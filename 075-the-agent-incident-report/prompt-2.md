# 075-the-agent-incident-report — Prompt 2 (action)

```text
Create a five-field agent incident report template in this repository, ready
for the first incident.

1. Write the file `docs/agent-incident-report-template.md` (create docs/ if
   absent) with exactly these sections:

   # Agent Incident Report — <date> — <short name>
   ## 1. What happened
   (Action timeline. Facts only, timestamps where known.)
   ## 2. What the agent believed
   (The best-reconstructable operational belief state — NOT inner truth.
   Answer: what proposition was the agent acting as if true, and where did
   that proposition come from? Cite the prompt text, retrieved context,
   cached state, or tool output that supplied it.)
   ## 3. What authorization was in play
   (The explicit grant, and any authorization the agent inferred from
   context. Note the gap between the two if there is one.)
   ## 4. Blast radius
   (Trust boundaries crossed: customer-visible, security-relevant, data
   integrity, downstream systems. "None crossed" is a valid, recorded answer.)
   ## 5. What changed
   (Remediation. Must answer: what now prevents the same false premise from
   being trusted again — not just what fixed the mechanism.)

2. If the repo has an existing post-mortem template, do not modify it; add a
   one-line pointer from it to this template for agent-involved incidents.
3. Commit on a new branch `docs/agent-incident-template` with message
   "docs: add five-field agent incident report template". Do not push or
   open a PR unless the operator asks.

## Undo
- `git checkout -` to return to your prior branch, then
  `git branch -D docs/agent-incident-template` to delete the branch.
- If the pointer line was added to an existing template on that branch, it
  disappears with the branch; nothing on the default branch was touched.
- If docs/ was newly created and is now empty after the branch deletion, it
  never existed on any surviving ref — no further cleanup needed.
```

**Ground truth — tested 2026-07-10 (harness-agnostic wording, run without modification).** Codex CLI ✅ (fixture: the claude-codex repo; full transcript in project records). Claude Code and Grok legs: pending.
