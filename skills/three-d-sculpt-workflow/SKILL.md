---
name: three-d-sculpt-workflow
description: Use when the task is to plan sculpt stages from primary forms through surface detail.
license: Apache-2.0
---

# Three D Sculpt Workflow

## Outcome

Plan sculpt stages from primary forms through surface detail. The result must be traceable to supplied inputs and pass the checks below.

## Inputs and prerequisites

- Reference views, intended camera distance, target engine, polygon budget, UV/texture limits, and animation needs.
- Blender, Maya, ZBrush, MeshLab, or a compatible mesh inspection tool; FFmpeg is not a geometry validator.
- Confirm the target application's version and the actual capabilities available in this environment.

## Procedure

1. Define scale, axes, silhouette, target use, polygon budget, and required export formats before modeling.
2. Block primary shapes and compare silhouette and proportions against reference views.
3. Resolve topology, normals, transforms, pivots, UVs, and texel density before detailed materials.
4. Bake maps with an inspected cage and verify normal-map tangent convention.
5. Test deformation, collision, and LOD behavior at the intended runtime camera distance.
6. Export a new file and reopen it in a clean scene or target engine for round-trip verification.

## Quality gates

- A high polygon count is not evidence of useful detail; preserve silhouette and deformation first.
- Check manifoldness, scale, axis, transforms, material paths, and missing textures.
- Generated mesh quality is reported as observed, not assumed from a provider label.

## Deliverable

Editable scene or sculpt, validated interchange file, texture set, technical manifest, and known limitations. Include the exact commands or application operations used, the files changed, and the checks that were actually run.

## Boundaries

- Keep source files unchanged; write new versions to an explicit output path.
- Do not transmit private assets or prompts to an external provider unless the user has explicitly approved that destination.
- Do not run paid generation or destructive application operations without clear authorization and a stated budget or scope.
- If a required application, plugin, model, or entitlement is absent, report the limitation and stop at the last verified stage.
- Separate measured results from visual judgment, assumptions, and recommendations.
