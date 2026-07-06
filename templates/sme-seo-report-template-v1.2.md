# SME SEO Report — Reusable Template & Generation Spec

Version 1.2 · Designed for: GSC + GA4 + DataForSEO pipeline (SERP, Labs, Business Data, On-Page, AI Optimization)
Intended reader: the agent/pipeline generating the report. Sections marked `[FIELD]` are placeholders. Sections marked `>> GEN:` are generation instructions — delete them from the final client-facing output.

---

## PART A — ONE-TIME CLIENT ONBOARDING (do once, reference every month)

Fill this before the first report. Store per-client. The monthly report is only comparable over time if these stay fixed.

### A1. Client profile
- `[CLIENT_NAME]`, `[INDUSTRY]`, `[SERVICE_AREA]` (e.g., Klang Valley)
- `[PRIMARY_GOAL]`: leads via form / WhatsApp / calls / bookings (pick the real one — ask the client what a "good month" looks like in enquiries)
- `[SEASONALITY_NOTES]`: known busy/slow months, so trend commentary doesn't misattribute seasonal dips to SEO
- `[GBP_PROFILE]`: Google Business Profile link + primary category. `[LOCAL_INTENT: high/medium/low]`
  - **High:** buyers commonly choose from the map pack / "near me" results; local pack and GBP tracking are core report inputs.
  - **Medium:** local pack matters for service + location searches, but commercial organic visibility still leads the report.
  - **Low:** Maps/GBP is secondary; do not let local-pack metrics dominate the diagnosis.
- `[LOCAL_COMPETITORS]`: 2–3 named competitors (seed from the GEO competitor list after month 1 if unknown at onboarding) — used for review benchmarking and quarterly keyword-gap pulls
- `[BRAND_TERMS]`: company name, common abbreviations, founder/product names, and misspellings used to separate branded vs non-branded SEO demand
- `[LEAD_QUALITY_NOTES]`: what counts as a good-fit enquiry, known poor-fit patterns, minimum project size/budget if the client can define it

### A2. Money keyword set (10–20 terms, fixed)
Commercial-intent keywords only — terms a buyer types, not a researcher.
Selection procedure:
1. Pull 3 months of GSC queries, filter to queries with impressions ≥ 20 and clear buying intent
2. Validate each with DataForSEO search volume (drop anything < 30/mo volume unless strategically critical)
3. Client sign-off — they must recognize these as "the searches my customers make"
4. Assign each keyword a **theme** (service line) and a **target URL**

| # | Keyword | Theme | Target URL | Baseline pos | Baseline volume |
|---|---------|-------|-----------|--------------|-----------------|
| 1 | `[KW]` | `[THEME]` | `[URL]` | `[POS]` | `[VOL/mo]` |

Set changes require a changelog entry (A6). New keywords enter via the "Opportunities" section (Section 7) and only join the money set after one month of validation.

**Cold-start backfill:** at onboarding, pull 12 months of historical rank/visibility for the domain (DataForSEO Labs → Historical Rank Overview) so the first report already shows a trend line ("here's where you've been drifting before we started") instead of a context-free snapshot. Also record local pack presence baseline for each money keyword (in 3-pack: yes/no) if `[LOCAL_INTENT]` is high or medium.

### A3. Key event mapping (GA4)
Map GA4 key events to human labels. SME owners care about enquiries, not "key events."

| GA4 event | Report label | Value tier | Weight | Notes |
|-----------|--------------|------------|--------|-------|
| `[event_name]` | e.g., "Contact form submitted" | High | `1.0` | Usually a direct enquiry |
| `[event_name]` | e.g., "WhatsApp click" | High | `0.8` | Adjust if WhatsApp quality is poor/strong |
| `[event_name]` | e.g., "Phone number click" | Medium | `0.6` | Click does not always equal completed call |
| `[event_name]` | e.g., "Brochure download" | Low | `0.2` or excluded | Include only if commercially meaningful |

**Weighted enquiry formula:** `Σ(event count × event weight)` for organic traffic only. Always show the raw event breakdown beside the weighted number so the client can see what actually happened.

### A4. Lead quality feedback loop
Optional but recommended. If the client can share monthly enquiry quality, record it here and include a short note in Section 2.

| Feedback field | Definition |
|----------------|------------|
| Good-fit enquiry | `[client definition]` |
| Poor-fit enquiry | `[client definition: residential / too small / wrong location / supplier / job seeker / etc.]` |
| Feedback owner | `[client contact / CRM / sales team]` |
| Feedback cadence | Monthly / quarterly / unavailable |

