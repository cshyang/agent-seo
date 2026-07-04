# Adapters

Adapters are optional integration surfaces. The core repo remains operator-side and data-source-driven.

Potential adapters:

- `wordpress/`: content inventory, metadata/schema checks, internal-link suggestions, draft implementation tasks.
- `nextjs/`: route metadata/schema checks and sitemap validation.
- `google-workspace/`: report export to Docs/Drive/Gmail drafts.
- `hermes/`: install/sync skills into a Hermes profile.

Adapters should not own the methodology. They implement or inspect site-specific changes after the reporting loop identifies the work.
