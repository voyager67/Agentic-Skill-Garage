---
name: docs-sync
description: Bring documentation, examples, and configuration guides into agreement with the actual code.
license: Apache-2.0
---

# Docs Sync

## Outcome

Bring documentation, examples, and configuration guides into agreement with the actual code. Produce a reproducible result with explicit evidence and known limitations.

## Procedure

1. Identify the changed behavior and locate every related README, API reference, CLI help string, example, tutorial, and generated schema.
2. Use the implementation and tests as the source of truth. Flag stale instructions instead of assuming documentation is current.
3. Update examples to run against the current interface. Prefer minimal fixtures and remove placeholders that look like real credentials.
4. Check terminology, defaults, environment variables, platform paths, failure behavior, and version constraints.
5. Run example commands where safe and label unexecuted examples clearly.
6. Check links and references, then review the diff for claims that exceed the verified implementation.
7. Report which docs changed and which claims remain unverified.

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
