---
name: review-lens
description: Review a diff for actionable correctness, security, reliability, and maintainability defects.
license: Apache-2.0
---

# Review Lens

## Outcome

Review a diff for actionable correctness, security, reliability, and maintainability defects. Produce a reproducible result with explicit evidence and known limitations.

## Procedure

1. Read the task intent, relevant source, tests, and complete diff before assessing the change.
2. Prioritize correctness, data loss, security, authorization, compatibility, concurrency, and operational failure modes.
3. Trace changed code to callers and downstream consumers. Check nulls, boundaries, errors, retries, and partial failures.
4. Inspect tests for meaningful assertions and missing negative cases. Treat unexecuted tests as unverified.
5. Ignore style-only comments unless they hide a maintainability or correctness risk. Avoid speculative findings without evidence.
6. Write findings first, ordered by severity, each with file/line, impact, reproduction or reasoning, and a practical fix.
7. State explicitly when no actionable findings were found and identify the scope that was not reviewed.

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
