# SEO/GEO Site Audit — Template & Generation Spec

Version 0.1 · Designed for: DataForSEO On-Page + GSC + PageSpeed Insights/CrUX + deterministic pre-checks
Intended reader: the agent/pipeline generating the audit. Sections marked `[FIELD]` are placeholders. Sections marked `>> GEN:` are generation instructions — delete them from the final client-facing output.

An audit is a one-off diagnostic (onboarding, prospect, or re-baseline) — not a recurring report. It ends with a prioritized findings register and **no more than three actions**. A 40-item checklist dump is a failed audit.

---

# `[CLIENT_NAME]` Site Audit — `[MONTH YYYY]`
Domain: `[DOMAIN]` · Prepared by `[YOUR_NAME]` · `[DATE]` · Scope: `[full site / section / migration check]`

---

## 1. Executive summary
`[3–5 sentences: overall health verdict, the ONE structural issue that matters most, and what the top 3 actions will change.]`

>> GEN: Write this LAST. No jargon. If a non-technical owner reads only this, they should know whether the site is fundamentally healthy, what the single biggest problem is, and what happens next. State P0 issues plainly — never soften deindexing, site-wide noindex, or broken tracking into "opportunities."

---

## 2. Health scorecard

| Area | Status | Evidence |
|------|--------|----------|
| Indexation | 🟢 / 🟡 / 🔴 | `[indexed vs sitemap URLs, coverage issues]` |
| Core Web Vitals | 🟢 / 🟡 / 🔴 | `[field data pass/fail per metric]` |
| Crawl health | 🟢 / 🟡 / 🔴 | `[broken links, redirect chains, status errors]` |
| On-page metadata | 🟢 / 🟡 / 🔴 | `[duplicate/missing titles and metas, canonicals]` |
| Structured data | 🟢 / 🟡 / 🔴 | `[valid/invalid/missing schema on key pages]` |
| Local presence | 🟢 / 🟡 / 🔴 / n/a | `[GBP completeness, reviews, NAP consistency]` |
| GEO / AI citability | 🟢 / 🟡 / 🔴 | `[crawler access, rendering, citability]` |

>> GEN: Max 8 rows. 🔴 requires at least one matching entry in the Section 8 findings register — no red status without a written finding. Omit the Local presence row only when local intent is low (see client config). Every Evidence cell cites data, not opinion.

---

## 3. Technical health

### Indexation
`[Indexed pages vs sitemap URL count, coverage states, unexpected noindex/canonical exclusions.]`

### Crawl findings
`[DataForSEO On-Page results: status errors, broken internal links, redirect chains, orphan pages, crawl anomalies.]`

### Core Web Vitals
`[CrUX field data per metric (LCP/INP/CLS), mobile vs desktop, worst templates.]`

>> GEN: Indexation truth source is GSC index coverage where access exists; otherwise compare sitemap URLs against crawl results and label the conclusion Medium/Low confidence. CWV: prefer CrUX field data (real users) over lab scores; if the site has no CrUX data (low traffic), say so and use lab data as directional only. One On-Page crawl task per audit — reuse it for Sections 3, 4, and 5; do not re-crawl.

---

## 4. On-page & content
`[Duplicate/missing titles and meta descriptions, canonical correctness, thin/duplicate money pages, heading structure on priority pages.]`

>> GEN: Pull all of this from the same On-Page crawl. If a client config exists, check each money keyword's target URL: does the intended page exist, is it indexable, and does any other page compete with it (cannibalization)? Limit page-level commentary to money pages and templates — do not itemize every blog post.

---

## 5. Structured data
`[Schema present per key template, validation results per methodology checklist, conflicts/duplicates from plugins.]`

>> GEN: Apply `methodology/schema-checks.md` — the nine-point validation checklist and the deprecated rich-result expectations (no HowTo/FAQ rich-result promises). Check the homepage plus one page per money-keyword theme, not every URL. Every schema recommendation must map to a target URL.

---

## 6. Local presence
`[GBP completeness, primary category, review count/velocity vs competitors, NAP consistency across site/GBP/key directories.]`

>> GEN: Include only when local intent is high or medium. Pull GBP data via the DataForSEO Business Data API for the client and named competitors. Review velocity is the actionable number. Omit the section entirely when local intent is low — do not pad.

---

## 7. GEO / AI citability
`[AI crawler access per robots.txt, llms.txt status, server-rendered vs client-only content, citability of priority pages, presence on sources AI answers cite.]`

>> GEN: Apply `methodology/geo-ai-citability.md` — check the listed crawler tokens, distinguish blocking training crawlers from blocking search/answer visibility, and assess whether priority pages have self-contained answer blocks, dates, authorship, and entity clarity. Findings must translate to the concrete action types in that methodology's output discipline — never "improve AI visibility."

---

## 8. Findings register

| # | Priority | Finding | Evidence | Affected URLs/scope | Recommended fix |
|---|----------|---------|----------|---------------------|-----------------|
| 1 | P0 / P1 / P2 | `[FINDING]` | `[data]` | `[scope]` | `[fix]` |

>> GEN: Every finding gets a priority. P0 = actively destroying performance: deindexing, site-wide noindex, robots blocking Googlebot, CWV collapse, broken enquiry tracking. P1 = material and fixable this quarter. P2 = worth doing, not urgent. Max ~12 rows — consolidate repeats into one finding with scope ("34 pages missing meta descriptions"), never one row per URL. Any P0 must lead Section 1 and Section 9.

---

## 9. Top 3 actions

| # | Action | Fixes finding # | Expected impact | Effort | Owner |
|---|--------|-----------------|-----------------|--------|-------|
| 1 | `[ACTION]` | `[#]` | `[falsifiable: metric + timeframe]` | S / M / L | Us / Client / Developer |

>> GEN: Never more than 3 — same discipline as the monthly report. Every action references a finding number, has a falsifiable expected impact, and names an owner. P0 findings always claim slots first. Remaining P1/P2 findings stay in the register for future report cycles; do not smuggle them in as sub-bullets.

---

## 10. Appendix
- A. Deterministic pre-check output (`scripts/audit_site_checks.py`)
- B. Crawl summary data (On-Page task results)
- C. CWV raw metrics per template
- D. Data run log: DataForSEO task count / estimated cost, sources used, sources unavailable, confidence caveats

>> GEN: Reference material only — no commentary, no actions. Appendix D is mandatory: record task count/cost the same way monthly reports record Appendix F.
