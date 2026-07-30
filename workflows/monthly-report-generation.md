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
- Executive summary first, never executive summary only, unless an explicitly requested short review note links to the full report.
- Do not overfit low-volume changes.
- Explain any movement greater than 30%.
- Do not recommend new content without demand validation.
- Do not include more than three actions.
- Client blockers must be explicit.
- Preserve the full analytical baseline: scorecard; full fixed keyword tracker with rank, actual/target page, GSC and SERP/local fields; organic/landing quality; technical evidence; GEO coverage; methodology and caveats.
- If AI prompt coverage was not run, label it not measured. Do not substitute local pack/PAA/AI Overview counts for cross-platform GEO coverage.
- Gmail-safe formatting may change layout but not analytical coverage.

## Output

Write the finished client-facing report to `.seo-ops/clients/<slug>/reports/YYYY-MM.md` (gitignored). It must pass QA before delivery:

```bash
python scripts/qa_report.py .seo-ops/clients/<slug>/reports/YYYY-MM.md
```
