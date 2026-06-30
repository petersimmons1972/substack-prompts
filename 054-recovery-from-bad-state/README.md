# Recovery from bad state

_Three failure shapes that recur — and the recovery procedure for each that does not require inventing it under stress_

Prompts referenced in [Plutarch TX](https://plutarchtx.substack.com) article **054-recovery-from-bad-state**.

→ **Read the article:** <https://plutarchtx.substack.com/p/recovery-from-bad-state>

## How to use

Each `prompt-N.md` file is the prompt itself, with the teaching wrapper
stripped. Open the file, copy the contents, paste into Claude / ChatGPT /
your model of choice. The article (linked above) explains what the prompt
does and what to expect when you run it.

## Prompts in this article

### [`prompt-1.md`](./prompt-1.md) — Recovery Checklist — Personalized to Your Environment

Builds a recovery checklist tailored to the operator's actual environment — the actual paths, the actual backups, the actual hooks. A generic recovery doc is useless under stress; the operator wants a checklist with their paths in it. The prompt inspects the environment, identifies the three failure shapes the article describes (conversation loops, memory contamination, hook misbehavior), and produces a per-shape recovery procedure with the operator's specific commands. Prompt 2 stages a deliberate corruption in scratch and runs the checklist against it.

### [`prompt-2.md`](./prompt-2.md) — Recovery Drill — Stage a Corruption, Execute the Checklist

Runs a deliberate end-to-end recovery drill against a *simulated* corrupted state inside scratch. The drill has three phases — one per failure shape from Prompt 1's checklist — each executed against a scratch-only fixture. The point is to discover gaps in the recovery procedure under controlled conditions, before the operator needs the procedure under real stress. The prompt does not corrupt anything outside scratch; it copies the operator's environment into scratch, deliberately damages the copy, and then runs the procedure against the damaged copy.

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Attribution
to Plutarch TX appreciated when republishing.
