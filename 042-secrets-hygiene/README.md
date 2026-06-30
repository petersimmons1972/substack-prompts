# Secrets hygiene in memory files

Prompts referenced in [Plutarch TX](https://plutarchtx.substack.com) article **042-secrets-hygiene**.

→ **Read the article:** <https://plutarchtx.substack.com/p/secrets-hygiene>

_Published: 2026-05-26_

## How to use

Each `prompt-N.md` file is the prompt itself, with the teaching wrapper
stripped. Open the file, copy the contents, paste into Claude / ChatGPT /
your model of choice. The article (linked above) explains what the prompt
does and what to expect when you run it.

## Prompts in this article

### [`prompt-1.md`](./prompt-1.md) — Secrets Hygiene — Redacted Scan Across Memory Files

Scans the operator's memory files for indicator patterns that look like secrets — API keys, JWTs, hex tokens, RFC1918 IPs, bare emails, AWS access-key prefixes — and reports each hit as `(file, line, indicator-type, redacted-preview)`. The output ranks each hit by *confidence* (how strongly the indicator matches a known secret shape) so the operator can act on high-confidence hits first. The prompt does not modify any live file. Everything written goes inside a dated scratch directory you delete with one command. Prompt 2 consumes the redacted hit list to stage replacements.

### [`prompt-2.md`](./prompt-2.md) — Secrets Hygiene — Stage Redacted Replacements

Reads the redacted hit list from Prompt 1, builds a per-file replacement plan, and stages each modified file in scratch with the candidate replaced by a placeholder. Computes a *post-redaction smoke test* — the operator's typical task can still be performed against the redacted memory, with the secret moved to a secret manager. The prompt does not modify any live file. You review the diffs, copy them manually if you agree, and have a tested rollback path.

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Attribution
to Plutarch TX appreciated when republishing.
