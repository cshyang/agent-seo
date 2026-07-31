# Draft comparison / final gate prompt

Compare every draft produced for this SUA brief (`drafts/draft-<route>.md`).
With a single draft this is a final gate, not a comparison.

Return JSON only with:
- winner: the route name that should be published, or "neither"
- quality_scores (per route):
  - commercial_fit
  - writing_quality
  - seo_structure
  - factual_risk
  - brand_fit
  - human_editing_needed
- best_sections_from_each
- recommended_final_route
- revision_plan

Judge against the brief document, the brief manifest, the style guide, and the
lead-quality guardrails.