If lead quality feedback is unavailable, do not infer quality from GA4. State: "Lead quality not yet validated by client."

### A5. GEO/AI prompt set (10–15 prompts, fixed)
Prompts a real buyer would ask an AI assistant. Same prompts, same platforms, every month.
- Platforms tested: `[e.g., ChatGPT, Claude, Gemini, Perplexity]`
- Record model/platform/date/location where available. AI responses vary; comparability depends on keeping the panel stable.
- Example prompt shapes: "best `[SERVICE]` company in `[CITY]`", "recommend a `[SERVICE]` firm for `[USE CASE]`", "`[COMPETITOR]` vs alternatives"

| # | Prompt | Platform(s) |
|---|--------|-------------|
| 1 | `[PROMPT]` | `[PLATFORMS]` |

### A6. Changelog
Every change to A2/A3/A5 gets a dated line here. This is what keeps month-12 comparable to month-1.

---

## PART B — MONTHLY REPORT TEMPLATE (client-facing)

# `[CLIENT_NAME]` SEO Report — `[MONTH YYYY]`
Prepared by `[YOUR_NAME]` · `[DATE]`

---

## 1. Bottom line
`[2–3 sentences: Are enquiries up or down? What is the ONE thing that mattered this month? What is the ONE focus for next month?]`

>> GEN: Write this LAST, after all other sections. No jargon. If a non-technical owner reads only this paragraph, they should know whether things are going well and what happens next. Never bury bad news — state it plainly with the diagnosis and the response plan. If data confidence is Low, say what we can and cannot conclude.

---

## 2. Scorecard
Six numbers max. Every number gets a MoM delta; add YoY once ≥13 months of history exists.

| Metric | This month | Last month | Δ MoM | Trend (3-mo) |
|--------|-----------|------------|-------|--------------|
| **Enquiries from organic** (weighted key events) | `[N]` | `[N]` | `[±%]` | `[sparkline/arrow]` |
| Organic sessions | `[N]` | `[N]` | `[±%]` | |
| Non-brand commercial clicks (GSC) | `[N]` | `[N]` | `[±%]` | |
| Money keyword avg. position (DataForSEO) | `[N]` | `[N]` | `[±]` | |
| Local pack presence (money keywords in 3-pack) | `[N/N]` | `[N/N]` | `[±]` | |
| AI visibility (prompts recommending/mentioning client / total) | `[N/N]` | `[N/N]` | `[±]` | |

Enquiry breakdown: `[Form: N · WhatsApp: N · Calls: N · Other: N]`  
Lead quality: `[Good-fit: N · Poor-fit: N · Unknown: N]` or `not yet validated by client`  
Data confidence: `[High / Medium / Low]` — `[reason: e.g., tracking complete; low enquiry volume; GA4 event issue; GSC lag; rank tracker missing; AI panel directional only]`

>> GEN: Enquiries row always first — it is the only row the owner truly cares about. Data sources: enquiries + sessions from GA4 (organic channel group only); weighted enquiries from A3 formula; non-brand commercial clicks from GSC after excluding A1 brand terms and informational/noise queries; avg position from DataForSEO rank tracker (NOT GSC — GSC position is an average across devices/queries and is noisy at SME volumes); local pack presence parsed from the SAME DataForSEO SERP responses used for rank tracking (local_pack items — no extra API spend); AI visibility from the fixed A5 prompt set. Omit the local pack row only if A1 says LOCAL_INTENT: low. If local intent is medium, keep the row only for service + location money keywords. If a delta is large (>30%), add ONE line of explanation below the table — seasonality, algorithm update (check known Google update dates for the period), tracking artifact, or our actions. Never leave a big swing unexplained. Do not over-interpret movements when data confidence is Low.

---

## 3. What we did last month → what happened
The accountability loop. One row per action committed in last month's Section 6.

| Action (from last report) | Status | Observable result | Verdict |
|---------------------------|--------|-------------------|---------|
| `[ACTION]` | Done / Partial / Blocked | `[metric, observation, or blocker]` | ✅ Worked / ⏳ Too early (expect signal by `[MONTH]`) / ❌ Didn't work → `[pivot]` / 🚧 Blocked → `[dependency]` |

