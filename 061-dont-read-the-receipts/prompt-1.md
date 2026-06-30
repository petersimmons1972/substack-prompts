Copy the prompt below and paste it into Claude, ChatGPT, or your model of choice. The article linked from this directory's README explains what to expect.

````text
You are writing the capability section of a handoff brief. For each capability the receiving agent will need, fill in one row: capability | endpoint | ttl_bucket | provenance | fallback.
- endpoint: the live query path (URL, CLI command, API method) or "NONE — no query endpoint exists".
- ttl_bucket: exactly one of static (stable for months), session (valid for this invocation only), request (specific to this task instance), or observed (artifact-inferred — always weakest).
- provenance: who or what produced this fact (live query, config file, prior session log, etc.).
- fallback: what the agent does if this capability is unavailable or unknown — must be "fail closed" for sensitive capabilities, "record unknown" for others. Never "assume yes."
Output a markdown table and nothing else.

TASK: (paste the handoff task description here)
````
