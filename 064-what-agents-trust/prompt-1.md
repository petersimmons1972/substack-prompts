Copy the prompt below and paste it into Claude, ChatGPT, or your model of choice. The article linked from this directory's README explains what to expect.

````text
You are auditing an AI-generated finding before anyone acts on it. For EACH distinct claim, output one row: **claim | type | source_pointer | evidence | falsifier | falsifier_cost**.
- `type` is exactly OBSERVATION (verifiable in source or running state) or CONCLUSION (cause, consequence, or recommendation).
- OBSERVATION rows require a `source_pointer` (file:line, a log line, a metric). If you cannot cite one, reclassify the claim as CONCLUSION.
- CONCLUSION rows require `evidence` (the observations it rests on), a `falsifier` (the cheapest live-system check that would disprove it), and `falsifier_cost` (low / med / high).
- One type per claim. Do not relabel an inference as an observation because it is well argued.
Output a markdown table and nothing else.
FINDING: *(paste the AI’s review/diagnosis here)*
````
