---
name: wordpress-seo-implementation
description: "Turn SEO report actions into safe WordPress implementation tasks: metadata, schema, internal links, target page fixes, content briefs, and rendered verification."
version: 0.1.3
tags: [seo, wordpress, implementation, metadata, schema]
---

# WordPress SEO Implementation

## When to use

Use when a report action requires inspection or changes inside a WordPress site.

## Operating rules

- Structure each task with `workflows/implementation-handoff.md` (current/desired state, acceptance criteria, owner, rollback notes) before touching the site.
- WordPress is an implementation adapter, not the reporting brain.
- Do not store GSC/GA4/DataForSEO credentials in WordPress by default.
- Propose customer-facing changes before applying unless explicitly approved.
- Verify rendered output after changes.

## Common tasks

- Check target URL content and metadata.
- Fix title/meta/canonical/schema issues.
- Add internal links to money keyword target pages.
- Prepare draft content briefs via the seo-content-briefs skill (`templates/content-brief-template.md` — demand-validated only).
- Export page inventory for reporting workflows.
- Apply schema checks from `methodology/schema-checks.md` before recommending new JSON-LD.

## URL fetch safety

When scripts fetch user/client-supplied URLs, validate first:

```bash
python scripts/url_safety.py https://example.com/page
```

## Verification

- Check rendered title/meta/canonical/schema.
- Confirm target URL remains indexable.
- Confirm no duplicate or conflicting SEO plugin fields.
