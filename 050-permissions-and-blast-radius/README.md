# Permissions and blast radius

_Most sessions touch a fraction of what your permissions allow — the gap between actual need and granted access is where the blast radius lives_

Prompts referenced in [Plutarch TX](https://plutarchtx.substack.com) article **050-permissions-and-blast-radius**.

→ **Read the article:** <https://plutarchtx.substack.com/p/permissions-and-blast-radius>

## How to use

Each `prompt-N.md` file is the prompt itself, with the teaching wrapper
stripped. Open the file, copy the contents, paste into Claude / ChatGPT /
your model of choice. The article (linked above) explains what the prompt
does and what to expect when you run it.

## Prompts in this article

### [`prompt-1.md`](./prompt-1.md) — Permissions Audit — Rank Each Rule by Blast Radius and Revocability

Audits the operator's permission surface — the entries in `permissions.allow`, `permissions.deny`, and `permissions.ask` across user and project settings — and ranks each rule by **blast radius** (what it allows in the worst case) and **revocability** (how easy it is to remove the rule and restore the previous capability if it turns out to be a problem). The output is a per-rule risk table. The prompt does not modify any setting; Prompt 2 stages a tightened replacement for the highest-blast-radius wildcard.

### [`prompt-2.md`](./prompt-2.md) — Permissions Tightening — Stage a Replacement and Dry-Run

Picks the highest-risk HIGH-blast + EASY-revocable rule from Prompt 1's audit and produces a tightened replacement. The replacement is staged in scratch as a JSON patch; a dry-run script matches the tightened rule against a fixture set of real commands the operator has run recently, and reports which fixtures the new rule would still allow versus which would now require approval. The operator reviews the diff and the dry-run output, then applies the patch by hand.

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Attribution
to Plutarch TX appreciated when republishing.
