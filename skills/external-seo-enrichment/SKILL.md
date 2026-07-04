---
name: external-seo-enrichment
description: "Use optional external SEO enrichment sources such as Common Crawl and Moz for source discovery, authority context, GEO citation research, and backlink sanity checks without turning them into default monthly KPIs."
version: 0.1.0
tags: [seo, backlinks, commoncrawl, moz, enrichment, geo]
---

# External SEO Enrichment

## When to use

Use when GSC/GA4/DataForSEO do not answer a source-discovery or authority-context question, or during onboarding/quarterly research where backlink/source context could change the recommendation.

## Source hierarchy

Core monthly truth remains GSC, GA4, DataForSEO, and client lead-quality feedback. Common Crawl and Moz are enrichment sources only.

## Common Crawl

Good for:

- public-web source discovery
- competitor mention discovery
- category/directory discovery
- GEO source research

Bad for:

- fresh visibility claims
- exact backlink counts
- monthly KPI movement

## Moz

Good for:

- DA/PA/spam score context
- linking root domain sanity checks
- competitor authority context

Bad for:

- monthly client scorekeeping
- standalone link-building advice
- replacing paid link datasets

## Output rule

Only surface enrichment when it creates a concrete action. Otherwise keep it as internal context.
