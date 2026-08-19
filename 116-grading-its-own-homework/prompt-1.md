# 116-grading-its-own-homework — Prompt 1 (audit)

```text
You have shell and repo access. I have a system whose quality is scored by an
LLM judge (a benchmark harness, a RAG pipeline, an eval suite — anything where
one model grades another model's output). Audit the scoring setup for
leniency-inflation risk. Do not run the benchmark; audit the configuration.

1. Locate the scoring configuration in this repo (judge model name, decoding
   params, judge prompt, any "lenient"/"strict"/"thinking" mode flags). Report
   the exact file paths and the active values.
2. Locate what generates the outputs being judged (model, config). Report the
   generator/judge pairing as a fact. Whether a shared vendor/family or
   stylistic lineage produces CORRELATED leniency is an unverified HYPOTHESIS
   you cannot settle from config alone — it would take cross-grading the same
   answers with an independent judge. Rate correlation risk UNKNOWN unless the
   repo already contains such cross-grading evidence; flag explicitly if you
   CANNOT even determine the pairing from the repo.
3. Check whether the repo contains evidence of qualification: search for any
   reference set, gold labels, human-agreement figure, or calibration run. If
   none exists in the repo, say so plainly — absence of evidence in the repo
   is not proof the judge was never qualified elsewhere, but a judge with no
   qualification evidence produces unqualified numbers.
4. Check whether the scorer configuration is locked/versioned (a manifest,
   pinned model+params, anything that makes two runs comparable). If scores
   from different scorer configs are being compared anywhere in docs or
   dashboards, list each instance.
5. Check for a sealed holdout: is any eval subset withheld from iteration?
   If the whole set is visible to the people/agents tuning against it, flag
   overfitting risk.

Output shape:
- SCORING CONFIG: paths + active values
- GENERATOR/JUDGE PAIRING: models; correlation risk UNKNOWN unless cross-grading
  evidence exists (only then HIGH/MED/LOW)
- QUALIFICATION EVIDENCE IN REPO: found (ref: <path>) / none found in repo
- LOCK STATUS: locked (manifest path) / unlocked; cross-config comparisons found
- HOLDOUT: sealed / none
- VERDICT: one paragraph — can the current headline number be trusted, and
  what is the cheapest experiment that would confirm or deflate it?
```

## Undo

Read-only — nothing to undo.

**Ground truth — tested 2026-07-10 (harness-agnostic wording, run without modification).** Codex CLI ✅ (fixture: the claude-codex repo; full transcript in project records). Claude Code and Grok legs: pending.
