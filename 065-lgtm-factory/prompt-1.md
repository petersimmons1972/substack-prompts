Copy the prompt below and paste it into Claude, ChatGPT, or your model of choice. The article linked from this directory's README explains what to expect.

````text
Write one adversary brief for the code review task below. Include: reviewed commit and base, 3–5 specific failure categories to hunt for, evidence requirements per finding (file, line range, failure mode, verification step), explicit license to dissent from prior LGTMs. Output: a table with columns **category | evidence_required | verification_step | finding** (or "none under this scope"). Not general concerns — named, citable, falsifiable failures only.

FIXTURE:
*(paste your reviewed commit hash or branch, base, diff summary, and any prior LGTM comments here)*
````
