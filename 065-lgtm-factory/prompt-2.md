Copy the prompt below and paste it into Claude, ChatGPT, or your model of choice. The article linked from this directory's README explains what to expect.

````text
For your last three AI LGTMs, write down the following for each: **reviewed_commit | base | reviewer_role | state_verified**.
- `reviewed_commit`: the exact commit hash or branch name that was reviewed — not "the PR" or "the latest."
- `base`: the exact base commit or branch the diff was computed against.
- `reviewer_role`: was the reviewer briefed as **adversarial** (explicit license to dissent, named failure categories) or **default** (general review, no explicit dissent license)?
- `state_verified`: YES if the reviewer was given the actual diff at the named commit; NO if the reviewer was given a description, a summary, or an older diff; UNKNOWN if you cannot confirm.

Output a table with one row per LGTM. Then add one line per blank or UNKNOWN: "Blank in [column] for LGTM [n] means: [what the reviewer was actually approving, stated honestly]."

FIXTURE: *(list your last three AI LGTMs — what was reviewed, when, by which agent, and what the brief said)*
````
