#!/usr/bin/env python3
"""Bilder im Aquarellstil ohne Handarbeit: malen, prüfen, wählen, ablegen, Blasen setzen, Schlussprüfung (docs/BILDSTIL.md).

Läuft in der GitHub-Action «bilder-aquarell» (OPENAI_API_KEY). Zwei Schritte:

  neu      --szenen JHN-002-K1,… --varianten 2 --runden 3
           Je Szene Varianten malen und automatisch prüfen (bilder_pruefung.py). Gewählt wird die Variante, die alle
           Pflichtregeln erfüllt, mit den meisten Punkten. Erfüllt keine, wird mit einem Hinweis aus den verfehlten Regeln
           neu gemalt (höchstens --runden). Danach wie «pruefen».
  pruefen  --szenen alle [--erzwingen]
           Die abgelegten Bilder prüfen (nur, wenn Bild, Regeln oder Szenenplan sich geändert haben, oder mit --erzwingen),
           Blasen nach den Kopfpositionen setzen, Bilder schreiben, jede Kachel rendern und schlussprüfen, Prüfstufe in den
           Datensatz.

Ergebnis: geänderte Dateien in data/ und bilder_aquarell_daten/auswahl.json (die Action pusht sie auf einen eigenen Branch),
Bericht ausgabe/aquarell/<lauf>/bericht.html mit allen Varianten, Antworten und gerenderten Kacheln.
"""
import argparse
import datetime
import html
import json
import os
import pathlib
import subprocess
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import bilder_aquarell as BA  # noqa: E402
import bilder_pruefung as BP  # noqa: E402

ROOT = BA.ROOT
DATEN = BA.DATEN
JETZT = datetime.datetime.now(datetime.timezone.utc)


def kontext():
    plaene = BA.plaene()
    fig0, allg = BA.lade(DATEN / "figuren.json"), BA.lade(DATEN / "pruefregeln.json")
    szenen, momente, band, fig = {}, {}, {}, {}
    for name, pd in plaene.items():
        for sid, sz in pd["szenen"].items():
            szenen[sid] = (name, sz)
            fig[sid] = BA.fig_fuer(fig0, pd)
        for b in pd["bilder"]:
            panels = BA.lade(BA.D / f"briefs/{b['brief']}.json")["panels"]
            for sid, p_ in zip(b["felder"], panels):
                momente.setdefault(sid, p_["action_de"])
                band.setdefault(sid, (b["felder"].index(sid) + 1, b.get("band", {}).get(sid) or pd["szenen"][sid].get("band") or p_.get("keywords") or {}))
    return plaene, fig, allg, szenen, momente, band


def stempel(pr, sz, fig, allg):  # fig: Figurenangaben der Szene
    pr["datum"] = JETZT.date().isoformat()
    pr["plan_sha"] = BP.plan_fingerabdruck(sz, fig, allg)
    pr["regeln_version"] = allg["version"]
    pr["prozess"] = BP.PROZESS
    return pr


def kachel_png(sid, sz, a, band):
    n, kw = band
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {BA.W} {BA.H + BA.BAND}">' + BA.kachel(n, sid, sz, {sid: a}, kw, 0, 0) + "</svg>"
    return BP.rendere(svg, BA.OUT)


