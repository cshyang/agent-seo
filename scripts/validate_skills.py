#!/usr/bin/env python3
"""Validate Hermes-style skill frontmatter in this repo."""
from __future__ import annotations

import argparse
from pathlib import Path

try:
    import yaml  # type: ignore
except Exception as exc:  # pragma: no cover - depends on environment
    raise SystemExit("PyYAML is required for skill validation. Install pyyaml.") from exc


def validate_skill(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    errors: list[str] = []
    if not text.startswith("---\n"):
        return ["missing opening YAML frontmatter marker"]
    end = text.find("\n---\n", 4)
    if end == -1:
        return ["missing closing YAML frontmatter marker"]
    raw = text[4:end]
    try:
        data = yaml.safe_load(raw)
    except Exception as exc:
        return [f"invalid YAML frontmatter: {exc}"]
    if not isinstance(data, dict):
        return ["frontmatter must parse to a mapping/object"]
    for key in ["name", "description"]:
        value = data.get(key)
        if not isinstance(value, str) or not value.strip():
            errors.append(f"missing or invalid required field: {key}")
    description = str(data.get("description", ""))
    if len(description) > 1024:
        errors.append("description exceeds 1024 characters")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="*", type=Path, default=[Path("skills")])
    args = parser.parse_args()

    skill_files: list[Path] = []
    for path in args.paths:
        if path.is_file():
            skill_files.append(path)
        else:
            skill_files.extend(path.rglob("SKILL.md"))

    failed = False
    for skill in sorted(skill_files):
        errors = validate_skill(skill)
        if errors:
            failed = True
            print(f"Skill invalid: {skill}")
            for error in errors:
                print(f"- {error}")
        else:
            print(f"Skill OK: {skill}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
