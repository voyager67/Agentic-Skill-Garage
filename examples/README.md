# Example project assets

Create a project-local asset folder and identity profile, then keep generated outputs and final approvals beside a manifest. Do not commit private assets to the public repository.

```bash
asg assets ingest ./private-references/hero.png --library ./project-assets
asg identity init "Project Hero" --kind character --output ./project/hero.json
asg identity prompt ./project/hero.json --manifest ./project-assets/manifest.jsonl
```
