Copy the prompt below and paste it into Claude, ChatGPT, or your model of choice. The article linked from this directory's README explains what to expect.

````text
Pick one real multi-session workstream. At the first session boundary — the moment a new agent window would open with no memory of the prior session — list what a fresh agent would not know. Then reconstruct the four checkpoint fields for that boundary.

Output two tables:

**Table 1 — What a fresh agent would not know.** Columns: **item | category | recoverable | recovery_cost**
- `category`: exactly one of `state` (what was done, what changed), `intent` (what was being attempted, what decision was in progress), `next_action` (the specific first step the new agent should take), or `authority` (what scope/risk was approved by the human operator, and when).
- `recoverable`: YES (can be reconstructed from artifacts, logs, or the human) / PARTIAL (some but not all) / NO (this knowledge is gone if the session closed).
- `recovery_cost`: the estimated time or effort to recover this item without a checkpoint — low (< 5 min), med (5–30 min), high (> 30 min or requires a new human decision).

**Table 2 — Checkpoint reconstruction.** Four fields, one value each:
| field | value |
|---|---|
| state | *(what was true at the boundary — completed work, current config, outstanding changes)* |
| intent | *(what the workstream was trying to accomplish and any decisions that were in progress)* |
| next_action | *(the specific first action the fresh agent should take, stated precisely enough to act without clarifying questions)* |
| authority | *(who approved what scope or risk level, when, and for how long — or "NOT RECORDED" if approval was implicit or verbal)* |

Mark any unknown field as `UNKNOWN — do not invent`. Then answer: if you gave only Table 2 to a fresh agent, could it take the next_action without asking you a clarifying question?

WORKSTREAM: *(describe the multi-session workstream: what work was done in the prior session, what remains, and what the human operator authorized)*
````
