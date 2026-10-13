#!/usr/bin/env python3
"""Import freier Wörterbücher für die Wörter der importierten Bücher (Lexikon-Ansicht im Lesestrom).

Aufruf:
    python3 scripts/import_lexica.py --ubs PFAD/ubs-open-license --ubs-commit SHA --step PFAD/STEPBible-Data --step-commit SHA

Quellen (Lizenz je Datei geprüft am 2026-10-14, Prüfsummen unten fest eingetragen):
1. UBS Dictionary of the Greek New Testament (v1.1, englisch) und UBS Dictionary of Biblical Hebrew (v0.9.3, englisch),
   github.com/ubsicap/ubs-open-license, Ordner dictionaries/: **CC BY-SA 4.0** (LICENSE.md im Wurzelordner und in
   dictionaries/greek/ bzw. dictionaries/hebrew/, identischer Text, SHA-256 7abe19ec…). «UBS Dictionary of New Testament
   Greek, © United Bible Societies, 2023. Adapted from Semantic Dictionary of Biblical Greek: © United Bible Societies
   2018-2023, which is adapted from Greek-English Lexicon of the New Testament: Based on Semantic Domains, Eds. J P Louw,
   Eugene Albert Nida © United Bible Societies 1988, 1989.» bzw. «UBS Dictionary of Biblical Hebrew © United Bible
   Societies, 2023. Adapted from Semantic Dictionary of Biblical Hebrew © 2000-2023 United Bible Societies.»
   Hinweis: Diese Ausgaben stehen unter CC BY-SA 4.0. Die SDBH-/MARBLE-Felder in MACULA (sdbh, lexdomain, domain, ln …)
   sind dagegen nur «used with permission» und bleiben ausgeschlossen; übernommen wird hier nur die CC-BY-SA-Ausgabe.
2. STEPBible TBESG und TBESH (Translators Brief lexicon of Extended Strongs), github.com/STEPBible/STEPBible-Data,
   Ordner Lexicons/: CC BY 4.0. Übernommen werden Strong-Nummern, Grundform, Umschrift, Kurzgrammatik und die
   englische Kurzglosse (laut Kopf «created by Tyndale scholars»). **Nicht übernommen:** die Bedeutungsspalte von
   TBESH (Abridged BDB von Online Bible, © Larry Pierce; laut Dateikopf «Permission should be gained from Online Bible
   before these definitions are applied in any project») und die Definitionsspalte von TBESG (Abbott-Smith bzw.
   «MiddleLiddell»/ohne Herkunftsangabe; Herkunft je Eintrag nicht sicher frei, für eine Kurzansicht nicht nötig).

Umfang: nur Einträge für Lemmata bzw. Strong-Nummern, die in den importierten Büchern vorkommen (MACULA-Annotationen
in data/annotations/, dazu disambiguierte Strong-Nummern aus data/tagged-alignments/). Bei UBS werden die
Stellenangaben je Bedeutung auf die importierten Bücher beschränkt (als kanonische Stelle in der Zählung von UBS);
Fussnoten, Abbildungen, Kollokationen und Übersetzungen in andere Sprachen sind weggelassen.

Ausgabe: data/lexica/LEX-UBS-DGNT-GRC.json, LEX-UBS-DBH-HEB.json (CC BY-SA 4.0), LEX-STEP-TBESG-GRC.json,
LEX-STEP-TBESH-HEB.json (CC BY 4.0); Typ lexicon.
"""
import argparse
import datetime
import hashlib
import json
import pathlib
import re
import sys
import unicodedata

