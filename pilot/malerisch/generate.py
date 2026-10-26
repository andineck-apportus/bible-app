#!/usr/bin/env python3
"""Pilot «malerische Bilder»: setzt aus Regie (szenen.json) und Stil (stile.json) die Prompts zusammen und lässt
die Bilder über die Replicate-API erzeugen. Nur Standardbibliothek.

Beispiele:
  python3 pilot/malerisch/generate.py --trocken                       # nur Prompts zeigen, nichts aufrufen
  REPLICATE_API_TOKEN=… python3 pilot/malerisch/generate.py           # alle Szenen, alle Stile, mit Tiefenvorlage
  REPLICATE_API_TOKEN=… python3 pilot/malerisch/generate.py --stile oel --szenen A,D --modell schnell

Modelle (--modell):
  tiefe   black-forest-labs/flux-depth-pro  – hält sich an die Kompositionsvorlage (Standard)
  pro     black-forest-labs/flux-1.1-pro    – nur Text, höchste Bildqualität
  schnell black-forest-labs/flux-schnell    – nur Text, sehr günstig (Apache-2.0-Modell), für schnelle Vorversuche

Ergebnis: pilot/malerisch/ausgabe/<lauf>/ mit den Bildern, lauf.json (Prompts, Modell, Seed, Zeit) und
kontaktbogen.html zum Vergleichen.
"""
import argparse
import base64
import datetime
import html
import json
import os
import pathlib
import sys
import time
import urllib.error
import urllib.request

HIER = pathlib.Path(__file__).resolve().parent
API = "https://api.replicate.com/v1"

MODELLE = {
    "tiefe": {"slug": "black-forest-labs/flux-depth-pro", "steuerung": True},
    "pro": {"slug": "black-forest-labs/flux-1.1-pro", "steuerung": False},
    "schnell": {"slug": "black-forest-labs/flux-schnell", "steuerung": False},
}


def lade(name):
    return json.loads((HIER / name).read_text(encoding="utf-8"))


def prompt_fuer(szene, stil, regie, stile):
    figuren = "; ".join(regie["figuren_en"][f] for f in szene["figuren"] if f in regie["figuren_en"])
    teile = [
        stil["prompt_en"],
        szene["szene_en"],
        szene["hintergrund_en"],
        f"Characters: {figuren}.",
        f"Lighting: {szene['licht_en']}.",
        f"Camera: {szene['kamera_en']}.",
        f"Emotional core: {szene['gefuehl_en']}.",
    ]
    if "FIG-JESUS" in szene["figuren"]:
        teile.append(f"Jesus: {regie['gesichter']['jesus_en']}.")
    teile.append(stile["allgemein_en"])
    teile.append(szene["vermeiden_en"][0].upper() + szene["vermeiden_en"][1:] + ".")
    teile.append(f"Avoid: {stile['negativ_en']}.")
    return " ".join(teile)


def eingaben(modell, prompt, szene, seed):
    if modell == "tiefe":
        png = (HIER / "vorlagen" / f"{szene['id']}.png").read_bytes()
        return {"prompt": prompt, "control_image": "data:image/png;base64," + base64.b64encode(png).decode(),
                "steps": 50, "guidance": 15, "seed": seed, "output_format": "png", "safety_tolerance": 2}
    if modell == "pro":
        return {"prompt": prompt, "aspect_ratio": "3:2", "output_format": "png", "seed": seed, "safety_tolerance": 2}
    return {"prompt": prompt, "aspect_ratio": "3:2", "output_format": "png", "seed": seed, "num_outputs": 1}


def anfrage(methode, url, token, daten=None):
    req = urllib.request.Request(url, method=methode, data=json.dumps(daten).encode() if daten else None, headers={
        "Authorization": f"Bearer {token}", "Content-Type": "application/json", "Prefer": "wait=60"})
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"HTTP {e.code} bei {url}: {e.read().decode(errors='replace')[:500]}") from None


def erzeuge(modell, inputs, token):
    p = anfrage("POST", f"{API}/models/{MODELLE[modell]['slug']}/predictions", token, {"input": inputs})
    while p.get("status") not in ("succeeded", "failed", "canceled"):
        time.sleep(3)
        p = anfrage("GET", p["urls"]["get"], token)
    if p["status"] != "succeeded":
        raise RuntimeError(f"Bild nicht erzeugt ({p['status']}): {p.get('error')}")
    out = p["output"]
    return out[0] if isinstance(out, list) else out


