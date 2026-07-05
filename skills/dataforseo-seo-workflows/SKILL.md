---
name: dataforseo-seo-workflows
description: "Use DataForSEO for SME SEO/GEO rank tracking, SERP blocker detection, local pack checks, opportunity validation, AI visibility, and quarterly refreshes with cost controls."
version: 0.1.2
tags: [seo, dataforseo, serp, rank-tracking, geo, local-seo]
---

# DataForSEO SEO Workflows

## When to use

Use when a report or diagnostic needs stable rank/SERP data, search volume validation, local pack presence, AI/GEO visibility, or quarterly competitor/technical refreshes.

## Required reading

`methodology/dataforseo-cost-control.md` is the canonical version of the monthly/quarterly/avoid lists below — read it first; this skill is a summary and must not drift from it.

## Default monthly pulls

- SERP rank for fixed money keywords.
- Ranking URL for cannibalization/target mismatch detection.
- SERP blockers: AI Overview, local pack, heavy ads.
- Local pack presence using the same SERP response where local intent is high or medium.
- Labs volume/difficulty validation for Section 7 opportunities only.

## Default quarterly pulls

- Competitor keyword gap.
- LLM Mentions Top Domains/Top Pages.
- On-Page crawl.
- GBP/review benchmark where local intent is relevant.

## Cost control

Reuse the same SERP response for as many report fields as possible. Record task count / estimated cost in the report appendix.

Before large pulls, estimate cost with:

```bash
python scripts/dataforseo_cost_estimate.py estimate serp_google_organic_live_advanced --count 20
```

For raw API envelopes, normalize items before handing them to an agent:

```bash
python scripts/dataforseo_normalize.py response.json --max-chars 12000
```

Prefer bulk endpoints over many single-keyword calls, and avoid re-fetching data already pulled in the same report run.

## Avoid by default

- Backlinks API.
- Content Generation API.
- AI search volume as a headline metric.
- Google Trends endpoints (seasonality notes in the client config suffice).
- Unscheduled full-domain crawls.
