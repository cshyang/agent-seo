# Monthly SEO/GEO Report Generation

## Inputs

- Client config from `.seo-ops/clients/<slug>/config.yaml`, matching `schemas/client-config.schema.json`
- Prior month report Section 6 actions, read from the lexically previous `YYYY-MM.md` in `.seo-ops/clients/<slug>/reports/` (see the AGENTS.md client state convention)
- Full calendar month date range
- Prior full calendar month comparison
- GSC data available no earlier than the 3rd of the following month

## Generation order

1. Pull/prepare money keyword tracker.
2. Pull/prepare opportunity candidates.
3. Pull/prepare AI/GEO visibility panel.
4. Grade last month’s actions.
5. Write one diagnosis.
6. Choose two to three next actions.
7. Compile scorecard.
8. Write bottom line last.
9. Run report QA.

## Rules

- Enquiries first.
- Do not overfit low-volume changes.
- Explain any movement greater than 30%.
- Do not recommend new content without demand validation.
- Do not include more than three actions.
- Client blockers must be explicit.

## Output

Write the finished client-facing report to `.seo-ops/clients/<slug>/reports/YYYY-MM.md` (gitignored). It must pass QA before delivery:

```bash
python scripts/qa_report.py .seo-ops/clients/<slug>/reports/YYYY-MM.md
```
