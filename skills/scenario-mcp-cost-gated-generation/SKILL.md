---
name: scenario-mcp-cost-gated-generation
description: Use when submitting a paid or metered Scenario MCP generation job that needs an exact payload, cost quote, and explicit approval.
license: Apache-2.0
---

# Scenario MCP Cost-Gated Generation

## Outcome
Submit only a schema-valid generation request whose exact inputs, quoted cost, and user approval are recorded.

## Procedure
1. Read the selected model's live schema immediately before preparing the request. Confirm that the intended reference assets and parameters are supported.
2. Build the final payload with explicit values for every important option. Avoid relying on undocumented defaults.
3. Run the platform's non-billable dry-run or quote operation with that exact payload, when available. Keep the quote identifier and exact cost string.
4. Show the user the model, output lane, quantity, input assets, price, currency/credit unit, and any uncertainty. Stop until the user approves that exact spend.
5. Submit using the same model, lane, and parameters that were quoted. Do not silently modify inputs after approval.
6. Wait on the returned job ID using the live job-wait/status tools until completion, failure, or the agreed timeout.
7. Record the job ID, model/schema date, prompt, seed, parameters, returned asset IDs, quote, and final output hashes.
8. If the submission response is uncertain, inspect job history before retrying. Never blindly repeat a potentially billable request.

## Quality gates
- A quote is not spending authorization; explicit approval is still required.
- A timeout is not proof that a job was never accepted.
- If the platform cannot quote the exact payload, label the cost unknown and stop before spending.

## Deliverable
A cost/approval record, job status, reproducibility metadata, returned assets, and any unresolved billing or delivery uncertainty.

## Boundaries
- Never fabricate a quote or treat an empty price as free.
- Never exceed the user's stated budget, job count, or iteration cap.
- Do not upload additional references as a side effect of submitting a workflow.
- Stop when the job fails or the approved budget is exhausted; ask before a paid retry.
