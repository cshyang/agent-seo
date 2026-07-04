---
name: seo-report-generation
description: Generate client-facing SME SEO/GEO monthly reports using fixed money keywords, GA4 enquiry events, GSC query data, DataForSEO rank/SERP/GEO data, and one-diagnosis discipline.
version: 0.1.0
author: Marle
license: MIT
metadata:
  hermes:
    tags: [seo, geo, reporting, gsc, ga4, dataforseo]
---

# SEO Report Generation

## When to use

Use when producing a monthly SEO/GEO report, preparing a client-facing SEO summary, or grading previous SEO actions.

## Inputs

- Client config matching `schemas/client-config.schema.json`.
- Previous report Section 6 actions.
- Current full calendar month data.
- Prior full calendar month data.
- Money keyword rank/SERP data from DataForSEO.
- GSC query/page data.
- GA4 organic sessions and events.
- Fixed GEO/AI prompt panel outputs.

## Workflow

1. Validate the client config.
2. Pull/prepare Sections 4, 7, and 8 data first.
3. Grade last month’s actions in Section 3.
4. Choose one diagnosis for Section 5.
5. Choose two to three next actions for Section 6.
6. Compile the Section 2 scorecard.
7. Write Section 1 bottom line last.
8. Run report QA.

## Reporting rules

- Enquiries first.
- One diagnosis only.
- Two to three actions only.
- Never recommend new content without demand validation.
- Label low-confidence data clearly.
- Separate branded demand from non-brand commercial SEO demand.
- Treat sampled AI/GEO visibility as directional.

## Verification

- Run `python scripts/qa_report.py <report.md>` before delivery.
- Confirm no `>> GEN:` instructions or unresolved placeholders remain.
