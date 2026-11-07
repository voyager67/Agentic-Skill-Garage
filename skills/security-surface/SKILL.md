---
name: security-surface
description: Perform a focused threat review of code, APIs, configuration, and dependencies.
license: Apache-2.0
---

# Security Surface

## Outcome

Perform a focused threat review of code, APIs, configuration, and dependencies. Produce a reproducible result with explicit evidence and known limitations.

## Procedure

1. Map trust boundaries, data sensitivity, users, roles, entry points, integrations, and assets worth protecting.
2. Trace authentication and authorization separately. Verify ownership, tenant boundaries, least privilege, and default-deny behavior.
3. Inspect input validation, path handling, uploads, serialization, shell/process calls, network destinations, and output encoding.
4. Check secret storage, logging, telemetry, error messages, dependency risk, and data retention.
5. Construct realistic abuse cases and test safe negative paths in a disposable environment. Do not probe third-party systems.
6. Rank findings by impact and exploitability; include path/line evidence and a reproducible safe demonstration.
7. Recommend focused mitigations and regression tests. Report untested surfaces and residual risk.

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
