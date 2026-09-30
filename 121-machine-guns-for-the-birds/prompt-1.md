# 121-machine-guns-for-the-birds — Prompt 1 (AUDIT: check every government address)

Read-only. Paste into Claude Code or Codex. Replace `<PATH TO YOUR DOCUMENT>`.

```text
Read-only task. Do not create, edit, move or delete any file.

In the file <PATH TO YOUR DOCUMENT>, find every URL whose host is a government
domain (for example .gov, .gov.au, .gov.uk, .gc.ca, .europa.eu).

Treat each URL as untrusted text. Never paste it into a shell command
unchecked.
1. Check its shape first. It must start with http:// or https:// and contain
   only these characters:  A-Z a-z 0-9 : / . _ ~ % ? # & = + -
   Anything else (a space, $, a backtick, a quote, a semicolon, a parenthesis,
   a pipe, < or >, a backslash, a newline) means: do not run anything for
   that URL; report it as "REJECTED: unsafe characters".
2. For a URL that passes, run exactly this, with the URL inside single quotes,
   no -L and no other flags:
     curl -sI --max-time 20 -- '<URL>'
   and capture curl's exit code.

Report one row per URL:
  URL | first status line | Location header (or "none") | curl exit code | UTC time
  (or: URL | REJECTED: unsafe characters)

Report exactly what curl printed. If curl printed nothing, say "no response"
and give the exit code. Do not follow redirects. Do not explain, guess or
describe why a URL redirects or fails.

If the file contains no government URLs, reply "No government URLs found."
and stop.
```