>> GEN: Every committed action MUST appear here — no silent drops. "Too early" is a legitimate verdict (SEO lag is 4–12 weeks) but must carry an expected-signal date; the same action cannot stay "too early" more than 3 consecutive months without escalation to "didn't work / re-diagnose." If an action was blocked on the client/developer/access/approval, say so factually and name the dependency. This is the mechanism that keeps client-side tasks moving and prevents SEO being blamed for work that never shipped.

---

## 4. Money keyword tracker
Fixed set from A2, always in the same order.

| Keyword | Theme | Position (DataForSEO) | Δ MoM | Clicks (GSC) | Impressions (GSC) | Ranking URL | Correct URL? | SERP blockers |
|---------|-------|----------------------|-------|--------------|-------------------|-------------|--------------|----------------|
| `[KW]` | `[THEME]` | `[POS]` | `[🟢▲ / 🔴▼ / ⚪ within ±2]` | `[N]` | `[N]` | `[URL]` | ✅ / ⚠️ | `[AIO / LP / LP✅ / Ads / —]` |

>> GEN: Movement thresholds — ⚪ stable if |Δ| ≤ 2 positions; 🟢/🔴 beyond that. The "Correct URL?" column is the cannibalization detector: compare the actual ranking URL (DataForSEO SERP data) against the A2 target URL. Every ⚠️ is a candidate for Section 5 or 6. "SERP blockers" is parsed from the same SERP response — flag AI Overview (AIO), Local Pack (LP), or heavy Ads sitting above the client's listing. This column is the missing variable in "rankings improved but clicks didn't": position 8 below an AI Overview + 3-pack is effectively position 12. A client IN the local pack for that keyword gets LP✅ instead. Do NOT put per-row action text in this table — actions live in Section 6 only, once.

---

## 5. Diagnosis of the month
`[One insight, 3–6 sentences: what the data reveals, why it's happening, what it implies. Optionally one small supporting table/chart.]`

>> GEN: ONE diagnosis, not five. Pick the highest-leverage pattern. Priority order for what qualifies: (1) tracking or data-confidence issue that invalidates the headline metric, (2) wrong page ranking for money keywords (cannibalization), (3) rankings fine but clicks poor — check the Section 4 "SERP blockers" column before blaming titles/metas: if an AI Overview or local pack sits above the listing, the fix is GEO/local-pack work, not meta rewrites, (4) traffic fine but enquiries poor (landing page / conversion problem — this is a website problem, say so honestly rather than promising SEO will fix it), (5) non-brand commercial demand is down/up while branded traffic masks the real trend, (6) a cluster of keywords moving together (algorithm or competitor shift — check DataForSEO competitor ranks), (7) an untapped demand pocket (validated gap). Explain the CAUSE, not just the symptom. If nothing notable happened, say "steady month, no structural change" — do not manufacture insight.

---

## 6. Next month: 3 actions
| # | Action | Why (links to §5 or §7) | Expected impact | Effort | Owner |
|---|--------|--------------------------|-----------------|--------|-------|
| 1 | `[ACTION]` | `[REASON]` | `[e.g., KW #3–5 from p12 → p6–8 within 8 wks]` | S / M / L | Us / Client / Developer / Client + Developer / Waiting for access / Waiting for approval |

>> GEN: Exactly 3 (2 acceptable in quiet months; never more than 3 — SMEs execute one to three things, a 10-item list executes zero). Expected impact must be falsifiable — a metric and a rough timeframe — because Section 3 will grade it next month. At least one action should usually be an optimization of existing assets rather than new content; new content requires demand validation first (Section 7). Flag any action requiring client resources (dev, photos, approvals, CRM feedback, access) in Owner explicitly. Do not include vague GEO actions like "improve AI visibility"; translate them into concrete placement/content/entity actions.

---

## 7. New opportunities (validated)
| Query / topic | Evidence | Validation (DataForSEO) | Recommendation |
|---------------|----------|-------------------------|----------------|
| `[QUERY]` | `[GSC: N impr @ pos X]` | `[volume/mo, difficulty, SERP check]` | Target existing page / New page / Add to money set / Skip |

