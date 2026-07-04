#!/usr/bin/env python3
"""Classify a simple GSC CSV export into brand/non-brand/commercial/noise buckets.

Expected columns: query, clicks, impressions, ctr, position.
This is a lightweight deterministic helper; final classification should still be reviewed.
"""
from __future__ import annotations

import argparse
import csv
from pathlib import Path

INFORMATIONAL = ("how", "what", "why", "guide", "tips", "ideas", "meaning")
NOISE = ("job", "career", "supplier", "wholesale", "cheap", "free")
COMMERCIAL = ("service", "company", "provider", "contractor", "agency", "consultant", "near me", "city")


def classify(query: str, brand_terms: list[str]) -> str:
    q = query.lower().strip()
    if any(term.lower() in q for term in brand_terms):
        return "brand"
    if any(token in q for token in NOISE):
        return "noise"
    if any(q.startswith(token + " ") or f" {token} " in q for token in INFORMATIONAL):
        return "informational"
    if any(token in q for token in COMMERCIAL):
        return "non-brand commercial"
    return "review"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_path", type=Path)
    parser.add_argument("--brand-term", action="append", default=[], help="Brand term to classify as branded. Repeatable.")
    args = parser.parse_args()

    with args.csv_path.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        fieldnames = list(reader.fieldnames or []) + ["classification"]
        writer = csv.DictWriter(__import__("sys").stdout, fieldnames=fieldnames)
        writer.writeheader()
        for row in reader:
            row["classification"] = classify(row.get("query", ""), args.brand_term)
            writer.writerow(row)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
