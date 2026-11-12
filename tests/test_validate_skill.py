"""Unit tests for documentation-package validation; not MCP security tests."""

import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_skill import validate_skill  # noqa: E402


class ValidateSkillTests(unittest.TestCase):
    def test_repo_skill_is_valid(self):
        self.assertEqual([], validate_skill())

    def test_missing_skill_fails_closed(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.assertTrue(validate_skill(Path(tmp)))

    def test_missing_references_detected(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill = Path(tmp) / "mcp-server-security"
            skill.mkdir()
            (skill / "SKILL.md").write_text(
                "---\nname: mcp-server-security\n"
                "description: Secure MCP servers.\nlicense: MIT\n"
                "---\n# MCP Server Security\n", encoding="utf-8"
            )
            findings = validate_skill(skill)
            self.assertTrue(any("Missing references/" in f for f in findings))


if __name__ == "__main__":
    unittest.main()
