---
name: performance-proof
description: Find and validate a measurable performance bottleneck before optimizing.
license: Apache-2.0
---

# Performance Proof

## Outcome

Find and validate a measurable performance bottleneck before optimizing. Produce a reproducible result with explicit evidence and known limitations.

## Procedure

1. Define the user-visible performance problem and choose a metric, workload, hardware, and acceptable threshold.
2. Capture a baseline using repeatable inputs and multiple runs. Record warm-up, environment, variance, and measurement method.
3. Profile before changing code. Identify the dominant CPU, GPU, I/O, memory, network, or rendering bottleneck.
4. Form one optimization hypothesis and change one relevant factor at a time.
5. Re-run the same workload and compare latency, throughput, memory, output correctness, and resource cost.
6. Check regressions on representative workloads and small/large inputs. Reject optimizations that merely move the bottleneck without user benefit.
7. Report baseline, candidate, measured delta, variance, environment, and reproducible commands.

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