>> GEN: Two candidate sources. Monthly: GSC queries NOT in the money set with impressions ≥ 30 and position 8–25 (page 1–3 striking distance), split into brand, non-brand commercial, informational, and noise. Quarterly: competitor keyword gap via DataForSEO Labs (Ranked Keywords / Domain Intersection) on the A1 LOCAL_COMPETITORS — keywords they rank top-10 for that the client doesn't rank top-50 for. This matters because GSC is a mirror: it only shows demand the client already surfaces for, so GSC-only sourcing structurally misses whole service lines competitors own. Then validate ALL candidates identically: DataForSEO volume ≥ 30/mo, and eyeball the live SERP — if it's dominated by directories/aggregators or national brands, an SME page won't crack it; say "Skip" and why. Max 5 rows. Never recommend new content without volume validation — this is the anti-content-farm rule.

---

## 8. AI / GEO visibility
- Panel visibility: `[N/N]` prompts recommend or mention `[CLIENT_NAME]` (last month: `[N/N]`), by platform: `[ChatGPT N/N · Gemini N/N · ...]`
- Mention quality: `[recommended: N · cited (URL linked): N · mentioned (named, no link): N · absent: N]`
- Competitor share of voice: `[top 3 competitors by mention count, Δ vs last month]`
- Sources shaping AI answers: `[top domains AI cites for the client's category — and whether the client is present on them]`
- Note: fixed prompt panel (see methodology), tracked monthly — a directional indicator, not exact market share.

>> GEN: Automate via DataForSEO AI Optimization API. (a) Run the exact A5 prompt panel through LLM Responses endpoints with web_search enabled — same prompts, same models/platforms where possible, every month; parse the response text for client/competitor names and the sources/annotations array for citations. (b) Pull LLM Mentions (Cross Aggregated Metrics) for client vs. A1 competitors for share-of-voice; note its index has a 2–7 day lag, so run it mid-month-cycle, not on the 1st. (c) Pull Top Domains/Top Pages for the category once a quarter — this is the actionable core: GEO work is mostly "be present in the sources AI reads," so the output of this section for Section 6 is concrete ("AI answers in this category are shaped by 4 directories; client is absent from 2 — get listed"), never vague ("improve AI visibility"). Distinguish recommendation, citation, and mention in commentary: recommendation means AI positions the client as a valid option; citation means AI trusts a page enough to link it; mention means brand presence without necessarily endorsing/citing it. They need different fixes. A competitor newly appearing across multiple prompts is worth a line. If visibility is low on ChatGPT/Copilot specifically while other platforms look normal, check Bing index coverage before diagnosing content: the Bing index gates ChatGPT citation, and wrong-index is a cheaper explanation than wrong-content (see `methodology/geo-ai-citability.md`).

---

## 9. Appendix
- A. Full GSC query table (top 50 by impressions), tagged brand / non-brand commercial / informational / noise
- B. Landing page performance (GA4: sessions, engagement, enquiries by page)
- C. Technical health check — **quarterly only** (`[Q1/Q2/Q3/Q4]` months): indexation count vs. sitemap, Core Web Vitals pass/fail, broken internal links, duplicate titles/metas, crawl anomalies
- D. Local presence benchmark — **quarterly only**: client vs. A1 LOCAL_COMPETITORS on Google Business Profile — rating, review count, review velocity (reviews gained this quarter), primary category. Omit or de-emphasize when `[LOCAL_INTENT]` is low.
- E. Methodology notes (data sources, date ranges, money set + prompt panel version from A6 changelog)
- F. Data run log (DataForSEO task count / estimated credit cost, missing sources, known data issues)

>> GEN: Appendix is reference material — no commentary, no actions. Automate C with the DataForSEO On-Page API (one crawl task per quarter) rather than a manual audit — manual audits are the section that silently stops happening by month 4. Pull D from the Business Data API (Google My Business Info) for client + competitors. Review velocity is the actionable number: "competitor X gained 40 reviews this quarter, you gained 3" is a client-executable action for Section 6 and a genuine local-pack ranking input. Both run quarterly because these signals don't move monthly; if the quarterly check finds a P0 (deindexed pages, site-wide noindex, CWV collapse), it overrides Section 5 as the diagnosis of the month.

---

## PART C — PIPELINE NOTES (data source division of labor)

