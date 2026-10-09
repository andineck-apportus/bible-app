#!/usr/bin/env python3
"""Erzeugt den klickbaren Prototyp für Mk 3,20–35 aus den Projektdaten.

Aufruf: python3 scripts/build_prototype.py
Eingabe: data/ (nur freier Kern), app/prototype/template.html
Ausgabe: app/prototype/data.json und app/prototype/mk3-20-35.html (eigenständige Seite, Daten eingebettet)

Der Prototyp zeigt nur, was in den Daten steht; er erzeugt keine Inhalte.
"""
import collections
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
D = ROOT / "data"
OUT = ROOT / "app/prototype"
VERSES = range(20, 36)


def load(rel):
    return json.loads((D / rel).read_text(encoding="utf-8"))


def by_id(folder):
    return {r["id"]: r for r in (json.loads(p.read_text(encoding="utf-8")) for p in (D / folder).rglob("*.json"))}


in_scope = lambda ref: ref.startswith("MRK.3.") and int(ref.split(".")[2].split("-")[0]) in VERSES

# Buchebene: Wörter, Variantenstellen und Stufen je Kapitel
counts = load("counts/SBLGNT-MRK.json")
variants = by_id("variants")
assess = {}
for p in sorted((D / "assessments/edition-agreement-mrk").glob("*.json")):
    for a in json.loads(p.read_text(encoding="utf-8"))["assessments"]:
        assess[a["assesses"]] = a
chap = collections.defaultdict(lambda: {"variants": 0, "levels": collections.Counter()})
for vid, a in assess.items():
    ch = int(a["reference"].split(".")[1])
    chap[ch]["variants"] += 1
    chap[ch]["levels"][next(r["level"] for r in a["results"] if r["reading"].endswith(":R1"))] += 1
book = [{"chapter": int(k.split(".")[1]), "tokens": v["tokens"], "variants": chap[int(k.split(".")[1])]["variants"],
         "levels": dict(chap[int(k.split(".")[1])]["levels"])} for k, v in counts["by_chapter"].items()]

# Wörter und Annotationen
tokens = [t for t in load("tokens/SBLGNT-MRK-003.json")["tokens"] if int(t["reference"].split(".")[2]) in VERSES]
mac = load("annotations/MACULA-SBLGNT-MRK-003.json")["entries"]
mgnt = load("annotations/MORPHGNT-SBLGNT-MRK-003-022-030.json")["entries"]
lemma_freq = counts["lemma_counts"]
keep = ["lemma", "pos", "subtype", "person", "number", "gender", "case", "tense", "voice", "mood", "degree",
        "role", "gloss_berean", "gloss_cherith_en", "subject_ref", "referent", "morph"]
words = []
for t in tokens:
    a = mac.get(t["id"], {})
    w = {"id": t["id"], "v": int(t["reference"].split(".")[2]), "n": t["position"], "text": t["text"], "word": t["word"]}
    w["mac"] = {k: a[k] for k in keep if k in a}
    w["freq"] = lemma_freq.get(a.get("lemma"), 0)
    if t["id"] in mgnt:
        m = mgnt[t["id"]]
        w["mgnt"] = {"lemma": m["lemma"], "pos": m["pos"], "parsing": m["parsing"]}
    words.append(w)

# Varianten und Bewertungen im Bereich
units = []
for vid, v in sorted(variants.items()):
    if not in_scope(v.get("reference", "")):
        continue
    u = {"id": vid, "ref": v["reference"], "level": v.get("evidence_level", "manuscripts_reported"),
         "tokens": v.get("base_tokens", []),
         "readings": [{"id": r["reading_id"], "text": r["text"], "sblgnt": r.get("is_sblgnt_text", False),
                       "editions": r.get("editions", []), "witnesses": r.get("witnesses_reported", []),
                       "gloss": r.get("gloss_de")} for r in v["readings"]],
         "note": v.get("note_de") or v.get("editorial_note")}
    if vid in assess:
        u["assessment"] = [{"reading": r["reading"].split(":")[1], "support": r["support"], "of": r["of"],
                            "level": r["level"], "editions": r["supporting_editions"]} for r in assess[vid]["results"]]
    units.append(u)

