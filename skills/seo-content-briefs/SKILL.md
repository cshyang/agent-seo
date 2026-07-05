---
name: seo-content-briefs
description: "Turn a demand-validated report action into a content brief — and optionally a draft — with cannibalization checks, SERP-shaped outlines, GEO answer blocks, schema and internal-link requirements, and falsifiable acceptance criteria."
version: 0.1.0
tags: [seo, geo, content, briefs, on-page]
---

# SEO Content Briefs

## When to use

Use when a report Section 6 action requires new or rewritten page content, or when the WordPress implementation skill needs a draft content brief. Do not use to originate content ideas — ideas enter through report Section 7 demand validation, never through this skill.

## Required reading (before writing anything)

This repo is the unit of operation: run from the repo root. Read these canonical files first:

1. `templates/content-brief-template.md` — the full brief spec including all `>> GEN:` instructions. Source of truth for structure and the demand gate.
2. `templates/sme-seo-report-template-v1.2.md` Section 7 — the validation rules a brief depends on.
3. `methodology/geo-ai-citability.md` — answer blocks, entity clarity, citability requirements baked into every outline.
4. `methodology/schema-checks.md` — schema requirements and deprecated rich-result expectations.
5. The client's config and source report from `.seo-ops/clients/<slug>/` (see AGENTS.md state convention).

## Hard rules

- **No brief without validation.** The brief must copy a real Section 7 row (validated volume ≥ 30/mo or an explicit strategic exception recorded in the report). A brief for an unvalidated topic is invalid by construction.
- **Rewrite beats new.** If an existing page partially covers the intent, brief a rewrite — a new URL needs a documented reason (the Section 3 cannibalization check).
- **One intent per page.**
- **No new API spend.** Briefs consume SERP and volume data already pulled for the report; do not re-pull.
- **No fabricated E-E-A-T.** Real credentials, projects, and dates or nothing — never invented statistics, testimonials, author bios, or review counts.

## Workflow

1. Locate the source action in the report (`.seo-ops/clients/<slug>/reports/YYYY-MM.md` Section 6) and its Section 7 validation row.
2. Run the cannibalization check against Section 4 ranking-URL data and the money-keyword target URLs in the client config.
3. Read the SERP context from the already-pulled data: who ranks, what shape, what blockers.
4. Write the outline with GEO requirements: answer block, entity signals, evidence, headings matched to the ranking shape.
5. Specify on-page requirements: title/meta, canonical, schema types, internal links in and out.
6. Write acceptance criteria ending with the falsifiable expected-signal line (this is what the next report's Section 3 grades).
7. Run brief QA.
8. If drafting the page too: follow the brief exactly, obey the voice/claims rules, and route the draft through `workflows/implementation-handoff.md` — customer-facing content is never published without client approval (see the WordPress skill's operating rules).

## Output location

Write briefs to `.seo-ops/clients/<slug>/briefs/YYYY-MM-<topic-slug>.md` (gitignored — see AGENTS.md state convention). Drafts produced from a brief live alongside it. Never write real client briefs or drafts into the repo tree.

## Verification

- Run `python scripts/qa_brief.py <brief.md>` before handoff.
- Confirm the demand-evidence volume is a real validated number, not an estimate.
- Confirm the acceptance criteria include the expected-signal line so the action is gradeable next month.
