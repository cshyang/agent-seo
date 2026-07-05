---
name: seo-report-generation
description: "Generate client-facing SME SEO/GEO monthly reports using fixed money keywords, GA4 enquiry events, GSC query data, DataForSEO rank/SERP/GEO data, and one-diagnosis discipline."
version: 0.2.1
tags: [seo, geo, reporting, gsc, ga4, dataforseo]
---

# SEO Report Generation

## When to use

Use when producing a monthly SEO/GEO report, preparing a client-facing SEO summary, or grading previous SEO actions.

## Required reading (before generating anything)

This repo is the unit of operation: run from the repo root. Read these canonical files — do not improvise report structure from this SKILL.md alone:

1. `templates/sme-seo-report-template-v1.2.md` — the full report spec, section by section, including all `>> GEN:` generation instructions. This is the source of truth for structure, thresholds, and data-source rules.
2. `templates/report-qa-checklist.md` — pre-delivery checklist.
3. `methodology/dataforseo-cost-control.md` — which pulls are monthly vs quarterly.
4. The client's config and prior report from `.seo-ops/clients/<slug>/` (see AGENTS.md state convention).

## Inputs

- Client config matching `schemas/client-config.schema.json`.
- Previous report Section 6 actions, read from `.seo-ops/clients/<slug>/reports/<prior YYYY-MM>.md`.
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

## Deterministic helpers

For the brand/non-brand split (Section 2 non-brand commercial clicks, Appendix A query tagging), classify the GSC export deterministically and review the output:

```bash
python scripts/classify_gsc_queries.py <gsc-export.csv> --brand-term <brand term>
```

## Output location

Write the finished client-facing report to `.seo-ops/clients/<slug>/reports/YYYY-MM.md` (gitignored). Never write real client reports into the repo tree.

## Verification

- Run `python scripts/qa_report.py <report.md>` before delivery.
- Confirm no `>> GEN:` instructions or unresolved placeholders remain.
