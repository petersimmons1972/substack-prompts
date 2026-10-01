# 122-every-fact-was-true-except-the-first — Prompt 2 (FIX: repair exactly one connective)

Paste into Claude Code or Codex.

```text
You may change exactly one existing file, <FILE>, and exactly one link:
<LINK ID> from the AUDIT, whose sentence is: "<QUOTE THE SENTENCE>".

PATH RULE (check before anything else). Treat <FILE> as untrusted text.
It must be non-empty, must not start with "-", and may contain only
A-Z a-z 0-9 . _ - /  (no space, $, backtick, quote, backslash, semicolon,
parenthesis, pipe, < or >, * or ?, or newline). If it contains anything
else, reply "REFUSED: unsafe file name" and write nothing. In every command
below, write the path inside single quotes exactly as shown ('<FILE>'), and
put -- before it wherever the command accepts -- .

NEW-FILE CONTRACT. This run may create only four new files next to <FILE>,
each only if absent: '<FILE>.seamfix.orig.tmp', '<FILE>.seamfix.sha256.tmp',
'<FILE>.seamfix.orig' and '<FILE>.seamfix.sha256'. Never overwrite, rename
over, or delete a file that existed before this run.

Run each command on its own and check its exit status is 0 before using
its output, except diff in step 11: after the edit it exits 1 (differences
shown); 0 means the edit did not happen, so say so; any other status is an
error, which you report. Do not pipe a hash command into another command.

Refuse before touching anything:
1. If that link is not labelled SEQUENCE-AS-CAUSE, FRAMING or UNSUPPORTED in
   the AUDIT, or the sentence is not in <FILE>, stop and write nothing.
2. If any of the four new-file names already exists, stop and write
   nothing. Do not delete, open or rename it, and print no UNDO KEY. List
   the names and say: "These files were here before this run, so this run
   did not make them. If an earlier FIX of yours printed an UNDO KEY, run
   UNDO with that key. Without that key, inspect them by hand: UNDO
   without a key cannot tie them to your run."
3. Pick the hash tool: `sha256sum` if it exists, otherwise `shasum -a 256`
   (macOS). If neither exists, stop and write nothing.

Prepare (every failure in steps 4-7 goes to CLEANUP):
4. Hash the file with the tool alone:  sha256sum -- '<FILE>'
   (or  shasum -a 256 -- '<FILE>'). The exit status must be 0 and the
   first field must be 64 characters of 0-9a-f. Keep it as
   ORIGINAL-DIGEST. Then make a run nonce:  od -An -N16 -tx1 /dev/urandom ,
   with spaces and newlines removed. Exit status 0 and exactly 32
   characters of 0-9a-f, or stop (nothing has been written yet). Keep it
   as RUN-NONCE. Before writing any file, print one line:
   UNDO KEY: <ORIGINAL-DIGEST> <RUN-NONCE>
   and tell the user to keep it: UNDO cannot restore without it.
5. Write ORIGINAL-DIGEST, one space, RUN-NONCE and a newline into
   '<FILE>.seamfix.sha256.tmp'. Then copy byte for byte:
     cp -p -- '<FILE>' '<FILE>.seamfix.orig.tmp'
   If either write fails, go to CLEANUP.
6. Verify the copy:  cmp -- '<FILE>' '<FILE>.seamfix.orig.tmp'  must exit 0,
   and hashing the .tmp copy (exit status 0, 64 hex) must give
   ORIGINAL-DIGEST exactly. Otherwise go to CLEANUP.
7. Publish without overwriting:
     mv -n -- '<FILE>.seamfix.orig.tmp' '<FILE>.seamfix.orig'
     mv -n -- '<FILE>.seamfix.sha256.tmp' '<FILE>.seamfix.sha256'
   After each mv, the .tmp name must be gone and the final name present.
   If a .tmp name is still there, the final name appeared from elsewhere:
   go to CLEANUP and do not touch that final name.
8. Record two facts about the original: its count of carriage-return bytes
   (tr -cd '\r' < '<FILE>' | wc -c) and its final byte
   (tail -c 1 -- '<FILE>' | od -An -c).

CLEANUP (only for a failure in steps 4-7, before any edit):
   Remove only the files this run created in steps 5-7, the .orig names
   first: the .tmp names, and any final sidecar this run itself published
   in step 7. Use rm -- '<name>' one file at a time. Never touch <FILE>.
   Never remove a file that existed before this run. Report which step
   failed and what you removed. <FILE> is unchanged, and FIX can be run
   again. If CLEANUP is itself interrupted, UNDO with the printed key
   reports PARTIAL (its state C): it lists the leftovers with their sizes
   and digests and a REMOVE line for each, and removes one only when you paste its
   line back into a later UNDO.

Edit:
9. Change only the words of that one sentence, in one of two ways: add a
   source you have opened and can quote that states the connection, or
   rewrite the connective so it claims no more than the sources state (for
   example "then" in place of "so"). Change nothing else: no reflowing, no
   formatter, no whitespace cleanup, no line-ending conversion, no added or
   removed final newline. Edit that one line in place; do not re-save the
   file through any tool that rewrites line endings or the final newline.

After:
10. Re-count carriage returns and re-read the final byte. Both must equal the
    values from step 8. If either differs, say so and tell the user to run UNDO.
11. Show  diff -- '<FILE>.seamfix.orig' '<FILE>'  (plain diff, not git). Print
    the old digest, the new digest and the backup path. Leave both sidecar
    files in place: UNDO needs them.
Last, whatever step 10 found: hash '<FILE>' again (exit 0, 64 hex) and print
one line:
EDITED DIGEST: <digest>
UNDO uses it, with the UNDO KEY, to confirm the file is still the one FIX
left.
```
