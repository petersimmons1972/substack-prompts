# 128-the-price-increase-that-never-happened — Prompt 3 (UNDO: restore the exact pre-FIX state)

Paste into Claude Code or Codex. Before pasting, replace every `<FILE>` with the same path you gave FIX.

```text
<FILE> is the path of the one file FIX edited, as the user gave it to FIX.
Inputs, pasted by the user from their own FIX output or from an earlier
UNDO; never compute, guess or rebuild them:
- the line  UNDO KEY: <K> <N>  (K is 64 characters of 0-9a-f, N is 32
  characters of 0-9a-f);
- zero or more lines exactly of the form  REMOVE '<name>' <digest>
  (64 of 0-9a-f), each copied from a list an earlier UNDO printed.
Anything else counts as missing. You never write, complete or correct a
REMOVE line yourself, and you never act on a line you printed until the
user pastes it back on a later run.

Tell the user first: Run UNDO while nothing else is changing these files.

You may write only '<FILE>' (step 7). You may delete only the five names
FIX may create, and only as steps 4a, 9 and 13 allow:
  '<FILE>.pricefix.orig'  '<FILE>.pricefix.manifest'
  '<FILE>.pricefix.orig.tmp'  '<FILE>.pricefix.new.tmp'
  '<FILE>.pricefix.manifest.tmp'
Never remove '<FILE>' or any other path. You create no file. Check <FILE>
first, treating it as untrusted text: <FILE> must be non-empty, must not
start with "-", and may contain only
  A-Z a-z 0-9 . _ - /  . Otherwise reply "REFUSED: unsafe file name"
and write nothing. Quote every path in single quotes; use -- where
accepted. No git. Run each command on its own and check its exit status is
0 before using its output, except cmp and diff, whose status a step below
reads on purpose. For diff, 0 means the files are identical and 1 means it
showed differences; any other diff status is an error: stop and change
nothing.

Keep one list for this whole run, CONFIRMED-REMOVED, empty at the start.
Every result you print names what is in it; "nothing changed" and
"deleted nothing" may be printed only while it is empty and step 4a
removed nothing.

1. Hash tool: sha256sum, else shasum -a 256. A digest counts only if the
   exit status is 0 and the first field is 64 characters of 0-9a-f.
   The tool and the hash of '<FILE>' (when it exists) must succeed;
   otherwise stop and change nothing. A FIX name whose hash fails is
   "digest unavailable": it is never removed, never verified, never
   PROTECTED, and gets no REMOVE line.
2. Hash '<FILE>' now; call the digest CURRENT (if <FILE> is missing,
   CURRENT is "missing"). List which of the five names exist.
3. No valid UNDO KEY: go to KEYLESS (step 14).
4. With the key: the one manifest UNDO trusts is the published
   '<FILE>.pricefix.manifest' whose whole content is exactly two lines, each
   ending in a newline: "RUN " followed by the key's K, a space and the
   key's N; then "POST " followed by 64 characters of 0-9a-f (call that
   digest P). FIX printed the key only after checking that none of the
   five names existed and before writing anything, so the nonce ties that
   manifest to the user's own run. Without a pasted REMOVE line, UNDO
   deletes a file only when that manifest verifies and the backup's digest
   equals K, and then the manifest itself; or the manifest alone, in step
   4a.
   PROTECT first, before acting on any REMOVE line: a manifest that has
   this form is PROTECTED on its own; record its digest now. It stays
   PROTECTED when '<FILE>.pricefix.orig' is missing, when another name
   fails its digest check, and when '<FILE>' was edited after FIX.
   '<FILE>.pricefix.orig' is PROTECTED when it hashes to K and that
   manifest is PROTECTED; the two are then a verified pair. They stay
   PROTECTED even when a .tmp name is present or '<FILE>' is torn. A lone
   '<FILE>.pricefix.orig', a manifest that fails this form, and every .tmp
   name are never PROTECTED.
   Then check every pasted REMOVE line: a name outside the five gets
   "REFUSED: <name> is not a FIX file name"; a PROTECTED name gets
   "ignored: verified FIX file"; a name that does not exist gets "already
   gone: <name>". Drop each such line from this run. If lines are left,
   run CONFIRMED REMOVAL (step 13), then hash '<FILE>' again (CURRENT)
   and list the names left.
4a. VERIFIED MANIFEST CLEANUP (on any run): if the manifest is PROTECTED,
   none of the other four names left has a digest equal to K or to P (the
   two digests it records), and a fresh hash of it equals the digest
   recorded in step 4: rm -- '<FILE>.pricefix.manifest' , confirm it is
   gone, and print  removed (verified): '<FILE>.pricefix.manifest' . This
   is the row's own verified cleanup, not a confirmation: it is not added
   to CONFIRMED-REMOVED and not counted in a PASS label. If the fresh
   digest differs, leave it in place. Every result of this run prints that
   line when step 4a ran. Then pick exactly one state on what is left:
   A. None of the five names exists. If CURRENT equals K, reply "Nothing
      to undo: the file matches the key and no FIX file is present." when
      CONFIRMED-REMOVED is empty and step 4a removed nothing; "PASS: the
      file matches your key and no FIX file remains." when
      CONFIRMED-REMOVED is empty and step 4a removed the manifest;
      otherwise "PASS (<n> removed on your confirmation: <names>): the
      file matches your key and no FIX file remains." If CURRENT does not
      equal K, reply "No FIX file is present and the file differs from the
      key; nothing changed." when CONFIRMED-REMOVED is empty and step 4a
      removed nothing, otherwise go to PARTIAL and say "no FIX file
      remains". Write nothing more either way.
   B. '<FILE>.pricefix.orig' and '<FILE>.pricefix.manifest' both exist and none of
      the three .tmp names exists: go to RESTORE.
   C. Any other combination (any .tmp name present, or only one of the
      two final names): an interrupted, torn or unproven run. Go to
      PARTIAL. Never reply "Nothing to undo." in state C.

RESTORE (state B):
5. The manifest must have exactly the form in step 4 with the key's K and
   N, and hashing '<FILE>.pricefix.orig' must give K. Otherwise go to PARTIAL
   without writing anything: the manifest is malformed or from another
   run, or the backup is damaged.
6. CURRENT must be K (FIX's edit is already undone) or P (the file FIX
   left). If it is neither, run
   diff -- '<FILE>.pricefix.orig' '<FILE>'  (0 or 1, per the rule above), show
   it, print CURRENT and CONFIRMED-REMOVED, reply "REFUSED: <FILE> changed
   after FIX; UNDO will not overwrite it", and stop, changing nothing more.
7. If CURRENT equals K, skip the copy. Otherwise:
   cp -p -- '<FILE>.pricefix.orig' '<FILE>'
8. Hash '<FILE>' and run  cmp -- '<FILE>' '<FILE>.pricefix.orig' . Continue
   only if the hash exits 0, its digest equals K and cmp exits 0.
   Otherwise FAIL: change nothing more, and report, naming
   CONFIRMED-REMOVED.
9. Remove FIX's files one at a time, the backup first:
   rm -- '<FILE>.pricefix.orig'  then  rm -- '<FILE>.pricefix.manifest' .
   Confirm each is gone. Report PASS only when both are gone: '<FILE>' is
   then byte-identical to its pre-FIX bytes by hash and cmp, and every
   file FIX created is removed, so the directory is back to its pre-FIX
   state. If CONFIRMED-REMOVED is empty, reply "PASS: verified restore;
   every FIX file removed." Otherwise reply "PASS (<n> removed on your
   confirmation: <names>; restore verified)". If an rm fails, report which
   name remains and stop; a later UNDO finds the pair again (state B), or
   the manifest alone, which step 4a removes.

PARTIAL (state C, a failed step 5, or state A after a confirmed or
verified removal with CURRENT not K). Never PASS. Beyond step 13's
removals and step 4a's verified removal, write, copy, rename and delete
nothing, and never touch '<FILE>'.
10. For each of the five names left, print its name, its size in bytes
    (wc -c < '<that name>') and its digest (the hash tool on that file
    alone; if it does not exit 0 with 64 characters of 0-9a-f, print
    "digest unavailable"), and one line
      REMOVE '<that name>' <its digest>
    for each name that is not PROTECTED and whose digest is available.
    Label a PROTECTED name "verified FIX backup; kept for restore". Print
    CURRENT and K, and whether they are equal.
11. Reply "PARTIAL: UNDO cannot verify these files against your FIX run."
    If CONFIRMED-REMOVED is empty and step 4a removed nothing, add "It
    deleted nothing." If CONFIRMED-REMOVED is not empty, add "Removed on
    your confirmation this run: <names>." Then: "Each file
    above may not be from your run. To have UNDO remove one, run UNDO
    again with your UNDO KEY and paste its REMOVE line. UNDO removes it
    only if it is unchanged." Then print the restore steps in step 12 for
    the user to follow by hand. Do not run any of them yourself.
12. Restore steps (print them with the real names):
    a. If CURRENT equals K, '<FILE>' already holds its pre-FIX bytes: do
       not copy anything over it.
    b. If CURRENT does not equal K, '<FILE>' changed after FIX started:
       FIX may have stopped while writing it, or it was edited since.
       Restore it only from a listed copy whose digest above equals K
       (your own key, so that copy holds your pre-FIX bytes): first
       diff -- '<that copy>' '<FILE>'  to see what you would lose, then
       cp -p -- '<that copy>' '<FILE>' , then check that
       cmp -- '<that copy>' '<FILE>'  exits 0 and '<FILE>' hashes to K. A
       '.new.tmp' is an edited draft and is never a restore source. If no
       listed copy's digest equals K, restore from none of them.
    c. If the backup and manifest are listed as "verified FIX backup;
       kept for restore", UNDO finishes from them itself once no other
       FIX name is left: it restores when '<FILE>' is K or P, and
       otherwise refuses (step 6), so restore a torn or edited '<FILE>'
       by hand with step b first.
    d. FIX refuses to start while any of the five names exists.

CONFIRMED REMOVAL (step 13; reached only from steps 4 and 14, and only for
lines pasted on this run):
13. For each line left from step 4 (or step 14), in order: hash the name
    now. If the hash fails, print "cannot read <name>; left in place" and
    skip it. If the digest is not the one in the line, print "changed
    since you confirmed; left in place: <name>" and skip it. Otherwise
    rm -- '<name>' , confirm it is gone, and add it to CONFIRMED-REMOVED.
    A kill during this step leaves a smaller set, which the next run lists
    again with fresh REMOVE lines.

KEYLESS (no valid UNDO KEY):
14. Never evaluate K, never RESTORE, never report PASS. Nothing is
    PROTECTED without a key. Check every pasted REMOVE line as in step 4
    (a name outside the five is REFUSED; an absent name is "already
    gone"), then run CONFIRMED REMOVAL (step 13) on the rest. Then, for
    each of the five names left, print its name, size and digest ("digest
    unavailable" if the hash fails) and, when the digest is available, its
    REMOVE line; print CURRENT. Reply "No UNDO KEY, so the file is not
    checked against a FIX run." Then either "Nothing changed."
    (CONFIRMED-REMOVED empty) or "Removed on your confirmation: <names>."
    and "Remaining: <names or none>."
```
