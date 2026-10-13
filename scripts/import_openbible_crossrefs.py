#!/usr/bin/env python3
"""Import der Querverweise von OpenBible.info (Treasury of Scripture Knowledge u. a., mit Stimmen).

Aufruf:
    python3 scripts/import_openbible_crossrefs.py PFAD/cross_references.txt --source-url URL --upstream-commit SHA

Quelle: https://www.openbible.info/labs/cross-references/ (CC BY), hier über die Kopie in
github.com/scrollmapper/bible_databases (sources/extras/cross_references.txt). Format: «Von  Nach  Stimmen»,
OSIS-Stellen, KJV-Versifikation. Die Stimmen sind Nutzerbewertungen der Relevanz (auch negativ) und
keine fachliche Prüfung.

Ausgabe: data/crossrefs/XREF-OPENBIBLE-<BUCH>.json (je Ausgangsbuch), Stellen kanonisch (USFM),
Verweise je Vers nach Stimmen absteigend sortiert. Eintrag: [Ziel, Stimmen] bzw. [Ziel, Stimmen, "split_cross_book"],
wenn ein Zielbereich über eine Buchgrenze reichte und deshalb in zwei Bereiche geteilt wurde.
"""
import argparse
import datetime
import hashlib
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import refs  # noqa: E402

OSIS = dict(zip(
    "Gen Exod Lev Num Deut Josh Judg Ruth 1Sam 2Sam 1Kgs 2Kgs 1Chr 2Chr Ezra Neh Esth Job Ps Prov Eccl Song Isa Jer Lam Ezek Dan "
    "Hos Joel Amos Obad Jonah Mic Nah Hab Zeph Hag Zech Mal Matt Mark Luke John Acts Rom 1Cor 2Cor Gal Eph Phil Col 1Thess 2Thess "
    "1Tim 2Tim Titus Phlm Heb Jas 1Pet 2Pet 1John 2John 3John Jude Rev".split(),
    "GEN EXO LEV NUM DEU JOS JDG RUT 1SA 2SA 1KI 2KI 1CH 2CH EZR NEH EST JOB PSA PRO ECC SNG ISA JER LAM EZK DAN "
    "HOS JOL AMO OBA JON MIC NAM HAB ZEP HAG ZEC MAL MAT MRK LUK JHN ACT ROM 1CO 2CO GAL EPH PHP COL 1TH 2TH "
    "1TI 2TI TIT PHM HEB JAS 1PE 2PE 1JN 2JN 3JN JUD REV".split()))

ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
ap.add_argument("file", type=pathlib.Path)
ap.add_argument("--source-url", required=True)
ap.add_argument("--upstream-commit", required=True)
args = ap.parse_args()
if not re.fullmatch(r"[0-9a-f]{40}", args.upstream_commit):
    sys.exit("ERROR: --upstream-commit muss eine vollständige Git-SHA sein")


def conv(osis):
    def one(p):
        b, c, v = p.split(".")
        return f"{OSIS[b]}.{int(c)}.{int(v)}"
    parts = osis.split("-")
    out = "-".join(one(p) for p in parts)
    refs.parse(out)
    return out


NAV = json.loads((ROOT / "data/navigation/NAV-PROT66-KJV.json").read_text(encoding="utf-8"))
LAST = {b["code"]: (len(b["verses_per_chapter"]), b["verses_per_chapter"][-1]) for b in NAV["books"]}


def targets(osis):
    """Bereiche über eine Buchgrenze werden in zwei Bereiche geteilt (Ende des ersten, Anfang des zweiten Buchs)."""
    parts = osis.split("-")
    if len(parts) == 2 and parts[0].split(".")[0] != parts[1].split(".")[0]:
        a, z = conv(parts[0]), conv(parts[1])
        b = a.split(".")[0]
        c, v = LAST[b]
        first = a if a == f"{b}.{c}.{v}" else f"{a}-{b}.{c}.{v}"
        zb = z.split(".")[0]
        second = z if z == f"{zb}.1.1" else f"{zb}.1.1-{z}"
        refs.parse(first); refs.parse(second)
        return [first, second], True
    return [conv(osis)], False


raw = args.file.read_bytes()
lines = raw.decode("utf-8").splitlines()
header = lines[0]
by_book, n, bad = {}, 0, []
for line in lines[1:]:
    if not line.strip():
        continue
    frm, to, votes = line.split("\t")
    try:
        f, (ts, split) = conv(frm), targets(to)
    except (KeyError, ValueError, refs.RefError) as exc:
        bad.append((line, str(exc)))
        continue
    for t in ts:
        by_book.setdefault(f.split(".")[0], {}).setdefault(f, []).append([t, int(votes)] + (["split_cross_book"] if split else []))
    n += 1
if bad:
    sys.exit(f"ERROR: {len(bad)} Zeilen nicht lesbar, z. B. {bad[:3]}")
out = ROOT / "data/crossrefs"
out.mkdir(parents=True, exist_ok=True)
today = datetime.date.today().isoformat()
sha = hashlib.sha256(raw).hexdigest()
for book, entries in sorted(by_book.items()):
    for k in entries:
        entries[k].sort(key=lambda x: (-x[1], x[0]))
    rec = {"id": f"XREF-OPENBIBLE-{book}", "type": "crossref_set", "status": "imported_unreviewed", "tags": [],
           "book": book, "versification": "KJV",
           "source": {"title": "OpenBible.info Cross References", "url": "https://www.openbible.info/labs/cross-references/",
                      "copy_url": args.source_url, "path": "sources/extras/cross_references.txt",
                      "upstream_commit": args.upstream_commit, "sha256": sha, "header": header,
                      "license": "CC BY (OpenBible.info)", "attribution": "Cross references: OpenBible.info, CC BY",
                      "imported_at": today},
           "votes_note_de": "Stimmen sind Relevanzbewertungen von Nutzern der Website (auch negativ), keine fachliche Prüfung.",
           "entries": dict(sorted(entries.items(), key=lambda kv: [int(x) for x in kv[0].split(".")[1:]]))}
    (out / f"{rec['id']}.json").write_text(json.dumps(rec, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")
print(f"PASS: {n} Querverweise in {len(by_book)} Büchern -> data/crossrefs/")
