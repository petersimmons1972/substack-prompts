# 122-every-fact-was-true-except-the-first — Prompt 3 (UNDO: restore the exact pre-FIX state)

Paste into Claude Code or Codex.

```text
Inputs, pasted by the user from their own FIX output or from an earlier
UNDO; never compute, guess or rebuild them:
- the line  UNDO KEY: <K> <N>  (K is 64 characters of 0-9a-f, N is 32);
- if FIX got that far, the line  EDITED DIGEST: <E>  (64 of 0-9a-f);
- only on a run after step 6 stopped: the line  OVERWRITE: <digest> ;
- zero or more lines exactly of the form  REMOVE '<name>' <digest>
  (64 of 0-9a-f), each copied from a list an earlier UNDO printed
  (a PARTIAL or a REPORT ONLY run).
Anything else counts as missing. You never write, complete or correct a
REMOVE or OVERWRITE line yourself, and you never act on a line you printed
until the user pastes it back on a later run.

Tell the user first: Run UNDO while nothing else is changing these files.

You may write only '<FILE>' (step 7). You may delete only names in this
fixed set, and only as steps 9 and 13 allow:
  '<FILE>.seamfix.orig'  '<FILE>.seamfix.sha256'
  '<FILE>.seamfix.orig.tmp'  '<FILE>.seamfix.sha256.tmp'
You create no file. Apply FIX's PATH RULE to <FILE> first; if it fails,
reply "REFUSED: unsafe file name" and write nothing. Write every path inside
single quotes, with -- before it wherever the command accepts -- . No git. Check each command's exit status is 0 before
using its output, except cmp and diff (0 identical, 1 different, any other
status is an error: stop and change nothing).

Keep one list for this whole run, CONFIRMED-REMOVED, empty at the start.
Every result you print names what is in it; "nothing changed" and
"deleted nothing" may be printed only while it is empty.

1. Hash tool: sha256sum, else shasum -a 256. A digest counts only if the
   exit status is 0 and the first field is 64 characters of 0-9a-f. The
   tool and the hash of '<FILE>' must succeed; otherwise stop and change
   nothing. A sidecar whose hash fails is "digest unavailable": it is
   never removed, never verified, and gets no REMOVE line.
2. Hash '<FILE>' now; call it CURRENT. List which of the four names exist.
   Check every pasted REMOVE line's name against the fixed set now: an
   out-of-set name gets "REFUSED: <name> is not a FIX file name" and is
   dropped from this run, whatever the state.
3. No valid UNDO KEY: go to KEYLESS (step 15).
4. With the key, RUN-LINE is K, one space, N and a newline. The one
   manifest UNDO trusts is the published '<FILE>.seamfix.sha256' whose whole
   content is RUN-LINE. Classify BEFORE acting on any REMOVE line:
   A. None of the four names exists. For each pasted in-set REMOVE line
      print "already gone: <name>". If CURRENT equals K, reply "Nothing to undo:
      the file matches the key and no FIX file is present." Otherwise
      reply "No FIX file is present and the file differs from the key;
      nothing changed." Write nothing.
   B. '<FILE>.seamfix.orig' and '<FILE>.seamfix.sha256' both exist and neither
      .tmp name exists: check step 5. If it passes, this is a verified
      pair: print "REMOVE lines ignored: this run has a verified FIX pair"
      if any were pasted, and go to RESTORE. If step 5 fails, go to
      C-PATH.
   C. Any other combination: go to C-PATH. Never reply "Nothing to
      undo." here.
5. (check) The whole content of '<FILE>.seamfix.sha256' must be RUN-LINE,
   and hashing '<FILE>.seamfix.orig' must give K.

RESTORE (a verified pair):
6. CURRENT must equal K or E. If it equals neither, run
   diff -- '<FILE>.seamfix.orig' '<FILE>' , show it, say "The file changed
   after FIX; UNDO will not overwrite it", print CURRENT and
   CONFIRMED-REMOVED, and stop. Only on a later run with
   OVERWRITE: <digest>  equal to CURRENT as hashed on that run, go on.
7. If CURRENT equals K, skip the copy. Otherwise restore by byte copy
   only:
   cp -p -- '<FILE>.seamfix.orig' '<FILE>'
   Do not open and re-save the file in an editor.
8. Hash '<FILE>' and run  cmp -- '<FILE>' '<FILE>.seamfix.orig' . Go on only
   if the digest equals K and cmp exits 0. Otherwise FAIL: change nothing
   more, and report, naming CONFIRMED-REMOVED.
9. rm -- '<FILE>.seamfix.orig' , then rm -- '<FILE>.seamfix.sha256' . Confirm
   each is gone. If CONFIRMED-REMOVED is empty, reply "PASS: verified
   restore; every FIX file removed." Otherwise reply "PASS (<n> removed on
   your confirmation: <names>; restore verified)". If an rm fails, report
   which name remains and stop; a later UNDO lands in C-PATH.

C-PATH (state C, or a pair that failed step 5):
9b. PROTECTED PAIR. If both final names exist and step 5 passes for them
    even though a .tmp name is present, they are a verified pair: mark both
    PROTECTED. A PROTECTED name is never offered a REMOVE line, and a
    pasted REMOVE line for it is ignored ("ignored: part of a verified FIX
    pair"). Only the .tmp names can be confirmed; once they are gone, step
    11c restores from the pair.
10. If REMOVE lines were pasted, run CONFIRMED REMOVAL (step 13) on the
    non-PROTECTED names, then hash '<FILE>' again (CURRENT) and list the
    names left.
11. Decide on what is left:
    a. No fixed-set name is left and CURRENT equals K: if
       CONFIRMED-REMOVED is empty, reply as state A. Otherwise reply
       "PASS (<n> removed on your confirmation: <names>): the file matches
       your key and no FIX file remains."
    b. No fixed-set name is left and CURRENT does not equal K: PARTIAL
       (step 12), saying "no FIX file remains".
    c. What is left is exactly the two final names, no .tmp, and step 5
       passes: go to RESTORE (step 6); its result carries
       CONFIRMED-REMOVED.
    d. Anything else: PARTIAL (step 12).
12. PARTIAL. Never PASS. Beyond step 13's removals, write, copy, rename
    and delete nothing, and never touch '<FILE>'.
    - For each fixed-set name left, print its name, size and digest
      ("digest unavailable" if the hash fails), and one line
        REMOVE '<that name>' <its digest>
      for each name whose digest is available and that is not PROTECTED.
      Label a PROTECTED name "verified FIX backup; kept for restore".
    - Print CURRENT and K and whether they are equal. If they differ,
      print the manual restore step: restore '<FILE>' only from a listed
      copy whose digest equals K, with diff, cp -p and a cmp check, by
      hand; if no listed copy's digest equals K, restore from none. UNDO
      does not restore on this path unless step 11c applies.
    - Reply "PARTIAL: UNDO cannot verify these files against your FIX
      run." If CONFIRMED-REMOVED is empty, add "It deleted nothing."
      Otherwise add "Removed on your confirmation this run: <names>."
      Then: "Each file above may not be from your run. To have UNDO
      remove one, run UNDO again with your UNDO KEY and paste its REMOVE
      line. UNDO removes it only if it is unchanged."

CONFIRMED REMOVAL (step 13, reached only from steps 10 and 15):
13. For each pasted REMOVE line, in order:
    a. The name must be exactly one of the four fixed-set names for
       '<FILE>'. Otherwise print "REFUSED: <name> is not a FIX file name"
       and skip it. Never remove '<FILE>' or any other path.
    b. If the name does not exist, print "already gone: <name>" and skip.
    c. If it is PROTECTED (step 9b), print "ignored: part of a verified
       FIX pair" and skip. Hash it now. If the hash fails, print "cannot
       read <name>; left in place" and skip. If the digest is not the one
       in the line, print "changed since you confirmed; left in place:
       <name>" and skip.
    d. rm -- '<name>', confirm it is gone, and add it to
       CONFIRMED-REMOVED.
14. (reserved)

KEYLESS (no valid UNDO KEY):
15. Never evaluate K, never RESTORE, never report PASS. Nothing is
    PROTECTED without a key. If REMOVE lines were pasted, run CONFIRMED
    REMOVAL (step 13). Then, for each fixed-set name left, print its name,
    size and digest ("digest unavailable" if the hash fails) and, when the
    digest is available, its REMOVE line; print CURRENT. Reply "No UNDO KEY, so the file is not checked against a
    FIX run." Then either "Nothing changed." (CONFIRMED-REMOVED empty) or
    "Removed on your confirmation: <names>." and "Remaining: <names or
    none>." A kill during step 13 leaves a smaller set, which the next run
    lists again.
```
