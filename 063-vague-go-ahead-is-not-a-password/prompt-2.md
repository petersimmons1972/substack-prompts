Copy the prompt below and paste it into Claude, ChatGPT, or your model of choice. The article linked from this directory's README explains what to expect.

````text
You are auditing the authorization language in an agent's system prompt and transcript history. For each authorization-bearing phrase you find, output one row: **phrase | action_named | target_named | expiry_named | single_use | verdict**.
- `phrase`: the exact quoted text of the authorization phrase.
- `action_named`: YES if the phrase names a specific action; NO if it uses vague language ("do what's needed," "go ahead," "handle it," "use your judgment").
- `target_named`: YES if the phrase names a specific resource, environment, or scope; NO if the target is implied or absent.
- `expiry_named`: YES if the phrase includes a time window or single-session scope; NO if it grants standing permission.
- `single_use`: YES if the phrase is clearly non-replayable (tied to this task instance only); NO if a prior "go ahead" could be interpreted as covering future actions.
- `verdict`: VALID-AUTHORIZATION (all YES) or VAGUE-PHRASE (any NO) or STANDING-PRIVILEGE (no expiry AND no single-use constraint — the most dangerous class).

Output a markdown table and nothing else. If the system prompt contains no authorization language, output a table with one row: phrase = "(none found)" and all other columns = N/A, verdict = NO-AUTHORIZATION-LANGUAGE.

**Access dependency:** This prompt requires the agent to surface its system prompt and transcript history. Results degrade if the agent does not have access to these or does not surface them fully. A VAGUE-PHRASE result is conservative and correct — do not reclassify to VALID-AUTHORIZATION without explicit evidence.

SYSTEM PROMPT AND TRANSCRIPT: *(paste the agent's system prompt and relevant transcript sections here)*
````
