---
name: scenario-mcp-reference-lineage
description: Use when managing approved reference uploads, generated assets, and source-to-output lineage through Scenario MCP.
license: Apache-2.0
---

# Scenario MCP Reference Lineage

## Outcome
Keep the origin, intended role, identity constraints, and generated descendants of every remote asset traceable.

## Procedure
1. Inventory candidate references locally and identify private, personal, licensed, or customer-owned content before upload.
2. Assign each reference a role: identity, composition, pose, camera, palette, material, motion, or audio. State which details must not transfer.
3. Ask for approval of the destination and data transfer. Upload only the selected files, not an entire directory by default.
4. Capture the returned asset identifiers and filenames. Pair them with local SHA-256 hashes and source/license notes in the project manifest.
5. When generating, record which reference IDs influence each output and what each reference is allowed to control.
6. Retrieve output metadata and store parent-child links, model identity, job ID, prompt, seed, parameters, and review status.
7. Before delivery, check the output against the authoritative references and verify that the correct asset version is being handed off.

## Quality gates
- A remote asset ID is not a substitute for source provenance or usage rights.
- Do not treat style references as permission to reproduce a protected logo, character, or person's likeness.
- Never overwrite or relabel an approved source asset as a generated final.

## Deliverable
A lineage manifest connecting local source hashes, approved remote references, generation jobs, output asset IDs, rights notes, and final approval.

## Boundaries
- Do not upload private material until the user approves the destination.
- Do not infer consent, ownership, or commercial rights from public availability.
- Preserve original local files and write manifest updates as new records.
- If lineage is missing or conflicting, stop before marking an output final.
