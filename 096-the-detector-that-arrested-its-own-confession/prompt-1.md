# 096-the-detector-that-arrested-its-own-confession — Prompt 1 (audit)

```text
You are auditing pattern-based security filters in this repository for two
symmetric failure modes: (1) mention/use confusion — the filter fires on
text that DESCRIBES the attack, including its own docs and tests; and
(2) normalization gaps — trivial variants of the payload evade it.

Steps:
1. Locate the filters. Search for regex- or keyword-based detection of
   hostile content: grep for regex literals near words like "quarantine",
   "block", "deny", "inject", "sanitize", "payload", "filter", "scan",
   plus any allow/deny wordlists in config files. List each detector with
   file:line and the patterns it matches.
2. Mention-vs-use test. For each detector, collect in-repo text that
   MENTIONS its patterns: its own README/docs, code comments, test files,
   PR/commit message templates. Run (or, if not directly executable,
   hand-evaluate) the detector against those texts. Record every false
   positive — especially any case where the detector flags its own
   documentation.
3. Normalization test. For each pattern, generate variants: missing/extra
   punctuation (don't -> dont), case changes, doubled spaces, hyphenation,
   simple unicode substitutions (Latin 'o' -> Cyrillic 'о'), and
   zero-width characters. Evaluate which variants evade the detector.
   Record every false negative.
4. Check whether any detector attempts an intent gate (imperative mood,
   position in message, quoting context) or input normalization before
   matching. Note presence/absence per detector.
5. Read-only. Modify nothing; do not commit generated payload variants.

Output a markdown report:
- Per detector: patterns; false positives found (with the exact triggering
  text); false negatives found (with the exact evading variant);
  normalization present yes/no; intent gate present yes/no.
- A verdict line per detector: SOUND / MENTION-CONFUSED / EVADABLE / BOTH.
- The single highest-risk finding overall, one paragraph.
```

## Undo

Read-only — nothing to undo.

**Ground truth — tested 2026-07-10 (harness-agnostic wording, run without modification).** Codex CLI ✅ (fixture: the claude-codex repo; full transcript in project records). Claude Code and Grok legs: pending.
