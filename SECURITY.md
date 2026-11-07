# Security policy

## Data handling

The core toolkit is local-first. It does not include telemetry, analytics, background uploads, or default provider API calls. Asset ingestion stores copies and hashes locally. Identity packets include file names and hashes, not file contents.

ComfyUI requests default to loopback. Remote HTTP endpoints are blocked; remote HTTPS endpoints require the explicit `--allow-remote` flag. A ComfyUI workflow can execute operations on the connected ComfyUI host, so submit only workflows and custom nodes you trust. Scenario MCP operations are performed only through a user-configured MCP connection; inspect the live tool schema and data-transfer/billing behavior before invoking it. Workflow submission does not upload referenced image files automatically. The separate `comfyui upload` command transfers only the one file explicitly named by the user to the selected ComfyUI instance (50 MiB maximum).

Do not place credentials in repository files, CLI arguments, screenshots, logs, or public issues. The examples contain no working API keys. Use each provider's supported secret store when you deliberately configure a provider.

## Reporting

Do not disclose an exploit, secret, private asset, or user data in a public issue. Report security issues privately to the repository maintainer using a private contact route shown on the public GitHub profile, where available.

## Maintainer checks

- Inspect symlink handling and no-overwrite behavior when changing file operations.
- Keep network access opt-in and restrict local service adapters to loopback by default.
- Keep optional app integrations disabled when the required application or entitlement is absent.
- Do not transmit repository contents or personal media to a model provider without explicit approval.
- Run `python -m unittest discover -s tests -v` after changing helpers.
