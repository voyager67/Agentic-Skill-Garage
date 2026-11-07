---
name: experiment-ledger
description: Make ML training experiments reproducible and comparable.
license: Apache-2.0
---

# Experiment Ledger

## Outcome

Make ML training experiments reproducible and comparable. Produce a reproducible result with explicit evidence and known limitations.

## Procedure

1. Assign a unique run ID and record the question, hypothesis, baseline, intended metric, and stopping rule before training.
2. Capture immutable model and tokenizer revisions, dataset hashes, preprocessing code, split IDs, environment, hardware, precision, and random seeds.
3. Record all hyperparameters, effective batch size, optimizer, scheduler, checkpoint policy, evaluation cadence, and resume state.
4. Log actual resource use, wall time, memory peaks, interruptions, failures, and any manual intervention.
5. Run the same evaluation protocol on baseline and candidate checkpoints. Preserve raw metrics and per-slice results.
6. Compare runs with uncertainty and known confounders. Never attribute an improvement to one variable when multiple variables changed.
7. Publish a reproducibility bundle with config, hashes, logs, metrics, and a concise interpretation.

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
