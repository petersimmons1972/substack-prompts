Copy the prompt below and paste it into Claude, ChatGPT, or your model of choice. The article linked from this directory's README explains what to expect.

````text
You are designing the minimum control set for one autonomous action. For the action supplied, output a control design with these exact fields: **action | state_rollback_procedure | consequence_rollback_procedure | rollback_owner | rollback_ttl | scope_constraint | audit_log_entry | rollback_tested | verdict**.
- `state_rollback_procedure`: the specific procedure to restore prior recorded system configuration, or "NONE — no state rollback path exists."
- `consequence_rollback_procedure`: the specific procedure to undo business/trust/downstream effects, or "NONE — consequence effects cannot be reversed." (This is NOT the same as state rollback.)
- `rollback_owner`: the named role or service responsible for executing rollback — not "the team" or "ops."
- `rollback_ttl`: the time window within which rollback remains meaningful, after which hardening of consequences makes rollback futile.
- `scope_constraint`: the explicit, enumerable set of systems or data this action may touch — not a class description.
- `audit_log_entry`: the structured log event this action must emit before execution begins.
- `rollback_tested`: YES / NO / UNTESTED — has the rollback procedure been executed successfully in a non-production environment?
- `verdict`: AUTONOMOUS-OK (all fields non-NONE, rollback_tested is YES, scope is bounded) or REQUIRES-HUMAN-APPROVAL (any NONE, any UNTESTED, unbounded scope) or SHOULD-NOT-BE-AUTONOMOUS (consequence rollback is NONE and scope is not tightly bounded — conclude the action should not run without a human in the loop).

Output a markdown table and nothing else. If you cannot design a credible control for a field, write "NONE" and let the verdict reflect it — do not fabricate a procedure that does not exist.

ACTION: *(describe the autonomous action, its target resources, and the authorization context here)*
````
