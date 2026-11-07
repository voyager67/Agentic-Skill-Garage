# Public references

The project uses these public resources as design and compatibility references. Their code and documentation retain their own licenses.

- [Scenario MCP documentation](https://mcp.scenario.com/docs): live hosted tool reference and connection documentation. The integration is invoked through a user-configured agent connection, not a bundled SDK.
- [Scenario Agent Skills](https://github.com/scenario-labs/skills): a large, production-oriented skill library covering generative media, asset consistency, model selection, DCC tools, and game engines. The repository is MIT-licensed. This release independently implements its own skills and tooling.
- [Agent Skills specification](https://agentskills.io/specification): directory structure, `SKILL.md` frontmatter, progressive disclosure, and validation guidance.
- [Blender command-line manual](https://docs.blender.org/manual/en/latest/advanced/command_line/index.html): background automation and batch rendering.
- [Blender Python API](https://docs.blender.org/api/current/): scripting and scene operations.
- [FFmpeg documentation](https://ffmpeg.org/documentation.html): media probing, filters, transcoding, and stream operations.
- [ComfyUI](https://github.com/Comfy-Org/ComfyUI): local graph-based diffusion interface and API workflows. ComfyUI is GPL-3.0; it is not bundled or copied into this repository.
- [GIMP](https://www.gimp.org/), [Krita](https://krita.org/), [Audacity](https://www.audacityteam.org/), [Kdenlive](https://kdenlive.org/), [Godot](https://godotengine.org/), [Maya](https://www.autodesk.com/products/maya/overview), [ZBrush](https://www.maxon.net/en/zbrush), [Unreal Engine](https://www.unrealengine.com/), and [Unity](https://unity.com/): optional application targets documented by the skills.

This list records design references, not an endorsement or a claim that every integration was tested in this environment.
