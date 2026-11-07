---
name: multi-agent-crosscheck
description: Use independent reviewers or model providers to challenge a plan or diff and synthesize evidence-based disagreement.
license: Apache-2.0
---

# Multi Agent Crosscheck

## Outcome

Use independent reviewers or model providers to challenge a plan or diff and synthesize evidence-based disagreement. Produce a reproducible result with explicit evidence and known limitations.

## Procedure

1. Confirm that independent reviewers or models are actually available. If not, report that independent cross-checking was unavailable.
2. Give each reviewer the same bounded question, evidence set, acceptance criteria, and known constraints. Do not leak unrelated private files.
3. Assign distinct review angles such as correctness, security, architecture, or evaluation methodology to reduce correlated blind spots.
4. Ask reviewers to cite exact evidence, state assumptions, and rank findings by impact. Request counterexamples rather than generic approval.
5. Reconcile findings by reproducing them against source and tests. Preserve unresolved disagreements instead of forcing consensus.
6. Produce a finding matrix with reviewer, evidence, disposition, residual uncertainty, and required human decision.

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
