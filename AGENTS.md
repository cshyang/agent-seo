# Agent Instructions

This repo defines reusable SEO/GEO operations workflows for agents such as Hermes, Codex, Claude, and human operators.

## Boundaries

- Keep the repo client-data-free by default.
- Do not add real API keys, OAuth tokens, raw analytics exports, lead details, or private reports.
- Prefer schemas, templates, sanitized fixtures, and deterministic helpers.
- If a future workflow needs real client configs, keep them in a separate private repo or local `.seo-ops/` directory that is gitignored.

## Development discipline

- Use deterministic scripts for validation, normalization, and QA.
- Use agent judgement for diagnosis, prioritization, and client-facing narrative.
- Every generated client-facing report must pass `scripts/qa_report.py` before delivery.
- Client-facing reports must remove `>> GEN:` instructions and unresolved placeholders.
- Keep report methodology commercially grounded: enquiries first, one diagnosis, two to three actions.

## Repo conventions

- `methodology/`: stable operating rules.
- `templates/`: reusable markdown/client input templates.
- `schemas/`: JSON schemas and sanitized examples.
- `skills/`: agent skills with `SKILL.md` and references.
- `workflows/`: step-by-step procedures.
- `scripts/`: small deterministic utilities with no required secrets by default.
- `adapters/`: optional integration plans or implementation adapters.
- `examples/`: sanitized fixtures only.

## Safety checklist before commit

- [ ] No `.env` or token files.
- [ ] No real client raw exports.
- [ ] No real lead names, phone numbers, emails, or WhatsApp transcripts.
- [ ] No client account IDs unless intentionally sanitized or documented as examples.
- [ ] Scripts run against example fixtures.
- [ ] Adapted upstream code or methodology is attributed in `NOTICE`.
