# Architecture

- `skills/`: portable Agent Skills instructions. They are deliberately separate from the Python runtime.
- `src/agentic_skill_garage/`: standard-library CLI and bounded adapters.
- `config/`: safe examples; no keys or live provider prices are included.
- `tests/`: deterministic tests using temporary directories and mocked external services.
- `assets/` + `index.html`: static GitHub Pages showcase.

The Python package is local-first. It has no telemetry, no background tasks, no database, and no automatic provider discovery. The ComfyUI adapter defaults to loopback. Pricing is read from a user-maintained card, never fetched.
