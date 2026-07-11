# 075-the-agent-incident-report — Prompt 1 (audit)

```text
You are auditing this repository's incident-response readiness for AI-agent incidents.

Using only shell and repository access, do the following:

1. Locate any post-mortem / incident-report templates or past incident documents:
   - Search: `grep -riEl 'post-?mortem|incident report|root cause|RCA' --include='*.md' .`
     plus common dirs: docs/, runbooks/, incidents/, postmortems/, .github/.
2. For each template or past incident report found, check whether it has any field that captures:
   a. WHAT HAPPENED — action timeline (most will have this)
   b. WHAT THE AGENT BELIEVED — the operational belief state: what proposition
      was the acting agent (human or AI) treating as true, and what input
      (prompt, cached state, tool output, doc) supplied that proposition
   c. WHAT AUTHORIZATION WAS IN PLAY — the explicit or inferred grant the
      actor was operating under
   d. BLAST RADIUS — trust boundaries crossed (customer-visible, security,
      data)
   e. WHAT CHANGED — remediation beyond "fixed the bug": what now prevents
      the same false premise from being trusted again
3. Separately, inventory where AI agents act in this repo (CI bots, merge
   automation, agent configs, CLAUDE.md/AGENTS.md, .github/workflows) and
   note which of those actors would produce NO reconstructable belief trace
   today (no logged prompt/context/tool-output for their actions).

Output format:
## Templates found
- <path>: fields present [a,c,d] / fields absent [b,e]
## Agent actors with no belief trace
- <actor>: <why its belief state could not be reconstructed after an incident>
## Verdict
READY | PARTIAL | UNPREPARED — one sentence on the biggest gap.
```

## Undo

Read-only — nothing to undo.

**Ground truth — tested 2026-07-10 (harness-agnostic wording, run without modification).** Codex CLI ✅ (fixture: the claude-codex repo; full transcript in project records). Claude Code and Grok legs: pending.