def kontaktbogen(lauf_dir, eintraege, regie, stile):
    zeilen = []
    for sz in regie["szenen"]:
        zellen = []
        for e in [e for e in eintraege if e["szene"] == sz["id"]]:
            bild = f'<img src="{html.escape(e["datei"])}" alt="">' if e.get("datei") else f'<div class="fehler">{html.escape(e.get("fehler", ""))}</div>'
            zellen.append(f'<figure>{bild}<figcaption>{html.escape(stile["stile"][e["stil"]]["name_de"])} · {e["modell"]} · Seed {e["seed"]}</figcaption></figure>')
        (lauf_dir / f"vorlage-{sz['id']}.png").write_bytes((HIER / "vorlagen" / f"{sz['id']}.png").read_bytes())
        vorlage = f'<figure><img src="vorlage-{sz["id"]}.png" alt=""><figcaption>Kompositionsvorlage</figcaption></figure>'
        zeilen.append(f'<section><h2>{html.escape(sz["titel_de"])} <small>{sz["reference"]}</small></h2>'
                      f'<p>{html.escape(sz["regie_de"])}</p><div class="reihe">{vorlage}{"".join(zellen)}</div></section>')
    (lauf_dir / "kontaktbogen.html").write_text(
        '<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
        '<title>Bildpilot Johannes 2</title><style>body{font:15px/1.5 system-ui;margin:16px;background:#111;color:#eee}'
        'h2{font-weight:600;margin:28px 0 4px}small{color:#999;font-weight:400}p{max-width:70ch;color:#bbb}'
        '.reihe{display:flex;gap:12px;overflow-x:auto}figure{margin:0;flex:0 0 min(90vw,520px)}img{width:100%;border-radius:6px}'
        'figcaption{font-size:13px;color:#999}.fehler{color:#f88;padding:20px;border:1px solid #633}</style>'
        f'<h1>Bildpilot Johannes 2 – Lauf {html.escape(lauf_dir.name)}</h1>{"".join(zeilen)}', encoding="utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--stile", default="oel,aquarell,holzschnitt")
    ap.add_argument("--szenen", default="alle", help="z. B. A,D oder alle")
    ap.add_argument("--modell", default="tiefe", choices=sorted(MODELLE))
    ap.add_argument("--varianten", type=int, default=1, help="Bilder je Szene und Stil (verschiedene Seeds)")
    ap.add_argument("--seed", type=int, default=2026)
    ap.add_argument("--trocken", action="store_true", help="nur Prompts ausgeben")
    a = ap.parse_args()

    regie, stile = lade("szenen.json"), lade("stile.json")
    wahl = None if a.szenen == "alle" else {s.strip().upper() for s in a.szenen.split(",")}
    szenen = [s for s in regie["szenen"] if wahl is None or s["id"].rsplit("-", 1)[1] in wahl]
    stilnamen = [s.strip() for s in a.stile.split(",") if s.strip()]
    unbekannt = [s for s in stilnamen if s not in stile["stile"]]
    if unbekannt or not szenen:
        sys.exit(f"Unbekannte Stile {unbekannt} oder keine Szene gewählt ({a.szenen}).")

    auftraege = [(sz, st, a.seed + v) for sz in szenen for st in stilnamen for v in range(a.varianten)]
    if a.trocken:
        for sz, st, seed in auftraege:
            print(f"\n## {sz['id']} · {st} · Seed {seed}\n{prompt_fuer(sz, stile['stile'][st], regie, stile)}")
        print(f"\n{len(auftraege)} Bilder mit Modell «{a.modell}» ({MODELLE[a.modell]['slug']}).")
        return

    token = os.environ.get("REPLICATE_API_TOKEN")
    if not token:
        sys.exit("REPLICATE_API_TOKEN fehlt (als Umgebungsvariable bzw. GitHub-Secret hinterlegen).")
    lauf = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%d-%H%M%S") + f"-{a.modell}"
    lauf_dir = HIER / "ausgabe" / lauf
    lauf_dir.mkdir(parents=True, exist_ok=True)
    eintraege, fehler = [], 0
    for sz, st, seed in auftraege:
        prompt = prompt_fuer(sz, stile["stile"][st], regie, stile)
        e = {"szene": sz["id"], "brief": sz["brief"], "panel": sz["panel"], "reference": sz["reference"], "stil": st,
             "modell": a.modell, "modell_slug": MODELLE[a.modell]["slug"], "seed": seed, "prompt": prompt,
             "steuerbild": f"vorlagen/{sz['id']}.png" if MODELLE[a.modell]["steuerung"] else None}
        try:
            url = erzeuge(a.modell, eingaben(a.modell, prompt, sz, seed), token)
            datei = f"{sz['id']}__{st}__{seed}.png"
            with urllib.request.urlopen(url, timeout=120) as r:
                (lauf_dir / datei).write_bytes(r.read())
            e["datei"] = datei
            print("ok   ", sz["id"], st, seed)
        except Exception as ex:  # ein fehlgeschlagenes Bild bricht den Lauf nicht ab
            e["fehler"] = str(ex)
            fehler += 1
            print("FEHLER", sz["id"], st, seed, ex, file=sys.stderr)
        eintraege.append(e)
    (lauf_dir / "lauf.json").write_text(json.dumps({
        "lauf": lauf, "erzeugt": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
        "hinweis_de": "KI-generierte Pilotbilder, nicht geprüft und nicht in der App. Bildliche Deutung, keine Darstellung historischer Tatsachen.",
        "bilder": eintraege}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    kontaktbogen(lauf_dir, eintraege, regie, stile)
    print(f"\n{len(eintraege) - fehler} von {len(eintraege)} Bildern erzeugt → {lauf_dir}")
    if fehler == len(eintraege):
        sys.exit(1)


if __name__ == "__main__":
    main()
