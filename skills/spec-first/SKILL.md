---
name: spec-first
description: Turn a feature request into testable acceptance criteria and a small implementation plan before editing.
license: Apache-2.0
---

# Spec First

## Outcome

Turn a feature request into testable acceptance criteria and a small implementation plan before editing. Produce a reproducible result with explicit evidence and known limitations.

## Procedure

1. Restate the desired outcome and identify the user, system boundary, and constraints that must not change.
2. Inspect current behavior and related code before drafting a solution. Separate facts from assumptions.
3. Define acceptance criteria in observable terms, including failure behavior and edge cases.
4. List likely affected interfaces, data, permissions, migrations, tests, and documentation.
5. Compare the smallest viable implementation options and name trade-offs, risks, and dependencies.
6. Create an ordered plan with verification steps and explicit stop conditions for unresolved requirements.
7. Ask only for information that materially changes the implementation; otherwise record a safe assumption and proceed.

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
