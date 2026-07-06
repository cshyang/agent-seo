#!/usr/bin/env python3
"""Deterministic pre-checks for an SEO/GEO site audit.

Fetches robots.txt, sitemap, llms.txt, and the homepage of a target site and
reports mechanical facts: crawler access, sitemap health, title/meta/canonical
presence, noindex flags, and JSON-LD validity. URLs are validated with
url_safety before any fetch. Judgement (what the facts mean) stays with the
agent — see templates/site-audit-template.md.

Output lines are prefixed OK / WARN / FAIL. Exit 1 when any FAIL is present.
"""
from __future__ import annotations

import argparse
import json
import re
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from urllib.parse import urljoin, urlparse

from url_safety import URLSafetyError, validate_url

USER_AGENT = "agent-seo-audit/0.1 (+https://github.com/cshyang/agent-seo)"

# Keep in sync with methodology/geo-ai-citability.md.
# Blocking a search/answer-retrieval crawler removes the site from that answer
# engine entirely (OAI-SearchBot gates ChatGPT Search even when Bing ranks the
# page), so those blocks are FAIL. Training-crawler blocks are a choice: WARN.
AI_CRAWLER_TOKENS = [
    "GPTBot",
    "ChatGPT-User",
    "ClaudeBot",
    "Claude-SearchBot",
    "PerplexityBot",
    "Google-Extended",
    "CCBot",
]
SEARCH_CRAWLER_TOKENS = ["Googlebot", "Bingbot", "OAI-SearchBot"]

TITLE_RE = re.compile(r"<title[^>]*>(.*?)</title>", re.IGNORECASE | re.DOTALL)
META_RE = re.compile(
    r"<meta\s[^>]*name=[\"'](description|robots)[\"'][^>]*content=[\"']([^\"']*)[\"']",
    re.IGNORECASE,
)
META_REVERSED_RE = re.compile(
    r"<meta\s[^>]*content=[\"']([^\"']*)[\"'][^>]*name=[\"'](description|robots)[\"']",
    re.IGNORECASE,
)
CANONICAL_RE = re.compile(
    r"<link\s[^>]*rel=[\"']canonical[\"'][^>]*href=[\"']([^\"']+)[\"']|"
    r"<link\s[^>]*href=[\"']([^\"']+)[\"'][^>]*rel=[\"']canonical[\"']",
    re.IGNORECASE,
)
JSONLD_RE = re.compile(
    r"<script[^>]*type=[\"']application/ld\+json[\"'][^>]*>(.*?)</script>",
    re.IGNORECASE | re.DOTALL,
)


