#!/usr/bin/env python3
"""Import biblischer Texte vom Toten Meer (Qumran, Murabbaʿat u. a.) aus ETCBC dss in die nicht kommerzielle
Studienschicht (data-nc/), mit maschinellem Vergleich zum Westminster Leningrad Codex.

Aufruf:
    pip install text-fabric
    python3 scripts/import_dss.py RUT OBA --dss PFAD/dss --dss-commit <sha> [--tf 2.0.1]
    python3 scripts/import_dss.py ISA PSA --dss PFAD/dss --dss-commit <sha> --macula PFAD/macula-hebrew --macula-commit <sha>
    (Bücher ohne WLC-Tokenschicht: Vergleichstext direkt aus MACULA Hebrew WLC/lowfat, umgerechnet wie beim Tokenimport)

Quelle: github.com/ETCBC/dss (Text-Fabric, Daten von Martin G. Abegg Jr., James E. Bowley, Edward M. Cook),
Lizenz CC BY-NC 4.0 – deshalb ausschliesslich in data-nc/ (LIZENZEN.md). Kerndaten verweisen nicht hierher.

Ausgabe:
    data-nc/witnesses/WIT-DSS-<ROLLE>.json                   Zeuge (Rolle bzw. Handschrift)
    data-nc/witness-texts/DSS-<ROLLE>-<BUCH>.json            Text je Vers mit Fundort (Fragment, Zeile) und Vergleich
Text: Buchstaben, die die Herausgeber ergänzt haben (in der Rolle nicht erhalten), stehen in eckigen Klammern; ganz
ergänzte Wörter sind keine Bezeugung. Vergleich: Wörter der Rolle werden mit den Wörtern des WLC ausgerichtet
(difflib, Konsonanten, Endbuchstaben normalisiert). Einstufung je Wort: same (gleiche Konsonanten), spelling (gleich,
wenn man die Lesehilfen ו und י im Wortinnern weglässt bzw. die lange Suffixform -כה/-תה: Schreibweise, keine andere Lesart),
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
         "Mur88": "MurXII (Mur 88)",
         # Jesaja und Psalmen (übliche Sigla nach DJD; KI-Zusammenstellung, ungeprüft)
         "1Qisaa": "1QIsa a (grosse Jesaja-Rolle)", "1Q8": "1QIsa b", "5Q3": "5QIsa", "Mur3": "MurIsa (Mur 3)",
         "4Q55": "4QIsa a", "4Q56": "4QIsa b", "4Q57": "4QIsa c", "4Q58": "4QIsa d", "4Q59": "4QIsa e", "4Q60": "4QIsa f", "4Q61": "4QIsa g", "4Q62": "4QIsa h", "4Q62a": "4QIsa i", "4Q63": "4QIsa j", "4Q64": "4QIsa k", "4Q65": "4QIsa l", "4Q66": "4QIsa m", "4Q67": "4QIsa n", "4Q68": "4QIsa o", "4Q69": "4QIsa p", "4Q69a": "4QIsa q", "4Q69b": "4QIsa r",
         "11Q5": "11QPs a (grosse Psalmenrolle)", "11Q6": "11QPs b", "11Q7": "11QPs c", "11Q8": "11QPs d", "11Q9": "11QPs e",
         "1Q10": "1QPs a", "1Q11": "1QPs b", "1Q12": "1QPs c", "2Q14": "2QPs", "3Q2": "3QPs", "5Q5": "5QPs", "6Q5": "pap6QPs",
         "8Q2": "8QPs", "5/6hev1b": "5/6ḤevPs", "Mas1e": "MasPs a", "Mas1f": "MasPs b",
         "4Q83": "4QPs a", "4Q84": "4QPs b", "4Q85": "4QPs c", "4Q86": "4QPs d", "4Q87": "4QPs e", "4Q88": "4QPs f", "4Q89": "4QPs g", "4Q90": "4QPs h", "4Q91": "4QPs j", "4Q92": "4QPs k", "4Q93": "4QPs l", "4Q94": "4QPs m", "4Q95": "4QPs n", "4Q96": "4QPs o", "4Q97": "4QPs p", "4Q98": "4QPs q", "4Q98a": "4QPs r", "4Q98b": "4QPs s", "4Q98c": "4QPs t", "4Q98d": "4QPs u", "4Q98e": "4QPs v", "4Q98f": "4QPs w", "4Q98g": "4QPs x"}
PLACES = {"Mur": "Wadi Murabbaʿat", "Hev": "Naḥal Ḥever", "Mas": "Masada"}
FINAL = str.maketrans("ךםןףץ", "כמנפצ")
LICENSE = "CC BY-NC 4.0 (Creative Commons Attribution-NonCommercial 4.0 International)"
ATTR = ("Dead Sea Scrolls data by Martin G. Abegg Jr., James E. Bowley and Edward M. Cook; Text-Fabric conversion by "
        "Jarod Jacobs, Martijn Naaijer and Dirk Roorda (ETCBC/CACCHT), https://github.com/ETCBC/dss")


def cons(s):
    s = unicodedata.normalize("NFD", s or "")
    return "".join(ch for ch in s if "א" <= ch <= "ת").translate(FINAL)


def no_matres(s):
    """Lesehilfen ו/י im Wortinnern weglassen (am Wortanfang ist ו meist «und» und zählt); lange Suffixformen
    -כה/-תה wie -כ/-ת (in Qumran häufige Schreibweise)."""
    s = s[:1] + s[1:].replace("ו", "").replace("י", "")
    return s[:-1] if len(s) > 2 and s[-1] == "ה" and s[-2] in "כת" else s


def place_of(scroll):
    for k, v in PLACES.items():
        if k.lower() in scroll.lower():
            return v
    m = re.match(r"(\d+)Q", scroll)
    return f"Qumran, Höhle {m.group(1)}" if m else "Fundort laut Edition"


def macula_words(book, macula):
    """Ohne Tokenschicht: ({ref: [konsonanten je wort]} in Navigationszählung, hebräische Stelle -> Navigationsstelle)
    aus MACULA Hebrew WLC/lowfat; Umrechnung wie scripts/import_macula_hebrew_book.py (scripts/versification.py)."""
    import xml.etree.ElementTree as ET
    import versification
    from ot_books import FILES
    files = sorted((macula / "WLC" / "lowfat").glob(f"{FILES[book]}-*-lowfat.xml"))
    if not files:
        sys.exit(f"ERROR: {book}: keine MACULA-Dateien unter {macula}")
    words = {}
    for f in files:
        for w in ET.fromstring(f.read_bytes()).iter("w"):
            m = re.fullmatch(r"([1-3]?[A-Z]{2,3}) (\d+):(\d+)!(\d+)", w.attrib["ref"])
            ref = f"{book}.{int(m.group(2))}.{int(m.group(3))}"
            ws = words.setdefault(ref, {})
            ws[int(m.group(4))] = ws.get(int(m.group(4)), "") + unicodedata.normalize("NFC", w.text or "")
    verses = {r: [ws[k] for k in sorted(ws)] for r, ws in words.items()}
    plan, _ = versification.heb_to_kjv(book, verses)
    out = {dst: [cons(verses[src][i]) for src, i, _ in items]
           for dst, items in versification.apply(book, verses, plan).items()}
    first = {src: parts[0][0] for src, parts in plan.items()}
    return out, (lambda r: first.get(r, r))


def wlc_words(book):
    """{ref: [konsonanten je wort]} aus data/tokens/WLC-<BUCH>-*.json (Navigationszählung)."""
    out = {}
    files = sorted((ROOT / "data/tokens").glob(f"WLC-{book}-*.json"))
    if not files:
        return None
    for p in files:
        for t in json.loads(p.read_text(encoding="utf-8"))["tokens"]:
            ws = out.setdefault(t["reference"], {})
            ws[t["word_no"]] = ws.get(t["word_no"], "") + cons(t["word"])
    return {r: [ws[k] for k in sorted(ws)] for r, ws in out.items()}


def align_block(a, b, i1, i2, j1, j2, gap=.55):
    """Ungleich lange Ersetzungsblöcke: Wörter nach Ähnlichkeit ausrichten (statt nach Position), damit ein
    zusätzliches Wort der Rolle (z. B. «Licht» in Jes 53,11) die folgenden Wörter nicht verschiebt."""
    def cost(x, y):
        if no_matres(x) == no_matres(y):
            return 0
        return 1 - difflib.SequenceMatcher(a=x, b=y, autojunk=False).ratio()
    n, m = i2 - i1, j2 - j1
    D = [[0.0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        D[i][0] = i * gap
    for j in range(1, m + 1):
        D[0][j] = j * gap
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            D[i][j] = min(D[i - 1][j - 1] + cost(a[i1 + i - 1], b[j1 + j - 1]), D[i - 1][j] + gap, D[i][j - 1] + gap)
    out, i, j = {}, n, m
    while i > 0:
        if j > 0 and D[i][j] == D[i - 1][j - 1] + cost(a[i1 + i - 1], b[j1 + j - 1]):
            out[i1 + i - 1] = j1 + j - 1 if cost(a[i1 + i - 1], b[j1 + j - 1]) < 1 else None
            i, j = i - 1, j - 1
        elif D[i][j] == D[i - 1][j] + gap:
            out[i1 + i - 1] = None
            i -= 1
        else:
            j -= 1
    return out


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
    ap.add_argument("--macula", type=pathlib.Path, help="für Bücher ohne WLC-Tokenschicht")
    ap.add_argument("--macula-commit")
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
        compare_src = {"text": "data/tokens (WLC)"}
        if wlc is not None:
            to_nav = heb_map(book, True)
        else:
            if not (a.macula and a.macula_commit and re.fullmatch(r"[0-9a-f]{40}", a.macula_commit)):
                sys.exit(f"ERROR: {book}: keine WLC-Tokenschicht; --macula und --macula-commit (40-stellige SHA) angeben")
            wlc, to_nav = macula_words(book, a.macula)
            compare_src = {"text": "MACULA Hebrew WLC/lowfat (Westminster Leningrad Codex)",
                           "url": "https://github.com/Clear-Bible/macula-hebrew", "upstream_commit": a.macula_commit,
                           "note_de": "Vergleichstext direkt aus MACULA gelesen (keine Tokenschicht im Kern); "
                                      "Navigationszählung nach scripts/versification.py"}
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
                dss_c = [i[1] for i in items]
                for tag, i1, i2, j1, j2 in sm.get_opcodes():
                    if tag == "equal" or (tag == "replace" and i2 - i1 == j2 - j1):
                        for k in range(i1, i2):
                            match[k] = j1 + (k - i1)
                    elif tag == "replace":
                        match.update(align_block(dss_c, mt, i1, i2, j1, j2))
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
                                            "im Wortinnern bzw. lange Suffixform anders (Schreibweise), partial = nur teilweise "
                                            "erhalten, differs = andere Konsonanten, extra = im WLC nicht "
                                            "vorhanden, reconstructed = ganz ergänzt (keine Bezeugung). Nicht am "
                                            "Faksimile geprüft; Ergänzungen der Herausgeber folgen oft dem "
                                            "masoretischen Text."),
                   "verification_de": "Sekundärtranskription (Abegg u. a.); nicht am Faksimile geprüft.",
                   "compare_text": compare_src, "counts": counts, "verses": out_verses}
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
