---
name: build-rescue
description: Investigate and repair a failing build or CI job from logs to a verified fix.
license: Apache-2.0
---

# Build Rescue

## Outcome

Investigate and repair a failing build or CI job from logs to a verified fix. Produce a reproducible result with explicit evidence and known limitations.

## Procedure

1. Reproduce the build using the project’s documented command and capture the complete failing stage and first meaningful error.
2. Inspect runtime/toolchain versions, lockfiles, generated sources, environment variables, cache state, and recent dependency changes.
3. Classify the failure as configuration, dependency resolution, compilation, code generation, test, packaging, or infrastructure.
4. Build a minimal reproduction or isolate the failing package. Avoid deleting caches or lockfiles until evidence shows they are corrupt.
5. Apply the smallest correction and preserve dependency pins unless an upgrade is justified.
6. Rerun the exact failing command plus the project’s relevant tests and package checks.
7. Report the root cause, changed files, exact build evidence, and any platform-specific limitation.

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
