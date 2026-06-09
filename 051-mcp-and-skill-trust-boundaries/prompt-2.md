Copy the prompt below and paste it into Claude, ChatGPT, or your model of choice. The article linked from this directory's README explains what to expect.

````text
You are a trust-boundary planner. You operate read-only against the live settings, the audit output from Prompt 1, and the target component's source files. You may write only inside the scratch directory used by Prompt 1. **You may not modify any settings file. You may not call any tool the component exposes. You may not install, remove, or modify the component.** You may not exfiltrate file contents. You may not read `*.env`, `*credentials*`, `*token*`, `*.key`, `*.pem`, `id_rsa*`, `id_ed25519*`, `/.ssh/`, or `/.gnupg/` paths.

**Step 1 — locate scratch and select the target.** Run:

```bash
SCRATCH="$HOME/.claude/experiments/$(date +%Y-%m-%d)-051-trust"
test -f "$SCRATCH/00-AUDIT.md" || { echo "ERROR: run prompt-1 first"; exit 1; }
```

Pick the target: the highest-priority WEAK + STATE-MODIFYING component from the audit, or `COMPONENT=<name>` from the operator's environment. Record in `$SCRATCH/20-target.md`.

**Step 2 — back up settings.** Copy the affected settings file to `$SCRATCH/21-backup-<basename>.json`. Verify byte and md5 match. Record in `$SCRATCH/21-backup-verified.md`.

**Step 3 — produce the trust-boundary report.** Write `$SCRATCH/22-report.md` with:

- **Component identity** — name, source URL/path, maintainer (if any), provenance verdict.
- **Declared capabilities** — full list from the component's manifest, with capability tags (READ-ONLY / STATE-MODIFYING-LOCAL / STATE-MODIFYING-REMOTE / CREDENTIAL-ACCESS).
- **Observed behavior** — how the component has actually been used in the last 30 days; which declared tools have been invoked vs unused.
- **Risk posture** — what the component could do in the worst case if its source were compromised, and what the operator's recovery path would be.
- **Recommended scope** — a tightened set of capabilities, paths, or domains the operator can defend. The recommended scope is always at most a subset of the union of (declared capabilities) ∩ (observed behavior).

**Step 4 — produce 2–3 candidate scopings.** Each candidate names: capabilities allowed, capabilities now denied, predicted impact on the component's usefulness, and a re-evaluation date (default 30 days). Examples:

| candidate | scope | impact |
|---|---|---|
| A — most aggressive | only the 2 tools observed in last 30 days; deny everything else | high risk that next session needs an unobserved tool and prompts |
| B — observed + adjacent (recommended) | observed tools + tools obviously related to observed use | low impact; prompts only on novel capability use |
| C — read-only subset | strip every STATE-MODIFYING-LOCAL/REMOTE tool; allow only READ-ONLY tools | safest; component may become unusable if its core function is state-modifying |

Write to `$SCRATCH/23-candidates.md` with a recommendation and rationale.

**Step 5 — generate the JSON patch.** Produce `$SCRATCH/24-patch.json` (RFC 6902) implementing the recommended candidate. The patch may add a `permissions.deny` entry, replace a wildcard with a list, or add an `ask` rule for the now-restricted capabilities. Validate syntax with `python -m jsonpatch --check`; do not apply.

**Step 6 — produce the staging report.** Write `$SCRATCH/00-PLAN.md` with: target component, recommended scope, predicted impact, JSON patch path, and the exact apply command (`python -m jsonpatch apply ...`) — but do not run it. Include the re-evaluation date and a one-paragraph "what to watch for" note: signals that the scope is too tight (frequent prompts on a specific tool) or too loose (the component invoking a capability outside its observed behavior).

Print to stdout.
````
