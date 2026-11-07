---
name: repo-scout
description: Map an unfamiliar codebase before changing it.
license: Apache-2.0
---

# Repo Scout

## Outcome

Map an unfamiliar codebase before changing it. Produce a reproducible result with explicit evidence and known limitations.

## Procedure

1. Read README, agent instructions, package manifests, contribution guidance, CI, and test configuration first.
2. Map the top-level tree, entry points, key modules, generated assets, and external integrations. Avoid dumping large directories.
3. Trace one representative execution path end to end using concrete file paths and symbols.
4. Identify configuration sources, secrets boundaries, storage, network calls, permissions, and destructive operations.
5. Find the exact commands for tests, lint, type checking, builds, packaging, and deployment from project files.
6. Separate verified findings from unknowns and assumptions. Do not infer implementation from a filename or README claim.
7. Produce a concise system map, likely change hotspots, verification commands, and open questions. Remain read-only.

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