ROOT = pathlib.Path(__file__).resolve().parents[1]
D = ROOT / "data"
UBS_REPO = "https://github.com/ubsicap/ubs-open-license"
STEP_REPO = "https://github.com/STEPBible/STEPBible-Data"
UBS_LICENSE_SHA = "7abe19ec9bb73b36141b999b861d24ad855e808bafe0f81e84cce28556f6c297"
UBS = {
    "grc": ("dictionaries/greek/JSON/UBSGreekNTDic-v1.1-en.JSON", "d84bb9077a43fa4a4f7e571fe2ffa460fa655d7b78439b366281ce527fd56893",
            "dictionaries/greek/LICENSE.md", "LEX-UBS-DGNT-GRC", "UBS Dictionary of the Greek New Testament (v1.1, englisch)",
            "UBS Dictionary of New Testament Greek, © United Bible Societies, 2023. Adapted from Semantic Dictionary of "
            "Biblical Greek: © United Bible Societies 2018-2023, which is adapted from Greek-English Lexicon of the New "
            "Testament: Based on Semantic Domains, Eds. J P Louw, Eugene Albert Nida © United Bible Societies 1988, 1989. "
            "CC BY-SA 4.0."),
    "heb": ("dictionaries/hebrew/JSON/UBSHebrewDic-v0.9.3-en.JSON", "3ed1758438762b4fc5db311d1e75720c82ee70b871e09d9caed30d4c64138be8",
            "dictionaries/hebrew/LICENSE.md", "LEX-UBS-DBH-HEB", "UBS Dictionary of Biblical Hebrew (v0.9.3, englisch)",
            "UBS Dictionary of Biblical Hebrew © United Bible Societies, 2023. Adapted from Semantic Dictionary of "
            "Biblical Hebrew © 2000-2023 United Bible Societies. CC BY-SA 4.0."),
}
STEP = {
    "grc": ("Lexicons/TBESG - Translators Brief lexicon of Extended Strongs for Greek - STEPBible.org CC BY.txt",
            "312f723d7b8ef263bbdfb0451c9b8057125804dfff390b6f8544cff2a84b57f4", "LEX-STEP-TBESG-GRC",
            "STEPBible TBESG – Translators Brief lexicon of Extended Strongs for Greek"),
    "heb": ("Lexicons/TBESH - Translators Brief lexicon of Extended Strongs for Hebrew - STEPBible.org CC BY.txt",
            "464dccadd95fd8620dd05fa0d7a4caba58ec3c4d5db3ebf38e43d046ca25b591", "LEX-STEP-TBESH-HEB",
            "STEPBible TBESH – Translators Brief lexicon of Extended Strongs for Hebrew"),
}
STEP_ATTR = "Data created by www.STEPBible.org based on work at Tyndale House Cambridge (CC BY 4.0)"
N = lambda s: unicodedata.normalize("NFC", s or "")


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def book_codes():
    nav = json.loads((D / "navigation/NAV-PROT66-KJV.json").read_text(encoding="utf-8"))
    return [b["code"] for b in nav["books"]]


def scope():
    """Lemmata und Strong-Schlüssel der importierten Bücher; Bücher (USFM) je Sprache."""
    s = {"grc": {"lemmas": set(), "keys": set(), "books": set()}, "heb": {"lemmas": set(), "keys": set(), "books": set()}}
    for p in sorted((D / "annotations").glob("MACULA-SBLGNT-*.json")):
        r = json.loads(p.read_text(encoding="utf-8"))
        s["grc"]["books"].add(r["reference"].split(".")[0])
        for e in r["entries"].values():
            s["grc"]["lemmas"].add(N(e.get("lemma")))
            for part in (e.get("strong") or "").split("+"):
                if part.isdigit():
                    s["grc"]["keys"].add("G%04d" % int(part))
    for p in sorted((D / "annotations").glob("MACULA-WLC-*.json")):
        r = json.loads(p.read_text(encoding="utf-8"))
        s["heb"]["books"].add(r["reference"].split(".")[0])
        for e in r["entries"].values():
            s["heb"]["lemmas"].add(N(e.get("lemma")))
            m = re.match(r"^(\d+)([a-z]?)$", e.get("strongnumberx") or "")
            if m:
                s["heb"]["keys"].add("H%04d%s" % (int(m[1]), m[2]))
    dstrong = {"grc": set(), "heb": set()}
    for p in sorted((D / "tagged-alignments").glob("TALIGN-*.json")):
        r = json.loads(p.read_text(encoding="utf-8"))
        if r.get("kind") == "edition_presence":
            dstrong["grc"].update(e["dstrong"] for e in r["entries"].values() if e.get("dstrong"))
        else:
            dstrong["heb"].update(r.get("dstrong", {}).values())
    for lang in s:
        s[lang]["bases"] = {k.rstrip("abcdefghijklmnopqrstuvwxyz") for k in s[lang]["keys"]}
    return s, dstrong


