---
name: research-evidence-map
description: Turn a technical research question into a traceable evidence map with source quality, uncertainty, and actionable next experiments.
license: Apache-2.0
---

# Research Evidence Map

## Outcome

Turn a technical research question into a traceable evidence map with source quality, uncertainty, and actionable next experiments. Produce a reproducible result with explicit evidence and known limitations.

## Procedure

1. Turn the research question into a falsifiable claim, comparison, or decision. Define scope and what evidence would change the conclusion.
2. Search primary sources first: specifications, papers, official docs, source code, and reproducible benchmark artifacts.
3. For each source record date, version, method, sample, metrics, assumptions, licensing, and conflicts of interest.
4. Extract claims and map each to direct evidence. Separate measured results, author interpretation, external replication, and opinion.
5. Compare methods and test conditions before comparing headline metrics. Identify missing baselines and likely confounders.
6. List contradictions, uncertainty, applicability limits, and evidence gaps. Never convert an absence of evidence into proof.
7. Produce a claim-evidence matrix and the smallest next experiment or source check that can reduce uncertainty.

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
