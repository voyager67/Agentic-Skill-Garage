---
name: video-social-reframe
description: Use when the task is to reframe landscape footage for vertical and square outputs without losing subjects.
license: Apache-2.0
---

# Video Social Reframe

## Outcome

Reframe landscape footage for vertical and square outputs without losing subjects. The result must be traceable to supplied inputs and pass the checks below.

## Inputs and prerequisites

- Brief, aspect ratio, duration, frame rate, shot list, source clips, music/dialogue, and platform delivery spec.
- FFmpeg/FFprobe, an editor such as Kdenlive or Blender VSE, and an approved video model only when configured.
- Confirm the target application's version and the actual capabilities available in this environment.

## Procedure

1. Build a shot list with time budgets, camera intent, screen direction, and continuity constraints.
2. Inspect all source clips with FFprobe before editing; note duration, codec, frame rate, color, and audio streams.
3. Assemble a rough cut before polishing transitions, grades, effects, or captions.
4. Match exposure, white balance, motion cadence, and sound levels across adjacent shots.
5. Render a review proxy and check the full timeline, not only representative frames.
6. Create final masters with explicit codec, bitrate, audio, color, and metadata settings.

## Quality gates

- No source clip is overwritten; exports go to a separate destination.
- Character, wardrobe, props, screen direction, and audio continuity are checked across cuts.
- Final files are decoded with FFprobe and inspected at full duration.

## Deliverable

Timeline/source manifest, review proxy, delivery masters, captions where required, and QC notes. Include the exact commands or application operations used, the files changed, and the checks that were actually run.

## Boundaries

- Keep source files unchanged; write new versions to an explicit output path.
- Do not transmit private assets or prompts to an external provider unless the user has explicitly approved that destination.
- Do not run paid generation or destructive application operations without clear authorization and a stated budget or scope.
- If a required application, plugin, model, or entitlement is absent, report the limitation and stop at the last verified stage.
- Separate measured results from visual judgment, assumptions, and recommendations.
