<div align="center">

<img src="assets/agentic-skill-garage-hero.svg" alt="Agentic Skill Garage" width="100%">

# Agentic Skill Garage

### Creative production workflows for AI agents.

A portable library of **219 agent skills** backed by a **local-first Python toolkit** for managing references, preparing creative assets, connecting local tools, and validating deliverables across image, video, audio, 3D, and game-art workflows.

<p>
  <a href="https://github.com/voyager67/Agentic-Skill-Garage/actions/workflows/ci.yml"><img src="https://img.shields.io/github/actions/workflow/status/voyager67/Agentic-Skill-Garage/ci.yml?branch=main&style=flat-square&label=CI" alt="CI status"></a>
  <a href="https://github.com/voyager67/Agentic-Skill-Garage/stargazers"><img src="https://img.shields.io/github/stars/voyager67/Agentic-Skill-Garage?style=flat-square" alt="GitHub stars"></a>
  <a href="https://github.com/voyager67/Agentic-Skill-Garage/network/members"><img src="https://img.shields.io/github/forks/voyager67/Agentic-Skill-Garage?style=flat-square" alt="GitHub forks"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python 3.10 or newer"></a>
  <a href="skills-index.json"><img src="https://img.shields.io/badge/Agent%20Skills-219-7867d5?style=flat-square" alt="219 agent skills"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/Toolkit%20License-Apache--2.0-3b9b83?style=flat-square" alt="Toolkit license Apache 2.0"></a>
</p>

