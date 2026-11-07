---
name: test-driven-change
description: Implement a behavior change with tests that demonstrate the requirement and protect regressions.
license: Apache-2.0
---

# Test Driven Change

## Outcome

Implement a behavior change with tests that demonstrate the requirement and protect regressions. Produce a reproducible result with explicit evidence and known limitations.

## Procedure

1. Convert the request into observable acceptance criteria and identify the smallest stable behavior boundary.
2. Inspect existing tests, fixtures, conventions, and public interfaces. Reuse their patterns.
3. Write a failing test for the expected behavior, including relevant negative and boundary cases.
4. Run the focused test and confirm it fails for the intended reason rather than a broken fixture.
5. Implement the smallest change that makes the test pass without weakening adjacent behavior.
6. Run focused tests, the broader regression suite, and applicable static checks; inspect the final diff.
7. Report exact commands and results, including skipped or unavailable checks.

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
