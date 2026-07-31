# Factual review prompt

Review factual risk using only provided sources/research notes.

Return JSON only with:
- verdict: pass | revise | reject
- unsupported_claims
- claims_needing_source
- claims_to_remove
- safe_rewrites

Do not validate claims from model memory.