| Job | Source | Cadence | Why |
|-----|--------|---------|-----|
| Query ↔ page mapping, gap discovery, impressions/clicks | GSC | Monthly | Only source of Google's actual query data |
| Brand vs non-brand query classification | GSC + A1 brand terms | Monthly | Prevents branded demand from masking commercial SEO performance |
| Enquiries, engagement, landing-page outcomes | GA4 | Monthly | Only source of conversion truth |
| Lead quality feedback | Client/CRM/sales notes | Monthly or quarterly | Validates whether SEO enquiries are commercially useful |
| Money keyword true rank (fixed device/location) | DataForSEO SERP | Monthly | Stable, comparable; GSC position is a noisy average |
| Local pack presence + SERP blockers (AIO/LP/Ads) | Same SERP responses, parsed further | Monthly | Zero extra API cost; explains rank-vs-clicks divergence |
| Cannibalization detection | DataForSEO ranking URL vs. A2 target URL | Monthly | The "Correct URL?" column |
| Volume validation, keyword difficulty | DataForSEO Labs | Monthly (§7 only) | Gates content investment |
| GEO prompt panel | DataForSEO LLM Responses (web_search on) | Monthly | Fixed-panel consistency; structured, scalable |
| AI share of voice, citation vs mention | DataForSEO LLM Mentions | Monthly (mid-cycle; 2–7 day index lag) | Competitor benchmark beyond the panel |
| Sources shaping AI answers | DataForSEO LLM Mentions Top Domains/Pages | Quarterly | Converts GEO observation into placement actions |
| Competitor keyword gap | DataForSEO Labs Ranked Keywords / Domain Intersection | Quarterly | GSC can't see demand the client never surfaces for |
| Technical health check | DataForSEO On-Page API | Quarterly | Automates Appendix C so it actually happens |
| GBP / review benchmark | DataForSEO Business Data API | Quarterly | Review velocity = client-executable local-pack action |
| Historical rank backfill | DataForSEO Labs Historical Rank Overview | Once (onboarding) | Month-1 report gets a trend line instead of a snapshot |

### DataForSEO cost/run control
- Monthly SERP pulls must reuse the same responses for true rank, ranking URL, local pack presence, AIO/local pack/ads blockers, and SERP competitor observations.
- Monthly Labs usage should be limited to Section 7 validation unless a deeper diagnostic is explicitly needed.
- Quarterly-only jobs: Top Domains/Pages, competitor keyword gap, On-Page crawl, GBP/review benchmark.
- Record task count / estimated cost in Appendix F.
- Do not add DataForSEO Backlinks, Content Generation, AI Keyword Data, or Google Trends endpoints by default.

Deliberately NOT used: Backlinks API (noise for local SMEs; invites unbillable link-building conversations — onboarding toxic-link check at most), Content Generation API (Claude does this), AI Keyword Data / AI search volume (immature metric, revisit when baselines exist), Google Trends endpoints (A1 seasonality notes suffice). Resist adding these back — every added section dilutes the one-diagnosis discipline.

Date-range convention: full calendar month, compared against the prior full calendar month. GSC data has a ~2-day lag — generate reports no earlier than the 3rd of the following month.

Generation order: Sections 4, 7, 8 (data pulls) → 3 (grade last month) → 5 (diagnose) → 6 (plan) → 2 (scorecard) → 1 (bottom line, written last). Quarterly pulls (Top Domains, keyword gap, On-Page, GBP benchmark) run in `[Q-months]` and feed the same sections.

---

## PART D — FINAL REPORT QA CHECKLIST

Run this before client delivery.

- [ ] No `[FIELD]` placeholders remain unless intentionally left in an appendix template.
- [ ] No `>> GEN:` instructions remain in the client-facing output.
- [ ] Date range is the full calendar month and compared with the prior full calendar month.
- [ ] GSC data was generated no earlier than the 3rd of the following month.
- [ ] GA4 organic channel/session filter is applied consistently.
- [ ] Weighted enquiry calculation follows A3 and raw event counts are shown.
- [ ] Brand terms are excluded from non-brand commercial clicks.
- [ ] Data confidence is labeled High/Medium/Low with a reason.
- [ ] Any swing >30% has a short explanation or tracking caveat.
- [ ] Every previous Section 6 action appears in Section 3.
- [ ] Section 5 contains one diagnosis only.
- [ ] Section 6 has 2–3 actions, never more than 3.
- [ ] Every Section 6 action has a falsifiable expected impact and owner.
- [ ] Client/developer/access blockers are explicit.
- [ ] AI/GEO visibility is labeled directional, not exact market share.
- [ ] DataForSEO quarterly jobs only ran in scheduled quarter months unless explicitly requested.
- [ ] Appendix F records DataForSEO task count / estimated cost and any missing data sources.
