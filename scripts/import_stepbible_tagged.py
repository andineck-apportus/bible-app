#!/usr/bin/env python3
"""Import aus STEPBible TAGNT (Editionen je Wort, NT) und TAHOT (Ketiv/Qere, AT), zugeordnet zu unseren Tokens.

Aufruf:
    python3 scripts/import_stepbible_tagged.py --step PFAD/STEPBible-Data --step-commit SHA [BUCH ...]

Ohne Buchangabe werden alle Bücher eingelesen, für die es in data/tokens/ SBLGNT- bzw. WLC-Tokens gibt.

Quelle: github.com/STEPBible/STEPBible-Data (CC BY 4.0, «Data created by www.STEPBible.org based on work at Tyndale
House Cambridge»), Ordner «Translators Amalgamated OT+NT»:
- TAGNT (Translators Amalgamated Greek NT): alle Wörter der grossen Ausgaben (NA27/28, Tyndale House GNT, SBLGNT,
  Westcott-Hort, Tregelles, Textus Receptus [Scrivener 1894], Byzantinischer Text [Robinson-Pierpont 2005]); je Wort
  die Ausgaben, die es enthalten. Das sind Angaben über **gedruckte Ausgaben**, keine Handschriftenbelege.
- TAHOT (Translators Amalgamated Hebrew OT): Leningrad-Text mit Qere-Formen; das Ketiv («geschrieben») steht als
  Variante (Typ «Q(K)» bzw. «Q(k)»). Die Vokalisierung des Ketiv ist von Tyndale-Gelehrten ergänzt; die Handschrift
  hat dafür nur die Konsonanten.

Zuordnung (keine Deutung, nichts geraten):
- NT: je Kapitel werden die TAGNT-Wörter, die laut Spalte «editions» in SBL stehen, mit den SBLGNT-Tokens verglichen
  (ohne Akzente, Gross/Klein, Satzzeichen; SBL-Schreibung aus der Spalte «Spelling variants», wo angegeben).
  Gleiche Folgen werden zugeordnet; ungleiche Blöcke nur, wenn sie gleich lang sind (dann als «by_position»
  markiert, mit beiden Formen). Alles andere wird als nicht zugeordnet gemeldet.
- AT: je Vers werden die TAHOT-Zeilen (Qere-Text) mit den MACULA-Wörtern (word_no) über die Konsonanten verglichen;
  übernommen werden die Ketiv-Angaben und je Morphem die dStrong-Nummer (für den Wörterbuch-Eintrag).
Nicht zuordenbare Wörter stehen in «unmatched» und in reports/stepbible-tagged-<BUCH>.json.

Übernommen (umformatiert; vom Lizenzgeber erlaubt, Änderungen vermerkt in source.changes_de): Wort-ID, Worttyp,
griechische bzw. hebräische Form, dStrong und Grammatik, Ausgabenliste, Bedeutungs- und Schreibvarianten (ohne die
englischen und spanischen Übersetzungen), Ketiv mit Umschrift und englischer Kurzglosse (TAHOT).
Nicht übernommen: englische Übersetzung (TAGNT: nach Berean Study Bible), spanische Übersetzung (Marvel Bible/OpenGNT,
CC BY-SA), Unterbedeutungen, Verknüpfungen.

Ausgabe: data/tagged-alignments/TALIGN-TAGNT-<BUCH>.json bzw. TALIGN-TAHOT-<BUCH>.json (Typ tagged_text_alignment).
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
D = ROOT / "data"
REPO = "https://github.com/STEPBible/STEPBible-Data"
DIR = "Translators Amalgamated OT+NT"
FILES = {
    "TAGNT Mat-Jhn": ("TAGNT Mat-Jhn - Translators Amalgamated Greek NT - STEPBible.org CC-BY.txt",
                      "ab8eaaeb68e17a1dcfa34e1e9350358f22f03bc2a97244d848750ad81044bc8e"),
    "TAGNT Act-Rev": ("TAGNT Act-Rev - Translators Amalgamated Greek NT - STEPBible.org CC-BY.txt",
                      "524e32375361e6d3fa2f7ef00b87605fdc4317a762f395651a05fdc31ad031b7"),
    "TAHOT Jos-Est": ("TAHOT Jos-Est - Translators Amalgamated Hebrew OT - STEPBible.org CC BY.txt",
                      "195fee1dc3653bab33701f170734eb894ed647c10cd08cc61749375fe8b73775"),
    "TAHOT Isa-Mal": ("TAHOT Isa-Mal - Translators Amalgamated Hebrew OT - STEPBible.org CC BY.txt",
                      "f3ded203d2a74d6368932c97ae550d1d0754b271af491dc0dedf36fe3ba0bcc5"),
}
NT_FILE = {b: "TAGNT Mat-Jhn" for b in ("MAT", "MRK", "LUK", "JHN")}
OT_FILE = {b: "TAHOT Jos-Est" for b in ("JOS", "JDG", "RUT", "1SA", "2SA", "1KI", "2KI", "1CH", "2CH", "EZR", "NEH", "EST")}
OT_FILE.update({b: "TAHOT Isa-Mal" for b in ("ISA", "JER", "LAM", "EZK", "DAN", "HOS", "JOL", "AMO", "OBA", "JON", "MIC",
                                              "NAM", "HAB", "ZEP", "HAG", "ZEC", "MAL")})
STEP_CODE = {"MAT": "Mat", "MRK": "Mrk", "LUK": "Luk", "JHN": "Jhn", "ACT": "Act", "ROM": "Rom", "1CO": "1Co",
             "2CO": "2Co", "GAL": "Gal", "EPH": "Eph", "PHP": "Php", "COL": "Col", "1TH": "1Th", "2TH": "2Th",
             "1TI": "1Ti", "2TI": "2Ti", "TIT": "Tit", "PHM": "Phm", "HEB": "Heb", "JAS": "Jas", "1PE": "1Pe",
             "2PE": "2Pe", "1JN": "1Jn", "2JN": "2Jn", "3JN": "3Jn", "JUD": "Jud", "REV": "Rev",
             "JOS": "Jos", "JDG": "Jdg", "RUT": "Rut", "1SA": "1Sa", "2SA": "2Sa", "1KI": "1Ki", "2KI": "2Ki",
             "1CH": "1Ch", "2CH": "2Ch", "EZR": "Ezr", "NEH": "Neh", "EST": "Est", "ISA": "Isa", "JER": "Jer",
             "LAM": "Lam", "EZK": "Ezk", "DAN": "Dan", "HOS": "Hos", "JOL": "Jol", "AMO": "Amo", "OBA": "Oba",
             "JON": "Jon", "MIC": "Mic", "NAM": "Nam", "HAB": "Hab", "ZEP": "Zep", "HAG": "Hag", "ZEC": "Zec", "MAL": "Mal"}
MAIN_EDITIONS = ["NA28", "NA27", "Tyn", "SBL", "WH", "Treg", "TR", "Byz"]
EDITIONS_DE = {"NA28": "Nestle-Aland 28. Auflage (2012)", "NA27": "Nestle-Aland 27. Auflage",
               "Tyn": "Tyndale House Greek New Testament (2017)", "SBL": "SBL Greek New Testament (Holmes 2010)",
               "WH": "Westcott-Hort (1881)", "Treg": "Tregelles (1879, ergänzt Jongkind 2009)",
               "TR": "Textus Receptus (Scrivener 1894)", "Byz": "Byzantinischer Text (Robinson-Pierpont 2005)",
               "KJV": "Grundtext, dem die King James Version an dieser Stelle folgt"}
LICENSE = "CC BY 4.0"
ATTRIBUTION = "Data created by www.STEPBible.org based on work at Tyndale House Cambridge (CC BY 4.0)"
REF = re.compile(r"^(?P<bk>[1-3]?[A-Za-z]{2,3})\.(?P<c>\d+)\.(?P<v>\d+)(?P<alt>(?:[\[\(\{][\d.]+[\]\)\}])*)#(?P<n>\d+)=(?P<type>\S*)$")


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def gnorm(s):
    s = unicodedata.normalize("NFD", s or "")
    s = "".join(ch for ch in s if not unicodedata.combining(ch)).lower().replace("ς", "σ")
    return "".join(ch for ch in s if "α" <= ch <= "ω")


def hcons(s):
    return "".join(ch for ch in (s or "") if "א" <= ch <= "ת")


def rows_of(text, code):
    """Datenzeilen eines Buchs: (Kapitel, Vers, NA-Kapitel, NA-Vers, Wortnummer, Typ, Spalten)."""
    pre = STEP_CODE[code] + "."
    for line in text.split("\n"):
        if not line.startswith(pre):
            continue
        cols = line.rstrip("\r").split("\t")
        m = REF.match(cols[0].strip())
        if not m:
            continue
        c, v = int(m["c"]), int(m["v"])
        alt = re.search(r"\((\d+)\.(\d+)\)", m["alt"] or "")  # Nestle-Aland-Zählung in runden Klammern
        yield {"id": cols[0].split("=")[0].strip(), "c": c, "v": v, "na": (int(alt[1]), int(alt[2])) if alt else (c, v),
               "n": int(m["n"]), "type": m["type"],
               "cols": cols + [""] * (13 - len(cols))}


def split_eds(s):
    out, moved = [], {}
    for x in (s or "").split("+"):
        x = x.strip()
        if not x:
            continue
        m = re.match(r"^([A-Za-z0-9]+)([»«]\d+)?$", x)
        if not m:
            out.append(x)
            continue
        out.append(m[1])
        if m[2]:
            moved[m[1]] = m[2]
    return out, moved


MV = re.compile(r"^(?P<grc>.+?) \((?P<kind>[A-Za-z])=[^)]*\) .*? - (?P<tags>[GH]\d.*?) in: (?P<eds>.+)$")


def meaning_variants(s):
    out, bad = [], []
    for part in [p.strip() for p in (s or "").split("¦") if p.strip()]:
        m = MV.match(part)
        if not m:
            bad.append(part.split(" (")[0])
            continue
        eds, moved = split_eds(m["eds"])
        x = {"grc": m["grc"].strip(), "kind": m["kind"], "tags": m["tags"].strip(), "editions": eds}
        if moved:
            x["moved"] = moved
        out.append(x)
    return out, bad


def spelling_variants(s):
    out = []
    for grp in [g.strip() for g in (s or "").split(";") if g.strip()]:
        if ":" not in grp:
            continue
        eds, word = grp.split(":", 1)
        if eds.strip().startswith(("L=", "K=")):
            continue
        out.append({"editions": [e for e in eds.replace(" ", "").lstrip("+").split("+") if e], "grc": word.strip()})
    return out


def token_sets(prefix, book):
    sets = []
    for p in sorted((D / "tokens").glob(f"{prefix}-{book}-*.json")):
        r = json.loads(p.read_text(encoding="utf-8"))
        if r.get("status") == "deprecated" or not re.fullmatch(rf"{prefix}-{book}-\d{{3}}\.json", p.name):
            continue
        sets.append(r)
    return sets


def provenance(key, commit, changes):
    name, digest = FILES[key]
    return {"repository": REPO, "commit": commit, "path": f"{DIR}/{name}", "sha256": digest, "license": LICENSE,
            "attribution": ATTRIBUTION, "changes_de": changes}


def write(rid, rec):
    """Kopf eingerückt, lange Listen/Tabellen je Eintrag eine Zeile (kompakt und gut vergleichbar)."""
    out = D / "tagged-alignments"
    out.mkdir(parents=True, exist_ok=True)
    c = lambda v: json.dumps(v, ensure_ascii=False, separators=(",", ":"))
    parts = []
    for k, v in rec.items():
        if k in ("entries", "dstrong") and v:
            body = ",\n".join(f"  {c(a)}: {c(b)}" for a, b in v.items())
            parts.append(f" {c(k)}: {{\n{body}\n }}")
        elif k in ("extra_words", "ketiv_without_qere") and v:
            parts.append(f" {c(k)}: [\n" + ",\n".join("  " + c(x) for x in v) + "\n ]")
        else:
            parts.append(f" {c(k)}: " + json.dumps(v, ensure_ascii=False, indent=1).replace("\n", "\n "))
    (out / f"{rid}.json").write_text("{\n" + ",\n".join(parts) + "\n}\n", encoding="utf-8")


def import_nt(book, text, commit, today):
    sets = token_sets("SBLGNT", book)
    toks = [t for s in sets for t in s["tokens"]]
    tags = sorted({t for s in sets for t in s.get("tags", [])})
    rows = list(rows_of(text, book))
    entries, extra, unmatched_tok, unmatched_src, by_pos, ref_diff, bad_mv = {}, [], [], [], 0, [], []
    second_pass = 0
    chapters = sorted({int(t["reference"].split(".")[1]) for t in toks})
    prev_tok = {}
    for ch in chapters:
        A = [t for t in toks if int(t["reference"].split(".")[1]) == ch]
        R = [r for r in rows if r["na"][0] == ch]
        B = []
        for i, r in enumerate(R):
            eds, moved = split_eds(r["cols"][5])
            r["eds"], r["moved"] = eds, moved
            r["grc"] = r["cols"][1].split(" (")[0].strip()
            r["spell"] = spelling_variants(r["cols"][7])
            r["mv"], bad = meaning_variants(r["cols"][6])
            bad_mv += [f"{r['id']}: {b}" for b in bad]
            if "SBL" in eds:
                sbl = next((s["grc"] for s in r["spell"] if "SBL" in s["editions"]), r["grc"])
                # Wortfolge der SBL: «SBL»k» bzw. «SBL«k» = in SBL um k Wörter später bzw. früher (gezählt in der
                # TAGNT-Folge); das Wort steht dann hinter dem Wort an Position i±k
                mv = moved.get("SBL")
                key = i if not mv else i + (int(mv[1:]) if mv[0] == "»" else -int(mv[1:])) + 0.5
                B.append((key, i, r, sbl))
        B = [(r, sbl) for _, _, r, sbl in sorted(B, key=lambda x: (x[0], x[1]))]
        a_norm = [gnorm(t["word"]) for t in A]
        b_norm = [gnorm(s) for _, s in B]
        sm = difflib.SequenceMatcher(None, a_norm, b_norm, autojunk=False)
        match, un_i, un_r = {}, [], []
        for op, i1, i2, j1, j2 in sm.get_opcodes():
            if op == "equal" or (op == "replace" and i2 - i1 == j2 - j1):
                for k in range(i2 - i1):
                    match[i1 + k] = (B[j1 + k][0], op != "equal", B[j1 + k][1])
            else:
                un_i += list(range(i1, i2))
                un_r += [B[j][0] for j in range(j1, j2)]
        matched_rows = set()
        for i, t in enumerate(A):
            if i not in match:
                continue
            r, positional, sbl = match[i]
            matched_rows.add(r["id"])
            na_ref = f"{book}.{r['na'][0]}.{r['na'][1]}"
            if na_ref != t["reference"]:
                ref_diff.append(f"{t['id']} ({t['reference']}) ↔ {r['id']}")
            dstrong, _, grammar = r["cols"][3].partition("=")
            dstrong = dstrong.strip()
            full = set(MAIN_EDITIONS) <= set(r["eds"])
            need = (not full) or r["moved"] or r["mv"] or r["spell"] or positional
            if need:
                e = {"src": r["id"], "type": r["type"], "editions": r["eds"], "dstrong": dstrong, "grammar": grammar.strip()}
                if r["moved"]:
                    e["moved"] = r["moved"]
                if r["mv"]:
                    e["alt"] = r["mv"]
                if r["spell"]:
                    e["spelling"] = r["spell"]
                if positional:
                    by_pos += 1
                    e["by_position"] = {"tagnt": r["grc"], "sbl_form_used": sbl}
                entries[t["id"]] = e
            elif re.search(r"\d[A-Z]$", dstrong):
                entries[t["id"]] = {"src": r["id"], "dstrong": dstrong}
            prev_tok[r["id"]] = t["id"]
        # Zweiter Durchgang je Vers für übrig gebliebene SBLGNT-Tokens: gleiches Wort (a) in einer TAGNT-Zeile, die SBL
        # nicht aufführt (z. B. Mk 16,9–20, das SBLGNT in doppelten eckigen Klammern druckt), oder (b) als Bedeutungs-
        # variante mit SBL in der Ausgabenliste. Beides wird gekennzeichnet; sonst bleibt das Token unzugeordnet.
        used = set(matched_rows)
        for i in un_i:
            t = A[i]
            na = lambda r: f"{book}.{r['na'][0]}.{r['na'][1]}"
            hit = None
            for r in R:
                if r["id"] in used or na(r) != t["reference"]:
                    continue
                if gnorm(r["grc"]) == gnorm(t["word"]) and "SBL" not in r["eds"]:
                    hit = (r, None)
                    break
                alt = next((a for a in r["mv"] if "SBL" in a["editions"] and gnorm(a["grc"]) == gnorm(t["word"])), None)
                if alt:
                    hit = (r, alt)
                    break
            if not hit:
                unmatched_tok.append(t["id"])
                continue
            r, alt = hit
            used.add(r["id"])
            dstrong, _, grammar = r["cols"][3].partition("=")
            if alt is None:
                entries[t["id"]] = {"src": r["id"], "type": r["type"], "editions": r["eds"], "dstrong": dstrong.strip(),
                                    "grammar": grammar.strip(), "sbl_not_listed": True}
                matched_rows.add(r["id"])
                prev_tok[r["id"]] = t["id"]
            else:
                ds, _, gr = alt["tags"].partition("=")
                entries[t["id"]] = {"src": r["id"], "type": r["type"], "editions": alt["editions"], "dstrong": ds.strip(),
                                    "grammar": gr.strip(), "via_variant": True,
                                    "alt": [{"grc": r["grc"], "kind": "main", "tags": r["cols"][3].strip(), "editions": r["eds"]}]}
            second_pass += 1
        unmatched_src += [r["id"] for r in un_r if r["id"] not in used]
        # Wörter, die SBLGNT nicht hat (andere Ausgaben): mit dem vorangehenden SBLGNT-Token verankert
        last = None
        for r in R:
            if r["id"] in prev_tok:
                last = prev_tok[r["id"]]
                continue
            if "SBL" in r["eds"] or r["id"] in used:
                continue  # SBL-Wort ohne Zuordnung: steht in unmatched
            dstrong, _, grammar = r["cols"][3].partition("=")
            x = {"src": r["id"], "ref": f"{book}.{r['na'][0]}.{r['na'][1]}", "after": last, "type": r["type"],
                 "grc": r["grc"], "dstrong": dstrong.strip(), "grammar": grammar.strip(), "editions": r["eds"]}
            if r["moved"]:
                x["moved"] = r["moved"]
            if r["mv"]:
                x["alt"] = r["mv"]
            extra.append(x)
    n_sbl = sum(1 for r in rows if "SBL" in split_eds(r["cols"][5])[0])
    rid = f"TALIGN-TAGNT-{book}"
    counts = {"sblgnt_tokens": len(toks), "tagnt_words": len(rows), "tagnt_words_in_sbl": n_sbl,
              "matched": len(toks) - len(unmatched_tok), "matched_by_position": by_pos,
              "matched_in_second_pass": second_pass, "unmatched_tokens": len(unmatched_tok), "unmatched_tagnt": len(unmatched_src),
              "entries": len(entries), "not_in_all_main_editions": sum(1 for e in entries.values() if "editions" in e and not set(MAIN_EDITIONS) <= set(e["editions"])),
              "extra_words": len(extra), "reference_differences": len(ref_diff)}
    rec = {"id": rid, "type": "tagged_text_alignment", "status": "imported_unreviewed", "tags": tags, "book": book,
           "kind": "edition_presence", "aligned_to": "SBLGNT-Tokens (data/tokens/SBLGNT-" + book + "-*.json)",
           "source": provenance(NT_FILE.get(book, "TAGNT Act-Rev"), commit,
                                "Spalten als Felder umformatiert und SBLGNT-Tokens zugeordnet; nur Wörter mit Abweichung zwischen "
                                "den Ausgaben, mit Bedeutungs- oder Schreibvarianten oder mit disambiguierter Strong-Nummer "
                                "gespeichert (alle übrigen stehen in allen acht Hauptausgaben); englische Übersetzung, "
                                "spanische Übersetzung, Unterbedeutungen und Verknüpfungen weggelassen; Bedeutungsvarianten "
                                "ohne Umschrift und englische Übersetzung. Werte sonst wörtlich."),
           "method_de": ("Zuordnung je Kapitel über die Wortfolge (ohne Akzente, Gross/Klein, Satzzeichen); gleich lange "
                         "ungleiche Blöcke werden nach Position zugeordnet und mit «by_position» markiert, alles andere "
                         "als nicht zugeordnet gemeldet. «editions» nennt die gedruckten Ausgaben, die das Wort enthalten "
                         "(Ausgabenbefund, kein Handschriftenbefund); »n/«n: in dieser Ausgabe um n Wörter verschoben. "
                         "Fehlt «editions», steht das Wort in allen acht Hauptausgaben."),
           "editions_legend_de": EDITIONS_DE, "main_editions": MAIN_EDITIONS,
           "entries": entries, "extra_words": extra,
           "unmatched": {"tokens": unmatched_tok, "tagnt": unmatched_src, "meaning_variants_unparsed": bad_mv},
           "counts": counts,
           "import": {"tool": "scripts/import_stepbible_tagged.py", "imported_on": today},
           "knowledge": {"asserted_at": today, "supersedes": None}}
    write(rid, rec)
    report(book, {"counts": counts, "unmatched": rec["unmatched"], "reference_differences": ref_diff})
    return counts


KETIV = re.compile(r"K= (?P<tr>\S+) \((?P<heb>[^)]*)\) \"(?P<gloss>[^\"]*)\" \((?P<tags>[^)]*)\)")


def import_ot(book, text, commit, today):
    sets = token_sets("WLC", book)
    toks = [t for s in sets for t in s["tokens"]]
    tags = sorted({t for s in sets for t in s.get("tags", [])})
    ann = {}
    for s in sets:
        p = D / "annotations" / f"MACULA-{s['id'].replace('TOKSET-', '')}.json"
        ann.update(json.loads(p.read_text(encoding="utf-8"))["entries"])
    words = {}  # (reference, word_no) -> [Token]
    for t in toks:
        words.setdefault((t["reference"], t["word_no"]), []).append(t)
    by_verse = {}
    for (ref, no), ts in words.items():
        by_verse.setdefault(ref, []).append((no, ts))
    rows = list(rows_of(text, book))
    rows_by_verse = {}
    for r in rows:
        rows_by_verse.setdefault(f"{book}.{r['c']}.{r['v']}", []).append(r)
    entries, ketiv_only, dstrong, unmatched_rows, unmatched_words, by_pos = {}, [], {}, [], [], 0
    by_sequence = 0
    for ref in sorted(set(by_verse) | set(rows_by_verse), key=lambda x: tuple(int(p) for p in x.split(".")[1:])):
        W = sorted(by_verse.get(ref, []))
        units = []  # (Zeile, Konsonanten)
        for r in rows_by_verse.get(ref, []):
            # «\» trennt Satzzeichen ab (Sof Pasuq, Maqqef, Abschnittszeichen ס/פ); mehrere Wörter: «/ /»
            heb = re.sub(r"\\.*$", "", r["cols"][1]).replace("/", "")
            for w in heb.split():
                if hcons(w):
                    units.append((r, hcons(w)))
        a = [hcons("".join(t["word"] for t in ts)) for _, ts in W]
        b = [u[1] for u in units]
        sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
        row_words = {}
        for op, i1, i2, j1, j2 in sm.get_opcodes():
            if op == "equal" or (op == "replace" and i2 - i1 == j2 - j1):
                for k in range(i2 - i1):
                    row_words.setdefault(units[j1 + k][0]["id"], []).append(W[i1 + k])
                    if op != "equal":
                        by_pos += 1
            else:
                unmatched_words += [f"{ref}#{W[i][0]} {''.join(t['word'] for t in W[i][1])}" for i in range(i1, i2)]
                unmatched_rows += [units[j][0]["id"] for j in range(j1, j2)]
        last = None
        for r in rows_by_verse.get(ref, []):
            ws = row_words.get(r["id"], [])
            tok_ids = [t["id"] for _, ts in ws for t in ts]
            # dStrong je Morphem: TAHOT trennt Vorsilben/Wurzel/Endungen mit «/» wie MACULA die Morpheme. Stimmt die
            # Anzahl, werden die Nummern der Reihe nach zugeordnet; sonst nur die Wurzel ({…}) dem Morphem mit gleicher
            # Strong-Zahl. Satzzeichen (\H90xx) und Fortsetzungsmarke «+» zählen nicht.
            tags_ = [x for x in re.sub(r"\\H\d+|[{}+ ]", "", r["cols"][4]).split("/") if x]
            if len(tags_) == len(tok_ids):
                for tid, tg in zip(tok_ids, tags_):
                    dstrong[tid] = tg
                    by_sequence += 1
            else:
                taken = set()
                for root in re.findall(r"\{(H\d+[A-Za-z]?)\}", r["cols"][4]):
                    num = int(re.match(r"H(\d+)", root)[1])
                    for tid in tok_ids:
                        sx = re.match(r"(\d+)", ann.get(tid, {}).get("strongnumberx") or "")
                        if tid not in taken and sx and int(sx[1]) == num:
                            dstrong[tid] = root
                            taken.add(tid)
                            break
            if re.search(r"\([^)]*[Kk]", r["type"]):
                k = KETIV.search(r["cols"][6])
                if k:
                    ketiv = {"text": k["heb"], "translit": k["tr"], "gloss_en": k["gloss"], "tags": k["tags"]}
                else:
                    m = re.search(r"K= ([^;¦]+)", r["cols"][6] + " " + r["cols"][7])
                    ketiv = {"text": m[1].strip()} if m else {}
                lm = re.search(r"L= ([^¦;]+)", r["cols"][7])
                e = {"src": r["id"], "type": r["type"], "qere": r["cols"][1].strip(), "translit_column": r["cols"][2].strip(),
                     "ketiv": ketiv}
                if lm:
                    e["leningrad"] = lm[1].strip()
                if tok_ids:
                    e["tokens"] = tok_ids
                    e["macula_qere_mark"] = any((ann.get(t, {}).get("transliteration") or "").startswith("**") for t in tok_ids)
                    entries[tok_ids[0]] = e
                elif not hcons(r["cols"][1]):
                    e["ref"] = ref
                    e["after"] = last
                    ketiv_only.append(e)
                else:
                    unmatched_rows.append(r["id"])
            if tok_ids:
                last = tok_ids[-1]
    marked = [t["id"] for t in toks if (ann.get(t["id"], {}).get("transliteration") or "").startswith("**")]
    covered = {t for e in entries.values() for t in e.get("tokens", [])}
    marked_missing = [t for t in marked if t not in covered]
    rid = f"TALIGN-TAHOT-{book}"
    counts = {"tahot_rows": len(rows), "wlc_words": len(words), "ketiv_entries": len(entries),
              "ketiv_without_qere": len(ketiv_only), "matched_by_position": by_pos,
              "unmatched_tahot_rows": len(unmatched_rows), "unmatched_wlc_words": len(unmatched_words),
              "macula_qere_marks": len(marked), "macula_qere_marks_without_ketiv_entry": len(marked_missing),
              "dstrong": len(dstrong), "dstrong_by_morpheme_sequence": by_sequence}
    rec = {"id": rid, "type": "tagged_text_alignment", "status": "imported_unreviewed", "tags": tags, "book": book,
           "kind": "ketiv_qere", "aligned_to": "WLC-Tokens nach MACULA Hebrew (data/tokens/WLC-" + book + "-*.json)",
           "source": provenance(OT_FILE[book], commit,
                                "Ketiv-Zeilen (Typ mit K) als Felder umformatiert und den WLC/MACULA-Wörtern zugeordnet; "
                                "dazu je Morphem die dStrong-Nummer (für den Wörterbuch-Eintrag). Übrige Spalten "
                                "(englische Übersetzung des Verses, Grammatik der übrigen Wörter, Varianten anderer "
                                "Handschriften) weggelassen. Werte sonst wörtlich."),
           "method_de": ("Je Vers werden die TAHOT-Zeilen (Qere-Text, Konsonanten) mit den MACULA-Wörtern verglichen; gleich "
                         "lange ungleiche Blöcke werden nach Position zugeordnet. «ketiv» ist die geschriebene Form, "
                         "«qere» die gelesene; die Vokale des Ketiv sind von Tyndale-Gelehrten ergänzt, die Handschrift "
                         "hat nur die Konsonanten. «leningrad»: Konsonanten des Ketiv mit den Vokalen des Qere, wie im "
                         "Codex. Typ Q(K): Unterschied kann die Übersetzung betreffen; Q(k): geringfügig. "
                         "«ketiv_without_qere»: geschrieben, aber nicht gelesen (in MACULA nicht enthalten). «translit_column»: "
                         "Umschrift-Spalte der TAHOT-Zeile wörtlich; sie gibt bei Q(K)-Zeilen offenbar die Ketiv-Lesung "
                         "wieder, nicht das Qere."),
           "entries": entries, "ketiv_without_qere": ketiv_only, "dstrong": dstrong,
           "unmatched": {"tahot_rows": unmatched_rows, "wlc_words": unmatched_words,
                         "macula_qere_marks_without_ketiv_entry": marked_missing},
           "counts": counts,
           "import": {"tool": "scripts/import_stepbible_tagged.py", "imported_on": today},
           "knowledge": {"asserted_at": today, "supersedes": None}}
    write(rid, rec)
    report(book, {"counts": counts, "unmatched": rec["unmatched"]})
    return counts


def report(book, data):
    out = ROOT / "reports"
    out.mkdir(exist_ok=True)
    (out / f"stepbible-tagged-{book}.json").write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--step", type=pathlib.Path, required=True, help="Klon von STEPBible-Data")
    ap.add_argument("--step-commit", required=True)
    ap.add_argument("books", nargs="*")
    args = ap.parse_args()
    if not re.fullmatch(r"[0-9a-f]{40}", args.step_commit):
        sys.exit("ERROR: --step-commit muss eine vollständige 40-stellige Git-SHA sein")
    today = datetime.date.today().isoformat()
    nt = sorted({p.name.split("-")[1] for p in (D / "tokens").glob("SBLGNT-*.json")})
    ot = sorted({p.name.split("-")[1] for p in (D / "tokens").glob("WLC-*.json")})
    books = args.books or nt + ot
    cache = {}

    def load(key):
        if key not in cache:
            p = args.step / DIR / FILES[key][0]
            if sha(p) != FILES[key][1]:
                sys.exit(f"Prüfsumme von {p.name} weicht ab; Quelle prüfen und Importer bewusst anpassen.")
            cache[key] = p.read_text(encoding="utf-8-sig")
        return cache[key]
    for b in books:
        if b in nt:
            c = import_nt(b, load(NT_FILE.get(b, "TAGNT Act-Rev")), args.step_commit, today)
        elif b in ot:
            c = import_ot(b, load(OT_FILE[b]), args.step_commit, today)
        else:
            sys.exit(f"Keine Tokens für {b}")
        print(f"{b}: {json.dumps(c, ensure_ascii=False)}")
    print(f"PASS: {len(books)} Bücher aus STEPBible TAGNT/TAHOT zugeordnet")


if __name__ == "__main__":
    main()