def schreibe_auswahl(aus):
    (DATEN / "auswahl.json").write_text(json.dumps(aus, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def blasen_und_schluss(sids, aus, fig, szenen, momente, band, schluessel, out, bericht, streng=False, behalten=False):
    """behalten (Neuprüfung unveränderter Bilder): findet die neue Ortung keinen Platz, bleibt die bisherige, vollständige
    Anordnung; die Ortung der Köpfe schwankt zwischen Läufen (Lauf 30, Joh 2 K3: Blase fiel weg)."""
    zweiter = []
    for sid in sids:
        _, sz = szenen[sid]
        a = aus[sid]
        e = bericht.setdefault(sid, {})
        if a.get("blasen") != "hand" and sz.get("speech"):
            pr_ = a.get("pruefung") or {}
            bl, fehler = BA.blasen_auto(sz["speech"], pr_.get("koepfe", {}), [p_.get("head") for p_ in pr_.get("personen", [])], streng=streng,
                                        belegt=BA.belegung(BA.OUT / a["datei"]))
            alt_bl = a.get("blasen_auto")
            if fehler and behalten and isinstance(alt_bl, list) and len(alt_bl) == len(sz["speech"]) and all(alt_bl):
                bl, fehler = alt_bl, []
                e["blasen_behalten"] = True
            a["blasen_auto"] = bl
            e["blasen_fehler"] = fehler
        png = kachel_png(sid, sz, a, band[sid])
        (out / f"{sid}__kachel.png").write_bytes(png)
        e["kachel"] = f"{sid}__kachel.png"
        try:
            a["schluss"] = BP.pruefe_kachel(schluessel, png, sz.get("speech", []), fig[sid], momente[sid])
            a["schluss"]["datum"] = JETZT.date().isoformat()
            a["schluss"]["prozess"] = BP.PROZESS
            if len(sz.get("speech", [])) > 1 and not BA.reihe_ok(sz["speech"], (a.get("pruefung") or {}).get("koepfe", {})):
                a["schluss"]["ergebnis"] = "durchgefallen"
                a["schluss"]["regeln"].append({"id": "S-REIHE", "ebene": "kachel", "stufe": "pflicht", "de": "Wer zuerst spricht, steht links",
                                                "ergebnis": "fehler", "antwort": None, "grund": "Sprecher in falscher Reihenfolge"})
            if e.get("blasen_fehler"):
                a["schluss"]["ergebnis"] = "durchgefallen"
                a["schluss"]["regeln"].append({"id": "S-PLATZ", "ebene": "kachel", "stufe": "pflicht", "de": "Platz für alle Blasen",
                                                "ergebnis": "fehler", "antwort": None, "grund": "; ".join(e["blasen_fehler"])})
            e["schluss"] = a["schluss"]
            print(f"schluss {sid}: {a['schluss']['ergebnis']} (Kern {a['schluss'].get('kern')}){' streng' if streng else ''}")
            blasen_falsch = any(r["ergebnis"] != "ok" and (r["id"].startswith("B") or r["id"] in ("S-GESICHT", "S-PLATZ")) for r in a["schluss"]["regeln"])
            if blasen_falsch and not streng and a.get("blasen") != "hand" and sz.get("speech"):
                zweiter.append(sid)
        except Exception as ex:
            BP.melde(f"{sid} Schlussprüfung: {ex}")
            e["schluss_fehler"] = str(ex)
    if zweiter:  # zweiter Versuch: Blasen nur im oberen Band, Köpfe mit grossem Rand
        alt = {s: (aus[s].get("blasen_auto"), aus[s].get("schluss")) for s in zweiter}
        blasen_und_schluss(zweiter, aus, fig, szenen, momente, band, schluessel, out, {}, streng=True)
        for s in zweiter:
            if (aus[s].get("schluss") or {}).get("ergebnis") != "bestanden" and (alt[s][1] or {}).get("punkte", 0) > (aus[s].get("schluss") or {}).get("punkte", 0):
                aus[s]["blasen_auto"], aus[s]["schluss"] = alt[s]


def pruefen(a, schluessel, out):
    plaene, fig, allg, szenen, momente, band = kontext()
    aus = BA.lade(DATEN / "auswahl.json")
    sids = [s for s in (aus if a.szenen == "alle" else a.szenen.split(",")) if s in aus and s in szenen]
    bericht = {}
    for sid in sids:
        _, sz = szenen[sid]
        bild = BA.OUT / aus[sid]["datei"]
        alt = aus[sid].get("pruefung") or {}
        aktuell = (alt.get("bild_sha") == BP.sha(bild.read_bytes()) and alt.get("plan_sha") == BP.plan_fingerabdruck(sz, fig[sid], allg)
                   and alt.get("regeln_version") == allg["version"])
        if aktuell and not a.erzwingen:
            print(f"aktuell {sid}")
            continue
        try:
            pr = stempel(BP.pruefe_feld(schluessel, bild, sz, fig[sid], allg, momente[sid]), sz, fig[sid], allg)
            aus[sid]["pruefung"] = pr
            bericht[sid] = {"varianten": [{"datei": None, "pruefung": pr}]}
            print(f"feld {sid}: {pr['ergebnis']} ({pr['punkte']} Punkte)")
        except Exception as ex:
            BP.melde(f"{sid}: {ex}")
    blasen_und_schluss(sids, aus, fig, szenen, momente, band, schluessel, out, bericht, behalten=True)
    schreibe_auswahl(aus)
    return bericht


def neu(a, schluessel, out):
    import bilder_aquarell_gen as G
    plaene, fig, allg, szenen, momente, band = kontext()
    bericht, gewaehlt = {}, {}
    for sid in a.szenen.split(","):
        sid = sid.strip()
        name, sz = szenen[sid]
        vorlagen = G.vorlagen_fuer(plaene[name])
        hinweis, beste = a.hinweis, None
        e = bericht.setdefault(sid, {"varianten": []})
        for runde in range(1, a.runden + 1):
            prompt = G.auftrag_feld(sz, fig[sid], len(vorlagen) > 1) + (f"\n\nADDITIONAL INSTRUCTION FOR THIS RUN: {hinweis}" if hinweis else "")
            try:
                m, bilder = G.male(prompt, vorlagen, schluessel, a.varianten)
            except Exception as ex:
                BP.melde(f"{sid} malen: {ex}")
                break
            for k, b in enumerate(bilder, 1):
                var = f"r{runde}v{k}"
                (out / f"{sid}__{var}.png").write_bytes(b)
                try:
                    pr = stempel(BP.pruefe_feld(schluessel, b, sz, fig[sid], allg, momente[sid]), sz, fig[sid], allg)
                except Exception as ex:
                    BP.melde(f"{sid} {var} prüfen: {ex}")
                    continue
                pr["modell_bild"] = m
                if len(sz.get("speech", [])) > 1 and not BA.reihe_ok(sz["speech"], pr.get("koepfe", {})):
                    pr["regeln"].append({"id": "S-REIHE", "ebene": "kachel", "stufe": "pflicht", "de": "Wer zuerst spricht, steht links",
                                         "ergebnis": "fehler", "antwort": None, "grund": "the first speaker must stand LEFT of the second speaker"})
                    pr["ergebnis"] = "durchgefallen"
                if sz.get("speech"):  # feste Prüfung: Platz für alle Blasen, sonst unbrauchbar (Joh 2 T2, Lauf 19)
                    _, bf = BA.blasen_auto(sz["speech"], pr.get("koepfe", {}), [p_.get("head") for p_ in pr.get("personen", [])], belegt=BA.belegung(b))
                    if bf:
                        pr["regeln"].append({"id": "S-PLATZ", "ebene": "kachel", "stufe": "pflicht", "de": "Platz für alle Blasen über den Köpfen",
                                             "ergebnis": "fehler", "antwort": None, "grund": "; ".join(bf) + " – leave more empty white paper above the heads"})
                        pr["ergebnis"] = "durchgefallen"
                e["varianten"].append({"datei": f"{sid}__{var}.png", "runde": runde, "pruefung": pr, "hinweis": hinweis})
                print(f"{sid} {var}: {pr['ergebnis']} ({pr['punkte']} Punkte)")
                rang = ({"bestanden": 2, "unklar": 1}.get(pr["ergebnis"], 0), pr["punkte"])
                if beste is None or rang > beste[0]:
                    beste = (rang, var, pr, m)
            if beste and beste[0][0] == 2:
                break
            if beste:
                hinweis = (a.hinweis + "\n" if a.hinweis else "") + BP.hinweis_aus(beste[2])
        if beste and (beste[0][0] == 2 or a.auch_unklar and beste[0][0] == 1):
            gewaehlt[sid] = beste
            e["gewaehlt"] = beste[1]
        else:
            e["gewaehlt"] = None
            BP.melde(f"{sid}: keine Variante hat alle Pflichtregeln erfüllt – nicht übernommen")
    meta = {"lauf": out.name, "bilder": [{"szene": s, "modell": g[3]} for s, g in gewaehlt.items()]}
    # Übernehmen braucht lauf.json mit Modell; Dateinamen Szene__Variante.png
    (out / "lauf.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if gewaehlt:
        BA.uebernehmen(out, [f"{s}={g[1]}" for s, g in gewaehlt.items()], {(s, g[1]): g[2] for s, g in gewaehlt.items()})
        aus = BA.lade(DATEN / "auswahl.json")
        for s in gewaehlt:  # Prüfung bezieht sich auf das abgelegte (verkleinerte) Bild
            aus[s]["pruefung"]["bild_sha"] = BP.sha((BA.OUT / aus[s]["datei"]).read_bytes())
            aus[s]["pruefung"]["bild_sha_quelle"] = "png vor Verkleinerung geprüft"
        subprocess.run([sys.executable, str(ROOT / "scripts/authoring/bilder_aquarell.py")], check=True)
        blasen_und_schluss(list(gewaehlt), aus, fig, szenen, momente, band, schluessel, out, bericht)
        schreibe_auswahl(aus)
    return bericht


def kalibrieren(a, schluessel, out):
    """Prüfmodell am Prüfsatz messen (bilder_kalibrierung/faelle.json): nur Feldprüfung, nichts wird übernommen."""
    import time
    plaene, fig, allg, szenen, momente, band = kontext()
    K = pathlib.Path(__file__).resolve().parent / "bilder_kalibrierung"
    faelle = json.loads((K / "faelle.json").read_text(encoding="utf-8"))["faelle"]
    erg, t0 = [], time.time()
    for f in faelle:
        if a.szenen != "alle" and f["szene"] not in a.szenen.split(","):
            continue
        _, sz = szenen[f["szene"]]
        try:
            pr = BP.pruefe_feld(schluessel, K / f["bild"], sz, fig[f["szene"]], allg, momente[f["szene"]])
        except Exception as ex:
            erg.append({**f, "fehler": str(ex)})
            BP.melde(f"{f['id']}: {ex}")
            continue
        r = {e["id"]: e["ergebnis"] for e in pr["regeln"]}
        ok_ges = (f["erwartet"] is None or (pr["ergebnis"] == "bestanden") == (f["erwartet"] == "bestanden"))
        ok_reg = {k: (r.get(k) == v if v != "nicht-ok" else r.get(k) not in (None, "ok")) for k, v in f["regeln"].items()}
        erg.append({**f, "ergebnis": pr["ergebnis"], "kern": pr.get("kern"), "stimmt": ok_ges and all(ok_reg.values()), "regeln_ist": {k: r.get(k) for k in f["regeln"]},
                    "abweichungen": [f"{e['id']} {e['ergebnis']}: {e['grund']}" for e in pr["regeln"] if e["ergebnis"] != "ok"], "blind": pr["blind"].get("story_guess")})
        print(f"{f['id']}: erwartet {f['erwartet']} {f['regeln']} → {pr['ergebnis']} {erg[-1]['regeln_ist']} {'✓' if erg[-1]['stimmt'] else '✗'}")
    zus = {"modell": BP.modelle(schluessel), "faelle": len(erg), "richtig": sum(1 for e in erg if e.get("stimmt")), "fehler": sum(1 for e in erg if "fehler" in e),
           "nutzung": dict(BP.NUTZUNG), "sekunden": round(time.time() - t0)}
    print(json.dumps(zus, ensure_ascii=False))
    (out / "kalibrierung.json").write_text(json.dumps({"zusammenfassung": zus, "faelle": erg}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if os.environ.get("GITHUB_ACTIONS"):
        BP.melde(f"Kalibrierung {zus['modell']}: {zus['richtig']} von {zus['faelle']} richtig; {zus['nutzung']['anfragen']} Anfragen, "
                 f"{zus['nutzung']['eingabe']} Eingabe- und {zus['nutzung']['ausgabe']} Ausgabe-Tokens, {zus['sekunden']} s")
    return {}


REDUKTION_EN = ("MUCH MORE REDUCED than usual (this matters most): at least two thirds of the sheet stay untouched white paper. "
                "Each figure is a few loose brush strokes and one flat pale wash; clothing has no folds, no seams, no texture; hair is one flat "
                "shape without strands; faces are a few small strokes (eyes, brows, nose, mouth, beard as one tone) that still show the feeling; "
                "hands are simple shapes. No background at all except, if needed, one single pale line or wash for the ground. "
                "Fewer, thinner, broken ink lines; leave contours open.")
STILPROBE = {"A-aktuell": (True, ""), "B-schaerfer": (True, REDUKTION_EN),
             "C-ohne-vorlage": (False, REDUKTION_EN + " (No reference image is attached: follow the STYLE text alone.)")}


def stilprobe(a, schluessel, out):
    """Stilprobe (Hinweis Andi Neck 2026-10-28: Bilder tendenziell zu detailliert): dieselben Szenen mit drei Einstellungen malen
    und prüfen – A wie bisher, B mit verschärfter Reduktion, C verschärft ohne Stilreferenz. Gemessen: Belegung (Anteil bemaltes
    Papier), Regel G-REDUKTION, Pflichtregeln, Kern. Nichts wird übernommen."""
    import bilder_aquarell_gen as G
    plaene, fig, allg, szenen, momente, band = kontext()
    bericht, zus = {}, []
    for sid in [s.strip() for s in a.szenen.split(",")]:
        name, sz = szenen[sid]
        for stil, (mit_ref, extra) in STILPROBE.items():
            vorlagen = G.vorlagen_fuer(plaene[name]) if mit_ref else []
            prompt = G.auftrag_feld(sz, fig[sid], len(vorlagen) > 1)
            if not mit_ref:
                prompt = prompt.split("\n\nThe first attached image")[0]
            prompt += f"\n\nREDUCTION: {extra}" if extra else ""
            try:
                m, bilder = G.male(prompt, vorlagen, schluessel, a.varianten)
            except Exception as ex:
                BP.melde(f"{sid} {stil} malen: {ex}")
                continue
            e = bericht.setdefault(f"{sid} · {stil}", {"varianten": []})
            for k, b in enumerate(bilder, 1):
                datei = f"{sid}__{stil}__v{k}.png"
                (out / datei).write_bytes(b)
                try:
                    pr = BP.pruefe_feld(schluessel, b, sz, fig[sid], allg, momente[sid])
                except Exception as ex:
                    BP.melde(f"{sid} {stil} prüfen: {ex}")
                    continue
                bel = round(float(BA.belegung(b).mean()), 3)
                red = next((x["ergebnis"] for x in pr["regeln"] if x["id"] == "G-REDUKTION"), None)
                e["varianten"].append({"datei": datei, "pruefung": pr, "belegung": bel})
                zus.append({"szene": sid, "stil": stil, "datei": datei, "belegung": bel, "reduktion": red, "ergebnis": pr["ergebnis"], "kern": pr.get("kern"),
                            "pflicht_offen": [x["id"] for x in pr["regeln"] if x["stufe"] == "pflicht" and x["ergebnis"] != "ok"]})
                print(f"{sid} {stil} v{k}: Belegung {bel}, G-REDUKTION {red}, {pr['ergebnis']}, Kern {pr.get('kern')}")
    (out / "stilprobe.json").write_text(json.dumps({"nutzung": dict(BP.NUTZUNG), "bilder": zus}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for stil in STILPROBE:
        z = [x for x in zus if x["stil"] == stil]
        if z:
            BP.melde(f"Stilprobe {stil}: Belegung im Mittel {sum(x['belegung'] for x in z) / len(z):.2f}, G-REDUKTION ok {sum(x['reduktion'] == 'ok' for x in z)}/{len(z)}, "
                     f"bestanden {sum(x['ergebnis'] == 'bestanden' for x in z)}/{len(z)}")
    return bericht


def bericht_html(out, bericht, titel):
    def zeile(e):
        return "".join(f'<li class="{x["ergebnis"]}"><b>{html.escape(x["id"])}</b> {html.escape(x["de"])}: {html.escape(str(x["antwort"]))}'
                       f' – <i>{html.escape(str(x["grund"]))}</i></li>' for x in e["regeln"] if x["ergebnis"] != "ok")
    teile = []
    for sid, e in bericht.items():
        teile.append(f"<h2>{html.escape(sid)}</h2>")
        for v in e.get("varianten", []):
            pr = v["pruefung"]
            img = f'<img src="{html.escape(v["datei"])}">' if v.get("datei") else ""
            gew = " ✔ gewählt" if v.get("datei") and e.get("gewaehlt") and v["datei"].endswith(f'__{e["gewaehlt"]}.png') else ""
            teile.append(f'<div class="v">{img}<p><b>{html.escape(v.get("datei") or "abgelegtes Bild")}</b>{gew}: {pr["ergebnis"]}, '
                         f'{pr["punkte"]} Punkte, Kern {pr.get("kern")} {html.escape(pr.get("kern_fehlt_de") or "")}</p>'
                         f'<p class="blind">Blind: {html.escape(str(pr["blind"].get("action")))} – {html.escape(str(pr["blind"].get("story_guess")))}</p>'
                         f'<ul>{zeile(pr)}</ul></div>')
        if e.get("kachel"):
            sl = e.get("schluss") or {}
            teile.append(f'<div class="v"><img src="{e["kachel"]}"><p><b>Kachel</b>: {sl.get("ergebnis", e.get("schluss_fehler"))}, Kern {sl.get("kern")} '
                         f'{html.escape(sl.get("kern_fehlt_de") or "")}</p><ul>{zeile(sl) if sl else ""}</ul></div>')
    (out / "bericht.html").write_text(
        f'<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{titel}</title>'
        '<style>body{font:15px system-ui;margin:16px;max-width:1100px}img{width:min(100%,640px);border:1px solid #ddd}'
        '.v{margin:0 0 24px}.fehler{color:#a00}.unklar{color:#a60}.blind{color:#555}</style>'
        f'<h1>{titel}</h1>' + "".join(teile), encoding="utf-8")
    (out / "bericht.json").write_text(json.dumps(bericht, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("schritt", choices=["neu", "pruefen", "kalibrieren", "stilprobe"])
    ap.add_argument("--szenen", default="alle")
    ap.add_argument("--varianten", type=int, default=2)
    ap.add_argument("--runden", type=int, default=3)
    ap.add_argument("--hinweis", default="")
    ap.add_argument("--erzwingen", action="store_true")
    ap.add_argument("--auch-unklar", action="store_true", help="auch Varianten mit unklarer Pflichtregel übernehmen")
    a = ap.parse_args()
    schluessel = os.environ.get("OPENAI_API_KEY")
    if not schluessel:
        BP.melde("OPENAI_API_KEY fehlt.")
        sys.exit(1)
    lauf = JETZT.strftime("%Y%m%d-%H%M%S") + f"-auto-{a.schritt}"
    out = ROOT / "ausgabe/aquarell" / lauf
    out.mkdir(parents=True, exist_ok=True)
    if a.schritt == "kalibrieren":
        kalibrieren(a, schluessel, out)
        return
    if a.schritt == "stilprobe":
        bericht_html(out, stilprobe(a, schluessel, out), f"Stilprobe {lauf}")
        return
    bericht = neu(a, schluessel, out) if a.schritt == "neu" else pruefen(a, schluessel, out)
    subprocess.run([sys.executable, str(ROOT / "scripts/authoring/bilder_aquarell.py")], check=True)
    bericht_html(out, bericht, f"Bildlauf {lauf}")
    print(f"Bericht: {out / 'bericht.html'}")


if __name__ == "__main__":
    main()
