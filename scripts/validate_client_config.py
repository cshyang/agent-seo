#!/usr/bin/env python3
"""Validate an Agent SEO client config.

This intentionally uses only the Python standard library plus PyYAML when
available. If PyYAML is unavailable, JSON configs still work.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from urllib.parse import urlparse

REQUIRED = {
    "client_name",
    "domain",
    "service_area",
    "primary_goal",
    "local_intent",
    "brand_terms",
    "money_keywords",
    "ga4_events",
    "geo_prompts",
}


def load_config(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if path.suffix.lower() == ".json":
        return json.loads(text)
    try:
        import yaml  # type: ignore
    except Exception as exc:  # pragma: no cover - depends on environment
        raise SystemExit("PyYAML is required for YAML configs. Use JSON or install pyyaml.") from exc
    data = yaml.safe_load(text)
    if not isinstance(data, dict):
        raise SystemExit("Config root must be an object/dict.")
    return data


def validate(config: dict) -> list[str]:
    errors: list[str] = []
    missing = sorted(REQUIRED - set(config))
    if missing:
        errors.append(f"Missing required fields: {', '.join(missing)}")

    parsed = urlparse(str(config.get("domain", "")))
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        errors.append("domain must be an http(s) URL")

    if config.get("local_intent") not in {"high", "medium", "low"}:
        errors.append("local_intent must be high, medium, or low")

    for field in ["brand_terms", "money_keywords", "ga4_events", "geo_prompts"]:
        if not isinstance(config.get(field), list) or not config.get(field):
            errors.append(f"{field} must be a non-empty list")

    for idx, kw in enumerate(config.get("money_keywords") or [], start=1):
        if not isinstance(kw, dict):
            errors.append(f"money_keywords[{idx}] must be an object")
            continue
        for key in ["keyword", "theme", "target_url"]:
            if not kw.get(key):
                errors.append(f"money_keywords[{idx}].{key} is required")

    for idx, event in enumerate(config.get("ga4_events") or [], start=1):
        if not isinstance(event, dict):
            errors.append(f"ga4_events[{idx}] must be an object")
            continue
        weight = event.get("weight")
        if not isinstance(weight, (int, float)) or not 0 <= weight <= 1:
            errors.append(f"ga4_events[{idx}].weight must be between 0 and 1")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("config", type=Path)
    args = parser.parse_args()

    config = load_config(args.config)
    errors = validate(config)
    if errors:
        print("Config validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Config OK: {args.config}")
    print(f"Client: {config['client_name']} · money keywords: {len(config['money_keywords'])} · GEO prompts: {len(config['geo_prompts'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
