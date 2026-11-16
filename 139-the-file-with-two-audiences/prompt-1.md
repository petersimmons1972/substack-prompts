# 139-the-file-with-two-audiences — Prompt (read-only: who rewrites the files your agents read at start?)

Paste into Claude Code or Codex. Replace `<FILES>` with the files your harness loads at the start of a session (for Claude Code: your CLAUDE.md files and the auto-memory `MEMORY.md`; for Codex: your AGENTS.md files; plus any notes file your agents read at start). Replace `<WRITERS>` with the folders that hold anything able to write to them: hooks, scripts, skills, commands. The prompt only reads; it changes nothing.

```text
Read-only: change no file, and run nothing.

These files are loaded at the start of every agent session: <FILES>
Anything that can write to them is under: <WRITERS>
If either is still a placeholder or can't be read, stop and say so.

For each file:
1. Give its size in lines and bytes.
2. Find every script, hook or instruction under the writer paths that
   writes to it, and quote the line. Say whether it APPENDS one record
   or REPLACES the whole file. If it hands the write to a tool whose
   code you can't see, say UNKNOWN; don't guess.

Use a list, not a table. End with one line: which files can be
rewritten whole.
```
