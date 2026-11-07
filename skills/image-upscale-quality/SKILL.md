---
name: image-upscale-quality
description: Use when the task is to upscale an image and inspect detail, halos, texture invention, and edge artifacts.
license: Apache-2.0
---

# Image Upscale Quality

## Outcome

Upscale an image and inspect detail, halos, texture invention, and edge artifacts. The result must be traceable to supplied inputs and pass the checks below.

## Inputs and prerequisites

- A visual brief, target dimensions, output format, reference roles, approved identity constraints, and a review bar.
- ComfyUI or another explicitly configured generation/editing tool, plus Pillow, GIMP, Krita, or ImageMagick when installed.
- Confirm the target application's version and the actual capabilities available in this environment.

## Procedure

1. Separate subject, composition, camera, lighting, palette, text, and negative constraints in the brief.
2. Choose a tool that supports the required control; prefer deterministic post-processing for exact dimensions and text.
3. Quote hosted work from a dated price source before submission; use local processing when adequate.
4. Generate a small, reviewable candidate set and compare each result with the approved references.
5. Repair bounded defects locally when possible; regenerate only when the defect is global.
6. Export to a new path and inspect dimensions, color mode, alpha, and compression artifacts.

## Quality gates

- Exact copy and logos are composited from approved source files, not trusted to generative lettering.
- Reference identity and product geometry are checked separately from aesthetic quality.
- Upscaling, background removal, and color conversion are verified on edge cases.

## Deliverable

Final image files, editable source where available, prompt/settings record, and a short quality report. Include the exact commands or application operations used, the files changed, and the checks that were actually run.

## Boundaries

- Keep source files unchanged; write new versions to an explicit output path.
- Do not transmit private assets or prompts to an external provider unless the user has explicitly approved that destination.
- Do not run paid generation or destructive application operations without clear authorization and a stated budget or scope.
- If a required application, plugin, model, or entitlement is absent, report the limitation and stop at the last verified stage.
- Separate measured results from visual judgment, assumptions, and recommendations.
