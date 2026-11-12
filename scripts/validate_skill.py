#!/usr/bin/env python3
"""Dependency-free structural validation for the bundled Agent Skill.

This intentionally does not audit or execute an MCP server.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = REPO_ROOT / "skills" / "mcp-server-security"
NAME = "mcp-server-security"
REQUIRED_REFERENCES = (
    "PROTOCOL.md",
    "THREATS.md",
    "CONTROLS.md",
    "TESTS.md",
    "SOURCES.md",
)


def validate_skill(skill_root: Path = SKILL_ROOT) -> list[str]:
    errors: list[str] = []
    path = skill_root / "SKILL.md"
    if not path.is_file():
        return [f"Missing {path}"]

    content = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\r?\n(.*?)\r?\n---\r?\n", content, re.DOTALL)
    if not match:
        return ["SKILL.md is missing YAML frontmatter"]

    frontmatter = match.group(1)
    name = re.search(r"^name:\s*(\S+?)\s*$", frontmatter, re.MULTILINE)
    description = re.search(r"^description:\s*(.+?)\s*$", frontmatter, re.MULTILINE)
    license_field = re.search(r"^license:\s*(.+?)\s*$", frontmatter, re.MULTILINE)

    if not name or name.group(1) != NAME or path.parent.name != NAME:
        errors.append("Skill name must match mcp-server-security directory")
    if not description or len(description.group(1).strip(" \"'")) not in range(1, 1025):
        errors.append("Missing or oversized description")
    elif ": " in description.group(1) and not (
        (description.group(1).startswith('"') and description.group(1).endswith('"'))
        or (description.group(1).startswith("'") and description.group(1).endswith("'"))
    ):
        errors.append("Description with a colon must be quoted as YAML")
    if not license_field or license_field.group(1).strip() != "MIT":
        errors.append("Skill license must be MIT")

    for required in REQUIRED_REFERENCES:
        if not (skill_root / "references" / required).is_file():
            errors.append(f"Missing references/{required}")

    if not (skill_root / "assets" / "CONTRACT.example.yaml").is_file():
        errors.append("Missing assets/CONTRACT.example.yaml")

    # Only inspect local Markdown references in the entry-point skill.
    for destination in re.findall(r"\]\(([^)]+)\)", content):
        target = destination.split("#", 1)[0]
        if target and not re.match(r"^[a-z]+://", target, re.IGNORECASE):
            resolved = (skill_root / target).resolve()
            try:
                resolved.relative_to(skill_root.resolve())
            except ValueError:
                errors.append(f"Link escapes the skill root: {destination}")
                continue
            if not resolved.is_file():
                errors.append(f"Broken local link: {destination}")

    return errors


if __name__ == "__main__":
    findings = validate_skill()
    for finding in findings:
        print(f"ERROR: {finding}", file=sys.stderr)
    if findings:
        sys.exit(1)
    print("PASS: skill package structure, metadata and referenced files")
