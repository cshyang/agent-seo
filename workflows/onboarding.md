# Client Onboarding Workflow

## Goal

Create a stable reporting baseline so month-to-month SEO/GEO reporting is comparable.

## Steps

1. Confirm client profile, industry, service area, and primary enquiry goal.
2. Define seasonality notes and lead-quality rules.
3. Collect brand terms for branded/non-branded classification.
4. Identify GSC property and GA4 property.
5. Map GA4 key events to human enquiry labels and weights.
6. Select 10–20 commercial money keywords.
7. Assign each money keyword a theme and target URL.
8. Validate money keywords with DataForSEO volume.
9. Define local intent level: high, medium, or low.
10. Define 10–15 fixed GEO/AI prompts.
11. Run cold-start historical rank/visibility backfill.
12. Record baseline local pack presence where relevant.
13. Save changelog entry for the initial panel and keyword set.

## Output

A single client config matching `schemas/client-config.schema.json` — money keywords, GA4 event mapping, GEO prompts, and the onboarding changelog entry are all embedded in it — written to `.seo-ops/clients/<slug>/config.yaml` (gitignored; see the AGENTS.md client state convention).

Validate before finishing:

```bash
python scripts/validate_client_config.py .seo-ops/clients/<slug>/config.yaml
```
