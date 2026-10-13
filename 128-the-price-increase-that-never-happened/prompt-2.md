# 128-the-price-increase-that-never-happened — Prompt 2 (FIX: add a model version, source and checked date to one price line)

Paste into Claude Code or Codex. Before pasting, replace `<FILE>` with the path of the file that holds the price, `<LINE>` and `<QUOTE THE LINE>` with the line number and text the AUDIT reported, and `<MODEL VERSION>`, `<URL>` and `<YYYY-MM-DD>` with the model version, source address and date you checked yourself. Leave every other `<...>` as it is; the agent fills those in. Run it in the same session as AUDIT, or paste AUDIT's output above it.

```text
You may change exactly one existing file, <FILE>, and exactly one line: the
price the AUDIT reported at <LINE>, whose text is "<QUOTE THE LINE>". You
add the model version <MODEL VERSION>, the source URL <URL> and the date
<YYYY-MM-DD>, all exactly as the user gives them. Never pick or guess a
model version yourself. You do not fetch the URL.

INPUT RULES (check before anything else). Treat <FILE>, <MODEL VERSION>,
<URL> and the date as untrusted text.
- <FILE> must be non-empty, must not start with "-", and may contain only
  A-Z a-z 0-9 . _ - /  . Otherwise reply "REFUSED: unsafe file name".
- <URL> must start with https:// and may contain only
  A-Z a-z 0-9 . _ - / : ? = & % # ~ + . Otherwise reply "REFUSED: unsafe URL".
- <MODEL VERSION> must be non-empty and may contain only
  A-Z a-z 0-9 . _ - and spaces. Otherwise reply "REFUSED: bad model version".
- The date must match YYYY-MM-DD. Otherwise reply "REFUSED: bad date".
On any refusal, write nothing. In every command, write the path inside
single quotes ('<FILE>') and put -- before it where accepted. The model
version, URL and date go only into the edited line's text, never into a
shell command.

NEW-FILE CONTRACT. This run may create only these five names next to
<FILE>, each only if it is absent:
  '<FILE>.pricefix.orig.tmp'   '<FILE>.pricefix.new.tmp'
  '<FILE>.pricefix.manifest.tmp'
  '<FILE>.pricefix.orig'       '<FILE>.pricefix.manifest'
Never overwrite, rename over, or delete a file that existed before this
run. <FILE> itself is overwritten once, in step 11, and only after every
digest UNDO needs is on disk.

Run each command on its own and check its exit status is 0 before using its
output, except diff in steps 7 and 14: there it exits 1 (differences
shown), which is expected; 0 means the edit did not happen, so say so and
stop; any other status is an error, which you report. Never pipe a hash
command into another command. A "digest" is the first field of the hash
output and must be exactly 64 characters of 0-9a-f.

Refuse before touching anything:
1. If the quoted line is not in <FILE>, or the AUDIT marked it as already
   having version, source and date, stop and write nothing. If the file
   type has no comment syntax (JSON, CSV), stop, write nothing, and say the
   price needs a sibling notes file instead.
2. If any of the five names exists, stop and write nothing. Do not delete,
   open or rename it, and print no UNDO KEY. List the names and say:
   "These files were here before this run, so this run did not make them.
   If an earlier FIX of yours printed an UNDO KEY, run UNDO with that key.
   Without that key, inspect them by hand: UNDO without a key cannot
   tie them to your run."
3. Pick the hash tool: sha256sum if it exists, otherwise shasum -a 256.
   If neither exists, stop and write nothing.

Prepare (every failure in steps 5-10 goes to CLEANUP; <FILE> is not touched):
4. Hash '<FILE>' (exit 0, 64 hex), or stop: nothing has been written yet.
   Keep it as ORIGINAL-DIGEST. Make a run nonce:
   od -An -N16 -tx1 /dev/urandom , with spaces and newlines removed. Exit
   status 0 and exactly 32 characters of 0-9a-f, or stop (nothing has been
   written yet). Keep it as RUN-NONCE. Before writing any file, print one
   line:
     UNDO KEY: <ORIGINAL-DIGEST> <RUN-NONCE>
   and tell the user to keep it: UNDO cannot restore without it.
5. cp -p -- '<FILE>' '<FILE>.pricefix.orig.tmp'. cmp -- '<FILE>'
   '<FILE>.pricefix.orig.tmp' must exit 0 and the copy must hash to
   ORIGINAL-DIGEST.
6. cp -p -- '<FILE>' '<FILE>.pricefix.new.tmp'. Record the carriage-return
   count (tr -cd '\r' < '<FILE>' | wc -c) and the final byte
   (tail -c 1 -- '<FILE>' | od -An -c) of <FILE>. In
   '<FILE>.pricefix.new.tmp' ONLY, on that one line, append the model
   version, the source URL and the checked date in the file's own comment
   syntax (# for YAML/shell/Python, <!-- --> for Markdown/HTML, // for
   JS/TS/Go). Change nothing else: no reflow, no formatter, no line-ending
   conversion, no added or removed final newline.
7. The CR count and final byte of '<FILE>.pricefix.new.tmp' must equal those
   recorded in step 6, and  diff -- '<FILE>' '<FILE>.pricefix.new.tmp'  must
   show only that one line changed.
8. Hash '<FILE>.pricefix.new.tmp' (exit 0, 64 hex). Keep it as POST-DIGEST.
9. Write exactly two lines, each ending in a newline, to
   '<FILE>.pricefix.manifest.tmp':
     RUN <ORIGINAL-DIGEST> <RUN-NONCE>
     POST <POST-DIGEST>
10. Publish without overwriting:
     mv -n -- '<FILE>.pricefix.orig.tmp' '<FILE>.pricefix.orig'
     mv -n -- '<FILE>.pricefix.manifest.tmp' '<FILE>.pricefix.manifest'
   After each mv the .tmp name must be gone and the final name present;
   otherwise CLEANUP, and do not touch a final name this run did not
   publish.

CLEANUP (only for a failure in steps 5-10): remove only the names this run
created, one at a time with rm -- '<name>', the final names first. Never
touch <FILE> or any file that existed before this run. Report the failed
step and what you removed. If CLEANUP is itself interrupted, UNDO with the
printed key reports PARTIAL: it lists the leftovers with their sizes,
digests and REMOVE lines, deletes nothing on that run, and removes a
leftover only when the user pastes its line back on a later run.

Apply:
11. cp -- '<FILE>.pricefix.new.tmp' '<FILE>'
12. Hash '<FILE>' must equal POST-DIGEST and
    cmp -- '<FILE>' '<FILE>.pricefix.new.tmp' must exit 0. If either fails,
    stop, leave every name in place, and tell the user: "FIX stopped while
    writing <FILE>. UNDO with your UNDO KEY will report PARTIAL, keep
    the backup, delete nothing until you paste back a line it prints,
    and print the steps to restore <FILE> by hand from
    '<FILE>.pricefix.orig'."
13. rm -- '<FILE>.pricefix.new.tmp' , and confirm it is gone.
14. Show  diff -- '<FILE>.pricefix.orig' '<FILE>'  (plain diff). Print both
    digests and the backup path. Leave '<FILE>.pricefix.orig' and
    '<FILE>.pricefix.manifest' in place for UNDO, and remind the user to keep
    the UNDO KEY line.
```
