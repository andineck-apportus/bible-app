# Bible Knowledge v0.5 — variant and translation alignment pilot

New objects: `variant` (additional ἐστιν/ἔσται locus), `alignment`, `translation`, `editorial_decision`. The original v0.4 dataset is preserved.

## Evidence status
- Witness claims have been compared with a publicly accessible **secondary transcription**, not independently inspected manuscript images.
- The source text of Mk 3:29–30 remains a working transcription. **No authoritative token or lemma counts are claimed.**
- The alignment is phrase-based; it is not yet a full token-by-token alignment.
- The preferred reading is a reasoned, revisable decision, not a source fact.
- Manuscript variants in the whole passage have **not** been exhaustively collated.

## Next steps
1. Supply `62-Mk-morphgnt.txt` and run `python scripts/import_morphgnt.py ...`.
2. Verify manuscript readings from facsimiles and a critical apparatus, including correctors.
3. Build complete token-level alignments for all nine verses, with translation licensing.
4. Add JSON Schema per object and validation of cross-object relations.

## Sources
- https://github.com/morphgnt/sblgnt
- https://www.greeklab.org/interlinear.php?book=Mark&cap=3&verse=29
- https://tips.translation.bible/tip_source/bratcher-nida-1961/page/84/
