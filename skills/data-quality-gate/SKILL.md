---
name: data-quality-gate
description: Design validation checks for structured datasets and data pipelines.
license: Apache-2.0
---

# Data Quality Gate

## Outcome

Design validation checks for structured datasets and data pipelines. Produce a reproducible result with explicit evidence and known limitations.

## Procedure

1. Define the dataset’s intended use, owner, schema, sensitivity, provenance requirements, and acceptance thresholds.
2. Validate encoding, schema, types, required fields, ranges, null policy, uniqueness, and allowed value sets.
3. Check semantic constraints across fields, referential integrity, temporal order, label consistency, and domain invariants.
4. Measure missingness, duplicates, skew, outliers, drift, leakage, and split contamination. Report denominators and thresholds.
5. Quarantine invalid rows with safe record identifiers and reason codes. Never silently repair ambiguous or high-impact values.
6. Emit a versioned quality report, reproducible validation command, exception list, and explicit pass/warn/fail decision.

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
