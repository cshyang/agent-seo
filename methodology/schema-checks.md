# Schema Checks

Schema work is an implementation aid. It should support search understanding, eligibility, entity clarity, and AI/citation quality — not create busywork.

## Validation checklist

For each schema block:

1. `@context` is `https://schema.org`.
2. `@type` is valid and appropriate for the page/business.
3. Required and recommended properties are present where useful.
4. URLs are absolute.
5. Dates use ISO 8601 format.
6. Values match expected types.
7. No placeholder text remains.
8. Markup content matches visible page content.
9. No conflicting duplicate schema from multiple plugins/themes.

## Common useful types

- Organization
- LocalBusiness and relevant subtypes
- Service
- WebPage
- WebSite
- BreadcrumbList
- Article / BlogPosting
- Person
- Product / Offer where e-commerce applies
- Review / AggregateRating only when policy-compliant and visible

## Deprecated or limited rich-result expectations

- Do not sell schema as a guaranteed rich-result lever.
- HowTo rich results were removed from Google Search in 2023.
- FAQ rich-result visibility has been heavily restricted/retired for most sites; FAQPage may still help structure content for AI/entity understanding, but should not be pitched as a SERP feature win.

## Implementation rule

Schema recommendations should map to a target URL and acceptance criteria. Verify rendered HTML/JSON-LD after implementation, not only CMS fields.
