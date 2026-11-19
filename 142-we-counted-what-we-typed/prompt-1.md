# 142-we-counted-what-we-typed — Prompt (read-only: does your tag rule count what your publisher sends?)

Paste into Claude Code or Codex. Replace `<FOLDER>` with the folder of Markdown posts to check, `<PUBLISHER>` with the script that publishes your tags, and `<LOW>` and `<HIGH>` with your rule's range (ours was 5 to 7). The prompt only reads; it changes nothing and never runs your publisher.

```text
Read-only: change no file, and run nothing, including the publisher.

Posts: <FOLDER>
Publisher script: <PUBLISHER>
Rule: each post needs <LOW> to <HIGH> tags.
If any of these is still a placeholder or can't be read, stop and say so.

Read the publisher and quote the lines that decide which tags it sends:
which tag list it reads first, any tags it adds, any it drops, and its
maximum.

Then, for each post, give the number of tags typed in its front matter
and the tags the publisher would send. Say whether the rule passes the
typed count and whether it would pass the sent count.

Use a list, not a table. End with one line: how many posts get a
different verdict.
```
