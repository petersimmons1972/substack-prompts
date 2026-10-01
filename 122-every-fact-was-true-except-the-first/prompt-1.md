# 122-every-fact-was-true-except-the-first — Prompt 1 (AUDIT: two layers, claims and links (read-only))

Paste into Claude Code or Codex.

```text
Read-only task. Do not create, edit, move or delete any file, and do not fetch
anything to improve a source's grade: grade what the document gives.

Target: <PATH TO YOUR DOCUMENT, or the text of yesterday's post pasted below>.

Report two separate layers. Never merge them into one verdict.

LAYER 1: CLAIM RECEIPTS.
1. List the document's factual claims in order as C1, C2, ... For each, give
   the source the document cites for it (link or citation), or NOT FOUND if
   it cites none, and grade what is cited: PRIMARY, PEER-REVIEWED, GOV, PRESS,
   SECONDARY, SATIRE/PARODY, or NOT FOUND. A claim the document itself marks
   as unverified is listed as DISCLOSED-UNVERIFIED.
2. End layer 1 with the count per grade. Do not call layer 1 "clean" unless
   every claim has a cited source graded above SATIRE/PARODY.

LAYER 2: LINK RECEIPTS.
3. Every step that carries the reader from one claim to the next is a link:
   "so", "therefore", "which is why", "then", "within a year", a
   juxtaposition, a pronoun that merges two groups, or a framing word. Number
   them L1, L2, ... Quote the words that make each link, and label it exactly
   one of:
   - SUPPORTED: a cited source states this connection itself (quote it).
   - SEQUENCE-AS-CAUSE: two events are placed in order and the order stands
     in for a cause no source states.
   - FRAMING: a word or phrase imports a claim no source makes (quote it).
   - UNSUPPORTED: any other connection no cited source states.
   A link can be a seam even when both of its claims have strong receipts.

NUMBERS.
4. For every number, say what it is a count or a fraction of. Give the
   denominator, whether the document states it, and who produced each figure.
   Flag any ratio that divides figures from different producers, or different
   kinds of quantity (for example a cumulative total divided by a standing
   population).

OUTPUT.
5. Three tables (claims, links, numbers), then two lines:
     Claims without an openable source: N
     Unsupported links: M
   where M counts SEQUENCE-AS-CAUSE, FRAMING and UNSUPPORTED links together.

If every claim has a cited source, every link is SUPPORTED and every number
has a stated denominator, write "No seams found." and list each link with its
supporting quote. Do not invent a seam to have something to report.
```