def fetch(url: str, timeout: int) -> tuple[int, str]:
    """Fetch a validated URL; return (status, body). Raises URLSafetyError first."""
    safe = validate_url(url)
    request = urllib.request.Request(safe, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return response.status, response.read(2_000_000).decode("utf-8", errors="replace")
    except urllib.error.HTTPError as exc:
        return exc.code, ""


def parse_robots(text: str) -> tuple[dict[str, list[str]], list[str]]:
    """Return ({user-agent-lower: [disallow rules]}, [sitemap urls])."""
    rules: dict[str, list[str]] = {}
    sitemaps: list[str] = []
    current: list[str] = []
    for raw in text.splitlines():
        line = raw.split("#", 1)[0].strip()
        if not line or ":" not in line:
            continue
        field, _, value = line.partition(":")
        field, value = field.strip().lower(), value.strip()
        if field == "user-agent":
            current = [value.lower()]
            rules.setdefault(value.lower(), [])
        elif field == "disallow" and current:
            for agent in current:
                rules[agent].append(value)
        elif field == "sitemap":
            sitemaps.append(value)
    return rules, sitemaps


def agent_fully_blocked(rules: dict[str, list[str]], token: str) -> bool:
    """True when the token's most specific matching group disallows everything."""
    token_lower = token.lower()
    for agent, disallows in rules.items():
        if agent != "*" and agent in token_lower:
            return "/" in disallows
    return "/" in rules.get("*", [])


def check_site(base_url: str, timeout: int) -> list[tuple[str, str]]:
    findings: list[tuple[str, str]] = []
    parsed = urlparse(validate_url(base_url))
    origin = f"{parsed.scheme}://{parsed.netloc}"

    # robots.txt
    status, robots_body = fetch(urljoin(origin, "/robots.txt"), timeout)
    sitemap_urls: list[str] = []
    if status != 200:
        findings.append(("WARN", f"robots.txt returned HTTP {status}"))
    else:
        rules, sitemap_urls = parse_robots(robots_body)
        for token in SEARCH_CRAWLER_TOKENS:
            if agent_fully_blocked(rules, token):
                findings.append(("FAIL", f"robots.txt fully blocks {token}"))
            else:
                findings.append(("OK", f"robots.txt allows {token}"))
        for token in AI_CRAWLER_TOKENS:
            if agent_fully_blocked(rules, token):
                findings.append(("WARN", f"robots.txt fully blocks AI crawler {token}"))
            else:
                findings.append(("OK", f"robots.txt allows AI crawler {token}"))
        if not sitemap_urls:
            findings.append(("WARN", "robots.txt declares no sitemap"))

    # sitemap
    for sitemap_url in sitemap_urls or [urljoin(origin, "/sitemap.xml")]:
        status, body = fetch(sitemap_url, timeout)
        if status != 200:
            findings.append(("WARN", f"sitemap {sitemap_url} returned HTTP {status}"))
            continue
        try:
            root = ET.fromstring(body)
        except ET.ParseError as exc:
            findings.append(("FAIL", f"sitemap {sitemap_url} is not valid XML: {exc}"))
            continue
        tag = root.tag.rsplit("}", 1)[-1]
        locs = [el.text.strip() for el in root.iter() if el.tag.endswith("}loc") and el.text]
        kind = "sitemap index" if tag == "sitemapindex" else "sitemap"
        findings.append(("OK", f"{kind} {sitemap_url}: {len(locs)} <loc> entries"))

    # llms.txt (informational — absence is not a failure)
    status, _ = fetch(urljoin(origin, "/llms.txt"), timeout)
    findings.append(("OK", f"llms.txt {'present' if status == 200 else 'absent'} (HTTP {status})"))

    # homepage
    status, html = fetch(origin + "/", timeout)
    if status != 200:
        findings.append(("FAIL", f"homepage returned HTTP {status}"))
        return findings

    title = TITLE_RE.search(html)
    if title and title.group(1).strip():
        findings.append(("OK", f"homepage <title>: {title.group(1).strip()[:80]}"))
    else:
        findings.append(("WARN", "homepage has no <title>"))

    metas = {name.lower(): content for name, content in META_RE.findall(html)}
    metas.update({name.lower(): content for content, name in META_REVERSED_RE.findall(html)})
    if metas.get("description", "").strip():
        findings.append(("OK", f"homepage meta description: {metas['description'].strip()[:80]}"))
    else:
        findings.append(("WARN", "homepage has no meta description"))
    if "noindex" in metas.get("robots", "").lower():
        findings.append(("FAIL", "homepage has a noindex robots meta tag"))

    canonical = CANONICAL_RE.search(html)
    if canonical:
        href = canonical.group(1) or canonical.group(2)
        findings.append(("OK", f"homepage canonical: {href}"))
    else:
        findings.append(("WARN", "homepage has no canonical link"))

    blocks = JSONLD_RE.findall(html)
    if not blocks:
        findings.append(("WARN", "homepage has no JSON-LD structured data"))
    for i, block in enumerate(blocks, 1):
        try:
            data = json.loads(block)
        except json.JSONDecodeError as exc:
            findings.append(("FAIL", f"homepage JSON-LD block {i} is invalid JSON: {exc}"))
            continue
        nodes = data if isinstance(data, list) else [data]
        types = [str(node.get("@type", "?")) for node in nodes if isinstance(node, dict)]
        contexts = {str(node.get("@context", "")) for node in nodes if isinstance(node, dict)}
        if not any("schema.org" in ctx for ctx in contexts):
            findings.append(("WARN", f"homepage JSON-LD block {i} has no schema.org @context"))
        findings.append(("OK", f"homepage JSON-LD block {i}: @type {', '.join(types) or '?'}"))
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("url", help="site root URL, e.g. https://www.example.com")
    parser.add_argument("--timeout", type=int, default=15)
    parser.add_argument("--json", action="store_true", help="emit findings as JSON")
    args = parser.parse_args()

    try:
        findings = check_site(args.url, args.timeout)
    except URLSafetyError as exc:
        print(f"FAIL URL unsafe: {exc}")
        return 1
    except (urllib.error.URLError, OSError) as exc:
        print(f"FAIL could not reach site: {exc}")
        return 1

    if args.json:
        print(json.dumps([{"level": level, "finding": text} for level, text in findings], indent=2))
    else:
        for level, text in findings:
            print(f"{level:4} {text}")
    return 1 if any(level == "FAIL" for level, _ in findings) else 0


if __name__ == "__main__":
    raise SystemExit(main())
