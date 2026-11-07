---
name: failure-forensics
description: Diagnose a reproducible software failure by narrowing symptoms to a root cause and verifying the repair.
license: Apache-2.0
---

# Failure Forensics

## Outcome

Diagnose a reproducible software failure by narrowing symptoms to a root cause and verifying the repair. Produce a reproducible result with explicit evidence and known limitations.

## Procedure

1. Capture the exact symptom, environment, triggering input, expected result, and first known failing revision.
2. Reproduce the failure with the smallest safe input. Preserve logs and stack traces while redacting credentials and private payloads.
3. Form competing hypotheses and design one experiment per hypothesis. Change one variable at a time.
4. Trace the failing path through inputs, state, dependencies, and side effects until the earliest incorrect assumption or transition is found.
5. Add a regression test that fails before the fix. Implement the smallest root-cause correction.
6. Rerun the regression and relevant neighboring tests; inspect outputs and edge cases. Record anything not tested.
7. Report root cause, evidence, fix, regression coverage, and residual risk.

## Deliverable

- Objective and scope.
- Findings tied to files, logs, metrics, or source references.
- Commands and checks actually executed, with their results.
- Assumptions, unresolved questions, and residual risks.

## Boundaries

- Do not claim verification, compatibility, performance, or security properties without evidence.
- Do not disclose credentials or private production data in reports or examples.
- Require appropriate human authorization before destructive, external, paid, or irreversible actions.
- Preserve existing project conventions and make the smallest safe change.
