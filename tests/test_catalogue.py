from __future__ import annotations
import json
import os
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class CatalogueTests(unittest.TestCase):
    def test_catalogue_matches_all_skill_directories(self):
        catalogue = json.loads((ROOT / "skills-index.json").read_text(encoding="utf-8"))
        actual = {
            path.name for path in (ROOT / "skills").iterdir()
            if path.is_dir() and (path / "SKILL.md").is_file()
        }
        indexed = {item["name"] for item in catalogue["skills"]}
        self.assertEqual(catalogue["name"], "Agentic Skill Garage")
        self.assertEqual(catalogue["skill_count"], 219)
        self.assertEqual(indexed, actual)

    def test_validator_succeeds(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "validate_skills.py")],
            cwd=ROOT, capture_output=True, text=True, check=False,
        )
        self.assertEqual(result.returncode, 0, msg=result.stdout + result.stderr)

    def test_python_module_version(self):
        env = os.environ.copy()
        env["PYTHONPATH"] = str(ROOT / "src") + os.pathsep + env.get("PYTHONPATH", "")
        result = subprocess.run(
            [sys.executable, "-m", "agentic_skill_garage", "--version"],
            cwd=ROOT, env=env, capture_output=True, text=True, check=False,
        )
        self.assertEqual(result.returncode, 0, msg=result.stdout + result.stderr)
        self.assertIn("Agentic Skill Garage 1.0.0", result.stdout)


if __name__ == "__main__":
    unittest.main()
