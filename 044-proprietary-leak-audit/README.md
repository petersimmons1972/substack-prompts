# The proprietary-leak audit

_The proprietary detail that slips past credential grep — the audit that catches what your scanner cannot see_

Prompts referenced in [Plutarch TX](https://plutarchtx.substack.com) article **044-proprietary-leak-audit**.

→ **Read the article:** <https://plutarchtx.substack.com/p/proprietary-leak-audit>

## How to use

Each `prompt-N.md` file is the prompt itself, with the teaching wrapper
stripped. Open the file, copy the contents, paste into Claude / ChatGPT /
your model of choice. The article (linked above) explains what the prompt
does and what to expect when you run it.

## Prompts in this article

### [`prompt-1.md`](./prompt-1.md) — Proprietary-Leak Audit — Find Identifying Detail Before It Ships

Scans memory files plus an operator-named draft directory for *proprietary identifiers* — client/customer names, real hostnames or domain names, internal repo names, customer-specific identifiers (PO numbers, ticket IDs, internal vendor IDs), and identifying personal detail (names, emails, phone numbers) — before any of it ships outside the operator's control. It is a pre-publish hygiene gate: drafts get audited, hits get triaged, redactions get staged in Prompt 2. Article 042 catches secret leaks; this one catches proprietary leaks. Both can sink a publication, only one trips a credentials scanner.

### [`prompt-2.md`](./prompt-2.md) — Proprietary-Leak Audit — Stage Redactions That Preserve the Lesson

Reads the redacted hit list from Prompt 1, builds a per-file replacement plan, and stages each modified file in scratch with each in-scope identifier replaced by a placeholder that preserves the *technical claim* the original line was making. The plan covers HIGH and MEDIUM hits in shipping drafts; LOW and memory-only MEDIUM hits are deferred to the operator's manual review. The prompt does not modify any live file. You review the diffs, decide what to keep, and have a tested rollback path.

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Attribution
to Plutarch TX appreciated when republishing.
