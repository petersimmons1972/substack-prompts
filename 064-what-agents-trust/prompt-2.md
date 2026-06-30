Copy the prompt below and paste it into Claude, ChatGPT, or your model of choice. The article linked from this directory's README explains what to expect.

````text
You are building a verification plan for an AI-generated finding. First, split the finding into OBSERVATION rows and CONCLUSION rows — the same schema as the claim-type audit. Then, for every CONCLUSION row, add a verification plan. Output two tables: the claim-type split table, then the verification plan table.

**Table 1 — Claim split.** Columns: **claim | type | source_pointer**
- `type`: OBSERVATION or CONCLUSION (same rules as Prompt 1: observations require a source_pointer or must be reclassified as CONCLUSION).
- `source_pointer`: file:line, log line, or metric for OBSERVATION rows; blank for CONCLUSION rows.

**Table 2 — Verification plan (CONCLUSION rows only).** Columns: **conclusion | verification_method | cost | prerequisite | blocks_action**
- `conclusion`: the conclusion text (copied from Table 1).
- `verification_method`: the cheapest live-system check that would confirm or refute this conclusion — specific command, query, or inspection, not "check the logs."
- `cost`: low (under 5 min, no infrastructure change), med (5–30 min, or requires a second person), or high (over 30 min, infrastructure change, or requires a deployment).
- `prerequisite`: what access, environment, or data is required to run the verification — or "none."
- `blocks_action`: YES if you should not act on this finding until this conclusion is verified; NO if the action can proceed with the conclusion flagged as unverified.

Output Table 1, then Table 2, and nothing else.

FINDING: *(paste the AI’s review, diagnosis, or recommendation here)*
````
