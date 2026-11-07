---
name: dependency-care
description: Evaluate dependency risk and upgrades without blind version bumps.
license: Apache-2.0
---

# Dependency Care

## Outcome

Evaluate dependency risk and upgrades without blind version bumps. Produce a reproducible result with explicit evidence and known limitations.

## Procedure

1. Identify the dependency’s purpose, direct/transitive status, supported versions, license, maintenance state, and security advisories.
2. Read the changelog and migration notes for the proposed version. Identify runtime, API, and transitive changes.
3. Check whether the dependency is actually used and whether a smaller or standard-library alternative meets the requirement.
4. Update lockfiles intentionally and preserve reproducibility. Avoid broad upgrades unrelated to the task.
5. Run vulnerability, license, unit, integration, packaging, and compatibility checks relevant to the dependency.
6. Review newly introduced install scripts, native binaries, permissions, and network behavior.
7. Report the upgrade rationale, residual risk, and rollback or pinning option.

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
