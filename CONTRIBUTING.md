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

New Python toolkit code, repository documentation, website files, and newly authored skills default to Apache-2.0 unless a file or subtree carries another license. Preserve existing per-skill license metadata and upstream notices. Repository history records 25 legacy engineering/research skills as MIT, but the corresponding MIT license file and affected-path list are absent from the current tree; do not relabel or claim those legacy files as Apache-2.0 until their source provenance and notices are restored. See NOTICE.md.
