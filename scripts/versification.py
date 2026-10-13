"""Umrechnung von Verszählungen nach TVTMS (STEPBible, CC BY 4.0; data/versification/VRS-TVTMS-<BUCH>.json).

Derzeit umgesetzt: hebräische Zählung (WLC/MACULA Hebrew) -> Navigationszählung (KJV, englische Tradition).

    plan = heb_to_kjv("JOL", verses)    # verses: {"JOL.3.1": ["וְהָיָה", ...], ...} (Wörter je Vers, Quellzählung)
    plan["JOL.3.1"] -> [("JOL.2.28", 0, None)]   # (Zielvers, ab Wort, bis Wort) – Teilstücke eines Quellverses

Regeln (TVTMS, Teil «Expanded»):
- Zeilen gelten für eine Quelltradition, wenn «Hebrew» zu ihrem source_type gehört und ihre Bedingungen («tests»)
  am Quelltext erfüllt sind (Vers existiert/fehlt, letzter Vers des Kapitels, Längenvergleiche in Wörtern).
- «Renumber verse»/«Keep verse»: ganzer Vers bekommt die Zielstelle.
- «Renumber title» (Psalmüberschriften als eigener hebräischer Vers): Die englische Tradition zählt die Überschrift
  als «Vers 0», die Navigation kennt keinen Vers 0. Die Überschrift wird deshalb dem ersten Vers vorangestellt
  (Ziel = Vers 1) und als Überschrift gekennzeichnet (kind "title").
- «DividedPrev/Next», «MergedPrev»: Ein Quellvers wird an einen Nachbarvers angehängt bzw. geteilt. Wo TVTMS
  keinen Teilungspunkt angibt, steht er in SPLITS (erstes Wort des zweiten Teils, Konsonanten), am Text geprüft.
- «IfEmpty verse»: Vers fehlt im Quelltext; der Zielvers bleibt leer (wird gemeldet, nicht erfunden).
Nach der Umrechnung prüft der Aufrufer, dass die Verszahlen je Kapitel der Navigation entsprechen.
"""
import json
import pathlib
import re
import unicodedata

ROOT = pathlib.Path(__file__).resolve().parents[1]
VRS = ROOT / "data" / "versification"

# Quellvers -> Konsonanten des ersten Worts, mit dem der zweite Teil («!b») beginnt (Hebräisch, WLC).
# ISA 63,19b = KJV 64,1 («Oh that thou wouldest rend the heavens»: לוּא); PSA 13,6b = KJV 13,6 («I will sing»: אָשִׁירָה).
SPLITS = {"ISA.63.19": "לוא", "PSA.13.6": "אשירה"}


def _cons(s):
    s = unicodedata.normalize("NFD", s)
    return "".join(ch for ch in s if "א" <= ch <= "ת")


def _rows(book):
    p = VRS / f"VRS-TVTMS-{book}.json"
    return json.loads(p.read_text(encoding="utf-8"))["entries"] if p.exists() else []


_RAW = re.compile(r"(?:[1-4]?[A-Za-z]{2,3})\.(\d+):(TextBeforeV1|\d+)(?:\.(\d+))?")


def _test(expr, book, verses, last):
    """Bedingung am Quelltext auswerten. verses: {ref: [wörter]}, last: {kapitel: letzter vers}."""

    def length(term):
        term = term.strip()
        mul = 1
        if "*" in term:
            term, m = term.split("*")
            mul = int(m)
        m = _RAW.fullmatch(term.strip())
        if not m:
            raise ValueError(term)
        return mul * len(verses.get(f"{book}.{int(m[1])}.{m[2]}", []))

    def side(s):
        return sum(length(t) for t in s.split("+"))

    expr = expr.strip()
    if not expr:
        return True
    if "=" in expr:
        ref, cond = expr.split("=")
        m = _RAW.fullmatch(ref.strip())
        if not m:
            return False  # Bücher mit Buchstaben-Kapiteln (Ester griechisch) betreffen Hebräisch nicht
        c, v, sub = int(m[1]), m[2], m[3]
        if v == "TextBeforeV1":
            exists = False  # WLC hat keinen Text vor Vers 1
        elif sub:
            exists = False  # Teilverse kennt der hebräische Text nicht
        else:
            exists = f"{book}.{c}.{v}" in verses
        if cond == "Exist":
            return exists
        if cond == "NotExist":
            return not exists
        if cond == "Last":
            return exists and last.get(c) == int(v)
        raise ValueError(expr)
    for op in ("<", ">"):
        if op in expr:
            a, b = expr.split(op)
            return side(a) < side(b) if op == "<" else side(a) > side(b)
    raise ValueError(expr)


