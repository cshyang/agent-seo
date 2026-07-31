# Brand and commercial lead-quality review prompt

Review whether this article sounds like SUA and attracts the right enquiries.

Return JSON only with:
- verdict: pass | revise | reject
- commercial_fit_score: 1-5
- style_fit_score: 1-5
- weak_lead_risks
- credibility_issues
- missing_business_context
- revision_instructions

Reject if the article is mainly residential, cheap/affordable, generic inspiration, repair/maintenance, or furniture-only.
