#!/usr/bin/env python3
"""QA checks for content briefs (templates/content-brief-template.md)."""
from __future__ import annotations

import argparse
import re
from pathlib import Path

from qa_report import _section, find_placeholders

VOLUME_RE = re.compile(r"\d[\d,]*\s*/\s*mo\b")
REQUIRED_SECTIONS = [
    ("## 1.", "Section 1 demand evidence"),
    ("## 2.", "Section 2 target"),
    ("## 3.", "Section 3 cannibalization check"),
    ("## 5.", "Section 5 outline & GEO requirements"),
    ("## 8.", "Section 8 acceptance criteria"),
]


def qa_brief(path: Path, *, template: bool = False) -> list[str]:
    text = path.read_text(encoding="utf-8")
    errors: list[str] = []

    if not template:
        if ">> GEN" in text:
            errors.append("Delivered brief still contains generation instructions")
        placeholders = find_placeholders(text)
        if placeholders:
            errors.append("Unresolved placeholders: " + ", ".join(placeholders[:20]))

        for heading, label in REQUIRED_SECTIONS:
            if heading not in text:
                errors.append(f"Missing {label}")

        demand = _section(text, "## 1.")
        if "## 1." in text and not VOLUME_RE.search(demand):
            errors.append("Section 1 has no validated volume figure (expected e.g. '90/mo')")

        criteria = _section(text, "## 8.")
        checklist = [l for l in criteria.splitlines() if l.strip().startswith("- [")]
        if "## 8." in text and len(checklist) < 3:
            errors.append(f"Section 8 has {len(checklist)} acceptance criteria; expected at least 3")
        if "## 8." in text and "Expected signal" not in criteria:
            errors.append("Section 8 lacks the expected-signal line (falsifiable metric + timeframe)")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("brief", type=Path)
    parser.add_argument("--template", action="store_true", help="Allow placeholders and GEN instructions")
    args = parser.parse_args()

    errors = qa_brief(args.brief, template=args.template)
    if errors:
        print("Brief QA failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Brief QA OK: {args.brief}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
