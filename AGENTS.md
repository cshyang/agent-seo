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

## Repo as the unit of operation

This repo is cloned and used whole, from the repo root. Skills are repo-resident, not standalone-installable: SKILL.md files reference `templates/`, `schemas/`, and `scripts/` by repo-root-relative path. Do not copy individual skill folders into `~/.claude/skills/` or similar — the references will dangle. Templates live only in `templates/` (single source of truth); skill folders must not carry their own copies.

## Client state convention

Real client state lives in `.seo-ops/` at the repo root (gitignored), one folder per client slug:

```text
.seo-ops/
  clients/
    <slug>/                # e.g., sua
      config.yaml          # matches schemas/client-config.schema.json
      reports/
        2026-06.md         # one file per monthly report, YYYY-MM.md
        2026-07.md
      quarterly/
        2026-Q3.md         # quarterly refresh outputs
      audits/
        2026-07-audit.md   # one-off site audits (onboarding, prospect, re-baseline)
      briefs/
        2026-07-topic.md   # content briefs and drafts, one per validated topic
```

The monthly workflow finds "last month" mechanically: the lexically previous `YYYY-MM.md` in `reports/`. The Section 3 accountability loop reads that file's Section 6 — no memory, no guessing, no asking the operator. If the prior report file is missing, say so explicitly in the report rather than fabricating a Section 3.

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
