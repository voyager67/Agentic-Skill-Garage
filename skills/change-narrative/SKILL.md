---
name: change-narrative
description: Explain a change through impact, trade-offs, and verification.
license: Apache-2.0
---

# Change Narrative

## Outcome

Explain a change through impact, trade-offs, and verification. Produce a reproducible result with explicit evidence and known limitations.

## Procedure

1. State the user or system problem in one sentence, then name the observable impact. Avoid describing the code before the outcome.
2. Summarize the smallest meaningful change and identify affected interfaces, users, data, and operational paths.
3. List verification performed with exact commands and actual outcomes. Separate automated checks, manual inspection, and checks not run.
4. Explain meaningful trade-offs and remaining limitations. Distinguish measured results from estimates or expectations.
5. Call out migration, rollout, monitoring, and rollback actions only when they are genuinely relevant.
6. Write a concise change narrative with problem, behavior change, proof, risk, and follow-up. Link evidence by path or test name.

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
