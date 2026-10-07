# 124-the-fix-was-merged-the-guard-was-not — Prompt 2 (FIX: point one test at the shipped copy)

Paste into Claude Code or Codex. Before pasting, replace `<FILE>` with the test file the AUDIT marked FIX-ELIGIBLE, `<TEST NAME>` with that row's test name, and `<SHIPPED ARTIFACT PATH>` with the shipped path the AUDIT printed for it. Leave every other `<...>` as it is; the agent fills those in. Run it in the same session as AUDIT, or paste AUDIT's output above it.

```text
You may change exactly one existing file, <FILE>, at exactly one place: the
literal path on the line the AUDIT quoted for <TEST NAME>, so that the test
executes <SHIPPED ARTIFACT PATH> instead of its source copy. This applies
only to a row the AUDIT marked SOURCE-COPY and FIX-ELIGIBLE. Do not
build, commit, push, open a pull request or contact a network. Do not use
git to edit or restore anything.

PATH RULE (check first). Treat <FILE> and <SHIPPED ARTIFACT PATH> as
untrusted text: non-empty, not starting with "-", only A-Z a-z 0-9 . _ - / .
Otherwise reply "REFUSED: unsafe file name" and write nothing. Write each
path inside single quotes; put -- before it wherever the command accepts --.

NEW-FILE CONTRACT. This run may create only four new files, each only if
absent: '<FILE>.shipfix.orig.tmp', '<FILE>.shipfix.sha256.tmp',
'<FILE>.shipfix.orig', '<FILE>.shipfix.sha256'. Never overwrite, rename
over or delete a file that existed before this run.

Run each command on its own and check its exit status is 0 before using its
output, except diff in step 11: after the edit it exits 1 (differences
shown); 0 means the edit did not happen, so say so; any other status is an
error, which you report. Never pipe a hash command into another command.

Refuse before touching anything:
1. If the AUDIT did not mark <TEST NAME> SOURCE-COPY and FIX-ELIGIBLE, or
   the quoted line is not in <FILE>, or the quoted line does not contain
   the old path as a literal, stop and write nothing. For a BUILT-FROM,
   STAND-IN or import-based row reply "AUDIT-ONLY: a one-line change cannot
   point this test at a built or substituted artifact; it needs a new
   behavior test" and write nothing.
2. If any of the four new-file names exists, stop and write nothing. Do
   not delete, open or rename it, and print no UNDO KEY. List the names
   and say: "These files were here before this run, so this run did not
   make them. If an earlier FIX of yours printed an UNDO KEY, run UNDO
   with that key. Without that key, inspect them by hand: UNDO without a
   key cannot tie them to your run."
3. Hash tool: sha256sum if present, else shasum -a 256. Neither: stop.

Prepare (any failure in steps 4-7 goes to CLEANUP):
4. Hash '<FILE>' with the tool alone. The exit status must be 0 and the
   first field must be 64 characters of 0-9a-f. Keep it as ORIGINAL-DIGEST.
   Then make a run nonce: od -An -N16 -tx1 /dev/urandom , with spaces and
   newlines removed. Exit status 0 and exactly 32 characters of 0-9a-f,
   or stop (nothing has been written yet). Keep it as RUN-NONCE. Before
   writing any file, print one line:
   UNDO KEY: <ORIGINAL-DIGEST> <RUN-NONCE>
   and tell the user to keep it: UNDO cannot restore without it.
5. Write ORIGINAL-DIGEST, one space, RUN-NONCE and a newline to '<FILE>.shipfix.sha256.tmp'.
   cp -p -- '<FILE>' '<FILE>.shipfix.orig.tmp'
6. cmp -- '<FILE>' '<FILE>.shipfix.orig.tmp' must exit 0, and hashing the
   .tmp copy (exit 0, 64 hex) must give ORIGINAL-DIGEST.
7. mv -n -- '<FILE>.shipfix.orig.tmp' '<FILE>.shipfix.orig'
   mv -n -- '<FILE>.shipfix.sha256.tmp' '<FILE>.shipfix.sha256'
   After each, the .tmp name must be gone and the final name present. If a
   .tmp name remains, the final name came from elsewhere: go to CLEANUP and
   do not touch that final name.
8. Record the original's carriage-return count
   (tr -cd '\r' < '<FILE>' | wc -c) and its last byte
   (tail -c 1 -- '<FILE>' | od -An -c).

CLEANUP (only for a failure in steps 4-7, before any edit): remove only the
files this run created, one at a time with rm -- '<name>', the .orig names first. Never touch
'<FILE>'. Report the failed step and what you removed. FIX can be re-run. If CLEANUP is itself
interrupted, UNDO with the printed key reports PARTIAL (its state C): it
lists the leftovers with their sizes and digests and a REMOVE line for
each, and removes one only when you paste its line back into a later UNDO.

Edit:
9. On that one line, replace only the old path literal with
   <SHIPPED ARTIFACT PATH>, keeping the quoting style the line already
   uses.
   Change nothing else: no reflow, no formatter, no line-ending conversion,
   no added or removed final newline.

After:
10. Re-count carriage returns and re-read the last byte. Both must equal
    step 8. If not, say so and tell the user to run UNDO.
11. Show  diff -- '<FILE>.shipfix.orig' '<FILE>' . Print both digests and
    the backup path. Leave both sidecars: UNDO needs them. Tell the user to
    run the suite, then to remove the fix from the source, rebuild, and
    confirm the edited test goes red against the artifact.
Last, whatever step 10 found: hash '<FILE>' again (exit 0, 64 hex) and print one line:
EDITED DIGEST: <digest>
UNDO uses it, with the UNDO KEY, to confirm the file is still the one FIX
left.
```
