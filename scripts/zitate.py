#!/usr/bin/env python3
"""Zitate in Erklärtexten wörtlich gegen den Bibeltext prüfen (docs/WEITERDENKEN.md, «Zitate wörtlich»).

Ein Zitat steht in «…» (innere Anführung ‹…›); Auslassungen mit «…». Es muss wörtlich in der Übersetzungsschicht der
Sprache stehen, in der der Erklärtext geschrieben ist: Hochdeutsch (Originalfeld `_de`) gegen die hochdeutsche
Arbeitsübersetzung, eine Lokalisierung gegen die Arbeitsübersetzung ihrer Sprache (z. B. Züridüütsch gegen die
Mundart-Schicht). Gesucht wird in den Versen der Stelle: Stellenmarken [[…]] im Text und die Stelle des Bezugs
(Texteinheit, Kapitel, Buch). Gross-/Kleinschreibung und Satzzeichen zählen nicht, Wörter und Wortformen schon.

Ergebnis je Zitat: «fehlt» (steht nicht im Text der Stelle) oder «unübersetzt» (Stelle in dieser Schicht nicht übersetzt
oder nicht bestimmbar; dann nur ein Hinweis). Benutzt von scripts/validate.py und den Autorenwerkzeugen.
Nur Standardbibliothek.
"""
import bisect
import re

import prose_refs
import refs

QUOTE_RE = re.compile(r"«([^«»]+)»")


def norm(s):
    return " " + re.sub(r"[^\w]+", " ", str(s).lower()).strip() + " "


def subject_ref(sid, records):
    """Stelle eines Bezugs: Texteinheit (range), Kapitel- bzw. Buch-Zusammenfassung (aus der ID), Kernanalyse (reference)."""
    r = records.get(sid) or {}
    if r.get("range") or r.get("reference"):
        ref = r.get("range") or r.get("reference")
        return ref if refs.is_canonical(ref) else None
    if sid.startswith("SUM-CH-"):
        b, c = sid[7:].rsplit("-", 1)
        return f"{b}.{int(c)}"
    if sid.startswith("SUM-BOOK-"):
        return sid[9:]
    return None


class Layers:
    """Arbeitsübersetzungen je Sprachgrundtag (de, gsw …): Verse und Index je Buch."""

    def __init__(self, records):
        self.text, self.index = {}, {}
        for r in records.values():
            if r.get("type") != "translation" or r.get("translation_kind") != "literal_original_working" or r.get("status") == "deprecated":
                continue
            lg = (r.get("language") or "de").split("-")[0]
            t = self.text.setdefault(lg, {})
            for k, v in (r.get("text_by_reference") or {}).items():
                t.setdefault(k, v)
        for lg, t in self.text.items():
            idx = self.index.setdefault(lg, {})
            for k in t:
                b, c, v = k.split(".")
                idx.setdefault(b, []).append(((int(c), int(v)), k))
            for b in idx:
                idx[b].sort()

    def verses(self, lang, ref):
        """Verse der Schicht in einem Bereich (Buch, Kapitel, Vers oder Bereich davon)."""
        try:
            (b, c1, v1), (_, c2, v2) = refs.parse(ref)
        except refs.RefError:
            return []
        lst = self.index.get(lang, {}).get(b, [])
        lo = (c1 or 0, v1 or 0)
        hi = (c2 if c2 is not None else 10**6, v2 if v2 is not None else 10**6)
        i = bisect.bisect_left(lst, (lo, ""))
        out = []
        while i < len(lst) and lst[i][0] <= hi:
            out.append(lst[i][1])
            i += 1
        return out


def check(fields, lang, layers, subject=None):
    """fields: {feld: text}. Gibt [(feld, zitat, 'fehlt'|'unübersetzt')] zurück."""
    texts = [t for t in fields.values() if isinstance(t, str)]
    if not any("«" in t for t in texts):
        return []
    ctx_refs = [m for t in texts for m in prose_refs.marks(t)] + ([subject] if subject else [])
    keys, gap = [], not ctx_refs
    for r in ctx_refs:
        vs = layers.verses(lang, r)
        gap = gap or not vs
        keys += vs
    t = layers.text.get(lang, {})
    hay = norm(" ".join(t[k] for k in dict.fromkeys(keys)))
    out = []
    for f, s in fields.items():
        if not isinstance(s, str):
            continue
        for q in QUOTE_RE.findall(s):
            parts = [p for p in re.split(r"…|\.\.\.", q) if norm(p).strip()]
            if not parts or all(norm(p) in hay for p in parts):
                continue
            out.append((f, q, "unübersetzt" if gap else "fehlt"))
    return out
