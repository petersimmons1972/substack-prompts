# 099-the-auditors-own-name-is-in-the-ledger — Prompt 1 (audit)

```text
You are auditing whether actors who judge others can receive findings under
equivalent standards, in the same record or a governed linked oversight
record. You have shell access. Read-only; change nothing.

1. BOUND THE RECORD: locate ledgers, review logs, defect registers, and
   scorecards. List the files/tables/APIs and time range inspected; mark
   inaccessible layers OUT-OF-SCOPE.
2. MAP ROLES: distinguish evaluator, finding author, submitting identity,
   and storage identity. Map human, bot, CI/service-account aliases with
   evidence. Test actors exercising judgment, not mechanical row writers.
3. COUNT: inventory judged actors and counts. For each evaluator, count
   findings against that actor or a proved alias; quote one with all
   credential and connection details masked.
4. CHECK PARITY: compare evidence and severity standards, role-appropriate
   fields/consequences, and same-record or governed-link storage. Cite fields.
5. CHECK CAPABILITY: inspect constraints, filters, permissions, and workflow.
   Distinguish improper exemption from separation of duties with governed
   oversight. Report YES, NO-WITHIN-BOUNDARY, or UNKNOWN/OUT-OF-SCOPE.
6. CHECK OBSERVATION: report age, volume, and evidenced qualifying
   opportunities. A zero count proves neither cleanliness nor asymmetry.
7. REPORT per evaluator: total | self-findings | parity (EQUIVALENT /
   SOFTENED / DISCONNECTED / N-A) | exemption | observation sufficiency.
   Verdict:
   - EVIDENCED-INSTANCE-OF-SYMMETRY: one entry passes parity; no system claim.
   - SYSTEM-SYMMETRY-SUPPORTED: capability, representative sampling,
     consequences, coverage, and independent oversight are evidenced.
   - ASYMMETRIC-BY-DESIGN: an exemption is evidenced.
   - ASYMMETRIC-BY-PRACTICE: zero entries despite sufficient observation
     and an evidenced qualifying opportunity.
   - INCONCLUSIVE: evidence, identity, opportunity, frequency, or scope is
     insufficient. Default here when unsure.
```

## Undo

Read-only — nothing to undo.
