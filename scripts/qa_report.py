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

    return errors


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