# Übersetzungen (deutsch) und Wortzuordnung
tr = by_id("translations")
de = {}
sources = {}
for tid in ["TRANS-MRK-003-020-021-DE-WORKING", "TRANS-MRK-003-022-030-DE-WORKING", "TRANS-MRK-003-031-035-DE-WORKING"]:
    for ref, text in tr[tid]["text_by_reference"].items():
        de[int(ref.split(".")[2])] = text
        sources[int(ref.split(".")[2])] = tid
align = load("alignments/ALIGN-MRK-003-022-030-001.json")
tok_de = {}
for a in align["alignments"]:
    for i, t in enumerate(a["source_tokens"]):
        tok_de[t] = {"target": a["target"], "kind": a["kind"], "note": a.get("note_de"), "first": i == 0,
                     "group": a["source_tokens"]}

# Gliederung, Befunde, Deutungen, Prinzip, Anwendung, Parallelen
tu = by_id("text-units")
section = tu["TU-MRK-003-020-035"]
parts = [{"id": p, "range": tu[p]["range"], "title": tu[p]["title"]} for p in section["parts"]]
findings = by_id("findings")
ints = by_id("interpretations")
prin = by_id("principles")
apps = by_id("applications")
ctx = by_id("contexts")
rels = by_id("relations")
qs = by_id("questions")
method = load("methods/METHOD-EDITION-AGREEMENT-V1.json")
editions = {k: {"title": v["title"], "year": v.get("year")} for k, v in by_id("editions").items()}

chain_unit = "TU-MRK-003-022-030"
data = {
    "built_from": "bible-app data/ (freier Kern)",
    "book": book, "book_tokens": counts["token_count"], "book_lemmas": counts["unique_lemmas"],
    "section": {"id": section["id"], "range": section["range"], "title": section["title"], "parts": parts},
    "words": words, "variants": units, "de": de, "de_source": sources, "tok_de": tok_de,
    "findings": [{"id": k, "claim": v["claim_de"], "kind": v.get("kind"), "confidence": v.get("confidence"),
                  "subject": v.get("subject"), "caveat": v.get("confidence_rationale_de")} for k, v in sorted(findings.items())],
    "interpretations": [{"id": k, "claim": v["claim_de"], "confidence": v.get("confidence"), "caveat": v.get("caveat_de"),
                         "counter": v.get("counterarguments_de", []), "based_on": v.get("based_on", []),
                         "subject": v.get("subject")} for k, v in sorted(ints.items())],
    "principles": [{"id": k, "text": v["statement_de"], "confidence": v.get("confidence"),
                    "derived_from": v.get("derived_from", [])} for k, v in prin.items()],
    "applications": [{"id": k, "text": v["statement_de"], "limits": v.get("limitations_de"), "principle": v.get("principle"),
                      "context": ctx.get(v.get("context"), {}).get("audience"),
                      "confidence": v.get("confidence")} for k, v in apps.items()],
    "relations": [{"to": v["to_ref"], "kind": v["relation"], "confidence": v.get("confidence")} for v in rels.values()],
    "questions": [{"q": v["question_de"], "finding": v.get("finding_de")} for v in qs.values()],
    "method": {"name": method["name_de"], "question": method["question_de"], "limits": method["assumptions_and_limits_de"]},
    "editions": editions,
}
OUT.mkdir(parents=True, exist_ok=True)
(OUT / "data.json").write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
html = (OUT / "template.html").read_text(encoding="utf-8").replace(
    "/*__DATA__*/null", json.dumps(data, ensure_ascii=False).replace("</", "<\\/"))
(OUT / "mk3-20-35.html").write_text(html, encoding="utf-8")
print(f"PASS: Prototyp gebaut: {len(words)} Wörter, {len(units)} Variantenstellen, {len(de)} Verse deutsch -> app/prototype/mk3-20-35.html")
