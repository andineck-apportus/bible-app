"""Offline-Tests des Importers mit synthetischen Tokens (KEINE biblischen Quelldaten).

Das Zeilenformat entspricht dem echten MorphGNT-Format (Referenz BBCCVV, Markus = 02),
abgeglichen mit 62-Mk-morphgnt.txt aus MorphGNT 6.12.
"""
from pathlib import Path
import json
import shutil
import subprocess
import sys
import tempfile

root = Path(__file__).resolve().parents[1]
COMMIT = "0" * 40


def run(sandbox, source, *extra):
    return subprocess.run([sys.executable, str(sandbox / "scripts/import_morphgnt.py"), str(source), *extra],
                          capture_output=True, text=True)


with tempfile.TemporaryDirectory() as temp:
    sandbox = Path(temp) / "repo"
    (sandbox / "scripts").mkdir(parents=True)
    shutil.copy(root / "scripts/import_morphgnt.py", sandbox / "scripts/import_morphgnt.py")
    source = Path(temp) / "fixture.txt"
    line = "N- ----NSF- ΔΟΚΙΜΗ, ΔΟΚΙΜΗ ΔΟΚΙΜΗ δοκιμή\n"
    other = "".join(f"0203{v:02d} {line}" for v in (21, 31)) + f"010322 {line}"  # ausserhalb des Umfangs
    source.write_text(other + "".join(f"0203{v:02d} {line}" for v in range(22, 31)), encoding="utf-8")

    result = run(sandbox, source, "--upstream-commit", COMMIT, "--upstream-ref", "test")
    assert result.returncode == 0, (result.stdout, result.stderr)
    data = json.loads((sandbox / "data/tokens/SBLGNT-MRK-003-022-030.json").read_text())
    assert len(data["tokens"]) == 9
    assert data["tokens"][0]["reference"] == "MRK.3.22" and data["tokens"][-1]["reference"] == "MRK.3.30"
    assert data["tokens"][0]["text"] == "ΔΟΚΙΜΗ," and data["tokens"][0]["word"] == "ΔΟΚΙΜΗ"
    assert len(data["source"]["sha256"]) == 64 and data["source"]["upstream_commit"] == COMMIT
    counts = json.loads((sandbox / "data/counts/SBLGNT-MRK-003-022-030.json").read_text())
    assert counts["token_count"] == 9 and counts["unique_lemmas"] == 1

    # Ohne Upstream-Commit wird nichts geschrieben
    assert run(sandbox, source).returncode != 0
    # Altes, falsches Referenzformat (6203xx) wird nicht als Markus erkannt
    source.write_text("".join(f"6203{v:02d} {line}" for v in range(22, 31)), encoding="utf-8")
    assert run(sandbox, source, "--upstream-commit", COMMIT).returncode != 0
    # Unvollständige Verse werden abgelehnt
    source.write_text(f"020322 {line}", encoding="utf-8")
    assert run(sandbox, source, "--upstream-commit", COMMIT).returncode != 0
    # Fehlerhafte Zeilen werden abgelehnt
    source.write_text("".join(f"0203{v:02d} N- ----NSF- ΔΟΚΙΜΗ\n" for v in range(22, 31)), encoding="utf-8")
    assert run(sandbox, source, "--upstream-commit", COMMIT).returncode != 0

print("PASS: synthetic importer tests (real MorphGNT line format, pinned source, rejects unpinned/incomplete/malformed input)")
