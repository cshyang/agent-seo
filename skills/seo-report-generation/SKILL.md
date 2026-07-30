---
name: seo-report-generation
description: "Generate client-facing SME SEO/GEO monthly reports using fixed money keywords, GA4 enquiry events, GSC query data, DataForSEO rank/SERP/GEO data, and one-diagnosis discipline."
version: 0.3.0
tags: [seo, geo, reporting, gsc, ga4, dataforseo]
---

# SEO Report Generation

## When to use

Two templates in `templates/`: **`sme-seo-audit-template-v1.md`** for the one-time month-1 baseline audit at client onboarding (establishes baselines, freezes the A2/A5 panels, sets the first three actions); **`sme-seo-report-template-v1.3.md`** for every monthly report after. The first monthly report grades the audit's three actions in Section 3.

Use when producing a monthly SEO/GEO report, preparing a client-facing SEO summary, or grading previous SEO actions.

## Inputs

- Client config matching `schemas/client-config.schema.json`.
- Previous report Section 6 actions.
- Current full calendar month data.
- Prior full calendar month data.
- Money keyword rank/SERP data from DataForSEO.
- GSC query/page data.
- GA4 organic sessions and events.
- Fixed GEO/AI prompt panel outputs (min 10 language-tagged prompts, ChatGPT + Gemini + Perplexity via DataForSEO LLM Responses).

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
- Executive summary first, never executive summary only, unless the user explicitly asks for a short review note.
- One diagnosis only.
- Two to three actions only.
- Never recommend new content without demand validation.
- Label low-confidence data clearly.
- Separate branded demand from non-brand commercial SEO demand.
- Treat sampled AI/GEO visibility as directional.
- A real/full audit or monthly report must include the enquiries-first scorecard, full fixed money-keyword tracker, organic/landing-page quality, technical/on-page evidence, GEO coverage, methodology and caveats.
- Every approved money keyword must include rank/status, GSC clicks/impressions/position where available, actual ranking page, intended target page, correct-page status, and SERP/local-pack fields. A keyword-name list is not a tracker.
- Distinguish local-pack presence from client inclusion.
- GEO reporting must include fixed prompt results by platform, recommendation/citation/mention state and sources when captured. If the prompt panel was not run, state that AI recommendation coverage was not measured; SERP feature counts alone are not complete GEO coverage.
- Gmail-safe layout may split a wide tracker into language/theme tables or stacked detail blocks. It must not remove analytical fields.

## Client-facing HTML report (reference)

When the deliverable is a polished client-facing HTML audit (not the plain markdown/Gmail report), the target format is the worked example `templates/client-audit-report-example.html` (the Sommerfield baseline audit). Reproduce that structure and its fixed house design -- do NOT theme per client (a fixed, readable house style beats pulling each client brand palette into dense data tables; a logo and single accent are the only per-client visual touches).

Generation is reference-only, not a generic engine:
- **Pattern generator:** `scripts/build_sommerfield_seo_html_report.py`. For a new client, copy it, swap the `DATA`/`OUT` paths and dates, and rewrite the per-client narrative prose (diagnosis, roadmap). The section skeleton, CSS, and component patterns (metric cards, callouts, table-wrap, funnel) carry over unchanged.
- **GEO section is data-driven and reusable as-is:** `build_geo_section(geo)` reads the client `data/<client>/<client>-ai-geo-baseline-*.json` and renders the engine x language coverage matrix, the sources-shaping-answers list (search/grounding-infra domains filtered via `NOISE_SOURCE_DOMAINS`/`_is_noise_source`), and the honest presence-not-traffic callout. Renders empty if no GEO data exists.

## GEO baseline pull (generic tool)

`scripts/client_ai_geo_baseline.py --config data/<client>/<client>-client-config.yaml --city "<City>"` runs the config geo_prompts through ChatGPT + Gemini + Perplexity (DataForSEO LLM Responses, live) and writes `data/<client>/<client>-ai-geo-baseline-<date>.json` plus the coverage matrix. Config-driven -- works for any client; replaces the old per-client `*_ai_geo_baseline.py` scripts. Model pins live in the config `geo_model_pins` (currently ChatGPT gpt-5.6-terra, Gemini gemini-3.5-flash, Perplexity sonar) and are held stable for month-over-month comparability; change only via a dated config changelog entry. Note: only ChatGPT accepts geo-localization fields; Gemini/Perplexity are prompt-localized.

## Verification

- Run `python scripts/qa_report.py <report.md>` before delivery.
- Confirm no `>> GEN:` instructions or unresolved placeholders remain.
- Confirm every fixed keyword has the required tracker fields or an explicit missing-data marker.
- Confirm GEO coverage matrix is per engine x language with the sources-shaping-answers list, and no AI referral traffic is forecast; coverage present by platform or explicitly labeled not measured.
- Confirm technical/on-page evidence and methodology are present.
