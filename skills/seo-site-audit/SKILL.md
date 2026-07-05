---
name: seo-site-audit
description: "Run a one-off SEO/GEO site audit at onboarding, for a prospect, or as a re-baseline: crawl and indexation, Core Web Vitals, on-page metadata, structured data, local presence, and AI citability, ending in a prioritized findings register and no more than three actions."
version: 0.1.0
tags: [seo, geo, audit, technical-seo, schema, local-seo]
---

# SEO Site Audit

## When to use

Use for a one-off diagnostic: at client onboarding (before the first monthly report), for a prospect evaluation, after a migration/redesign, or when a quarterly check surfaces something structural. Do not use for recurring monthly reporting — that is `skills/seo-report-generation`.

## Required reading (before auditing anything)

This repo is the unit of operation: run from the repo root. Read these canonical files — do not improvise audit structure from this SKILL.md alone:

1. `templates/site-audit-template.md` — the full audit spec, section by section, including all `>> GEN:` generation instructions. This is the source of truth for structure and priorities.
2. `methodology/schema-checks.md` — structured data validation checklist and deprecated rich-result expectations.
3. `methodology/geo-ai-citability.md` — AI crawler tokens, citability checks, and output discipline.
4. `methodology/dataforseo-cost-control.md` — canonical API usage rules; an audit spends roughly one quarterly bundle, no more.
5. The client's config from `.seo-ops/clients/<slug>/config.yaml` if one exists (see AGENTS.md state convention). Audits may run pre-onboarding without a config — money-keyword cannibalization checks are skipped and the audit says so.

## Inputs

- Target domain and audit scope (full site / section / migration check).
- Client config if available (local intent, money keywords, competitors, brand terms).
- GSC access if available; otherwise indexation conclusions are labeled Medium/Low confidence.
- DataForSEO credentials for On-Page, SERP, and Business Data pulls.
- PageSpeed Insights API key (`PAGESPEED_API_KEY`, free) for CrUX field data.

## Workflow

1. Validate the target URL and run deterministic pre-checks:

   ```bash
   python scripts/audit_site_checks.py https://www.example.com
   ```

   This covers robots.txt (Googlebot and AI crawler access, sitemap declaration), sitemap fetch/parse, llms.txt presence, and homepage title/meta/canonical/noindex/JSON-LD. Its output goes in Appendix A; a FAIL here is a P0 candidate.
2. Estimate DataForSEO cost, then run ONE On-Page crawl task. Reuse it for Sections 3, 4, and 5 — never re-crawl within an audit.
3. Pull indexation truth: GSC index coverage where access exists, else sitemap-vs-crawl comparison with a confidence caveat.
4. Pull CWV field data (CrUX via PageSpeed Insights API); fall back to lab data as directional only when no field data exists.
5. Review on-page metadata and money-page cannibalization from the crawl data.
6. Validate structured data on the homepage plus one page per money-keyword theme, per `methodology/schema-checks.md`.
7. If local intent is high or medium: pull GBP data for client and competitors (Business Data API).
8. Run GEO/AI citability checks per `methodology/geo-ai-citability.md`.
9. Compile the Section 8 findings register (P0/P1/P2, max ~12 consolidated rows).
10. Choose the top 3 actions (P0 first, falsifiable impact, named owner).
11. Write the Section 1 executive summary last, then run audit QA.

## Cost control

An audit costs roughly one quarterly bundle: one On-Page crawl, one SERP pull for money keywords (config permitting), one Business Data pull where local intent warrants. PSI/CrUX is free. No Backlinks API, no Content Generation, no repeated crawls. Record task count / estimated cost in Appendix D:

```bash
python scripts/dataforseo_cost_estimate.py estimate onpage_task_post --count 1
```

## Output location

Write the finished audit to `.seo-ops/clients/<slug>/audits/YYYY-MM-audit.md` (gitignored — see AGENTS.md state convention). Prospects get a slug the same way clients do. Never write real audits into the repo tree.

## Verification

- Run `python scripts/qa_audit.py <audit.md>` before delivery.
- Confirm no `>> GEN:` instructions or unresolved placeholders remain.
- Confirm every 🔴 scorecard row has a findings-register entry and every action references a finding number.
