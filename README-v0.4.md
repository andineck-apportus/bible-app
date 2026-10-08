# Bible Knowledge v0.4 — reproducible import preparation

This release fixes the v0.3 importer format: generated token sets and count reports now have `id`, `type`, `status`, `tags` so the existing repository validator can read them. It also rejects malformed target lines, incomplete verse coverage, and records the SHA-256 digest of the input file. The source itself is not bundled or claimed to have been downloaded.

## Sources
- SBLGNT: https://github.com/Faithlife/SBLGNT (CC BY 4.0, check attribution requirements)
- MorphGNT: https://github.com/morphgnt/sblgnt (morphology CC BY-SA; consult repository license and provenance)

## Steps
1. Download `62-Mk-morphgnt.txt` from the MorphGNT repository at a known commit/release.
2. Record the commit SHA in the study/source metadata before accepting the import as reviewed.
3. `python scripts/import_morphgnt.py 62-Mk-morphgnt.txt`
4. `python scripts/validate.py`
5. Check the Greek text and morphological tags against the named editions. Do not confuse a critical edition with direct manuscript transcriptions.

## Tests
`python scripts/test_import.py` runs only **synthetic** input. No token counts for Mark 3:22–30 are asserted until the real source is imported.

## Next
Primary manuscript collations for Mark 3:29, translation alignment, explicit edition-version IDs, reviewed text count status, and scholarly references with locators.
