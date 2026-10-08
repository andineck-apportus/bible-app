# Bible Knowledge v0.1 — pilot Mark 3:22–30

Git-first, structured knowledge prototype. All study assertions are **provisional**, not a verified critical apparatus. The pilot deliberately distinguishes textual observations, interpretations, principles and context-dependent applications.

## Model conventions
- Stable IDs and typed references; each record has `tags` (multiple controlled tag IDs).
- `knowledge` records when an assertion was made; `context.period` describes the period being studied or addressed.
- Git history preserves edits; substantive changes to a claim should create a new version with `supersedes`.
- Source-language text is **not** reconstructed here; manuscript readings and token counts must be imported from verified licensed/open datasets with edition and witness provenance.
- `status: draft` signals a working hypothesis, not a finished study.

## Quick start
`python3 scripts/validate.py`

## Next
1. Add source/edition/witness identifiers and attested readings with precise citations.
2. Import a licensed tokenized Greek text and aligned translation, then compute reproducible word counts.
3. Add argument/evidence records and compare competing interpretations.
4. Generate SQLite as a read-only index, leaving Git as source of truth.
