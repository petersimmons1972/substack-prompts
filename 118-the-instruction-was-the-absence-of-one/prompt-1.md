# 118-the-instruction-was-the-absence-of-one — Prompt 1 (audit)

```text
You are auditing an agent pipeline for model-attribution integrity: whether
the system can PROVE which model produced each recorded piece of work, rather
than inferring it from configuration. You have shell access to this repo and
its logs. Read-only; change nothing.

1. Find the attribution records: search for ledgers, scorecards, results
   files, or logs that record per-task outcomes tagged with a model name
   (look for JSONL/CSV/DB files and fields like "model", "engine", "version").
2. For each record source found, answer:
   a. Where does the model name in each row COME FROM — a per-run log line
      emitted by the process itself, or a config file read at write time?
   b. Could a config change mid-flight cause rows to be attributed to the
      wrong model? Explain the exact window.
3. Reconstruct one recent config-change event if any exists. Prefer an
   actual audit trail — `git log` on the model/engine configuration file(s)
   if it's version-controlled, or deploy logs — over raw filesystem
   timestamps, since mtime/ctime are corroborating signals, not proof (many
   filesystems don't expose reliable birth time, and ctime is
   metadata-change time, not necessarily creation time). Only fall back to
   file mtimes when no better trail exists, and flag the reconstruction as
   approximate when you do. However you date the change, list work items
   (worktrees, job dirs, log files) whose creation times fall within 4 hours
   on either side of it. Flag any work item whose recorded model attribution
   cannot be confirmed from its own run log.
4. Report:
   - attribution sources table: record file | model field source
     (per-run log / config-at-write / unknown)
   - any mid-flight ambiguity windows found, with the timestamps
   - a verdict per record source: VERIFIED-PER-RUN, CONFIG-TRUSTED (at risk),
     or UNVERIFIABLE
Do not fabricate timestamps. If no attribution records exist, say so — that
is itself the finding.
```

## Undo

Read-only — nothing to undo.

**Ground truth — tested 2026-07-10 (harness-agnostic wording, run without modification).** Codex CLI ✅ (fixture: the claude-codex repo; full transcript in project records). Claude Code and Grok legs: pending.
