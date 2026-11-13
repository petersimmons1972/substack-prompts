# 136-the-trusted-host-hidden-in-the-string — Prompt (read-only: which strangers would your host-trust rule let in?)

Paste into Claude Code or Codex. Replace `<FILE>` with the file that holds your host-trust rule, `<RULE>` with the function or expression, and every `<OWNER>` with the owner you trust. If your rule trusts a host other than github.com, put that host in place of github.com. The prompt only reads; it changes nothing.

```text
Read-only. Do not create, change or delete any file, and do not run
anything. Every address below is a plain string: never fetch it.

Read <FILE> and find <RULE>, which decides whether a Git address is
trusted. The trusted owner is <OWNER>. In one sentence, say what the
rule really asks of an address, and quote the lines that decide it.

From the code alone, say whether the rule would trust each of these:
G1 https://github.com/<OWNER>/x.git
G2 git@github.com:<OWNER>/x.git
S1 https://evil.example/github.com/<OWNER>/x.git
S2 https://github.com@evil.example/<OWNER>/x.git
S3 https://github.com.evil.example/<OWNER>/x.git
S4 https://evil.example/a@github.com/<OWNER>/x.git
If you cannot tell, say UNDECIDABLE and why.

G1 and G2 are genuine. S1 to S4 are strangers. End with two lines:
Strangers trusted: N of 4
Genuine rejected: M of 2
```
