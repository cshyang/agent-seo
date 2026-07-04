#!/usr/bin/env python3
"""Estimate and log approximate DataForSEO costs for agent-seo workflows.

Prices are approximate placeholders and must be checked against current
DataForSEO pricing before financial reporting. The goal is operational
friction: make expensive choices visible before they become habits.
"""
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

COST_TABLE_USD = {
    "serp_google_organic_live_advanced": 0.002,
    "serp_google_organic_live_regular": 0.001,
    "labs_google_keyword_ideas": 0.05,
    "labs_google_ranked_keywords": 0.05,
    "labs_bulk_keyword_difficulty": 0.01,
    "business_data_google_my_business_info": 0.002,
    "onpage_task_post": 0.001,
    "llm_responses": 0.001,
    "llm_mentions": 0.01,
}


def estimate(endpoint: str, count: int) -> float:
    if endpoint not in COST_TABLE_USD:
        raise KeyError(f"unknown endpoint: {endpoint}")
    return COST_TABLE_USD[endpoint] * count


def main() -> int:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="cmd", required=True)

    est = sub.add_parser("estimate")
    est.add_argument("endpoint", choices=sorted(COST_TABLE_USD))
    est.add_argument("--count", type=int, default=1)

    log = sub.add_parser("log")
    log.add_argument("endpoint", choices=sorted(COST_TABLE_USD))
    log.add_argument("--count", type=int, default=1)
    log.add_argument("--note", default="")
    log.add_argument("--ledger", type=Path, default=Path(".seo-ops/dataforseo-ledger.jsonl"))

    args = parser.parse_args()
    cost = estimate(args.endpoint, args.count)
    if args.cmd == "estimate":
        print(json.dumps({"endpoint": args.endpoint, "count": args.count, "estimated_usd": round(cost, 6)}, indent=2))
        return 0

    args.ledger.parent.mkdir(parents=True, exist_ok=True)
    record = {
        "ts": datetime.now(timezone.utc).isoformat(),
        "endpoint": args.endpoint,
        "count": args.count,
        "estimated_usd": round(cost, 6),
        "note": args.note,
    }
    with args.ledger.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(record) + "\n")
    print(json.dumps(record, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
