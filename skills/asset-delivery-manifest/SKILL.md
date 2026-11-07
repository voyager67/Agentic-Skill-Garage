---
name: asset-delivery-manifest
description: Use when the task is to package a delivery with checksums, formats, sizes, and provenance.
license: Apache-2.0
---

# Asset Delivery Manifest

## Outcome

Package a delivery with checksums, formats, sizes, and provenance. The result must be traceable to supplied inputs and pass the checks below.

## Inputs and prerequisites

- Original files, approved references, source/rights notes, intended uses, and a clear project destination.
- Agentic Skill Garage asset commands, SHA-256 manifests, JSON identity profiles, and the target DCC or image viewer.
- Confirm the target application's version and the actual capabilities available in this environment.

## Procedure

1. Inventory the supplied files before copying; do not assume names or extensions describe their contents.
2. Assign a stable role to every reference and record the exact details it is allowed to influence.
3. Use the local asset manifest to record hashes, media type, destination, and source provenance.
4. Compare candidate assets against the approved identity or brand invariants, not vague similarity.
5. Freeze the accepted set and include a machine-readable manifest with the handoff.

## Quality gates

- Byte-identical duplicates are identified by hash, never guessed from filenames.
- Rights, consent, attribution, and usage restrictions are visible beside the relevant asset.
- A reference never silently becomes a public deliverable.

## Deliverable

An organized asset library, role map, identity/brand profile where relevant, and a provenance manifest. Include the exact commands or application operations used, the files changed, and the checks that were actually run.

## Boundaries

- Keep source files unchanged; write new versions to an explicit output path.
- Do not transmit private assets or prompts to an external provider unless the user has explicitly approved that destination.
- Do not run paid generation or destructive application operations without clear authorization and a stated budget or scope.
- If a required application, plugin, model, or entitlement is absent, report the limitation and stop at the last verified stage.
- Separate measured results from visual judgment, assumptions, and recommendations.
