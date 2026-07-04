#!/usr/bin/env python3
"""Normalize common DataForSEO response envelopes.

Adapted conceptually from AgriciDaniel/claude-seo's normalization helpers.
Keeps this repo's first implementation compact: flatten successful task result
items and optionally truncate JSON for agent context.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


def extract_items(response: dict[str, Any]) -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    for task in response.get("tasks", []) or []:
        if task.get("status_code") not in (None, 20000):
            continue
        for result in task.get("result", []) or []:
            result_items = result.get("items")
            if isinstance(result_items, list):
                items.extend(item for item in result_items if isinstance(item, dict))
    return items


def truncate_for_context(items: list[dict[str, Any]], max_chars: int = 12000) -> list[dict[str, Any]]:
    kept: list[dict[str, Any]] = []
    size = 2
    for item in items:
        rendered = json.dumps(item, ensure_ascii=False, separators=(",", ":"))
        if kept and size + len(rendered) + 1 > max_chars:
            break
        kept.append(item)
        size += len(rendered) + 1
    return kept


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path, nargs="?", help="DataForSEO JSON file; stdin if omitted")
    parser.add_argument("--max-chars", type=int, default=12000)
    parser.add_argument("--count", action="store_true", help="Only print extracted item count")
    args = parser.parse_args()

    text = args.input.read_text(encoding="utf-8") if args.input else sys.stdin.read()
    response = json.loads(text)
    items = extract_items(response)
    if args.count:
        print(len(items))
        return 0
    print(json.dumps(truncate_for_context(items, args.max_chars), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
