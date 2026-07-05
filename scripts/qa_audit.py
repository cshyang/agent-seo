#!/usr/bin/env python3
"""QA checks for generated site audit markdown (templates/site-audit-template.md)."""
from __future__ import annotations

import argparse
from pathlib import Path

from qa_report import PLACEHOLDER_RE, _count_table_rows, _section

PRIORITIES = ("P0", "P1", "P2")


def qa_audit(path: Path, *, template: bool = False) -> list[str]:
    text = path.read_text(encoding="utf-8")
    errors: list[str] = []

    if not template:
        if ">> GEN" in text:
            errors.append("Client-facing audit still contains generation instructions")
        placeholders = sorted(set(PLACEHOLDER_RE.findall(text)))
        if placeholders:
            errors.append("Unresolved placeholders: " + ", ".join(placeholders[:20]))

        for heading, label in [
            ("## 1.", "Section 1 executive summary"),
            ("## 2.", "Section 2 health scorecard"),
            ("## 8.", "Section 8 findings register"),
            ("## 9.", "Section 9 top actions"),
        ]:
            if heading not in text:
                errors.append(f"Missing {label}")

        finding_rows = [
            row
            for row in _section(text, "## 8.").splitlines()
            if row.strip().startswith("|")
            and not set(row.replace("|", "").strip()) <= set("-: ")
        ][1:]  # drop header row
        if not finding_rows and "## 8." in text:
            errors.append("Section 8 findings register is empty")
        for row in finding_rows:
            if not any(priority in row for priority in PRIORITIES):
                errors.append(f"Finding row lacks a P0/P1/P2 priority: {row.strip()[:60]}")
        if len(finding_rows) > 12:
            errors.append(f"Section 8 has {len(finding_rows)} findings; consolidate to 12 or fewer")

        action_rows = _count_table_rows(_section(text, "## 9."))
        if "## 9." in text and action_rows == 0:
            errors.append("Section 9 has no actions")
        if action_rows > 3:
            errors.append(f"Section 9 has {action_rows} actions; maximum is 3")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("audit", type=Path)
    parser.add_argument("--template", action="store_true", help="Allow placeholders and GEN instructions")
    args = parser.parse_args()

    errors = qa_audit(args.audit, template=args.template)
    if errors:
        print("Audit QA failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Audit QA OK: {args.audit}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
