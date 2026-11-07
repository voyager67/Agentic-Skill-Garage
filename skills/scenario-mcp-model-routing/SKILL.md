---
name: scenario-mcp-model-routing
description: Use when choosing a Scenario model for an image, video, audio, texture, or 3D capability from the live catalog.
license: Apache-2.0
---

# Scenario MCP Model Routing

## Outcome
Select a current catalog member that supports the required output and input controls, with price and rights constraints visible before work starts.

## Procedure
1. Convert the request into an output lane, input types, reference needs, resolution/duration, quality bar, latency, and hard constraints.
2. Use the live MCP recommendation tool for capability-led discovery. Use keyword search only when a specific member is already known or needs to be found by name.
3. Inspect the returned model/provider identity and current availability. Never hardcode a versioned model ID from old examples.
4. Retrieve the selected member's live schema and read required inputs, defaults, ranges, supported files, outputs, and limits.
5. Reject candidates that cannot accept the required reference type, dimensions, or control. Do not treat a related model as equivalent.
6. Compare the available candidates on verified price, latency, quality evidence, license, and data policy. Mark missing fields as unknown.
7. Save the chosen member, schema snapshot or retrieval date, constraints, and fallback decision in the task record.

## Quality gates
- A model's presence in a search result does not prove it can run for the user's plan or workspace.
- Capability labels are not evidence of quality; evaluate representative outputs on the actual brief.
- Do not choose the cheapest member when it cannot satisfy the hard constraints.

## Deliverable
A compact routing decision with the chosen live member, reason, schema prerequisites, known trade-offs, and tested fallback.

## Boundaries
- Do not invent catalog IDs, schemas, latency measurements, or prices.
- Do not start a generation job during discovery.
- Do not send private references until the destination and data policy are approved.
- Keep a clear distinction between observed catalog facts and subjective evaluation.
