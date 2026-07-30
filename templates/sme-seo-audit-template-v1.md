# SME SEO Baseline Audit — Template & Generation Spec

Version 1.0 · Companion to `sme-seo-report-template-v1.3.md` (Parts A–D)
Structure salvaged from a real client baseline audit (2026-07-15), generalized here.

**When to use:** once per client, at onboarding, BEFORE the first monthly report. The audit's jobs are: (1) establish every baseline the monthly report will compare against, (2) finalize the Part A config (money keywords, event mapping, GEO panel), (3) produce the first three actions that month-1's Section 3 will grade. The monthly template covers month 2 onward; this covers month 1.

**Relationship to config:** the audit both consumes and finalizes `client-config.yaml`. Keyword panel and GEO prompt panel are FROZEN at audit sign-off — changes after that go through the A6 changelog.

>> GEN: Sections marked `>> GEN:` are generation instructions — delete from client-facing output. Write Section 1 LAST. Operating boundary is read-only: an audit that changed things mid-measurement has corrupted its own baseline.

---

# `[CLIENT_NAME]` SEO, Technical & GEO Audit — `[DATE]`

**Site:** `[URL]`
**Business focus:** `[one line: what a qualified enquiry is, which locations/languages matter]`
**Search-data window:** `[trailing ~90 days]` vs `[prior ~90 days]`
**Sources:** `[GSC, GA4, live crawl, GSC URL Inspection, DataForSEO SERP (device + location), Google Ads volume, DataForSEO LLM Responses]`
**Operating boundary:** Read-only audit. No website, GBP, GA4/GTM, GSC, or ads changes made.

