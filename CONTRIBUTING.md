# Contributing to Agentic Skill Garage

Contributions should improve a real task, not inflate a skill count.

## Add a skill

1. Create `skills/<lowercase-hyphen-name>/SKILL.md` with `name`, `description`, and `license` frontmatter.
2. Make the description searchable and trigger-oriented. Keep the body focused on prerequisites, steps, quality checks, a concrete deliverable, and safety boundaries.
3. Ground application-specific commands in public documentation and identify version or license prerequisites.
4. Update `skills-index.json` and add tests for any helper code.
5. Do not include API keys, personal media, private file paths, customer assets, or copied third-party content without a compatible license and required attribution.

## Code quality

- Inspect existing conventions before editing; favor simple, surgical changes.
- Use the standard library unless an optional dependency materially adds capability. Keep optional dependencies lazy-loaded.
- Never overwrite source assets by default. Reject symlink inputs and unsafe output paths.
- Do not invent provider prices. Require dated, sourced rate-card entries and an explicit approval step for paid work.
- External data transfer and destructive actions require explicit authorization.
- Add deterministic tests, then run the validator and full unit-test suite.
- Report measured results separately from assumptions and visual judgment.

## License

New contributions are Apache-2.0 unless a file or subtree carries an explicitly preserved third-party license. Do not relabel the original MIT-licensed skill files.
