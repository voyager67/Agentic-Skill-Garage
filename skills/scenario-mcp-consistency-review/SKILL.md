---
name: scenario-mcp-consistency-review
description: Use when reviewing Scenario-generated batches for character, brand, product, environment, and shot-to-shot consistency.
license: Apache-2.0
---

# Scenario MCP Consistency Review

## Outcome
Review generated assets against an explicit identity brief and reference-role map, then route each defect to a bounded edit or a new generation.

## Procedure
1. Create a canonical identity brief listing visible invariants, permitted variation, forbidden changes, and authoritative references.
2. For each output lane, inspect its live schema and confirm the selected model supports the reference inputs required by the brief.
3. Attach each approved reference to a named role in the request; do not assume the model interprets a reference correctly without a prompt instruction.
4. Review outputs in a comparison grid at consistent scale. Check silhouette, face, wardrobe, logos, product geometry, palette, camera, lighting, and continuity separately.
5. Record defects by location and severity. Distinguish identity breaks from aesthetic preferences and technical artifacts.
6. Use a masked/local edit for a localized defect when it preserves approved regions. Regenerate only when the error is global or the source is unusable.
7. Compare the revision against the same canonical baseline and update the lineage manifest. Keep rejected variants for traceability unless the user requests deletion.

## Quality gates
- A similarity score cannot replace direct comparison against the approved references.
- A composite or contact sheet may hide a single failed frame; inspect every deliverable unit.
- Never change multiple identity variables in one iteration unless the user explicitly requests a redesign.

## Deliverable
A pass/warn/fail matrix with evidence, reference mapping, defect locations, recommended correction, and approved final asset IDs.

## Boundaries
- Do not claim identity preservation when no reference comparison was performed.
- Do not erase a user's source or rejected assets during review.
- Do not trigger another paid generation without approval and an available budget.
- Report model limitations and remaining visual uncertainty plainly.
