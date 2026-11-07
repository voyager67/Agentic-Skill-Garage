---
name: blender-python-automation
description: Use when the task is to automate Blender through bpy with bounded, reviewable scripts.
license: Apache-2.0
---

# Blender Python Automation

## Outcome

Automate Blender through bpy with bounded, reviewable scripts. The result must be traceable to supplied inputs and pass the checks below.

## Inputs and prerequisites

- A named .blend file, target Blender version, expected scene objects, render target, and allowed edit scope.
- Blender Python API (bpy), Blender background mode, and the Agentic Skill Garage Blender audit command.
- Confirm the target application's version and the actual capabilities available in this environment.

## Procedure

1. Inspect the scene and its version before editing; record objects, collections, cameras, render engine, and frame range.
2. Open files with Python auto-execution disabled unless the user explicitly trusts the source.
3. Make changes through small bpy scripts with explicit object names and deterministic parameters.
4. Save to a new project file before batch operations; preserve the original as a rollback point.
5. Render a low-cost preview and inspect framing, materials, lighting, and output dimensions.
6. Run the final export or render and record Blender version, command, exit code, and output hash.

## Quality gates

- Do not execute unknown embedded scripts or enable auto-run as a workaround.
- Use background mode for deterministic batch tasks; GUI-only capture tools must be identified as such.
- Never claim a Blender test passed when Blender is absent.

## Deliverable

A versioned .blend file, rendered/exported outputs, scene audit JSON, and exact verification evidence. Include the exact commands or application operations used, the files changed, and the checks that were actually run.

## Boundaries

- Keep source files unchanged; write new versions to an explicit output path.
- Do not transmit private assets or prompts to an external provider unless the user has explicitly approved that destination.
- Do not run paid generation or destructive application operations without clear authorization and a stated budget or scope.
- If a required application, plugin, model, or entitlement is absent, report the limitation and stop at the last verified stage.
- Separate measured results from visual judgment, assumptions, and recommendations.
