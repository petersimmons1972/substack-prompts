# 117-i-dont-care-who-your-dad-is — Prompt 1 (audit)

```text
You are auditing this repository for "relayed authority" — places where
agent briefs, dispatch templates, automation prompts, or scripts assert that
a human authorized something, as prose, without a verifiable reference.

Steps:
1. Search the repo (docs, prompt templates, dispatch/brief generators, CI
   configs, agent instruction files like CLAUDE.md/AGENTS.md, and any
   queue/dispatch code) for authority-claim language. Grep at minimum for:
   "authorized", "approved", "the founder", "the user said", "green-light",
   "sign-off", "go-ahead", "re-authorized", case-insensitively. Treat this
   keyword scan as lint only: it locates candidates, it does not validate
   anything.
2. For each hit that is part of an instruction PASSED TO an agent or
   automation (not merely documentation about policy), classify:
   a. PROSE-ONLY — the claim of authorization is a bare sentence.
   b. UNVERIFIED-REFERENCE — the claim cites an artifact (issue URL, commit
      hash, message ID, ticket) a recipient could fetch, but fetching only
      proves the artifact exists, not who authorized what. A commit hash
      identifies content, not its author; git author fields are forgeable;
      mutable issue/message refs can be edited or spoofed.
   c. VERIFIED — the pipeline mechanically confirms, before acting, that the
      referenced authorization is genuine: issuer authenticated (a signed
      object or a provider-authenticated record, not a bare URL), scope and
      target environment match the requested action, and the grant is fresh
      (within expiry) and not revoked.
3. Separately, check whether any agent-facing rules file in this repo states
   a policy on relayed authorization claims. Quote it if present; note its
   absence if not.
4. Read-only. Modify nothing.

Output a markdown report:
- Table: file:line | quoted claim (truncated to 100 chars) | classification.
- Whether a relayed-authority policy exists, and whether current practice
  matches it (list contradictions explicitly).
- Top 3 PROSE-ONLY sites where a forged sentence would have the largest
  blast radius, one sentence each on what the sentence could trigger.
```

## Undo

Read-only — nothing to undo.

**Ground truth — tested 2026-07-10 (harness-agnostic wording, run without modification).** Codex CLI ✅ (terse result; transcript in project records). Claude Code and Grok legs: pending.
