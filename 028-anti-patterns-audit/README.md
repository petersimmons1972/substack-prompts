# Anti-patterns audit

Prompts referenced in [Plutarch TX](https://plutarchtx.substack.com) article **028-anti-patterns-audit**.

→ **Read the article:** <https://plutarchtx.substack.com/p/anti-patterns-audit>

## How to use

Each `prompt-N.md` file is the prompt itself, with the teaching wrapper
stripped. Open the file, copy the contents, paste into Claude / ChatGPT /
your model of choice. The article (linked above) explains what the prompt
does and what to expect when you run it.

## Prompts in this article

### [`prompt-1.md`](./prompt-1.md) — Anti-patterns Audit Prompt — Find and Rank

Inspects your live AI configuration for the five most common anti-patterns — bloated memory files, secrets in memory files, missing undo discipline, wildcard permissions, and absent model-selection guidance — then ranks every finding by blast radius (how bad if exploited or hit) and ease of fix (how cheap to remediate). The output is a single ranked table you can hand to Prompt 2. The prompt does not modify any live file. Everything written goes inside a dated scratch directory you delete with one command.

### [`prompt-2.md`](./prompt-2.md) — Anti-patterns Audit Prompt — Remediate the Top Finding

Reads the ranked findings table produced by Prompt 1, picks the top-scoring anti-pattern, and produces a reversible remediation plan with three artifacts: a backup of the live file, a proposed replacement (in scratch), and a single-line undo command. The prompt does not apply the fix — it stages it. You review the diff, apply manually if you agree, and have a tested rollback path in your hand before you touch anything live. This prompt assumes Prompt 1 ran today and its scratch directory exists; if it does not, stop and run Prompt 1 first.

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Attribution
to Plutarch TX appreciated when republishing.
