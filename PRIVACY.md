# Privacy and data handling

Agentic Skill Garage is local-first. It does not include telemetry, usage analytics, background uploads, or automatic provider calls.

## Local operations

- `assets ingest`, `assets list`, and identity prompt generation operate on local files.
- SHA-256 values and asset metadata are written to a project-local JSONL manifest. The manifest contains local file names, not absolute source paths.
- FFmpeg and Blender commands execute locally when those applications are installed.
- `doctor` checks local executable availability. It does not probe third-party services.

## Network boundaries

- ComfyUI defaults to `http://127.0.0.1:8188`. Non-loopback hosts are rejected unless `--allow-remote` is deliberately supplied.
- ComfyUI submission sends the supplied workflow JSON to the configured ComfyUI endpoint. It does not automatically upload local reference images.
- There are no bundled hosted-provider API clients and no API keys in the repository.
- Scenario MCP workflows run only through a server connection the user configures in their agent. Prompts, uploaded assets, billing, and retention are then governed by that service and its current settings.
- External providers, MCP servers, and cloud storage are used only when the user explicitly connects them through their own agent/application configuration.

## Credentials and files

- Never commit `.env`, access tokens, private URLs, customer assets, or personal data.
- `.env.example` contains only a loopback endpoint placeholder.
- Do not place confidential assets in public demo directories or GitHub Pages.
- Keep project asset manifests and identity profiles out of version control when they describe private projects.

## Retention

Agentic Skill Garage does not retain or sync files outside the directories selected by the user. Deleting a local project library is a user-managed filesystem action. External provider retention is governed by that provider's terms and settings, not this project.


Image commands read local files using Pillow when installed. They create new outputs, do not overwrite inputs, and do not transmit the images.

The optional ComfyUI upload command sends one explicitly selected image to the configured ComfyUI server. It defaults to loopback; a remote HTTPS destination requires `--allow-remote`. No references are uploaded as a side effect of submitting a workflow.
