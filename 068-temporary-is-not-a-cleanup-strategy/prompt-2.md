Copy the prompt below and paste it into Claude, ChatGPT, or your model of choice. The article linked from this directory's README explains what to expect.

````text
Write a lifecycle policy for one resource class. The policy must include all required fields and pass three scenario tests. Output two things: the policy table, then the scenario test results.

**Policy table.** Columns: **field | value**

Required fields (output one row per field):
| field | value |
|---|---|
| resource_class | *(the specific class: e.g., Docker volumes, build artifacts, agent temp dirs)* |
| ttl | *(the maximum age before a resource in this class is eligible for deletion — be specific: "30 days," not "short-lived")* |
| enforcement_mechanism | *(the automated process that checks TTL and deletes — keyed to TTL, NOT keyed to disk pressure. Name it specifically.)* |
| owner | *(the named role or service responsible for this policy — not "the team")* |
| exception_path | *(how a resource gets marked long-lived and why — must require explicit human approval or a `protected` label)* |
| audit_log | *(what is written, where, when a resource is deleted under this policy)* |
| dry_run_mode | *(how to run the enforcement mechanism without deleting — the command or flag)* |
| capacity_alert | *(the threshold at which an alert fires before deletion is needed — should be below 100% to give response time)* |
| response_playbook | *(the specific steps when the capacity alert fires)* |
| exposure_estimate | *(estimate of how much storage this policy reclaims in the first enforcement run, with assumptions stated)* |

**Scenario tests.** For each of the three scenarios below, output: **scenario | expected_outcome | policy_verdict** — either CORRECT (policy handles this correctly) or GAP (policy does not cover this case, and here is the gap).

Scenarios:
1. A resource in this class has passed its TTL. The enforcement mechanism runs.
2. A resource in this class has no TTL annotation and no `protected` label. The enforcement mechanism runs.
3. A resource in this class has a `protected` label. The enforcement mechanism runs.

RESOURCE CLASS: *(name the resource class and the infrastructure context — shared build host, Kubernetes namespace, cloud bucket, etc.)*
````
