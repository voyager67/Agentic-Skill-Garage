---
name: release-readiness
description: Assess whether a change is ready for a tagged release or deployment.
license: Apache-2.0
---

# Release Readiness

## Outcome

Assess whether a change is ready for a tagged release or deployment. Produce a reproducible result with explicit evidence and known limitations.

## Procedure

1. Identify the release scope, version, supported platforms, distribution artifacts, and release owner.
2. Run required tests, lint/type checks, packaging, install/uninstall checks, and smoke tests on supported environments.
3. Inspect changelog, migration notes, licenses, bundled notices, default configuration, examples, and documentation links.
4. Scan the staged tree for credentials, private data, debug artifacts, local absolute paths, and accidentally included build outputs.
5. Check dependency provenance, signatures/checksums, reproducibility, backward compatibility, and rollback path.
6. Classify blockers, warnings, and accepted risks. Do not infer production readiness from a green unit-test suite alone.
7. Produce a release decision with evidence, artifact hashes, and required human approvals.

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
