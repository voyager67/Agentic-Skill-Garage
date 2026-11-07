# Agentfieldkit maintainer and agent guidance

- The combined library follows the Agent Skills format. Canonical skill files live in `skills/<name>/SKILL.md`.
- Keep new skills focused, searchable, portable, and grounded in capabilities available from installed tools or explicitly connected providers.
- Think before editing: inspect the relevant code, requirements, and tests first. Prefer the smallest correct change.
- Preserve original inputs. File-processing commands must write to new paths and reject overwrite by default.
- Verify behavior with repeatable commands. Report exactly what ran and what was unavailable.
- Never include API keys, tokens, credentials, personal file paths, private media, or non-public customer data in public files, logs, examples, or test fixtures.
- New creative-production skills and new Python tooling use Apache-2.0. The original 25 engineering/research skills remain MIT; retain `licenses/ORIGINAL-MIT.txt` and their existing per-skill metadata.
- Keep ComfyUI local by default. Scenario MCP is an optional user-configured connection: inspect live schemas, price exact payloads when supported, and obtain authorization before uploads or paid jobs.
- Do not claim a paid application has been replaced when the workflow only orchestrates it. State the installed application, model, license, and host requirements.
- Run `python scripts/validate_skills.py` and `python -m unittest discover -s tests -v` before publishing.
