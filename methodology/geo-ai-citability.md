# GEO / AI Citability Checks

> Last verified: 2026-07-06. Crawler tokens, llms.txt guidance, and the engine→index mapping rot fast — re-verify quarterly against upstream and primary sources.

GEO work should produce concrete source, content, or entity actions — not vague advice to "improve AI visibility."

## Answer engine → underlying index

Being cited by an AI answer engine requires being in the index that engine retrieves from. Optimizing for Google does not index a site in Bing.

| Answer engine | Retrieval index | Crawler access required |
|---------------|-----------------|-------------------------|
| ChatGPT Search | Bing index (primary) + OpenAI's own | Bingbot AND OAI-SearchBot |
| Microsoft Copilot | Bing | Bingbot |
| Google AI Overviews / Gemini | Google | Googlebot |
| Perplexity | Own index | PerplexityBot |
| Claude | Anthropic search fetching | Claude-SearchBot |

Directional evidence (unverified-correlation rules apply): a 2025 Seer Interactive analysis of 500+ ChatGPT search citations found ~87% matched Bing's top organic results for the same query. Blocking OAI-SearchBot removes a site from ChatGPT Search even when it ranks well on Bing — it is a two-key lock.

## Bing indexation path

Google ranking work carries over to Bing; Google *indexation* does not, and Bing's coverage of small sites is thinner. One-time setup at onboarding (all free):

1. Verify the site in Bing Webmaster Tools (use the import-from-GSC flow).
2. Submit the sitemap.
3. Enable IndexNow where the CMS supports it (WordPress SEO plugins commonly do).
4. Confirm robots.txt allows Bingbot and OAI-SearchBot.

Then leave it alone — Bing indexation is an onboarding task and an audit/diagnostic check, never a monthly KPI. When AI visibility is low on ChatGPT/Copilot specifically, check Bing index coverage before diagnosing content problems: wrong-index is a cheaper explanation than wrong-content.

## Checks

- AI crawler access: robots.txt rules for major AI search/crawler agents.
- `/llms.txt`: present, absent, malformed, or intentionally omitted.
- RSL/licensing: note presence when relevant; do not treat absence as a ranking failure.
- Technical accessibility: server-rendered/indexable content vs. client-only shell.
- Citability: self-contained answer blocks, clear headings, concise definitions, sourced claims, dates, authorship, and organization/entity clarity.
- Source presence: directories, review sites, industry lists, local portals, and third-party pages that AI systems cite or summarize.

## AI crawler tokens to review

- GPTBot
- OAI-SearchBot
- ChatGPT-User
- ClaudeBot
- Claude-SearchBot
- PerplexityBot
- Google-Extended
- Googlebot
- Bingbot
- CCBot

Interpret carefully: blocking training crawlers is not the same as blocking search indexing or AI answer visibility.

## Output discipline

For monthly reports, GEO findings should become one of these concrete actions:

- Get listed on a source/domain AI answers already cite.
- Improve a priority service page with clearer answer blocks and evidence.
- Add or fix organization/person/service schema.
- Fix crawler access or rendering if content is unavailable to AI/search systems.
- Strengthen entity consistency across site, GBP, social, and key directories.

Do not use unsupported exact correlation claims as client-facing facts unless independently verified and cited.
