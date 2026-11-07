---
name: genai-job-monitoring
description: Use when the task is to track asynchronous generation jobs and recover from uncertain submissions.
license: Apache-2.0
---

# Genai Job Monitoring

## Outcome

Track asynchronous generation jobs and recover from uncertain submissions. The result must be traceable to supplied inputs and pass the checks below.

## Inputs and prerequisites

- Capability request, input/reference constraints, acceptable quality floor, budget, latency target, and data policy.
- Agentic Skill Garage quote and asset commands, local ComfyUI, installed local models, or an explicitly configured provider.
- Confirm the target application's version and the actual capabilities available in this environment.

## Procedure

1. Discover available capabilities from the live environment instead of assuming a model ID is current.
2. Separate required input types, reference roles, output dimensions, and hard constraints from stylistic preferences.
3. Check model terms, data handling, and whether references may leave the local machine.
4. Quote from a dated, sourced rate card; if price is absent or stale, stop and label the request unpriced.
5. Submit only the smallest useful batch after explicit approval for hosted spend or external transmission.
6. Record model/version, prompt, seed, parameters, cost basis, job ID, and output hash.

## Quality gates

- A price estimate is not permission to spend; hosted jobs need explicit approval.
- Local endpoints default to loopback; remote destinations require a deliberate opt-in.
- Model selection, output quality, and commercial rights are different questions.

## Deliverable

A model decision record, cost quote, reproducible job manifest, outputs, and uncertainty notes. Include the exact commands or application operations used, the files changed, and the checks that were actually run.

## Boundaries

- Keep source files unchanged; write new versions to an explicit output path.
- Do not transmit private assets or prompts to an external provider unless the user has explicitly approved that destination.
- Do not run paid generation or destructive application operations without clear authorization and a stated budget or scope.
- If a required application, plugin, model, or entitlement is absent, report the limitation and stop at the last verified stage.
- Separate measured results from visual judgment, assumptions, and recommendations.
