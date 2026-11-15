# 138-it-decoded-the-first-one — Prompt 1 (AUDIT: what would your guard decide? Read-only)

Paste into Claude Code or Codex, with your hook's path in place of the placeholder. It only reads: it changes nothing and runs nothing.

```text
Read-only: change no file, and run neither my hook nor any command
below. Decide by reading the code.

My command-guard hook is at: <PATH TO YOUR HOOK>
If that is still a placeholder or you can't read it, stop and say so.

For each command, say what the hook would do (ALLOW, DENY, or UNDECIDABLE
if the code can't tell you) and quote the deciding line. Use a list, not
a table.
1. rm -rf /
2. printf aGVsbG8= | base64 -d | bash
3. echo ok && printf Li90ZXN0 | base64 -d | sh
4. printf aGVsbG8= | base64 -d | env bash
5. printf aGVsbG8= | base64 -d | /usr/bin/env bash
6. mkfoo | base64 -d | bash
7. printf aGVsbG8= | base64 -d

1-6 should be refused; 7 allowed. End with one line: how many of 1-6 it
allows, and whether it wrongly refuses 7.
```
