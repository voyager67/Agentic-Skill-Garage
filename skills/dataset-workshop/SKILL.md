---
name: dataset-workshop
description: Prepare consistent, traceable instruction-tuning or evaluation datasets with reproducible cleaning rules.
license: Apache-2.0
---

# Dataset Workshop

## Outcome

Prepare consistent, traceable instruction-tuning or evaluation datasets with reproducible cleaning rules. Produce a reproducible result with explicit evidence and known limitations.

## Procedure

1. Read target model, tokenizer/chat template, trainer requirements, intended use, and source licenses before selecting a schema.
2. Publish a canonical record contract, UTF-8/newline policy, normalization rules, and positive/negative examples for contributors.
3. Validate every record; reject malformed rows, empty turns, illegal role order, truncation, and unsupported fields.
4. Deduplicate with exact and documented near-duplicate checks. Preserve provenance and record rejection counts without logging sensitive text.
5. Split source groups before augmentation. Keep paraphrases, templates, documents, and related examples in one split to reduce leakage.
6. Independently check labels or final answers where feasible; document generated content as generated, not human-verified ground truth.
7. Freeze a dataset version with checksums, source licenses, preprocessing command, split rationale, and known contamination risks.

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
