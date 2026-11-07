---
name: scenario-mcp-quality-budget-loop
description: Use when iterating on Scenario outputs with quality checks, a bounded spend budget, and a measurable stop condition.
license: Apache-2.0
---

# Scenario MCP Quality and Budget Loop

## Outcome
Improve a creative output through bounded, evidence-led iterations without repeating paid analyses or generating endlessly.

## Procedure
1. Define the acceptance bar, iteration limit, total spend cap, and the outputs that must pass before the first generation.
2. Check whether a platform quality analysis is available and whether the user's workspace has the required entitlement.
3. When the quality tool supports dry-run, quote a new analysis before first use. Read a stored verdict when it is available rather than paying to recompute it.
4. Inspect the verdict's reasons and suggestions. Map each item to a concrete correction, and verify whether the analysis actually covers the requested quality dimension.
5. Change one major variable per iteration. Track the baseline asset, prompt, settings, job, cost, and before/after evidence.
6. Regenerate only when the fix requires a new asset. Use a local or masked edit for a localized defect when feasible.
7. Stop when the acceptance bar passes, the budget or iteration limit is reached, results stop improving, or the quality tool's known limits make more runs uninformative.
8. If a paid quality feature is unavailable, explain the limitation and use a human review checklist rather than retrying an entitlement failure.

## Quality gates
- Do not use a numeric quality score as the sole release decision.
- Check structural plausibility and reference compliance separately from aesthetic quality.
- Do not assume a fresh asset has no stored verdict or that a plain read is free; inspect the live schema and billing semantics.

## Deliverable
A bounded iteration ledger with quality observations, decisions, spend, stop reason, best asset, and remaining risks.

## Boundaries
- Never exceed the approved budget or iteration cap.
- Do not rerun a billable analysis without the user's approval when its cost is not already covered.
- Do not claim a quality tool detects requirements outside its documented scope.
- At the stop condition, deliver the best verified asset and disclose any failed acceptance criteria.
