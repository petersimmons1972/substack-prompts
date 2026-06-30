Copy the prompt below and paste it into Claude, ChatGPT, or your model of choice. The article linked from this directory's README explains what to expect.

````text
You are auditing five autonomous actions for authorization under the reversibility gate. For each action, output one row: **action | state_reversible | consequence_reversible | rollback_path | rollback_tested | scope_bounded | verdict**.
- `state_reversible`: YES/NO — can the system return to prior recorded configuration?
- `consequence_reversible`: YES/NO — can the business/trust/downstream effects be undone? (Not the same as state_reversible.)
- `rollback_path`: the specific procedure, or "NONE".
- `rollback_tested`: YES / NO / UNTESTED.
- `scope_bounded`: YES/NO — does the action touch a defined, enumerable set of systems?
- `verdict`: PASS (agent may proceed autonomously) or BLOCK (requires human approval or hard deny).
A PASS requires YES on both reversibility columns, a non-"NONE" rollback path, and scope bounded. Any NO or NONE → BLOCK.
Output a markdown table and nothing else.

ACTIONS: *(list five autonomous actions here)*
````
