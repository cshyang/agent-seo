# Common Crawl Adapter

Status: experimental / optional enrichment.

Common Crawl is free public web crawl data. It is useful for source discovery and historical web graph context, but it is not a default monthly SEO KPI source.

## Intended uses

- Find third-party pages/directories mentioning a client, competitor, or category.
- Research source domains that may shape AI/GEO answers.
- Inspect historical domain presence and public crawl visibility.
- Support backlink/source discovery when paid link APIs are unavailable.

## Limitations

- Crawl coverage is incomplete and not real-time.
- Parsing WARC/WAT/WET files has compute and storage cost.
- Domain-level web graph data is directional, not a replacement for backlink APIs.
- Results need human/agent review before becoming recommendations.

## Future script ideas

- Query Common Crawl index for URL/domain mentions.
- Extract candidate source pages for GEO placement research.
- Compare client vs competitors on public-web mentions.
- Cache releases and record freshness in report appendix.
