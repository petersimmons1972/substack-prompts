Copy the prompt below and paste it into Claude, ChatGPT, or your model of choice. The article linked from this directory's README explains what to expect.

````text
You are auditing an agent transcript for capability claims. For each claim you find, output one row: claim | claim_type | basis | authority | ttl_bucket | verdict.
- claim_type: exactly QUERIED (the agent called a live, authenticated discovery endpoint to learn this) or INFERRED (the agent read a file, log, artifact, or prior message to learn this).
- basis: the specific source — a file path, a log line, a prior message, an API call, or "basis unknown."
- authority: who or what asserted this claim (live authenticated endpoint, config file, session artifact, prior agent output, etc.).
- ttl_bucket: exactly one of static (stable for months), session (valid for this invocation only), request (specific to this task instance), or observed (artifact-inferred — always weakest).
- verdict: SOUND (basis is a live, authenticated query with explicit TTL) or WEAK (basis is artifact, log, prior output, or unknown). Any INFERRED claim is WEAK by definition. Any claim without a named authority is WEAK.

Output a markdown table and nothing else. If a claim cannot be classified with the evidence in the transcript, write "basis unknown" in the basis column and WEAK in the verdict column — do not omit it.

TRANSCRIPT: (paste the agent's session transcript or capability-section output here)
````
