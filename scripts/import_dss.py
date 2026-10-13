#!/usr/bin/env python3
"""Import biblischer Texte vom Toten Meer (Qumran, Murabbaʿat u. a.) aus ETCBC dss in die nicht kommerzielle
Studienschicht (data-nc/), mit maschinellem Vergleich zum Westminster Leningrad Codex.

Aufruf:
    pip install text-fabric
    python3 scripts/import_dss.py RUT OBA --dss PFAD/dss --dss-commit <sha> [--tf 2.0.1]

Quelle: github.com/ETCBC/dss (Text-Fabric, Daten von Martin G. Abegg Jr., James E. Bowley, Edward M. Cook),
Lizenz CC BY-NC 4.0 – deshalb ausschliesslich in data-nc/ (LIZENZEN.md). Kerndaten verweisen nicht hierher.

Ausgabe:
    data-nc/witnesses/WIT-DSS-<ROLLE>.json                   Zeuge (Rolle bzw. Handschrift)
    data-nc/witness-texts/DSS-<ROLLE>-<BUCH>.json            Text je Vers mit Fundort (Fragment, Zeile) und Vergleich
Text: Buchstaben, die die Herausgeber ergänzt haben (in der Rolle nicht erhalten), stehen in eckigen Klammern; ganz
ergänzte Wörter sind keine Bezeugung. Vergleich: Wörter der Rolle werden mit den Wörtern des WLC ausgerichtet
(difflib, Konsonanten, Endbuchstaben normalisiert). Einstufung je Wort: same (gleiche Konsonanten), spelling (gleich,
wenn man die Lesehilfen ו und י weglässt bzw. die lange Suffixform -כה/-תה: Schreibweise, keine andere Lesart),
partial (nur Anfang oder Ende des Worts erhalten), differs (andere Konsonanten),
extra (Wort fehlt im WLC), reconstructed (ganz ergänzt, nicht verglichen). Maschinell, nicht am Faksimile geprüft.
Verszählung: Die Rollen folgen der hebräischen Zählung; Bücher mit abweichender Zählung werden mit
scripts/versification.py umgerechnet (ganze Verse).
"""
import argparse
import datetime
import difflib
import hashlib
import json
import pathlib
import re
import sys
import unicodedata

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import refs  # noqa: E402

DSS_BOOK = {"GEN": "Gen", "EXO": "Ex", "LEV": "Lev", "NUM": "Num", "DEU": "Deut", "JOS": "Josh", "JDG": "Judg",
            "RUT": "Ruth", "1SA": "1Sam", "2SA": "2Sam", "1KI": "1Kgs", "2KI": "2Kgs", "2CH": "2Chr", "EZR": "Ezra",
            "JOB": "Job", "PSA": "Ps", "PRO": "Prov", "ECC": "Eccl", "SNG": "Song", "ISA": "Is", "JER": "Jer",
            "LAM": "Lam", "EZK": "Ezek", "DAN": "Dan", "HOS": "Hos", "JOL": "Joel", "AMO": "Amos", "OBA": "Obad",
            "JON": "Jonah", "MIC": "Mic", "NAM": "Nah", "HAB": "Hab", "ZEP": "Zeph", "HAG": "Hag", "ZEC": "Zech",
            "MAL": "Mal"}
# Übliche Bezeichnungen (Sigla) der Rollen; ohne Eintrag bleibt die Inventarnummer.
NAMES = {"2Q16": "2QRuth a", "2Q17": "2QRuth b", "4Q104": "4QRuth a", "4Q105": "4QRuth b", "4Q82": "4QXII g", "4Q76": "4QXII a", "4Q81": "4QXII f",
         "Mur88": "MurXII (Mur 88)"}
PLACES = {"Mur": "Wadi Murabbaʿat", "Hev": "Naḥal Ḥever", "Mas": "Masada"}
FINAL = str.maketrans("ךםןףץ", "כמנפצ")
LICENSE = "CC BY-NC 4.0 (Creative Commons Attribution-NonCommercial 4.0 International)"
ATTR = ("Dead Sea Scrolls data by Martin G. Abegg Jr., James E. Bowley and Edward M. Cook; Text-Fabric conversion by "
        "Jarod Jacobs, Martijn Naaijer and Dirk Roorda (ETCBC/CACCHT), https://github.com/ETCBC/dss")


def cons(s):
    s = unicodedata.normalize("NFD", s or "")
    return "".join(ch for ch in s if "א" <= ch <= "ת").translate(FINAL)


def no_matres(s):
    """Lesehilfen ו/י weglassen; lange Suffixformen -כה/-תה wie -כ/-ת (in Qumran häufige Schreibweise)."""
    s = s.replace("ו", "").replace("י", "")
    return s[:-1] if len(s) > 2 and s[-1] == "ה" and s[-2] in "כת" else s