def _ref(raw, book):
    m = re.fullmatch(r"[1-4]?[A-Za-z]{2,3}\.(\d+):(\d+|Title)(?:!([ab]))?", raw.strip())
    if not m:
        raise ValueError(raw)
    return int(m[1]), (0 if m[2] == "Title" else int(m[2])), m[3]


def heb_to_kjv(book, verses):
    """-> {quellvers: [(zielvers, ab_wort, bis_wort, art)]}, art: same|renumber|title|join|split; fehlende Zielverse."""
    last = {}
    for r in verses:
        _, c, v = r.split(".")
        last[int(c)] = max(last.get(int(c), 0), int(v))
    chosen = {}
    for row in _rows(book):
        if "Hebrew" not in row["source_type"].split("+"):
            continue
        if not all(_test(t, book, verses, last) for t in (row.get("tests") or "").split("&")):
            continue
        key = (row["source_ref_raw"], row["action"])
        prev = chosen.get(key)
        if prev and prev["standard_ref_raw"] != row["standard_ref_raw"]:
            raise SystemExit(f"{book}: widersprüchliche Zeilen für {key}")
        chosen[key] = row
    plan = {r: [(r, 0, None, "same")] for r in verses}
    empty = []
    for (src_raw, action), row in sorted(chosen.items()):
        dst_raw = row["standard_ref_raw"]
        if action in ("Keep verse", "Renumber verse"):
            sc, sv, _ = _ref(src_raw, book)
            dc, dv, _ = _ref(dst_raw, book)
            src = f"{book}.{sc}.{sv}"
            if src in verses:
                plan[src] = [(f"{book}.{dc}.{dv}", 0, None, "same" if (sc, sv) == (dc, dv) else "renumber")]
        elif action == "Renumber title":
            sc, sv, _ = _ref(src_raw, book)
            dc, _, _ = _ref(dst_raw, book)
            plan[f"{book}.{sc}.{sv}"] = [(f"{book}.{dc}.1", 0, None, "title")]
        elif action in ("DividedPrev verse", "DividedNext verse"):
            sc, sv, _ = _ref(src_raw, book)
            dc, dv, _ = _ref(dst_raw, book)
            plan[f"{book}.{sc}.{sv}"] = [(f"{book}.{dc}.{dv}", 0, None,
                                          "join_after" if action == "DividedPrev verse" else "join_before")]
        elif action == "MergedPrev verse":
            sc, sv, part = _ref(src_raw, book)
            dc, dv, _ = _ref(dst_raw, book)
            src = f"{book}.{sc}.{sv}"
            words = verses[src]
            want = SPLITS.get(src)
            idx = [i for i, w in enumerate(words) if _cons(w) == want] if want else []
            if len(idx) != 1:
                raise SystemExit(f"{src}: Teilungspunkt nicht eindeutig (SPLITS)")
            first = plan[src][0]
            plan[src] = [(first[0], 0, idx[0], first[3] if first[3] != "same" else "split"),
                         (f"{book}.{dc}.{dv}", idx[0], None, "split")]
        elif action == "IfEmpty verse":
            dc, dv, _ = _ref(dst_raw, book)
            empty.append(f"{book}.{dc}.{dv}")
        elif action == "Concatenation":
            continue  # beschreibt nur das Ergebnis der Teilzeilen
        else:
            raise SystemExit(f"{book}: unbekannte Handlung {action}")
    targets = {d for parts in plan.values() for d, *_ in parts}
    return plan, [e for e in empty if e not in targets]


def apply(book, verses, plan):
    """Wörter je Zielvers in Lesereihenfolge: {ziel: [(quellvers, wortindex, art)]}."""
    out = {}
    order = sorted(verses, key=lambda r: tuple(int(x) for x in r.split(".")[1:]))
    pending_before = {}
    for src in order:
        for dst, a, b, kind in plan[src]:
            items = [(src, i, kind) for i in range(len(verses[src]))[a:b]]
            if kind == "join_before":
                pending_before.setdefault(dst, []).extend(items)
            else:
                out.setdefault(dst, []).extend(items)  # Überschriften kommen im Quelltext vor Vers 1
    for dst, items in pending_before.items():
        out[dst] = items + out.get(dst, [])
    return out
