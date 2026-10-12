#!/usr/bin/env python3
"""Baut den Lesestrom (app/reading-stream/index.html) aus Vorlage und Projektdaten.

Eingebettet werden:
- Navigationsgerüst (data/navigation/NAV-PROT66-KJV.json)
- Zusammenfassungen (data/summaries/*.json)
- Studienprojektion Markus 3,20–35 aus scripts/build_prototype.py
- Hintergrundnotizen (data/background/*.json), Stellen für die Anzeige aufbereitet

Die Vorlage app/reading-stream/template.html bearbeiten, danach dieses Skript ausführen.
Erzeugte Datei nicht von Hand ändern.
"""
import json
import pathlib
import runpy
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import refs  # noqa: E402
study = runpy.run_path(str(ROOT / "scripts/build_prototype.py"))["data"]
nav = json.loads((ROOT / "data/navigation/NAV-PROT66-KJV.json").read_text(encoding="utf-8"))
summaries = {}
for p in sorted((ROOT / "data/summaries").glob("*.json")):
    s = json.loads(p.read_text(encoding="utf-8"))
    summaries[s["id"]] = {"text": s["text_de"], "status": s["status"]}

section_id = study["section"]["id"]
contexts = {p.stem: json.loads(p.read_text(encoding="utf-8")) for p in (ROOT / "data/contexts").glob("*.json")}
background = []
for p in sorted((ROOT / "data/background").glob("*.json")):
    b = json.loads(p.read_text(encoding="utf-8"))
    ref = b["reference"]
    assert ref.startswith("MRK.3."), ref  # Anzeige bisher nur für die Pilotstelle
    a, _, z = ref.partition("-")
    background.append({"id": b["id"], "topic": b["topic_de"], "text": b["text_de"], "uncertain": b.get("uncertain_de"),
                       "confidence": b.get("confidence"), "subject": b["subject"], "wide": b["subject"] == section_id,
                       "from": int(a.split(".")[2]), "to": int((z or a).split(".")[2]), "ref_de": refs.display_de(ref),
                       "readers": "READERS" in b["context"],
                       "evidence": [refs.display_de(r) for r in b.get("evidence_refs", [])],
                       "sources": b.get("sources_de", []), "status": b["status"]})

template = (ROOT / "app/reading-stream/template.html").read_text(encoding="utf-8")
dump = lambda o: json.dumps(o, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
for marker, payload in (("/*__MARKUS__*/null", study), ("/*__NAV__*/null", nav), ("/*__SUMMARIES__*/null", summaries),
                        ("/*__BACKGROUND__*/null", background)):
    assert template.count(marker) == 1, marker
    template = template.replace(marker, dump(payload))
(ROOT / "app/reading-stream/index.html").write_text(template, encoding="utf-8")
print(f"PASS: Lesestrom gebaut: {len(nav['books'])} Bücher, {len(summaries)} Zusammenfassungen, {len(background)} Hintergrundnotizen, Markus 3,20–35 eingebunden.")
