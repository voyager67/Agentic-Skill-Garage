---
name: maya-fx-simulation
description: Use when the task is to plan Bifrost, nCloth, particles, and simulation caches safely.
license: Apache-2.0
---

# Maya Fx Simulation

## Outcome

Plan Bifrost, nCloth, particles, and simulation caches safely. The result must be traceable to supplied inputs and pass the checks below.

## Inputs and prerequisites

- Maya scene, application version, reference policy, target renderer/engine, and named output scope.
- Autodesk Maya, maya.cmds, OpenMaya API 2.0, mayapy, and a version-matched batch runtime.
- Confirm the target application's version and the actual capabilities available in this environment.

## Procedure

1. Inspect the Maya version, scene units, references, namespaces, plugins, render settings, and file paths.
2. Resolve broken references and naming collisions before modeling or rigging changes.
3. Use maya.cmds for readable operations and OpenMaya for operations that require explicit mesh/API access.
4. Keep scripts scene-scoped and idempotent; log changed nodes and avoid broad wildcard edits.
5. Run validation in a fresh mayapy or batch process when the task supports headless execution.
6. Export to a new location and reopen in a clean scene or target engine.

## Quality gates

- Do not assume a plugin or renderer is installed because a scene references it.
- Do not delete unknown nodes, references, or namespaces to silence warnings.
- Version-specific commands must be checked against the installed Maya API.

## Deliverable

Updated scene, versioned scripts, reference report, export package, and reproducible validation log. Include the exact commands or application operations used, the files changed, and the checks that were actually run.

## Boundaries

- Keep source files unchanged; write new versions to an explicit output path.
- Do not transmit private assets or prompts to an external provider unless the user has explicitly approved that destination.
- Do not run paid generation or destructive application operations without clear authorization and a stated budget or scope.
- If a required application, plugin, model, or entitlement is absent, report the limitation and stop at the last verified stage.
- Separate measured results from visual judgment, assumptions, and recommendations.
