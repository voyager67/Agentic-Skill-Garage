---
name: context-handoff
description: Create a reliable handoff note so another engineer or coding agent can continue work without redoing exploration.
license: Apache-2.0
---

# Context Handoff

## Outcome

Create a reliable handoff note so another engineer or coding agent can continue work without redoing exploration. Produce a reproducible result with explicit evidence and known limitations.

## Procedure

1. Record the objective and acceptance criteria in the user’s wording where precision matters. Do not broaden the task.
2. Summarize repository or system context with exact paths, symbols, commands, and relevant versions. Exclude secrets and private payloads.
3. Separate completed work, verified behavior, open work, and failed or inconclusive attempts.
4. Capture decisions and rationale, including rejected options and the constraints that made them unsuitable.
5. List the next two or three concrete actions in dependency order, plus the exact validation command to rerun.
6. Write a handoff that another person or agent can act on without repeating exploration. Mark every unknown explicitly.

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