def place_of(scroll):
    for k, v in PLACES.items():
        if k in scroll:
            return v
    m = re.match(r"(\d+)Q", scroll)
    return f"Qumran, Höhle {m.group(1)}" if m else "Fundort laut Edition"


def wlc_words(book):
    """{ref: [konsonanten je wort]} aus data/tokens/WLC-<BUCH>-*.json (Navigationszählung)."""
    out = {}
    files = sorted((ROOT / "data/tokens").glob(f"WLC-{book}-*.json"))
    if not files:
        sys.exit(f"ERROR: {book}: zuerst den WLC-Text importieren (scripts/import_macula_hebrew_book.py)")
    for p in files:
        for t in json.loads(p.read_text(encoding="utf-8"))["tokens"]:
            ws = out.setdefault(t["reference"], {})
            ws[t["word_no"]] = ws.get(t["word_no"], "") + cons(t["word"])
    return {r: [ws[k] for k in sorted(ws)] for r, ws in out.items()}


def heb_map(book, wlc_files_present):
    """Hebräische Stelle -> Navigationsstelle (ganze Verse). Ohne Abweichung: Identität."""
    if not wlc_files_present:
        return lambda r: r
    toks = []
    for p in sorted((ROOT / "data/tokens").glob(f"WLC-{book}-*.json")):
        toks += json.loads(p.read_text(encoding="utf-8"))["tokens"]
    m = {t.get("source_reference", t["reference"]): t["reference"] for t in toks}
    return lambda r: m.get(r, r)


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("books", nargs="+", choices=sorted(DSS_BOOK))
    ap.add_argument("--dss", type=pathlib.Path, required=True)
    ap.add_argument("--dss-commit", required=True)
    ap.add_argument("--tf", default="2.0.1")
    a = ap.parse_args()
    if not re.fullmatch(r"[0-9a-f]{40}", a.dss_commit):
        sys.exit("ERROR: --dss-commit muss eine vollständige 40-stellige Git-SHA sein")
    from tf.fabric import Fabric
    loc = a.dss / "tf" / a.tf
    api = Fabric(locations=str(loc), silent="deep").load(
        "scroll fragment line book chapter verse glyph rec after type", silent="deep")
    F, L = api.F, api.L
    digest = hashlib.sha256()
    for name in ("otext", "oslots", "book", "chapter", "verse", "glyph", "rec", "after", "scroll", "fragment", "line"):
        digest.update((loc / f"{name}.tf").read_bytes())
    today = datetime.date.today().isoformat()
    nc = ROOT / "data-nc"
    report = {}
    for book in a.books:
        wlc = wlc_words(book)
        to_nav = heb_map(book, True)
        per = {}  # rolle -> ref -> liste von [anzeige, konsonanten, erhaltene buchstaben, fundort]
        skipped = []
        pending = None
        for w in F.otype.s("word"):
            if F.book.v(w) != DSS_BOOK[book]:
                continue
            ch, vs = F.chapter.v(w), F.verse.v(w)
            if not (ch and vs and str(ch).isdigit() and str(vs).isdigit()):
                skipped.append(f"{F.scroll.v(L.u(w, 'scroll')[0])} {ch}:{vs}")
                continue
            if F.type.v(w) != "glyph":
                continue
            ref = to_nav(f"{book}.{int(ch)}.{int(vs)}")
            refs.parse(ref)
            scroll = F.scroll.v(L.u(w, "scroll")[0])
            where = f"{F.fragment.v(L.u(w, 'fragment')[0])} {F.line.v(L.u(w, 'line')[0])}"
            disp, kept, inbr = "", 0, False
            for s in L.d(w, "sign"):
                g = F.glyph.v(s) or ""
                if not g or not cons(g):
                    continue
                r = bool(F.rec.v(s))
                if r and not inbr:
                    disp += "["
                if not r and inbr:
                    disp += "]"
                inbr = r
                disp += g
                kept += 0 if r else 1
            if inbr:
                disp += "]"
            item = [disp, cons(F.glyph.v(w) or ""), kept, where]
            if pending and pending[0] == (scroll, ref):  # Vorsilbe ohne Leerzeichen an das nächste Wort hängen
                p = pending[1]
                item = [p[0] + item[0], p[1] + item[1], p[2] + item[2], p[3]]
            elif pending:
                per.setdefault(pending[0][0], {}).setdefault(pending[0][1], []).append(pending[1])
            pending = ((scroll, ref), item) if F.after.v(w) is None else None
            if pending is None:
                per.setdefault(scroll, {}).setdefault(ref, []).append(item)
        stats = {}
        for scroll, verses in sorted(per.items()):
            wid = f"WIT-DSS-{re.sub(r'[^A-Za-z0-9]', '', scroll).upper()}"
            wpath = nc / "witnesses" / f"{wid}.json"
            if not wpath.exists():
                wpath.parent.mkdir(parents=True, exist_ok=True)
                wpath.write_text(json.dumps({
                    "id": wid, "type": "witness", "status": "draft", "tags": ["TAG-TEXT-CRITICISM"],
                    "symbol": NAMES.get(scroll, scroll), "name_de": NAMES.get(scroll, scroll), "inventory": scroll,
                    "material_de": "Leder bzw. Pergament (Rolle)", "languages": ["he"], "location_de": place_of(scroll),
                    "date_de": "Zeit des Zweiten Tempels bis Anfang 2. Jh. n. Chr. (Fundgruppe); Einzeldatierung nicht geprüft",
                    "about_de": "Hebräische Bibelhandschrift aus der Wüste Juda, rund tausend Jahre älter als der Codex Leningradensis.",
                    "authorship_de": f"Metadaten zusammengestellt {today} (KI-Entwurf, Claude); ungeprüft."},
                    ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
            out_verses, counts = {}, {"same": 0, "spelling": 0, "partial": 0, "differs": 0, "extra": 0, "reconstructed": 0}
            for ref in sorted(verses, key=lambda r: tuple(int(x) for x in r.split(".")[1:])):
                items = verses[ref]
                mt = wlc.get(ref, [])
                sm = difflib.SequenceMatcher(a=[i[1] for i in items], b=mt, autojunk=False)
                words = []
                match = {}
                for tag, i1, i2, j1, j2 in sm.get_opcodes():
                    for k in range(i1, i2):
                        j = j1 + (k - i1) if tag in ("equal", "replace") and j1 + (k - i1) < j2 else None
                        match[k] = j
                for k, (disp, cs, kept, where) in enumerate(items):
                    j = match.get(k)
                    if kept == 0:
                        st = "reconstructed"
                    elif j is None:
                        st = "extra"
                    elif cs == mt[j]:
                        st = "same"
                    elif no_matres(cs) == no_matres(mt[j]):
                        st = "spelling"
                    elif len(cs) < len(mt[j]) and (mt[j].startswith(cs) or mt[j].endswith(cs)):
                        st = "partial"
                    else:
                        st = "differs"
                    counts[st] += 1
                    e = {"t": disp, "s": st}
                    if st in ("spelling", "partial", "differs") and j is not None:
                        e["wlc"] = mt[j]
                    words.append(e)
                out_verses[ref] = {"loc": sorted({i[3] for i in items}), "words": words,
                                   "preserved_letters": sum(i[2] for i in items)}
            tid = f"DSS-{re.sub(r'[^A-Za-z0-9]', '', scroll).upper()}-{book}"
            rec = {"id": tid, "type": "witness_transcription", "status": "imported_unreviewed",
                   "tags": ["TAG-TEXT-CRITICISM"], "witness": wid, "bibliographic_source": "SRC-ETCBC-DSS",
                   "encoding": "ETCBC dss (Text-Fabric), Unicode; [ ] = von den Herausgebern ergänzt",
                   "imported_scope": [book], "verse_count": len(out_verses),
                   "source": {"url": "https://github.com/ETCBC/dss", "upstream_commit": a.dss_commit,
                              "path": f"tf/{a.tf}", "sha256_features": digest.hexdigest(), "license": LICENSE,
                              "attribution": ATTR, "import": {"tool": "scripts/import_dss.py", "imported_on": today}},
                   "comparison_method_de": ("Maschineller Vergleich mit dem Westminster Leningrad Codex: Wörter nach "
                                            "Konsonanten ausgerichtet; same = gleich, spelling = nur Lesehilfen ו/י "
                                            "bzw. lange Suffixform anders (Schreibweise), partial = nur teilweise "
                                            "erhalten, differs = andere Konsonanten, extra = im WLC nicht "
                                            "vorhanden, reconstructed = ganz ergänzt (keine Bezeugung). Nicht am "
                                            "Faksimile geprüft; Ergänzungen der Herausgeber folgen oft dem "
                                            "masoretischen Text."),
                   "verification_de": "Sekundärtranskription (Abegg u. a.); nicht am Faksimile geprüft.",
                   "counts": counts, "verses": out_verses}
            path = nc / "witness-texts" / f"{tid}.json"
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(json.dumps(rec, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
            stats[NAMES.get(scroll, scroll)] = (len(out_verses), counts)
        report[book] = {"scrolls": stats, "skipped": skipped}
    for book, r in report.items():
        print(f"PASS: {book}: " + "; ".join(f"{n}: {v} Verse, {c}" for n, (v, c) in r["scrolls"].items())
              + (f"; übersprungen (keine Verszahl): {len(r['skipped'])}" if r["skipped"] else ""))


if __name__ == "__main__":
    main()
