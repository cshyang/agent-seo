# WordPress Adapter Plan

WordPress should be an implementation adapter, not the reporting brain.

## Useful responsibilities

- Inventory pages/posts/custom post types.
- Check titles, metas, canonical tags, schema, headings, and internal links.
- Map money keyword target URLs to actual WordPress content.
- Create draft implementation tasks or content briefs.
- Export page metadata for agent review.

## Avoid by default

- Storing GA4/GSC/DataForSEO credentials in WordPress.
- Running full monthly reports inside WordPress.
- Storing lead-quality data in WordPress unless the client already uses it as the CRM.

## Future implementation options

- WP-CLI command package.
- Minimal admin plugin.
- Authenticated JSON export endpoint.
