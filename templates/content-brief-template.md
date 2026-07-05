# Content Brief — Template & Generation Spec

Version 0.1 · Consumes data already pulled for report Section 7 — a brief adds no new API spend.
Intended reader: the agent/operator producing the brief, then whoever writes and implements the page. Sections marked `[FIELD]` are placeholders. Sections marked `>> GEN:` are generation instructions — delete them from the delivered brief.

A brief exists only downstream of demand validation. If there is no validated Section 7 row behind it, the brief is invalid by construction — stop and validate first.

---

# Content Brief — `[PAGE TITLE / TOPIC]`
Client: `[CLIENT_NAME]` · Source: `[report YYYY-MM, Section 6 action #N]` · Prepared by `[YOUR_NAME]` · `[DATE]`

---

## 1. Demand evidence

- Target query/topic: `[QUERY]`
- Validated volume: `[N]`/mo (DataForSEO, validated `[DATE]`)
- GSC evidence: `[N impressions @ position X over M months, or "no current visibility"]`
- Section 7 recommendation: `[Target existing page / New page — copied from the report row]`

>> GEN: Copy the actual Section 7 validation row — do not re-derive or estimate. A brief without a real volume number does not proceed; that is the anti-content-farm rule. If validation is older than one quarter, re-check volume before writing.

---

## 2. Target

- Primary keyword: `[KW]`
- Theme (A2 service line): `[THEME]`
- Search intent: `[transactional / commercial / informational-supporting]`
- Page type: `[new page / rewrite of existing page]`
- Target URL: `[/slug/ or existing URL]`
- Money-set relationship: `[candidate to join money set after one month of validation / supporting page only]`

>> GEN: One intent per page. If the query mixes intents, pick the commercial interpretation and note the other for a possible supporting page — do not write one page that half-serves both.

---

## 3. Cannibalization check

- Existing URLs touching this intent: `[URLs + what they currently rank for, from Section 4 ranking-URL data]`
- Why they cannot simply be extended: `[reason, or "they can — this brief is a rewrite"]`
- Differentiation: `[what this page covers that no existing page does]`

>> GEN: This is the step that prevents two pages competing for one query. Default to rewriting/extending an existing page over creating a new one — a new URL needs a reason. If an existing money page partially covers the intent, the brief MUST become a rewrite of that page unless there is a clear intent split.

---

## 4. SERP context

- Top results: `[who ranks top 5 — SME competitors / directories / national brands, and what page type each is]`
- SERP blockers: `[AI Overview / local pack / heavy ads, from the Section 4 blockers column]`
- Shape that ranks: `[service page / location page / guide / comparison — match it, don't fight it]`

>> GEN: Reuse the SERP response already pulled for validation — no new API spend. If the SERP is dominated by directories or national brands, the Section 7 verdict should have been "Skip"; a brief reaching this point against that verdict is an error. If an AI Overview is present, the answer-block requirements in Section 5 are doing double duty (GEO citation + featured placement) — weight them accordingly.

---

## 5. Outline & GEO requirements

- H1: `[H1]`
- Proposed sections: `[H2/H3 outline with a one-line intent note per section]`
- Answer block: `[the 2–4 sentence self-contained answer the page must contain near the top — the passage an AI or featured snippet could quote whole]`
- Evidence to include: `[dates, credentials, project examples, sourced claims]`
- Entity signals: `[organization name, service area, service terms to state plainly]`

>> GEN: Apply `methodology/geo-ai-citability.md`: self-contained answer blocks, clear headings, concise definitions, dates, authorship, entity clarity. FAQs only if genuinely useful for the reader — never pitch them as a rich-result win (see `methodology/schema-checks.md` deprecations). Outline depth should match the ranking shape from Section 4, not an arbitrary word count.

---

## 6. On-page requirements

- Title tag: `[≤ 60 chars, keyword near front]`
- Meta description: `[≤ 155 chars, includes the enquiry hook]`
- Canonical: `[self, or existing URL if rewrite]`
- Schema: `[types required per methodology/schema-checks.md, mapped to this URL]`
- Internal links IN: `[which existing pages link here, with what anchors]`
- Internal links OUT: `[money pages / supporting pages this page links to]`
- Media: `[images, alt text requirements, before/after or project photos if available]`

---

## 7. Voice & claims rules

- Brand voice: `[client tone notes]`
- Every claim verifiable: no invented statistics, awards, review counts, or client names.
- No fabricated E-E-A-T: no fake author bios, credentials, or testimonials. If the client has real credentials or projects, use them; if not, omit — do not manufacture.
- Localization: `[service-area terms, spelling conventions, currency]`

---

## 8. Acceptance criteria

- [ ] Page live at the target URL and indexable (no noindex, correct canonical).
- [ ] Answer block present near the top, matching Section 5.
- [ ] Title/meta within limits and matching Section 6.
- [ ] Required schema present and valid on the rendered page.
- [ ] Internal links in/out live with agreed anchors.
- [ ] Expected signal: `[falsifiable metric + timeframe, e.g. impressions for [KW] within 6–8 weeks]` — this line feeds the next report's Section 3.

>> GEN: These criteria plug directly into `workflows/implementation-handoff.md` (current state → desired state → acceptance criteria → owner). Verify against the RENDERED page after implementation, not CMS fields. The expected-signal line is mandatory — it is what makes the content action gradeable next month.
