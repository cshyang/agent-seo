---
name: seo-content-drafting
description: "Draft a page from an approved content brief around one defensible position backed by first-hand client evidence — research before drafting, receipts under claims, verified quotes, and sections cut rather than filled."
version: 0.1.0
tags: [seo, geo, content, drafting, e-e-a-t]
---

# SEO Content Drafting

## When to use

Use when a brief produced by `seo-content-briefs` needs to become an actual page. Do not use to
originate topics — the brief is the gate, and the brief is downstream of report Section 7 demand
validation.

## Required reading (before writing anything)

1. The brief itself, from `.seo-ops/clients/<slug>/briefs/YYYY-MM-<topic-slug>.md`.
2. `templates/practitioner-interview-template.md` — what the client fact base is and how it is used.
3. The client fact base at `.seo-ops/clients/<slug>/interview.md` plus anything in
   `.seo-ops/clients/<slug>/sources/`.
4. `methodology/geo-ai-citability.md` — answer blocks and citability.
5. The client config for service area, brand terms, spelling and currency conventions.

## The failure this skill exists to prevent

A brief supplies an outline and forbids invented statistics. An agent given an outline, no research
step, and no client evidence has exactly one option left: fill the outline with words. The result is
fluent, correct, locally-flavoured and completely hollow — and no instruction to "write better"
fixes it, because the problem is structural, not stylistic.

Research and first-hand evidence are inputs. If they are missing, the draft cannot be rescued at the
writing stage.

## Hard rules

- **Research before drafting.** Before writing a sentence of prose, gather what a practitioner would
  actually cite: the governing standards and their numbers, the local regulatory position, real
  costs, the quantitative conventions of the field. Record what you found with sources and dates.
  If a number is not findable, say so — never substitute a plausible one.
- **One position per article.** The page must state something the client would defend in a meeting
  and a competitor might dispute. A summary of what everyone already agrees on is not a position.
- **Every position carries a receipt.** A claim only the client can make: the project, the number,
  the timeframe, the thing that went wrong, the practice they changed. Receipts come from the
  fact base — they are never invented and never inferred.
- **No receipt → `[NEEDS: <a question the client can answer in one line>]`.** Never hedge an
  unsupported claim into vague prose. Vagueness is how "no invented statistics" gets satisfied
  dishonestly.
- **A section with no facts gets cut, not filled.** The brief's outline is a hypothesis. Deleting a
  section is a successful outcome.
- **Word count is an output.** Never pad toward a target. Outline depth follows the ranking shape
  recorded in the brief, per `templates/content-brief-template.md`.
- **Quotes are evidence, not authority.** Cite an outside source where it supplies proof the client
  cannot. A page that is mostly other people's words positions *them* as the expert.
- **Never fabricate a quote, a name, or an attribution.** Quote only text you retrieved and saved to
  `.seo-ops/clients/<slug>/sources/`. Reproduce it exactly, including typos and awkward grammar —
  never tidy a quote. Misattributing words to a named professional is the most damaging thing this
  pipeline can do.
- **Locale is checked, not mentioned.** Units, currency, spelling, date format and named local
  instruments must match the client config. If the page reads identically with a different country
  swapped in, the localisation has failed.
- **No fabricated E-E-A-T.** Inherited from `seo-content-briefs` and absolute.

## Do not bother with

Style rules. Sentence-rhythm variation, avoiding stock openers, limiting three-item lists,
suppressing hype adjectives — a competent model handles all of this unprompted, and rules about it
crowd out the rules that matter. Spend the instruction budget on evidence, not prose texture.

## Workflow

1. Read the brief, the client fact base, and the client config.
2. **Research.** Standards, codes, local mechanics, real costs. Save retrieved source text to
   `.seo-ops/clients/<slug>/sources/`. Record dates and editions.
3. **Choose the position.** One sentence. Write it down before drafting anything else. If you cannot
   find one the client would defend, stop and say so — the brief may need a different angle.
4. **Attach the receipt** from the fact base. If none exists, mark `[NEEDS:]` and continue.
5. Draft. Cut any outline section that has neither a fact nor a receipt behind it.
6. Write the answer block per `methodology/geo-ai-citability.md`.
7. Verify (below).
8. Route through `workflows/implementation-handoff.md`. Client-facing content is never published
   without client approval.

## Output location

`.seo-ops/clients/<slug>/briefs/` alongside the source brief. Never write client drafts into the
repo tree.

## Verification

- Run `python scripts/qa_draft.py <draft.md> --sources .seo-ops/clients/<slug>/sources/`.
  Every quoted passage must string-match a saved source file. An unmatched quote blocks handoff.
  PDFs are extracted automatically via `pdftotext` (requires poppler); save standards, journal
  articles and guidance documents as the original PDF rather than a summary of it.
- **Check source currency.** A real standard cited in a superseded edition passes every automated
  check and is still wrong. Confirm the edition year of every standard, code and guideline named.
- Confirm no unresolved `[NEEDS:]` markers remain in a delivered draft.
- Confirm the position is stated explicitly and carries a receipt.
