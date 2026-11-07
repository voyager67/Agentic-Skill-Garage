---
name: model-eval-design
description: Build an evaluation plan that measures a model capability rather than a single attractive example.
license: Apache-2.0
---

# Model Eval Design

## Outcome

Build an evaluation plan that measures a model capability rather than a single attractive example. Produce a reproducible result with explicit evidence and known limitations.

## Procedure

1. Translate the capability claim into observable tasks and define what counts as correct, partial, invalid, or unsafe.
2. Select representative examples across difficulty, domain, format, language, and edge cases. Keep test data isolated from tuning.
3. Define baselines, candidate systems, prompts, decoding parameters, tool permissions, and a deterministic evaluation harness.
4. Choose metrics that match the task, including exact match, rubric score, calibration, latency, cost, failure rate, or human preference as appropriate.
5. Blind or randomize comparisons when judgment could be biased. Double-rate a sample and measure reviewer agreement.
6. Analyze per-slice failures, confidence intervals, contamination risks, and sample-size limitations.
7. Publish a protocol, versioned examples, scoring rubric, raw outputs, summary, and explicit limits on interpretation.

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