>> GEN: Rolling ~90-day windows are correct for an audit (unlike the monthly report's calendar months) — say so here so nobody "fixes" it later. Name device + location for every rank claim.

---

## 1. Executive bottom line

`[3–5 sentences: where the client actually stands, the one commercial problem, whether the foundation is sound]`

### One diagnosis

> `[One paragraph. The single highest-leverage pattern explaining the gap between visibility and enquiries. Same priority order as monthly Section 5: tracking validity → wrong-page ownership → rank-vs-click gaps (check SERP blockers first) → conversion → brand masking → competitor/algorithm shift → untapped demand.]`

### Three priority actions

1. `[headline of Action 1]`
2. `[headline of Action 2]`
3. `[headline of Action 3]`

>> GEN: ONE diagnosis. The audit will surface 20+ findings; resist listing five diagnoses. Everything else becomes evidence for the one diagnosis or a line item inside the three actions. Never bury bad news.

---

## 2. Baseline scorecard

| Metric | Current `[window]` | Prior `[window]` | Δ / status |
|--------|---:|---:|---|
| GSC clicks | | | |
| GSC impressions | | | |
| Organic CTR | | | |
| GA4 organic sessions | | | |
| GA4 engaged sessions / engagement rate | | | |
| Deduplicated enquiry users (see §5) | | | |
| Enquiry-user/session rate | | | |
| Money keywords in top 10 (per language) | `[N/N]` | New baseline | |
| SERPs showing local pack | `[N/N]` | New baseline | |
| Client local-pack appearances | `[N/N]` | New baseline | |
| GEO panel coverage (per engine × language) | `[matrix ref §7]` | New baseline | |

**Interpretation:** `[2–3 sentences: what moved, what's a new baseline, what the numbers do NOT prove]`

>> GEN: The audit scorecard may exceed the monthly six-row cap — it is establishing many baselines at once. That license does NOT carry into monthly reports. Local-pack presence and client inclusion stay separate rows. GSC average position is allowed here only as a period-over-period comparison, clearly labeled GSC; DataForSEO is the rank source of record from month 1 on.

---

## 3. Fixed money-keyword panel

### Method
- **Organic ranking:** DataForSEO SERP, `[device]`, localized to `[location]`.
- **Volume:** Google Ads `[country]`; `—` = no stable exact volume returned.
- **GSC:** exact disclosed query rows for the window; privacy thresholds mean zeros do not prove no searches.
- **Cost:** `[USD, task count]`.

### `[LANGUAGE_1]` panel — `[N]` keywords

| Keyword | Volume | Live rank | Ranking page | Intended page | GSC imp / clicks | Local pack | Assessment |
|---|---:|---:|---|---|---:|---|---|
| `[KW]` | | | | | | `[Present; client absent / Present; client in / No local pack]` | `[Defend / Wrong-page ownership / Correct owner / Gap]` |

### `[LANGUAGE_2]` panel — `[N]` keywords

`[same columns]`

### Positioning watchlist — not scored as money keywords

`[terms the client cares about that have zero validated demand; state the evidence and the rule: do not judge SEO performance by them]`

>> GEN: Ranking-page vs intended-page is the cannibalization detector — populate both for every keyword. One language per table; never merge. Every keyword's assessment is one phrase. The panel printed here is the panel frozen into A2 — same order the monthly Section 4 will use forever.

---

## 4. Search Console diagnosis

- Overall movement (clicks, impressions, CTR, position) and what it means — efficiency vs breadth.
- Brand vs non-brand split (A1 brand terms): clicks, impressions, CTR, position for each cohort.
- Commercial theme movement: clicks by service-line theme, current vs prior.
- Page concentration: `[homepage share of clicks]`% — are money pages independently earning demand?
- Indexing discrepancies: live HTTP status vs GSC URL Inspection for priority pages.

>> GEN: Theme movement is where service-line weakness shows before keyword tables do. Flag any page 200-live but 404/excluded in GSC's index — that's a month-1 action candidate.

---

## 5. Analytics & conversion truth

- Enquiry events inventory: every GA4 event claiming to measure an enquiry, with counts and users.
- **Duplicate-event check (mandatory):** do two events fire on one physical interaction? State the deduplicated real number next to the reported number.
- Enquiry trend: deduplicated users current vs prior window; per-session rate.
- Lead quality: `[client feedback or "not yet validated by client"]`.

>> GEN: This section exists because inflated enquiry counts poison every future report. The deduplicated number becomes the A3 mapping and the monthly scorecard's first row. Clicks are interaction proxies, not verified enquiries — say so.

---

## 6. Technical SEO

- Crawl baseline: pages crawled, issues by severity, slow pages.
- Healthy foundations: canonicals, schema presence, priority-page status — say what is already fine.
- Schema gap: dominant types found vs the entity types the business actually needs (e.g., `LocalBusiness`/sector type, `Service`). Frame as entity hygiene, not a rankings lever.
- Metadata: duplicated titles/descriptions, keyword-stuffed boilerplate, visible spelling errors on money pages.
- Broken links: actionable 404s only; name known crawler artifacts (e.g., `/cdn-cgi/l/email-protection`) so they don't get "fixed".
- Sitemap hygiene: legacy submissions, non-canonical variants.

>> GEN: Cap at what is evidenced by the crawl. Separate "actionable" from "artifact" explicitly. Spelling errors on money pages go here — they are trust findings, not nitpicks.

---

## 7. GEO / AI-search baseline

### SERP features across the money panel
- Local pack: `[N/N]` · client in pack: `[N/N]` · People Also Ask: `[N/N]` · Ads: `[N/N]` · AI Overview: `[N/N]`

### Fixed prompt panel
Per template v1.3 A5: minimum 10 language-tagged prompts, ChatGPT + Gemini + Perplexity via DataForSEO LLM Responses. Record model, run date, location context, cost.

**Coverage matrix** (engine × language):

| | ChatGPT | Gemini | Perplexity | Total |
|---|---|---|---|---|
| `[LANG_1]` | `[N/N]` | `[N/N]` | `[N/N]` | |
| `[LANG_2]` | `[N/N]` | `[N/N]` | `[N/N]` | |

Per prompt: `[recommended / cited / mentioned / absent]` + main competing facilities/sources named by the AI.

**Sources shaping answers:** `[the directories, portals, review sites the engines cited; client present/absent on each]`

>> GEN: If the panel is under 10 prompts or fewer than 3 engines, label coverage "insufficient panel — directional only" and make panel completion a month-1 action. The sources-shaping-answers list is the actionable output — each absence maps to a listing/placement action in §8. Never forecast AI referral traffic. If AI Overview citations aren't returned by the API, say the feature exists but citation presence is unclaimed.

---

## 8. Three-action implementation plan

### Action `[N]` — `[name]`
**Owner:** `[us / client / developer / mixed]` · **Impact:** `[High/Med]` · **Effort:** `[S/M/L]`

#### Work
- `[concrete steps]`

#### Acceptance
- `[observable, falsifiable criteria — these are what monthly Section 3 will grade]`

>> GEN: Exactly three actions, each with acceptance criteria. These actions ARE month-1's committed actions — the first monthly report grades them, so every acceptance criterion must be checkable from data you'll actually have. Typical audit-shaped actions: entity/local-pack eligibility, page-ownership consolidation (one owner page per language — no thin translated page farms), measurement + technical repair. No vague GEO actions; translate to concrete placements from §7's source list.

---

## 9. Approval & implementation boundary

This audit did not modify `[systems]`. Before implementation, `[CLIENT]` should approve:
1. `[access scopes]`
2. `[factual claims used in copy — verify before publishing]`
3. `[copy changes per language]`
4. `[tracking changes]`
5. `[technical fixes]`

After any site change, verify rendered title, description, H1, canonical, schema, indexability, internal links and CTA behavior publicly.

---

## 10. Saved evidence

- `[path to each raw pull: GSC, GA4, crawl, SERP baseline, GEO panel responses, cost ledger]`

>> GEN: Every number in this audit must be reproducible from a saved file. No file, no claim.

---

## 11. Limitations

`[honest list: privacy-thresholded GSC rows, point-in-time SERP snapshots, engines not measured, proxies vs verified enquiries, anything quota-blocked]`

---

## Audit QA (delete from client output)

- [ ] One diagnosis only; bottom line written last.
- [ ] Read-only boundary stated and honored.
- [ ] Every rank claim names device + location; every number has a saved-evidence path.
- [ ] Keyword tables split per language; ranking-page vs intended-page populated for every keyword.
- [ ] Local-pack presence and client inclusion are separate fields.
- [ ] Duplicate-event check performed; deduplicated enquiry number stated next to reported number.
- [ ] GEO panel meets v1.3 spec (≥10 language-tagged prompts, ≥3 engines) or is labeled insufficient with panel completion as an action.
- [ ] Sources-shaping-answers list present; each client absence maps to an action.
- [ ] No AI referral traffic forecast anywhere.
- [ ] Exactly 3 actions, each with owner and falsifiable acceptance criteria.
- [ ] Client-config A1–A6 finalized and frozen; audit findings recorded in config changelog.
- [ ] No `>> GEN:` blocks or placeholders remain in client-facing output.
