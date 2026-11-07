---
name: sql-integrity-check
description: Review SQL queries and data-model changes for correctness, access scope, safe parameterization, and performance.
license: Apache-2.0
---

# Sql Integrity Check

## Outcome

Review SQL queries and data-model changes for correctness, access scope, safe parameterization, and performance. Produce a reproducible result with explicit evidence and known limitations.

## Procedure

1. Clarify the intended result grain, source tables, authorization scope, freshness needs, and expected row count.
2. Read schema, constraints, indexes, row-level security, and representative query plans before editing SQL.
3. Check joins for fan-out, filters for null behavior, time boundaries, duplicate rows, aggregation order, and timezone assumptions.
4. Use bound parameters for values. Avoid string interpolation, wildcard overexposure, and unnecessary selection of sensitive columns.
5. Run tests against fixtures covering empty data, duplicates, nulls, boundary dates, and unauthorized scopes.
6. Inspect query plans and bounded execution cost on representative data. Do not run destructive statements against production.
7. Report the query, expected grain, validation evidence, access assumptions, and performance trade-offs.

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
