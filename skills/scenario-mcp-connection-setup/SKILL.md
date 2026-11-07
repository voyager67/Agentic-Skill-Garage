---
name: scenario-mcp-connection-setup
description: Use when connecting an AI agent to the public Scenario MCP server or diagnosing its tool discovery and authorization setup.
license: Apache-2.0
---

# Scenario MCP Connection Setup

## Outcome
Establish a user-controlled Scenario MCP connection without exposing credentials or assuming a particular client configuration.

## Procedure
1. Confirm the user intends to use Scenario-hosted services and that sending the planned prompts and assets to that service is acceptable.
2. Read the current public Scenario MCP setup documentation and the connected agent's MCP configuration format. Do not rely on stale copied snippets.
3. Ask the user to complete authentication in the official client flow. Never request a raw API key, secret, bearer token, or session cookie in chat.
4. Store credentials only in the client-supported secret store or environment-variable reference. Do not commit a populated configuration file.
5. Ask the MCP client to reconnect, then enumerate the actual tools and read their descriptions before using them.
6. Run a non-billable read operation, if available, to confirm connectivity and account visibility. Do not submit a generation job as a connectivity test.
7. Record the client, server endpoint, observed tool names, and setup date without recording secret values.

## Quality gates
- A configured endpoint is not proof that authentication or permissions work.
- Do not infer tool names, parameters, plan entitlements, or model availability from a skill file.
- A local DCC bridge and the hosted Scenario MCP server are separate connections with separate permissions.

## Deliverable
A connection checklist with observed client/server status, available tool families, missing permissions, and a safe next step.

## Boundaries
- Never print, persist, screenshot, or transmit credentials in public artifacts.
- Do not alter account, billing, workspace, or team settings without explicit authorization.
- Treat every generation or upload operation as a possible external data transfer or paid action.
- If the current public docs or the live client schema are unavailable, stop and report what remains unverified.
