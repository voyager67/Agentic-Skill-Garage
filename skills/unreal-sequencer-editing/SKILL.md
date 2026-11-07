---
name: unreal-sequencer-editing
description: Use when the task is to assemble cinematic sequences with camera cuts and timecode review.
license: Apache-2.0
---

# Unreal Sequencer Editing

## Outcome

Assemble cinematic sequences with camera cuts and timecode review. The result must be traceable to supplied inputs and pass the checks below.

## Inputs and prerequisites

- Project version, target platform, render pipeline, plugin/package set, asset specifications, and acceptance criteria.
- The installed Unreal Editor or Unity Editor, their scripting/command-line interfaces, profilers, and project logs.
- Confirm the target application's version and the actual capabilities available in this environment.

## Procedure

1. Inspect project version, target platform, render pipeline, plugins/packages, and existing conventions.
2. Import assets into a dedicated staging location with correct units, pivots, materials, collisions, and LODs.
3. Use engine-native systems and keep generated assets separate from hand-authored source content.
4. Profile the target scene/build; do not optimize from visual guesswork or editor-only timing.
5. Build from a clean state and inspect logs, missing references, shader compilation, and startup behavior.
6. Test on the intended platform or report the exact platform that was not available.

## Quality gates

- A successful editor import does not prove a package build works.
- Do not change project-wide rendering or package versions without a scoped impact review.
- Performance claims require a captured baseline and comparable test conditions.

## Deliverable

Engine project changes, imported asset manifest, build/profile evidence, and platform-specific limitations. Include the exact commands or application operations used, the files changed, and the checks that were actually run.

## Boundaries

- Keep source files unchanged; write new versions to an explicit output path.
- Do not transmit private assets or prompts to an external provider unless the user has explicitly approved that destination.
- Do not run paid generation or destructive application operations without clear authorization and a stated budget or scope.
- If a required application, plugin, model, or entitlement is absent, report the limitation and stop at the last verified stage.
- Separate measured results from visual judgment, assumptions, and recommendations.