def ubs_import(lang, path, commit, sc, codes, today):
    rel, digest, lic_rel, rid, title, attribution = UBS[lang]
    f = path / rel
    if sha(f) != digest:
        sys.exit(f"Prüfsumme von {rel} weicht ab; Quelle prüfen und Importer bewusst anpassen.")
    if sha(path / lic_rel) != UBS_LICENSE_SHA or sha(path / "LICENSE.md") != UBS_LICENSE_SHA:
        sys.exit("Lizenztext im UBS-Repository hat sich geändert; Lizenz erneut prüfen.")
    data = json.loads(f.read_text(encoding="utf-8-sig"))
    books = sc[lang]["books"]
    entries, ai = {}, 0
    for e in data:
        strong = [x for x in e.get("StrongCodes") or [] if x]
        # Strong-Nummern mit und ohne Buchstabenzusatz (UBS «H1350a», MACULA «1350»)
        bases = {x.rstrip("abcdefghijklmnopqrstuvwxyz") for x in strong}
        if (N(e["Lemma"]) not in sc[lang]["lemmas"] and not set(strong) & sc[lang]["keys"]
                and not bases & sc[lang]["keys"] and not set(strong) & sc[lang]["bases"]):
            continue
        senses, pos = [], []
        for bf in e.get("BaseForms") or []:
            pos += [p for p in bf.get("PartsOfSpeech") or [] if p and p not in pos]
            for m in bf.get("LEXMeanings") or []:
                en = next((x for x in m.get("LEXSenses") or [] if x.get("LanguageCode") == "en"), None)
                if not en:
                    continue
                occ = []
                for ref in m.get("LEXReferences") or []:
                    b, c, v = int(ref[0:3]), int(ref[3:6]), int(ref[6:9])
                    code = codes[b - 1] if 0 < b <= len(codes) else None
                    if code in books and c and v:
                        r = f"{code}.{c}.{v}"
                        if r not in occ:
                            occ.append(r)
                x = {"lexid": m["LEXID"], "code": m.get("LEXEntryCode") or None,
                     "domains": [d["Domain"] for d in m.get("LEXDomains") or [] if d.get("Domain")],
                     "subdomains": [d["Domain"] for d in m.get("LEXSubDomains") or [] if d.get("Domain")],
                     "definition": en.get("DefinitionShort") or "", "glosses": en.get("Glosses") or []}
                if en.get("DefinitionLong"):
                    x["definition_long"] = en["DefinitionLong"]
                if en.get("AIGenerated"):
                    x["ai_generated"] = True
                    ai += 1
                if occ:
                    x["occurrences"] = occ
                senses.append({k: v for k, v in x.items() if v not in (None, [], "")})
        if len(senses) == 1:
            senses[0].pop("occurrences", None)  # bei nur einer Bedeutung ohne Nutzen für die Zuordnung
        entries[e["MainId"]] = {"lemma": e["Lemma"], "strong": strong, "pos": pos, "senses": senses,
                                **({"authors": e["Authors"]} if e.get("Authors") else {})}
    rec = {"id": rid, "type": "lexicon", "status": "imported_unreviewed", "tags": [], "title": title,
           "language": "grc" if lang == "grc" else "hbo", "gloss_language": "en",
           "key": "UBS MainId; Zuordnung zu Tokens über Lemma bzw. Strong-Nummer (StrongCodes)",
           "source": {"repository": UBS_REPO, "commit": commit, "path": rel, "sha256": digest,
                      "license": "CC BY-SA 4.0", "license_file": lic_rel, "license_sha256": UBS_LICENSE_SHA,
                      "attribution": attribution,
                      "changes_de": "Nur Einträge für Lemmata/Strong-Nummern der importierten Bücher; je Bedeutung englische "
                                    "Kurzdefinition, Glossen, Bedeutungsfelder und – bei mehreren Bedeutungen – die Stellen in "
                                    "den importierten Büchern (Zählung von UBS, als kanonische Stelle); weggelassen: Kommentare, "
                                    "Fussnoten, Formen, "
                                    "Kollokationen, Bilder, Querverweise, kontextuelle Bedeutungen, Übersetzungen in andere "
                                    "Sprachen. Wortlaut der übernommenen Felder unverändert."},
           "license_note_de": ("Diese Datei steht als Bearbeitung unter CC BY-SA 4.0. Die SDBH- bzw. MARBLE-Felder in MACULA "
                               "(«used with permission») sind davon unabhängig und bleiben ausgeschlossen."),
           "scope_books": sorted(books), "counts": {"entries": len(entries), "senses": sum(len(x["senses"]) for x in entries.values()),
                                                    "ai_generated_senses": ai},
           "entries": entries,
           "import": {"tool": "scripts/import_lexica.py", "imported_on": today},
           "knowledge": {"asserted_at": today, "supersedes": None}}
    return rec


