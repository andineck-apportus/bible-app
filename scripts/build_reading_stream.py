#!/usr/bin/env python3
"""Baut den Lesestrom (app/reading-stream/index.html) aus Vorlage und Projektdaten.

Eingebettet werden:
- Navigationsgerüst (data/navigation/NAV-PROT66-KJV.json)
- Zusammenfassungen (data/summaries/*.json)
- Studienprojektion Markus 3,20–35 aus scripts/build_prototype.py

Die Vorlage app/reading-stream/template.html bearbeiten, danach dieses Skript ausführen.
Erzeugte Datei nicht von Hand ändern.
"""
import json
import pathlib
import runpy

ROOT = pathlib.Path(__file__).resolve().parents[1]
study = runpy.run_path(str(ROOT / "scripts/build_prototype.py"))["data"]
nav = json.loads((ROOT / "data/navigation/NAV-PROT66-KJV.json").read_text(encoding="utf-8"))
summaries = {}
for p in sorted((ROOT / "data/summaries").glob("*.json")):
    s = json.loads(p.read_text(encoding="utf-8"))
    summaries[s["id"]] = {"text": s["text_de"], "status": s["status"]}

template = (ROOT / "app/reading-stream/template.html").read_text(encoding="utf-8")
dump = lambda o: json.dumps(o, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
for marker, payload in (("/*__MARKUS__*/null", study), ("/*__NAV__*/null", nav), ("/*__SUMMARIES__*/null", summaries)):
    assert template.count(marker) == 1, marker
    template = template.replace(marker, dump(payload))
(ROOT / "app/reading-stream/index.html").write_text(template, encoding="utf-8")
print(f"PASS: Lesestrom gebaut: {len(nav['books'])} Bücher, {len(summaries)} Zusammenfassungen, Markus 3,20–35 eingebunden.")
