# `AGENTS.md` and shared expectations

Prompts referenced in [Plutarch TX](https://plutarchtx.substack.com) article **039-agents-md-shared-expectations**.

→ **Read the article:** <https://plutarchtx.substack.com/p/agents-md-shared-expectations>

## How to use

Each `prompt-N.md` file is the prompt itself, with the teaching wrapper
stripped. Open the file, copy the contents, paste into Claude / ChatGPT /
your model of choice. The article (linked above) explains what the prompt
does and what to expect when you run it.

## Prompts in this article

### [`prompt-1.md`](./prompt-1.md) — `AGENTS.md` Boundary Audit — Whose File Is This Rule?

Reads both `AGENTS.md` and `CLAUDE.md` and decides, for each rule-bearing line, which file it should live in. `AGENTS.md` holds rules every agent on the project must agree on — coordination, naming, branch discipline, tool conventions. `CLAUDE.md` holds the operator's personal contract with the model — preferences, voice, escalation policy. Lines that crossed the boundary in either direction are flagged. The output is a per-line classification table plus a list of moves. The prompt does not modify any live file. Everything written goes inside a dated scratch directory you delete with one command.

### [`prompt-2.md`](./prompt-2.md) — `AGENTS.md` Missing Rule — Synthesize from Failure

Mines the operator's recent agent sessions for a *repeated* failure mode — a thing two or more agents got wrong the same way — and proposes a single new rule for `AGENTS.md` that would have prevented all of them. The rule is staged in scratch as a candidate diff against the live `AGENTS.md`. The prompt does not modify any live file. You review the proposed rule, copy it manually if you agree, and have a tested rollback path before you change anything.

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Attribution
to Plutarch TX appreciated when republishing.
