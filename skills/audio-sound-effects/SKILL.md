---
name: audio-sound-effects
description: Use when the task is to design and organize sound effects with source and usage records.
license: Apache-2.0
---

# Audio Sound Effects

## Outcome

Design and organize sound effects with source and usage records. The result must be traceable to supplied inputs and pass the checks below.

## Inputs and prerequisites

- Source recordings, consent status, target platform loudness, sample rate, channel layout, and cue sheet.
- FFmpeg/FFprobe, Audacity, REAPER or another installed editor, and an explicitly configured transcription model.
- Confirm the target application's version and the actual capabilities available in this environment.

## Procedure

1. Inspect duration, sample rate, channel layout, clipping, noise, and peak levels before processing.
2. Work on a copy and keep the untouched source as the recovery baseline.
3. Clean dialogue conservatively; compare before/after at normal listening level and on headphones.
4. Align music, effects, voice, and picture using timecode or measurable waveform cues.
5. Normalize to the stated platform target and verify integrated loudness and true peak.
6. Export stems and master files with consistent start time, naming, bit depth, and metadata.

## Quality gates

- Voice cloning or dubbing requires clear rights and consent for the voice and source material.
- Noise reduction must not erase consonants, transients, or meaningful ambience.
- Subtitles and transcripts are reviewed for names, numbers, and timing.

## Deliverable

A mastered audio file, required stems, transcript/captions, technical measurements, and consent/rights notes. Include the exact commands or application operations used, the files changed, and the checks that were actually run.

## Boundaries

- Keep source files unchanged; write new versions to an explicit output path.
- Do not transmit private assets or prompts to an external provider unless the user has explicitly approved that destination.
- Do not run paid generation or destructive application operations without clear authorization and a stated budget or scope.
- If a required application, plugin, model, or entitlement is absent, report the limitation and stop at the last verified stage.
- Separate measured results from visual judgment, assumptions, and recommendations.
