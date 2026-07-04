#!/usr/bin/env python3
"""Basic QA checks for generated SEO report markdown."""
from __future__ import annotations

import argparse
import re
from pathlib import Path

PLACEHOLDER_RE = re.compile(r"\[[A-Z0-9_ /.-]+\]")


def qa_report(path: Path, *, template: bool = False) -> list[str]:
    text = path.read_text(encoding="utf-8")
    errors: list[str] = []

    if not template and ">> GEN:" in text:
        errors.append("Client-facing report still contains >> GEN instructions")

    if not template:
        placeholders = sorted(set(PLACEHOLDER_RE.findall(text)))
        if placeholders:
            errors.append("Unresolved placeholders: " + ", ".join(placeholders[:20]))

    if "## 1. Bottom line" not in text and not template:
        errors.append("Missing Section 1 Bottom line")

    if "## 2. Scorecard" not in text and not template:
        errors.append("Missing Section 2 Scorecard")

    if not template and text.count("## 5. Diagnosis") > 1:
        errors.append("Report appears to contain more than one diagnosis section")

    if not template:
        action_rows = _count_table_rows(_section(text, "## 6."))
        if action_rows > 3:
            errors.append(f"Section 6 has {action_rows} actions; maximum is 3")
        if "## 6." in text and action_rows == 0:
            errors.append("Section 6 has no actions")

        scorecard_rows = _count_table_rows(_section(text, "## 2."))
        if scorecard_rows > 7:
            errors.append(f"Section 2 scorecard has {scorecard_rows} rows; maximum is 7")

        if "## 8." not in text:
            errors.append("Missing Section 8 AI/GEO visibility")
        if ">> GEN" in text:
            errors.append("Client-facing report still contains generation instruction fragments")

    return errors


def _section(text: str, heading_prefix: str) -> str:
    """Return the body of the section whose H2 starts with heading_prefix."""
    lines = text.splitlines()
    start = None
    for i, line in enumerate(lines):
        if start is None and line.startswith(heading_prefix):
            start = i + 1
        elif start is not None and line.startswith("## "):
            return "\n".join(lines[start:i])
    return "\n".join(lines[start:]) if start is not None else ""


def _count_table_rows(section: str) -> int:
    """Count markdown table data rows (excludes header and separator rows)."""
    rows = [l for l in section.splitlines() if l.strip().startswith("|")]
    data = [r for r in rows if not set(r.replace("|", "").strip()) <= set("-: ")]
    return max(len(data) - 1, 0) if data else 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("report", type=Path)
    parser.add_argument("--template", action="store_true", help="Allow placeholders and GEN instructions")
    args = parser.parse_args()

    errors = qa_report(args.report, template=args.template)
    if errors:
        print("Report QA failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Report QA OK: {args.report}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
