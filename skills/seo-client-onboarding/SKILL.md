---
name: seo-client-onboarding
description: "Establish stable client SEO/GEO reporting baselines: profile, goals, brand terms, lead quality, money keywords, GA4 events, local intent, competitors, and AI prompt panel."
version: 0.2.2
tags: [seo, onboarding, reporting, client-config]
---

# SEO Client Onboarding

## When to use

Use before a client’s first recurring SEO/GEO report or when rebuilding a broken reporting baseline.

## Required reading (before starting)

Run from the repo root and read these canonical files first:

1. `templates/client-onboarding-template.md` — the full onboarding structure (Part A of the report spec).
2. `schemas/client-config.schema.json` and `schemas/client-config.example.yaml` — the output contract.
3. `templates/sme-seo-report-template-v1.2.md` Part A — context for why each baseline field exists.

## Steps

1. Confirm client profile, service area, and primary goal.
2. Define good-fit and poor-fit enquiry patterns.
3. Collect brand terms for brand/non-brand split.
4. Confirm GSC and GA4 properties.
5. Verify the site in Bing Webmaster Tools (import-from-GSC flow), submit the sitemap, and enable IndexNow where the CMS supports it — Bing indexation gates ChatGPT/Copilot citation (see `methodology/geo-ai-citability.md`). One-time setup, never a monthly KPI.
6. Map GA4 key events to human labels and weights.
7. Select 10–20 commercial money keywords.
8. Validate keyword volume with DataForSEO.
9. Assign each keyword a theme and target URL.
10. Define local intent level.
11. Choose local competitors.
12. Define fixed GEO/AI prompt panel.
13. Run cold-start backfill: 12 months of historical rank/visibility (DataForSEO Labs Historical Rank Overview) so the first report shows a trend line, not a snapshot.
14. Record baseline local pack presence for each money keyword where local intent is high or medium.
15. Record changelog.

## Output

A client config matching `schemas/client-config.schema.json`, written to `.seo-ops/clients/<slug>/config.yaml` (gitignored — see AGENTS.md state convention). Validate before finishing:

```bash
python scripts/validate_client_config.py .seo-ops/clients/<slug>/config.yaml
```
