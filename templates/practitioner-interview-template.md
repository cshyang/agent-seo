# Practitioner Interview — Template & Generation Spec

Version 0.1 · Run once per client at onboarding, refreshed when the business changes.
Output feeds every draft produced by `skills/seo-content-drafting`.
Sections marked `>> GEN:` are instructions for the operator — delete them from the stored fact base.

The purpose is **not** to collect quotable soundbites. It is to extract the positions the client
holds and the experience underneath them. A position without experience under it is an opinion any
model can generate; a position with a receipt attached is the only content a competitor cannot copy.

Store at `.seo-ops/clients/<slug>/interview.md` (gitignored — see AGENTS.md state convention).

---

# Practitioner Interview — `[CLIENT_NAME]`
Interviewer: `[NAME]` · Date: `[DATE]` · Duration: `[MM]` min · Recording: `[y/n]`

---

## 1. Positions

>> GEN: Ask one question at a time and let them talk. Do not move on until you have the story
>> underneath the claim — the project, the number, the year, what it cost. The claim alone is
>> worthless; the claim plus the receipt is the whole asset. Record answers verbatim where possible,
>> including hedges and self-corrections. Do not tidy their phrasing.

- What do you argue with other firms in your field about?
- What do most clients believe that is wrong?
- What did you used to believe that a job changed your mind about?
- What do you refuse to do, even when a client asks and is willing to pay?
- Where does the standard industry advice break down in Malaysian conditions specifically?

## 2. Receipts

>> GEN: These are the claims nobody else can make. Push for specificity: how many, how much, when,
>> what happened next. "Several projects" is not a receipt. "Two floors, back within eighteen
>> months, RM40k of masking they'd already paid to avoid" is.

- The most expensive mistake you have watched a client make more than once:
- A number you have measured yourself that surprised you:
- A job that went wrong and what you changed afterwards:
- What a competitor quotes for versus what you quote for, and why:
- The question a client should ask a supplier and never does:

## 3. Local conditions

- What is different about doing this work in Malaysia versus what the textbooks assume?
- Which local regulation, standard or authority actually governs, and is it mandatory or voluntary?
- Typical costs in RM, and what drives the variance:
- What does the local building stock / market / climate impose that overseas guidance ignores?

## 4. Vocabulary

>> GEN: Capture how they actually speak — the terms they use for their own services, what they call
>> their customers, the shorthand they use on site. This is the voice reference, and it is more
>> useful than any tone-of-voice document. Record raw; do not paraphrase into marketing language.

- Terms they use that the industry does not, or vice versa:
- What they call their customers:
- Phrases that recur across their answers:

## 5. Existing corpus

>> GEN: Zero client effort — collect what they have already written. This supplements the interview
>> and costs nothing. Save retrieved text to `.seo-ops/clients/<slug>/sources/`.

- [ ] Current site copy
- [ ] Quotes / proposals / scopes of work
- [ ] Replies to customer enquiries (WhatsApp, email)
- [ ] Google Business Profile review responses
- [ ] Past newsletters, LinkedIn posts, talks

## 6. Usage log

>> GEN: One line per article that draws on this fact base, so it is visible when the corpus is
>> running dry and needs a refresh interview.

| Date | Brief / page | Position used | Receipt used |
|---|---|---|---|
| | | | |

---

## Operating notes

- **Interview, do not survey.** A questionnaire sent to an SME comes back empty or generic. A
  recorded conversation where each answer is followed up produces usable material in 30–45 minutes.
- **Amortise.** One interview serves every article for that client. Top up with targeted
  `[NEEDS:]` questions raised by individual drafts rather than re-interviewing.
- **Reacting beats originating.** Clients who ignore a question list will answer "here is your
  draft, I need these four things to finish it." Send `[NEEDS:]` markers against real prose.
- **Never invent an answer.** An unanswered question stays `[NEEDS:]` and the claim stays out of the
  draft. A fabricated receipt is worse than a missing one.
