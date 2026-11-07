---
name: game-parallax-backgrounds
description: Use when the task is to build layered backgrounds with depth, repeat, and camera-motion checks.
license: Apache-2.0
---

# Game Parallax Backgrounds

## Outcome

Build layered backgrounds with depth, repeat, and camera-motion checks. The result must be traceable to supplied inputs and pass the checks below.

## Inputs and prerequisites

- Godot version, target platform, scene/resource paths, input map, asset dimensions, and expected behavior.
- Godot editor/CLI, GDScript, project.godot, import settings, and reproducible export presets.
- Confirm the target application's version and the actual capabilities available in this environment.

## Procedure

1. Inspect Godot version, project settings, autoloads, input map, scenes, resources, and export presets.
2. Import assets with explicit filtering, compression, pixel density, and atlas/terrain settings.
3. Keep scene ownership, resource paths, and node responsibilities clear and testable.
4. Validate animation timing, collision, focus/navigation, audio buses, and shader fallback.
5. Run headless project checks where supported and open a representative scene in the editor.
6. Export to a new build folder and test the resulting project rather than relying on editor state.

## Quality gates

- Do not assume a resource imported correctly because it appears in the FileSystem dock.
- Check pixel art at native scale and game UI at supported aspect ratios.
- Report missing export templates or platform SDKs rather than hiding the failure.

## Deliverable

Validated scenes/resources, import settings, a reproducible export, and an issue list for unverified targets. Include the exact commands or application operations used, the files changed, and the checks that were actually run.

## Boundaries

- Keep source files unchanged; write new versions to an explicit output path.
- Do not transmit private assets or prompts to an external provider unless the user has explicitly approved that destination.
- Do not run paid generation or destructive application operations without clear authorization and a stated budget or scope.
- If a required application, plugin, model, or entitlement is absent, report the limitation and stop at the last verified stage.
- Separate measured results from visual judgment, assumptions, and recommendations.