[Explore the showcase](https://voyager67.github.io/Agentic-Skill-Garage/) · [Browse all skills](skills/) · [Read the security policy](SECURITY.md)

</div>

---

## Overview

Creative work often spans multiple tools: references need organizing, assets need consistent treatment, applications need coordination, and final outputs need validation. Agentic Skill Garage brings those steps together through two complementary components:

- **Agent skills** — focused, reusable `SKILL.md` workflows that give compatible AI agents structured procedures, prerequisites, quality gates, and clear deliverables.
- **Python toolkit** — the `asg` command-line interface for practical local operations such as asset intake, hashing, identity profiles, image processing, media conversion, ComfyUI requests, and Blender scene checks.

The project is designed to work alongside the tools you already use. It does not require a particular model provider, and it does not claim that a skill replaces a dedicated creative application.

## Demo

<div align="center">

[![Agentic Skill Garage CLI walkthrough](assets/agentic-skill-garage-preview.gif)](assets/agentic-skill-garage-demo.mp4)

[**Watch the full CLI walkthrough (MP4)**](assets/agentic-skill-garage-demo.mp4) · [Open the project showcase](https://voyager67.github.io/Agentic-Skill-Garage/)

</div>

The demonstration uses synthetic inputs and shows local CLI operations. It is not a recording of a paid hosted-generation workflow.

## Capabilities

| Area | Workflows and operations |
|---|---|
| **Image** | Reference preparation, generation workflows, restoration, compositing, resizing, contact sheets, sprite sheets, and export checks |
| **Video** | Briefs and storyboards, shot planning, continuity, rough cuts, audio sync, color workflows, and delivery validation |
| **Audio** | Dialogue cleanup, sound design, localization, loudness and true-peak checks, and mastering preflight |
| **3D** | Modeling, sculpting, topology, UVs, materials, rigging, baking, and interchange formats |
| **Creative applications** | Specialist workflows for Blender, Maya, ZBrush, Unreal Engine, Unity, and Godot |
| **Generative workflows** | Local ComfyUI, model selection, capability discovery, prompt contracts, job monitoring, and cost gates |
| **Asset operations** | File intake, SHA-256 manifests, duplicate detection, identity profiles, and reference handoffs |
| **Engineering and research** | Repository analysis, API contracts, testing, debugging, security review, dataset quality, and model evaluation |

The complete catalogue is available in the [skill index](skills-index.json). Each skill lives in its own directory under [`skills/`](skills/).

## Getting started

### Requirements

- Python **3.10 or newer** for the toolkit.
- Pillow for optional image-processing commands.
- FFmpeg and FFprobe for media operations.
- Blender for Blender scene auditing and rendering.
- A running ComfyUI instance for ComfyUI operations.
- Node.js and the `skills` CLI only if you want to install the skill library into a supported agent environment.

External creative applications and services are optional. Install and configure only the tools required by the workflows you plan to use.

### 1. Clone and install the Python toolkit

```bash
git clone https://github.com/voyager67/Agentic-Skill-Garage.git
cd Agentic-Skill-Garage

python -m venv .venv

# Activate the environment:
# Windows PowerShell
.venv\Scripts\Activate.ps1
# macOS / Linux
source .venv/bin/activate

# Install the toolkit with optional image support
python -m pip install -e ".[images]"

# Check which local tools are available
asg doctor
```

The core package uses Python's standard library. The `images` extra installs Pillow; it does not install FFmpeg, Blender, ComfyUI, or other creative applications.

### 2. Install the agent skills

The skill library uses the open Agent Skills format. Install it with the `skills` CLI:

```bash
npx skills add voyager67/Agentic-Skill-Garage --all
```

To disable the installer's own anonymous telemetry for this command, set the environment variable first:

```bash
# macOS / Linux
DISABLE_TELEMETRY=1 npx skills add voyager67/Agentic-Skill-Garage --all

# Windows PowerShell
$env:DISABLE_TELEMETRY = "1"
npx skills add voyager67/Agentic-Skill-Garage --all
```

The installer's telemetry setting is separate from Agentic Skill Garage. This project includes no analytics or telemetry code. Refer to the [skills CLI documentation](https://www.skills.sh/docs/cli) for supported agents and installation options.

## Using the toolkit

The `asg` CLI provides explicit local operations. Run `asg --help` or `asg <command> --help` for the full command reference.

### Asset library and identity

```bash
# Ingest selected folders while preserving their relative structure
asg assets ingest ./references --recursive --library ./asg-assets

# List ingested assets
asg assets list --library ./asg-assets

# Create an identity profile
asg identity init "Nova" --kind character --output ./identity/nova.json

# Build a reference-aware prompt packet
asg identity prompt ./identity/nova.json --manifest ./asg-assets/manifest.jsonl
```

### Image and media

```bash
# Inspect an image
asg image info ./references/hero.png

# Resize without overwriting the source
asg image resize ./references/hero.png ./exports/hero.webp --width 1600 --height 900 --fit contain

# Create a contact sheet
asg image contact-sheet ./references/one.png ./references/two.png --output ./exports/contact.jpg

# Inspect media and measure loudness
asg media probe ./input.mov
asg media loudness ./input.mov

# Normalize audio and transcode media
asg media normalize-audio ./input.mov ./exports/normalized.wav --target-lufs -16
asg media transcode ./input.mov ./exports/web.mp4 --preset h264-web
```

### Local ComfyUI and Blender

```bash
# Check the default local ComfyUI endpoint
asg comfyui status

# Explicitly upload one selected reference image
asg comfyui upload ./references/hero.png

# Submit an API-format workflow and monitor the returned prompt ID
asg comfyui submit ./workflow-api.json
asg comfyui wait <prompt-id> --timeout 600

# Audit a Blender scene or render a still frame
asg blender audit ./scene.blend
asg blender render ./scene.blend ./renders/preview --frame 1
```

ComfyUI defaults to loopback. Remote HTTPS endpoints require the explicit `--allow-remote` option. A workflow submission sends the supplied workflow JSON to the configured ComfyUI server; it does not automatically upload the local reference files referenced by that workflow. Use the separate upload command only for files you intend to transfer.

## How the project is organized

```text
.
├── skills/                       # Portable SKILL.md workflows
├── skills-index.json              # Machine-readable skill catalogue
├── src/agentic_skill_garage/      # Python package and CLI implementation
├── tests/                         # Automated tests
├── scripts/                       # Catalogue validation
├── config/                        # Safe example configuration
├── docs/                          # Architecture notes
├── examples/                      # Usage examples
├── assets/                        # Demo and visual assets
├── .github/workflows/             # CI and Pages deployment
├── index.html                     # Static project showcase
└── pyproject.toml                  # Python package configuration
```

### Design principles

- **Local-first:** local asset and media operations run on the user's machine.
- **Explicit network boundaries:** no automatic provider discovery, background uploads, or hidden external transfers.
- **Cost awareness:** estimates are based on user-maintained, dated rate cards; missing or stale prices are not treated as free.
- **Safer file handling:** inputs are preserved, outputs use explicit destinations, and overwrite behavior is guarded.
- **Portable skills:** workflows are plain Markdown and are kept separate from the Python runtime.
- **Evidence over claims:** application-specific compatibility and live service behavior must be tested in the environment where they will be used.

## Privacy and security

Agentic Skill Garage includes no telemetry, analytics, or background synchronization. It does not bundle hosted-provider API clients or require provider credentials for the core toolkit.

Some operations intentionally communicate with a local or explicitly configured service. For example, ComfyUI status checks, workflow submissions, and explicit image uploads send requests to the selected ComfyUI endpoint. Review the destination before allowing a remote connection.

Before using the project with private assets or external services, read:

- [Privacy and data handling](PRIVACY.md)
- [Security policy](SECURITY.md)

Do not commit API keys, access tokens, private URLs, customer assets, identity profiles, or local asset manifests.

## Testing and validation

Run the catalogue validator and unit tests from the repository root:

```bash
python scripts/validate_skills.py
python -m unittest discover -s tests -v
```

GitHub Actions runs the validation and test suite against Python 3.10, 3.11, 3.12, and 3.13. The tests use temporary files and mocked external services where appropriate; they do not replace testing with the actual installed creative applications or a live ComfyUI server.

## Contributing

Issues and pull requests are welcome for concrete workflow improvements, bug fixes, compatibility corrections, tests, and documentation.

Before contributing:

1. Read [CONTRIBUTING.md](CONTRIBUTING.md).
2. Keep changes focused and consistent with the existing architecture.
3. Add or update tests when changing executable behavior.
4. Run the validator and relevant tests.
5. Document application versions, prerequisites, and limitations for workflow changes.

Please do not submit credentials, private media, customer data, or unlicensed third-party content.

## Project scope

A skill provides instructions and workflow structure; it does not install a proprietary editor, provide a hosted model, or guarantee that an external service is available. Blender, Maya, ZBrush, Unreal Engine, Unity, Godot, ComfyUI, Scenario MCP, and other integrations require the relevant application, service, configuration, and permissions. Capabilities that have not been tested in the target environment should be treated as unverified.

## License and provenance

The Python toolkit and project-authored repository documentation and showcase are covered by the root [Apache License 2.0](LICENSE).

The skill library has a documented licensing-provenance issue: all 219 current `SKILL.md` files declare Apache-2.0 in their frontmatter, while an earlier maintainer record identifies 25 legacy engineering/research skills as MIT-licensed and refers to an original MIT notice that is not present in the current tree. The affected paths and original attribution still require verification. Do not assume the root license resolves that historical issue; review [NOTICE.md](NOTICE.md) before redistributing skill files.

Third-party applications, models, extensions, and services retain their own licenses and terms. See [REFERENCES.md](REFERENCES.md) for project and compatibility references.

---

<div align="center">

**Agentic Skill Garage**  
*Open workflows. Practical tools. Verifiable output.*

</div>
