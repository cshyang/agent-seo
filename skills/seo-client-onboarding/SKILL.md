---
name: seo-client-onboarding
description: "Establish stable client SEO/GEO reporting baselines: profile, goals, brand terms, lead quality, money keywords, GA4 events, local intent, competitors, and AI prompt panel."
version: 0.2.0
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
5. Map GA4 key events to human labels and weights.
6. Select 10–20 commercial money keywords.
7. Validate keyword volume with DataForSEO.
8. Assign each keyword a theme and target URL.
9. Define local intent level.
10. Choose local competitors.
11. Define fixed GEO/AI prompt panel.
12. Record changelog.

## Output

A client config matching `schemas/client-config.schema.json`, written to `.seo-ops/clients/<slug>/config.yaml` (gitignored — see AGENTS.md state convention). Validate before finishing:

```bash
python scripts/validate_client_config.py .seo-ops/clients/<slug>/config.yaml
```
