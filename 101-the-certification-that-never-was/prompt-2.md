# 101-the-certification-that-never-was — Prompt 2 (action)

```text
You have shell and repo access. Institute linked-verification discipline for
this project's plan/changelog/handoff documents.

1. Name the exact target paths. Require a clean worktree; if it is dirty, stop
   nonzero. Then produce a read-only manifest of every proposed edit. Do not
   edit until the operator approves it; without interactive approval, stop
   after the manifest.
2. Add a linked-verification invariant to the approved operating document:
   "Every gate/audit/certification claim recorded here MUST link its artifact
   — the actual PR comment URL, CI run ID, or equivalent durable record. A
   verification claim with no link is UNVERIFIED, regardless of who asserts
   it, and must be re-checked against the primary source — not another
   summary of it — before being relied on."
3. Sweep only the approved paths: for every verification claim, attach the
   artifact link. Mark claims [UNVERIFIED] when no artifact is found and
   [CHECK INCOMPLETE] when access, tooling, or search errors prevent a complete
   check. Record the attempted scope and errors; do not delete either class.
4. Establish correct-in-place: when a recorded claim is found false, strike it
   through with a dated correction note directly below citing the artifact
   that refutes it. Never silently overwrite. The strikethrough is a visible
   correction; version-control history and review are the audit trail. Write
   this rule into the operating document.
5. If this project uses succession/handoff briefs, add two lines to the
   template: (a) the successor's first act is to re-verify every load-bearing
   claim in this brief against primary artifacts; (b) the predecessor is
   explicitly retired at handoff — confirm it, don't assume it.
6. Report: approved paths, claims linked, claims marked UNVERIFIED, checks
   marked incomplete, claims struck, and any errors. A worktree that became
   dirty outside the approved paths is an error: stop nonzero and make no
   further edits. Deciding consequences for false claims is the operator's
   call.

## Undo
- If the introducing commit is isolated and reverts cleanly, `git revert`
  restores its prior text. Otherwise resolve conflicts under review; do not
  claim exact restoration automatically.
- Strikethrough corrections preserve the original prose in the current
  document; reversing one removes the strike markup and correction note.
- No CI, hooks, or enforcement automation is installed by this action.
```

**Ground truth status — revised 2026-07-27 after adversarial review.** The earlier unguarded version passed a Codex CLI fixture on 2026-07-10. The bounded-path and approval flow above has not been re-run. Claude Code and Grok legs: pending.
