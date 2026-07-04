# Agent SEO

Agent SEO is an operator-side SEO/GEO operations system for agents and humans. It packages reusable methodology, Hermes skills, templates, schemas, workflows, and deterministic scripts for commercial SME SEO reporting and implementation planning.

The repo is intentionally **client-data-free**. Real client configs, credentials, raw exports, report outputs, and lead data should live in private client environments or separate private repos.

## What this repo is

- A reusable SEO/GEO reporting and operations toolkit.
- A source of truth for agent workflows used by Hermes, Codex, Claude, or humans.
- A set of schemas and QA checks that keep reports comparable over time.
- A foundation for future adapters such as WordPress, Next.js, Google Workspace, Common Crawl, Moz, or cron jobs.

## What this repo is not

- Not a central dump for all client data.
- Not a WordPress plugin first.
- Not a replacement for GSC, GA4, or DataForSEO.
- Not a place for OAuth tokens, API keys, raw lead data, or private client reports.

## Current shape

```text
agent-seo/
  methodology/        Operating principles and measurement rules
  templates/          Client/report templates
  schemas/            Config schemas and examples
  skills/             Installable/reusable agent skills
  workflows/          Step-by-step operating workflows
  scripts/            Deterministic helpers and QA checks
  adapters/           Future implementation adapters
  examples/           Sanitized fixtures only
```

## First operating principle

Use code for deterministic work and agents for judgement.

- Deterministic: config validation, date ranges, event weighting, placeholder checks, query classification, report QA.
- Agentic: diagnosis, prioritization, client-facing narrative, trade-offs, implementation recommendations.

## Quick start

Validate the example client config:

```bash
python scripts/validate_client_config.py schemas/client-config.example.yaml
```

Check a generated markdown report for obvious delivery issues:

```bash
python scripts/qa_report.py templates/sme-seo-report-template-v1.2.md --template
```

Classify a GSC export draft:

```bash
python scripts/classify_gsc_queries.py examples/sample-gsc-export.csv --brand-term examplebrand
```

Estimate a DataForSEO run before adding API spend:

```bash
python scripts/dataforseo_cost_estimate.py estimate serp_google_organic_live_advanced --count 20
```

Validate skill frontmatter:

```bash
python scripts/validate_skills.py
```

## Data safety

Do not commit:

- `.env` files or credentials
- OAuth token files
- raw GSC/GA4/DataForSEO exports from real clients
- real client lead/enquiry data
- unredacted client reports
- private client configs unless this repo is deliberately kept private for that purpose

Use `.env.example` and sanitized examples instead.