def step_import(lang, path, commit, sc, dstrong, today):
    rel, digest, rid, title = STEP[lang]
    f = path / rel
    if sha(f) != digest:
        sys.exit(f"Prüfsumme von {rel} weicht ab; Quelle prüfen und Importer bewusst anpassen.")
    keys = set(sc[lang]["keys"]) | {re.sub(r"[A-Z]$", "", d) for d in dstrong[lang]}
    keys_lower = {k.lower() for k in keys}
    entries = {}
    for line in f.read_text(encoding="utf-8-sig").split("\n"):
        if not re.match(r"^[GH]\d{4}", line):
            continue
        c = line.rstrip("\r").split("\t") + [""] * 8
        est = c[0].strip()
        dst, _, rel_txt = c[1].partition("=")
        if est.lower() not in keys_lower and re.sub(r"[a-z]$", "", est) not in keys and dst.strip() not in dstrong[lang]:
            continue
        e = {"estrong": est, "ustrong": c[2].strip(), "lemma": c[3].strip(), "translit": c[4].strip(),
             "morph": c[5].strip(), "gloss": c[6].strip()}
        if rel_txt.strip():
            e["relation"] = rel_txt.strip()
        entries[dst.strip()] = {k: v for k, v in e.items() if v}
    rec = {"id": rid, "type": "lexicon", "status": "imported_unreviewed", "tags": [], "title": title,
           "language": "grc" if lang == "grc" else "hbo", "gloss_language": "en",
           "key": "dStrong (STEPBible, disambiguiert); «estrong» = erweiterte Strong-Nummer",
           "source": {"repository": STEP_REPO, "commit": commit, "path": rel, "sha256": digest, "license": "CC BY 4.0",
                      "attribution": STEP_ATTR,
                      "changes_de": "Nur Zeilen für Strong-Nummern der importierten Bücher; Spalten umbenannt; "
                                    + ("Bedeutungsspalte (Abridged BDB, © Online Bible, nur mit Erlaubnis) nicht übernommen."
                                       if lang == "heb" else
                                       "Definitionsspalte (Abbott-Smith/Middle Liddell, Herkunft je Eintrag nicht sicher) nicht übernommen.")
                                    + " Werte sonst wörtlich."},
           "counts": {"entries": len(entries)},
           "entries": entries,
           "import": {"tool": "scripts/import_lexica.py", "imported_on": today},
           "knowledge": {"asserted_at": today, "supersedes": None}}
    return rec


def dump(rec, path):
    head = json.dumps({k: v for k, v in rec.items() if k != "entries"}, ensure_ascii=False, indent=1)
    body = ",\n".join(f"  {json.dumps(k, ensure_ascii=False)}: {json.dumps(v, ensure_ascii=False, separators=(',', ':'))}"
                      for k, v in rec["entries"].items())
    path.write_text(head[:-2] + ',\n "entries": {\n' + body + "\n }\n}\n", encoding="utf-8")


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--ubs", type=pathlib.Path, required=True)
    ap.add_argument("--ubs-commit", required=True)
    ap.add_argument("--step", type=pathlib.Path, required=True)
    ap.add_argument("--step-commit", required=True)
    args = ap.parse_args()
    for c in (args.ubs_commit, args.step_commit):
        if not re.fullmatch(r"[0-9a-f]{40}", c):
            sys.exit("ERROR: Commits als vollständige 40-stellige Git-SHA angeben")
    today = datetime.date.today().isoformat()
    sc, dstrong = scope()
    codes = book_codes()
    out = D / "lexica"
    out.mkdir(exist_ok=True)
    for lang in ("grc", "heb"):
        for rec in (ubs_import(lang, args.ubs, args.ubs_commit, sc, codes, today),
                    step_import(lang, args.step, args.step_commit, sc, dstrong, today)):
            dump(rec, out / f"{rec['id']}.json")
            print(f"{rec['id']}: {json.dumps(rec['counts'], ensure_ascii=False)}, "
                  f"{(out / (rec['id'] + '.json')).stat().st_size // 1024} KB")
    print("PASS: Wörterbücher importiert")


if __name__ == "__main__":
    main()
