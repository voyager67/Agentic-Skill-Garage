---
name: api-contract-check
description: Check API and schema changes for compatibility with existing clients and stored data.
license: Apache-2.0
---

# Api Contract Check

## Outcome

Check API and schema changes for compatibility with existing clients and stored data. Produce a reproducible result with explicit evidence and known limitations.

## Procedure

1. Locate the public endpoint, schema, event, command, and every known consumer. Record the current contract before changing it.
2. Capture field names, types, requiredness, defaults, null semantics, enum values, error shapes, pagination, auth scope, and version behavior.
3. Compare old and proposed contracts. Classify each difference as additive, behavior-changing, or breaking; include generated clients and persisted payloads.
4. Add compatibility tests for old clients and representative payloads. Test malformed inputs, omitted fields, explicit nulls, unknown enum values, and boundary sizes.
5. Choose an explicit migration strategy: expand/contract, versioned endpoint, adapter, or coordinated release. Define a removal date only when consumers are accounted for.
6. Validate the published schema or OpenAPI output and inspect the final diff for unintentional contract drift.

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
