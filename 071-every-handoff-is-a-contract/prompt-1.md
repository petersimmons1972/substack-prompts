Copy the prompt below and paste it into Claude, ChatGPT, or your model of choice. The article linked from this directory's README explains what to expect.

````text
Pull three recent handoffs from your pipeline. For each, score it against the four contract fields. Then revise one handoff into a reusable template your current tooling could actually populate, marking the one field it cannot safely auto-populate.

Output three things: the scoring table, the assumption statements, and the revised template.

**Table 1 — Scoring.** Columns: **handoff | origin_authority | scope | evidence | refusal_signal | score**
- `origin_authority`: PRESENT (handoff names who authorized this delegation and from what source) or MISSING.
- `scope`: PRESENT (handoff names what the receiver is and is not authorized to do, explicitly) or MISSING.
- `evidence`: PRESENT (handoff includes a verifiable artifact — diff, path, test output, approval object — that proves prior work was done) or MISSING.
- `refusal_signal`: PRESENT (handoff includes an explicit instruction for what the receiver should do if scope is ambiguous or authorization is unclear) or MISSING.
- `score`: count of PRESENT fields (0–4).

**Table 2 — Assumption statements.** For every MISSING field in every handoff, write one row: **handoff | missing_field | assumption_the_receiver_had_to_make**
- `assumption_the_receiver_had_to_make`: what the receiver had to guess, infer, or assume in order to proceed. Be specific — not "assumed scope was OK" but "assumed it was authorized to delete all resources with prefix 'tmp-' in the workspace, because the sender said 'handle the cleanup.'"

**Template.** Take the handoff with the lowest score. Revise it into a minimal template with all four fields populated. Then name one field and explain why your current tooling cannot safely auto-populate it — what it would have to guess to do so.

HANDOFFS: *(paste three recent handoff messages from your pipeline — the actual text passed between agents or from agent to agent)*
````
