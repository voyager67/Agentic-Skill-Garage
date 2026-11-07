---
name: agent-skill-audit
description: Validate a skill library for metadata correctness, discoverability, duplicate naming, risky instructions, and portability.
license: Apache-2.0
---

# Agent Skill Audit

## Outcome

Validate a skill library for metadata correctness, discoverability, duplicate naming, risky instructions, and portability. Produce a reproducible result with explicit evidence and known limitations.

## Procedure

1. Enumerate every skill directory and parse its frontmatter. Check that name, directory, description, and body are present and consistent.
2. Check uniqueness, description quality, supported spec fields, link depth, and references to files that are not shipped.
3. Compare triggers and expected outputs to find duplicates or overlapping skills that should be merged or distinguished.
4. Read every workflow for unsafe commands, destructive actions, silent uploads, credential exposure, spend, and unjustified permissions.
5. Check portability, dependencies, host-specific assumptions, command accuracy, and disclosure of unavailable integrations.
6. Run the repository validator, package sample skills, and inspect the resulting archives and index counts.
7. Produce a prioritized audit with concrete fixes, compatibility evidence, and issues that remain unverified.

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
