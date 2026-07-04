# Upstream Review: AgriciDaniel/claude-seo

Source: https://github.com/AgriciDaniel/claude-seo  
License: MIT  
Reviewed for: agent-seo operator-side SEO/GEO engine

## Decision

Cherry-pick selectively. Do not port the Claude Code plugin wholesale.

## Why not copy wholesale

- The upstream repo is optimized for Claude Code plugin/agent conventions.
- It is broad audit-suite software; agent-seo is a commercial operating loop for recurring SEO/GEO reporting and implementation planning.
- Some modules produce scores and long action lists, while agent-seo intentionally enforces one diagnosis and two to three actions.
- Some claims and ranking-factor numbers require verification before becoming default methodology.

## Selected ideas to adapt

| Upstream area | Agent SEO adaptation | Status |
|---|---|---|
| `agents/seo-dataforseo.md`, `scripts/dataforseo_costs.py`, `scripts/dataforseo_normalize.py` | Cost warnings, bulk endpoint discipline, response normalization, timestamped live-data caveats | Adapted as docs + compact scripts |
| `agents/seo-backlinks.md`, `scripts/commoncrawl_graph.py`, `scripts/moz_api.py` | Optional backlink/source enrichment via Common Crawl and Moz; not monthly KPIs | Adapted as optional enrichment docs |
| `agents/seo-geo.md` | AI crawler checks, llms.txt/RSL checks, citability and entity signals | Adapted as methodology; exact correlation claims excluded |
| `agents/seo-schema.md` | Schema validation rules and implementation checklist | Adapted as methodology for implementation adapters |
| `scripts/url_safety.py`, `scripts/render_page.py` | Safe URL validation and future rendered-page inspection patterns | Compact URL safety helper added; renderer deferred |

## Deliberately not imported yet

- Claude plugin packaging and install scripts.
- Full parallel agent set.
- Large Playwright renderer.
- E-commerce, visual, image-generation, FLOW, and release tooling.
- Numeric SEO health score system.

## Attribution rule

If code or methodology is adapted from upstream, keep `NOTICE` current and preserve MIT attribution.
