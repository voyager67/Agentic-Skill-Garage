---
name: zbrush-character-sculpt
description: Use when the task is to sculpt character anatomy with proportion and landmark review.
license: Apache-2.0
---

# Zbrush Character Sculpt

## Outcome

Sculpt character anatomy with proportion and landmark review. The result must be traceable to supplied inputs and pass the checks below.

## Inputs and prerequisites

- Source sculpt, target subdivision strategy, reference landmarks, scale, and intended print or runtime use.
- ZBrush, ZScript/macros, GoZ where configured, and a DCC mesh validator for downstream checks.
- Confirm the target application's version and the actual capabilities available in this environment.

## Procedure

1. Inspect subdivision history, polygroups, masks, symmetry state, and source scale before sculpting.
2. Work from primary forms to secondary forms, then surface detail; do not polish an incorrect silhouette.
3. Use symmetry for structural passes and deliberately break it only when the design requires it.
4. Record destructive operations such as remeshing, decimation, or Boolean application.
5. Validate topology, thickness, UVs, vertex color, and export format in the target DCC.
6. Save a new ZTL/project version and a review render before handoff.

## Quality gates

- Keep a high-resolution source before decimation or destructive Boolean operations.
- Print readiness requires measured scale, wall thickness, watertightness, and drain access.
- A ZBrush export is not considered engine-ready until reopened and checked downstream.

## Deliverable

Source sculpt, optimized/export mesh, turntable or review views, and a compact technical handoff. Include the exact commands or application operations used, the files changed, and the checks that were actually run.

## Boundaries

- Keep source files unchanged; write new versions to an explicit output path.
- Do not transmit private assets or prompts to an external provider unless the user has explicitly approved that destination.
- Do not run paid generation or destructive application operations without clear authorization and a stated budget or scope.
- If a required application, plugin, model, or entitlement is absent, report the limitation and stop at the last verified stage.
- Separate measured results from visual judgment, assumptions, and recommendations.
