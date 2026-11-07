---
name: parallel-task-design
description: Break a multi-part engineering task into safely parallel work units with clear ownership and integration points.
license: Apache-2.0
---

# Parallel Task Design

## Outcome

Break a multi-part engineering task into safely parallel work units with clear ownership and integration points. Produce a reproducible result with explicit evidence and known limitations.

## Procedure

1. Break the objective into work units with independent inputs and verifiable outputs. Identify shared files and hidden dependencies.
2. Assign one owner per write scope. Avoid concurrent edits to the same file or generated artifact.
3. Define interface contracts, file ownership, branch or worktree boundaries, and integration checkpoints before parallel work starts.
4. Order dependent tasks and identify tasks that can run in parallel safely. Keep high-risk architecture decisions centralized.
5. Require each work unit to report changed paths, tests run, evidence, assumptions, and unresolved conflicts.
6. Integrate incrementally, run cross-workstream tests, resolve conflicts by inspecting behavior, and preserve a single authoritative result.

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
