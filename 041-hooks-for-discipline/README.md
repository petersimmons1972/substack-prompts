# Hooks for the things you keep forgetting

_The things you correct every session deserve a hook — automation for the patterns you keep reinstalling by hand_

Prompts referenced in [Plutarch TX](https://plutarchtx.substack.com) article **041-hooks-for-discipline**.

→ **Read the article:** <https://plutarchtx.substack.com/p/hooks-for-discipline>

## How to use

Each `prompt-N.md` file is the prompt itself, with the teaching wrapper
stripped. Open the file, copy the contents, paste into Claude / ChatGPT /
your model of choice. The article (linked above) explains what the prompt
does and what to expect when you run it.

## Prompts in this article

### [`prompt-1.md`](./prompt-1.md) — Hook Inventory Audit — Tag Every Hook

Walks every configured hook and tags it as **DISCIPLINE-AUTOMATION** (the hook prevents a forgetfulness failure the operator has actually experienced — e.g., backup-before-edit, secrets-redact-before-commit), **NICE-TO-HAVE** (the hook does something useful but the failure it prevents has not been observed), or **MISPLACED-LOGIC** (the hook is doing work that should be a skill, a permission, or a memory file — typically a hook that adds context or advice rather than enforces a discipline). The output is a per-hook table plus a list of hooks worth keeping, retiring, or relocating. The prompt does not modify any live file. Everything written goes inside a dated scratch directory you delete with one command.

### [`prompt-2.md`](./prompt-2.md) — Hook Design — From Repeated Failure to Spec

Mines the operator's recent sessions for a repeated forgetfulness failure (the kind a hook can deterministically prevent), then drafts a hook *specification* in scratch — script body, event-key, matcher, fail mode, and the proposed `settings.json` patch. The prompt does not install the hook. It does not modify `settings.json`. It produces a spec the operator reads, manually pastes into `settings.json`, and rolls back if it misbehaves. Per the security floor, this prompt never modifies the live `settings.json` — that is a permission boundary the audit cannot cross.

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Attribution
to Plutarch TX appreciated when republishing.
