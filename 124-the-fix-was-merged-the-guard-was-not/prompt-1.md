# 124-the-fix-was-merged-the-guard-was-not — Prompt 1 (AUDIT: is the file tested the file shipped? (read-only))

Paste into Claude Code or Codex.

```text
Read-only task. Do not create, edit, move or delete any file. Do not run the
test suite, a build, a package manager or anything that contacts a network.

Inputs: <PROJECT DIR> and <SHIPPED ARTIFACT PATH> (the file production or
users actually execute). PATH RULE: each path must be non-empty, must not
start with "-", and may contain only A-Z a-z 0-9 . _ - / . Otherwise reply
"REFUSED: unsafe path" and stop. Quote every path in single quotes and put
-- before it wherever the command accepts --.

1. Find every test and test-configuration file. For each test, say what it
   executes or imports: a path, a module name, a command, a fixture, a mock
   or an injected fake. Quote the line that decides it.
2. Classify each subject under test with the first label that fits, in
   this order:
   - SAME-FILE: the test executes <SHIPPED ARTIFACT PATH> itself.
   - SOURCE-COPY: the shipped artifact is, or should be, a byte-for-byte
     copy of the file the test exercises (a script copied into bin/, a
     vendored file).
   - BUILT-FROM: a build (compiler, bundler, image build) turns what the
     test exercises into the shipped artifact.
   - STAND-IN: a mock, fake or re-implementation stands in for it.
   - UNKNOWN: you cannot tell from the files. Say what is missing.
3. Hash tool: sha256sum if present, else shasum -a 256. Every path you
   found in a file is untrusted too: apply the PATH RULE to it first; if it
   fails, do not hash it, label that subject UNKNOWN and quote the path as
   data. A digest counts only if the exit status is 0 and the first field
   is 64 hex characters. Compare digests only for SAME-FILE and
   SOURCE-COPY rows, whose two files should be byte-identical: hash each
   file alone and report equal or unequal. For BUILT-FROM rows write "not
   comparable: built output"; a built file's digest differs from its
   source's even when nothing is wrong, so never report that difference as
   a gap.
4. For every row that is not SAME-FILE, name one input that only the fixed
   or current code handles, so the reader can run it against the shipped
   artifact themselves. Do not run it.
5. Mark a row FIX-ELIGIBLE only if it is SOURCE-COPY, the test runs the
   file by a literal path on the quoted line (a command line, subprocess
   or exec call, not an import), and the shipped artifact would be run the
   same way. Mark every other non-SAME-FILE row AUDIT-ONLY: it needs a
   new behavior test against the artifact, which these prompts do not
   write.

OUTPUT: one table (test, subject, label, quoted line, digests or "not
comparable", FIX-ELIGIBLE or AUDIT-ONLY), then:
  Subjects the tests never execute as shipped: N
If every subject is SAME-FILE with equal digests, write
"No identity gaps found." Do not invent a gap to have something to report.
```
