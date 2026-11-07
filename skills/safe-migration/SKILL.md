---
name: safe-migration
description: Plan and execute a controlled migration of code, schemas, frameworks, or configuration while preserving a rollback path.
license: Apache-2.0
---

# Safe Migration

## Outcome

Plan and execute a controlled migration of code, schemas, frameworks, or configuration while preserving a rollback path. Produce a reproducible result with explicit evidence and known limitations.

## Procedure

1. Inventory affected code, stored data, external consumers, runtime versions, and operational constraints. Identify the authoritative source of truth.
2. Define preconditions and invariants that must remain true. Capture a baseline and create representative migration fixtures.
3. Choose a reversible sequence. Prefer expand, migrate, verify, then contract; avoid destructive one-step transformations.
4. Write an idempotent migration with bounded batches, checkpoints, explicit transaction behavior, and safe handling of partial completion.
5. Validate counts, checksums, referential integrity, read/write compatibility, and application behavior before switching traffic or deleting old fields.
6. Document rollback limits and the point after which rollback requires restore or forward-fix. Never describe a destructive migration as reversible without evidence.

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
