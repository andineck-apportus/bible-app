# Bible Knowledge v0.3 — edition-bound token pipeline

This package preserves the v0.2 pilot and adds a **reproducible importer** for Mark 3:22–30. It does **not** claim to contain a newly verified complete Greek text: upstream download could not be completed in this execution environment. Earlier working samples and manuscript attributions remain provisional.

## Reproduce

1. Download `62-Mk-morphgnt.txt` from https://github.com/morphgnt/sblgnt (version 6.12).
2. Run `python scripts/import_morphgnt.py 62-Mk-morphgnt.txt`.
3. Review `data/tokens/SBLGNT-MRK-003-022-030.json` and `data/counts/SBLGNT-MRK-003-022-030.json`.

The importer verifies coverage of all nine verses, keeps edition identity and source SHA-256, and counts by lemma. The script expects MorphGNT's seven whitespace-separated columns. The MorphGNT input uses book code `62` for Mark.

## Research status

- Edition provenance: established from publisher/repository descriptions.
- Full passage tokenization and count: **pending source import**.
- Manuscript readings/witness attributions: **provisional**, require inspection of primary transcriptions or apparatus.
- Translation alignment: **pending**.
- v0.2 pilot interpretations: exploratory, not source-certified.

## Attribution

SBLGNT, edited by Michael W. Holmes; © Society of Biblical Literature and Logos Bible Software, CC BY 4.0. MorphGNT SBLGNT Edition 6.12, J. K. Tauber, CC BY-SA for morphology/lemmatization. https://github.com/Faithlife/SBLGNT and https://github.com/morphgnt/sblgnt
