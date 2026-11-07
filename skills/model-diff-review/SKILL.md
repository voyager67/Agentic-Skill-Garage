---
name: model-diff-review
description: Compare two model checkpoints or prompt configurations using a consistent evaluation harness and error taxonomy.
license: Apache-2.0
---

# Model Diff Review

## Outcome

Compare two model checkpoints or prompt configurations using a consistent evaluation harness and error taxonomy. Produce a reproducible result with explicit evidence and known limitations.

## Procedure

1. Identify the exact base and candidate checkpoints, tokenizer, inference template, decoding settings, and hardware/runtime versions.
2. Freeze one evaluation set and run both models with identical preprocessing and generation settings where technically valid.
3. Compare aggregate metrics and stratified slices. Include sample counts, confidence intervals where appropriate, and run-to-run variance.
4. Cluster regressions and gains by error type; inspect representative examples rather than relying only on aggregate scores.
5. Check contamination, data changes, prompt changes, quantization, and evaluation drift before attributing a difference to weights.
6. Report accepted improvements, regressions, inconclusive results, and the next experiment. Do not claim a benchmark win without reproducible evidence.

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
