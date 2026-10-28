#!/usr/bin/env python3
"""Einzelporträts für das Bildlexikon im Aquarellstil (docs/BILDSTIL.md, Abschnitt 4; PROC-BILD-AQUARELL 2.4).

Entscheid Andi Neck 2026-10-28: Jeder Lexikon-Eintrag, den der Aquarellstil zeichnet (alle «renderings» von
ILLSTYLE-AQUARELL), erhält ein eigenes gemaltes Bild – Personen als Ganzkörper- bzw. Kniestück-Porträt, Gruppen als
kleine Gruppe, Gegenstände, Orte und Zeichen als Vignette, alles auf warmweissem Papier. Vorlagen beim Malen: die
Stilreferenz und, für die Personen von Joh 2, das Figurenblatt, damit sie gleich aussehen wie in den Szenen.

Ablauf je Eintrag (Schritt «figuren» von bilder_aquarell_lauf.py, Action «bilder-aquarell» → «auto-figuren»):
  1. Varianten malen (Hochformat 1024×1536).
  2. Blind: eine weitere Instanz beschreibt das Bild, ohne Beschreibung oder Namen zu kennen.
  3. Regeln: allgemeine Regeln (pruefregeln.json, ohne die szenenbezogenen), Porträtregeln je Art und für alle
     (portraets.json: eine Person bzw. kleine Gruppe bzw. Vignette, entspricht der Beschreibung, keine zusätzlichen
     Attribute, passt zum Lexikon), Figurenregeln (figuren.json «pruef», Porträt-Ersatz aus portraets.json).
     Verfehlte Pflichtregeln fragt die zweite Instanz noch zweimal (Mehrheit), wie bei den Szenen.
  4. Kern: Ein Textvergleich bewertet, ob die Blindbeschreibung zur Beschreibung passt (0–2, mindestens 1).
  5. Wahl: bestandene Variante mit den meisten Punkten; sonst neu malen mit Hinweis aus den verfehlten Regeln
     (höchstens --runden). Ohne bestandene Variante wird nichts abgelegt.
  6. Ablage: data/illustrations/aquarell/figuren/<ID>.webp (384×576) und im Stil-Datensatz renderings[ID].image und
     .check (Datum, Ergebnis, Regeln, Grenzen, Fingerabdrücke von Bild und Auftrag).

Die Szenen verwenden geprüfte Porträts danach als Vorlage (bilder_aquarell_gen.vorlagen_szene), aber nur, wenn die
Figur in ihrem Szenenplan dieselbe Beschreibung hat wie das Porträt.

Ohne API-Schlüssel:
  python3 scripts/authoring/bilder_aquarell_lauf.py figuren --szenen FIG-JESUS,FIG-OBJ-BOOT --trocken
  python3 scripts/authoring/bilder_aquarell_lauf.py figuren --szenen alle --trocken --platzhalter   # Ablage mit Platzhaltern
Platzhalter nie committen: sie tragen check.trocken und Stufe «entwurf».
"""
import datetime
import io
import json
import pathlib
import subprocess
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import bilder_aquarell as BA  # noqa: E402
import bilder_pruefung as BP  # noqa: E402

ROOT = BA.ROOT
DATEN = BA.DATEN
STIL = ROOT / "data/illustrations/styles/ILLSTYLE-AQUARELL.json"
ORDNER = "data/illustrations/aquarell/figuren"
LEX = ROOT / "data/illustrations/lexicon"
JETZT = datetime.datetime.now(datetime.timezone.utc)
PROZESS = "PROC-BILD-AQUARELL@2.4"
GRENZEN = ("Automatisch geprüft durch weitere Instanzen (Blindbeschreibung, Regeln, Vergleich mit Beschreibung und Lexikon); "
           "kein Test mit Leserinnen und Lesern, keine fachliche Prüfung. Alter, Kleidung und Aussehen sind Bildgestaltung (R), keine Textfakten. "
           "Ob die Figur in jeder Szene gleich aussieht, prüft erst die Szene.")


def cfg():
    return BA.lade(DATEN / "portraets.json")


def art_von(kind):
    return "einzel" if kind in ("person", "role", "divine") else "gruppe" if kind == "group" else "vignette"


def eintraege():
    """Alle Einträge des Stils: {ID: {beschreibung, kenn, pruef (Figurenregeln), art, lexikon, figurenblatt}}. Die Beschreibung
    kommt wie im Stil-Datensatz aus figuren.json, sonst aus dem (letzten) Szenenplan, der die Figur beschreibt; die
    Figurenregeln aus derselben Quelle."""
    fig = BA.lade(DATEN / "figuren.json")
    alle = BA.plaene()
    besch = BA.beschreibungen(fig, alle)
    quelle = {}
    for pd in alle.values():
        for k in pd.get("figuren", {}):
            if k not in fig["figuren"]:
                quelle[k] = pd
    import bilder_aquarell_gen as G
    out = {}
    for fid, b in besch.items():
        src = fig if fid in fig["figuren"] else quelle.get(fid, {})
        lx = BA.lade(LEX / f"{fid}.json") if (LEX / f"{fid}.json").is_file() else {}
        merk = (lx.get("legend") or {}).get("de") or " · ".join(t["trait_de"] for t in lx.get("traits", []))
        out[fid] = {"id": fid, "beschreibung": b, "kenn": (src.get("kenn_en") or {}).get(fid), "pruef": (src.get("pruef") or {}).get(fid, []),
                    "art": art_von(lx.get("kind")), "kind": lx.get("kind"), "name_de": (lx.get("names") or {}).get("de", fid), "lexikon": merk,
                    "figurenblatt": fid in G.FIGBLATT_IDS and src is fig}
    return out


def regeln(e, c=None):
    c = c or cfg()
    allg = BA.lade(DATEN / "pruefregeln.json")
    out = []
    for r in allg["regeln"]:
        if r["id"] in c["allgemein_ohne"] or (r.get("wenn") and r["wenn"] != e["id"]):
            continue
        if r["id"] == "G-PROPORTION" and e["art"] == "vignette":
            continue
        out.append({**r, "ebene": "allgemein"})
    for r in c["regeln"][e["art"]]:
        out.append({**r, "ebene": "portraet"})
    for r in c["regeln"]["alle"]:
        if r["id"] == "P-LEXIKON" and not e["lexikon"]:
            continue
        erl = c["pruef"].get(e["id"], {}).get("erlaubt_en")
        out.append({**r, "en": r["en"].replace("{beschreibung}", e["beschreibung"]).replace("{lexikon}", e["lexikon"] or "")
                    .replace("{erlaubt}", f" (also allowed: {erl})" if erl else ""), "ebene": "portraet"})
    ers = c["pruef"].get(e["id"], {})
    for r in e["pruef"]:
        if r["id"] not in ers.get("ersetzt", []):
            out.append({**r, "ebene": "figur", "figur": e["id"]})
    for r in ers.get("regeln", []):
        out.append({**r, "ebene": "figur", "figur": e["id"]})
    return out


def fingerabdruck(e, c=None):
    """Was das Porträt bestimmt: Verfahren, Beschreibung, Regeln, Malauftrag. Ändert sich etwas, gilt die Prüfung als veraltet."""
    c = c or cfg()
    return BP.sha({"verfahren": BP.VERFAHREN, "portraets": c["version"], "beschreibung": e["beschreibung"], "regeln": regeln(e, c), "auftrag": auftrag(e, c)})


def beschreibung_sha(text):
    return BP.sha({"beschreibung": text})


def auftrag(e, c=None):
    c = c or cfg()
    fig = BA.lade(DATEN / "figuren.json")
    t = c["auftrag_en"][e["art"]].replace("{beschreibung}", e["beschreibung"])
    erl = c["pruef"].get(e["id"], {}).get("erlaubt_en")
    if erl:
        t += f" Allowed in addition: {erl}."
    vorl = "The first attached image shows the drawing style (use only its style – line, wash, palette, white space; ignore its content and ages)."
    if e["figurenblatt"]:
        import bilder_aquarell_gen as G
        pos = {"FIG-MARIA-MUTTER-JESU": "the 1st person from the left", "FIG-JESUS": "the 2nd person from the left",
               "FIG-ROLLE-SPEISEMEISTER": "the 3rd person from the left", "FIG-ROLLE-BRAEUTIGAM": "the 4th person from the left",
               "FIG-GRUPPE-DIENER": "the 5th and 6th persons from the left", "FIG-GRUPPE-JUENGER": "the 7th and 8th persons from the left"}
        assert set(pos) == set(G.FIGBLATT_IDS)
        vorl += (f" The second attached image is the character sheet; this portrait shows {pos[e['id']]} on it: keep face shape, hair, beard, "
                 "apparent age and clothing colours exactly as there, but paint as loosely as the style requires. Paint ONLY "
                 "this person (or these persons) – none of the other people on the sheet, and none of their clothing or attributes (for example the "
                 "bridegroom's wreath or violet robe).")
    return f"{t}\n\nSTYLE: {fig['stil_en']}\n\n{vorl}"


def vorlagen(e):
    import bilder_aquarell_gen as G
    return [G.STILREF] + ([G.FIGBLATT] if e["figurenblatt"] and G.FIGBLATT.is_file() else [])


def stil():
    return BA.lade(STIL)


def gueltig(r, e, c=None):
    """Hat der Eintrag ein abgelegtes, bestandenes und aktuelles Porträt?"""
    ch = (r or {}).get("check") or {}
    return bool(r and r.get("image") and (ROOT / r["image"]).is_file() and ch.get("ergebnis") == "bestanden"
                and not ch.get("trocken") and ch.get("plan_sha") == fingerabdruck(e, c))


def wahl(eintr, szenen, alle_ohne_bild=True, erzwingen=False):
    if szenen in ("alle", "", None):
        if erzwingen or not alle_ohne_bild:
            return list(eintr)
        rend = stil().get("renderings", {})
        c = cfg()
        return [f for f in eintr if not gueltig(rend.get(f), eintr[f], c)]
    ids = [s.strip() for s in szenen.split(",") if s.strip()]
    fehlt = [i for i in ids if i not in eintr]
    if fehlt:
        sys.exit(f"Nicht im Aquarellstil: {fehlt} (bekannt: {', '.join(eintr)})")
    return ids


def portraets_fuer(ids, fig):
    """Geprüfte Porträts für eine Szene: [(ID, Pfad)] für Figuren, deren Beschreibung im Szenenplan (fig, nach fig_fuer)
    dieselbe ist wie die des Porträts."""
    if not STIL.is_file():
        return []
    rend = stil().get("renderings", {})
    out = []
    for fid in ids:
        r = rend.get(fid) or {}
        ch = r.get("check") or {}
        if (r.get("image") and (ROOT / r["image"]).is_file() and ch.get("ergebnis") == "bestanden" and not ch.get("veraltet") and not ch.get("trocken")
                and fid in fig.get("figuren", {}) and ch.get("beschreibung_sha") == beschreibung_sha(fig["figuren"][fid])):
            out.append((fid, ROOT / r["image"]))
    return out


# ---------------------------------------------------------------- Prüfung

SYS_KERN = "You compare a blind description of a picture with the intended description of a single figure or object for a picture lexicon. Answer in JSON."


def txt_kern(e, blind):
    return f"""Intended (English): {e['beschreibung']}

Blind description by someone who saw only the picture:
persons: {json.dumps(blind.get("persons", []), ensure_ascii=False)}
objects: {json.dumps(blind.get("objects", []), ensure_ascii=False)}
action: {blind.get("action")}

Score: 2 = the description clearly fits the intended figure or object (sex, apparent age, hair, beard, clothing colours, objects – or shape, material and number); 1 = partly (an essential feature is missing or ambiguous); 0 = it does not fit or contradicts it (for example a young woman where an older woman is intended).
Return JSON: {{"score": 0 | 1 | 2, "missing_de": what is missing or wrong, in German, short}}"""


def pruefe(schluessel, bild, e, c=None):
    c = c or cfg()
    blind = BP.frage(schluessel, BP.SYS_BLIND, BP.TXT_BLIND, bild)
    rg = regeln(e, c)
    r = BP.frage(schluessel, BP.SYS_REGELN, BP.txt_regeln(rg, [], blind), bild)
    erg = BP.zweitmeinung(schluessel, bild, rg, BP.bewerte(rg, r.get("questions", {})), [], blind)
    k = BP.frage(schluessel, SYS_KERN, txt_kern(e, blind))
    ergebnis, punkte = BP.gesamt(erg, k.get("score"), kern_pflicht=1)
    daten = bild if isinstance(bild, bytes) else pathlib.Path(bild).read_bytes()
    return {"ergebnis": ergebnis, "punkte": punkte, "kern": k.get("score"), "kern_fehlt_de": k.get("missing_de", ""), "regeln": erg,
            "blind": {k_: blind.get(k_) for k_ in ("action", "story_guess", "cut_off", "text_in_picture", "style")},
            "personen": blind.get("persons", []), "modell": BP.modelle(schluessel), "bild_sha_quelle": BP.sha(daten)}


# ---------------------------------------------------------------- Ablage

def ablegen(fid, png, pr, e, meta, c=None):
    """Bild verkleinert ablegen und Prüfvermerk in renderings[ID] des Stils schreiben."""
    from PIL import Image
    c = c or cfg()
    w, h = c["ablage_px"]
    ziel = ROOT / ORDNER / f"{fid}.webp"
    ziel.parent.mkdir(parents=True, exist_ok=True)
    im = Image.open(io.BytesIO(png)).convert("RGB")
    im = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
    if im.height != h:  # auf 2 : 3 bringen (Papierrand ergänzen bzw. mittig zuschneiden)
        neu = Image.new("RGB", (w, h), (251, 248, 241))
        neu.paste(im, (0, (h - im.height) // 2))
        im = neu
    im.save(ziel, "WEBP", quality=80, method=6)
    st = stil()
    rend = st.setdefault("renderings", {}).setdefault(fid, {"description_en": e["beschreibung"]})
    rend["image"] = f"{ORDNER}/{fid}.webp"
    ok = pr["ergebnis"] == "bestanden" and not meta.get("trocken")
    rend["check"] = {
        "stufe": "ki-geprueft" if ok else "entwurf", "ergebnis": pr["ergebnis"], "datum": JETZT.date().isoformat(), "process": PROZESS,
        "method_de": "Einzelporträt nach dem Prozess in «process» (docs/PROZESSE.md): Blindbeschreibung durch eine weitere Instanz, "
                     "Regeln (allgemein, Porträt, Figur) und Vergleich mit Beschreibung und Bildlexikon; bei Fehlschlag neu gemalt.",
        "punkte": pr["punkte"], "kern": pr.get("kern"), "modell": pr.get("modell"), "modell_bild": meta.get("modell"),
        "lauf": meta.get("lauf"), "variante": meta.get("variante"), "runden": meta.get("runden"),
        "bild_sha": BP.sha(ziel.read_bytes()), "plan_sha": fingerabdruck(e, c), "beschreibung_sha": beschreibung_sha(e["beschreibung"]),
        "regeln": [{k: x[k] for k in ("id", "stufe", "ergebnis")} for x in pr["regeln"]],
        "open_de": [f"{x['de']} ({x['ergebnis']}: {x['grund']})" for x in pr["regeln"] if x["ergebnis"] != "ok"]
                   + ([f"Beschreibung nicht ganz getroffen: {pr['kern_fehlt_de']}"] if (pr.get("kern") or 0) < 2 and pr.get("kern_fehlt_de") else []),
        "blind_de": (pr.get("blind") or {}).get("action"),
        "limits_de": GRENZEN}
    if meta.get("trocken"):
        rend["check"]["trocken"] = True
    BA.schreibe(STIL, st)
    return ziel


# ---------------------------------------------------------------- Lauf

def lauf(a, schluessel, out):
    import bilder_aquarell_gen as G
    c = cfg()
    eintr = eintraege()
    ids = wahl(eintr, a.szenen, erzwingen=a.erzwingen)
    print(f"Porträts: {len(ids)} Einträge – {', '.join(ids)}")
    bericht, ergebnis = {}, {}
    for fid in ids:
        e = eintr[fid]
        hinweis, beste = a.hinweis, None
        b = bericht.setdefault(fid, {"varianten": []})
        vl = vorlagen(e)
        for runde in range(1, a.runden + 1):
            prompt = auftrag(e, c) + (f"\n\nADDITIONAL INSTRUCTION FOR THIS RUN: {hinweis}" if hinweis else "")
            try:
                m, bilder = G.male(prompt, vl, schluessel, a.varianten, c["groesse"])
            except Exception as ex:
                BP.melde(f"{fid} malen: {ex}")
                break
            for k, png in enumerate(bilder, 1):
                var = f"r{runde}v{k}"
                (out / f"{fid}__{var}.png").write_bytes(png)
                try:
                    pr = pruefe(schluessel, png, e, c)
                except Exception as ex:
                    BP.melde(f"{fid} {var} prüfen: {ex}")
                    continue
                b["varianten"].append({"datei": f"{fid}__{var}.png", "runde": runde, "pruefung": pr, "hinweis": hinweis})
                print(f"{fid} {var}: {pr['ergebnis']} ({pr['punkte']} Punkte, Kern {pr.get('kern')})")
                rang = ({"bestanden": 2, "unklar": 1}.get(pr["ergebnis"], 0), pr["punkte"])
                if beste is None or rang > beste[0]:
                    beste = (rang, var, pr, m, png, runde)
            if beste and beste[0][0] == 2:
                break
            if beste:
                hinweis = (a.hinweis + "\n" if a.hinweis else "") + BP.hinweis_aus(beste[2])
        if beste and (beste[0][0] == 2 or a.auch_unklar and beste[0][0] == 1):
            ablegen(fid, beste[4], beste[2], e, {"modell": beste[3], "lauf": out.name, "variante": beste[1], "runden": beste[5]}, c)
            b["gewaehlt"] = beste[1]
            ergebnis[fid] = "bestanden" + (f" (Runde {beste[5]})" if beste[5] > 1 else "") if beste[0][0] == 2 else "unklar (abgelegt als Entwurf)"
        else:
            b["gewaehlt"] = None
            ergebnis[fid] = "offen"
            BP.melde(f"{fid}: keine Variante hat alle Pflichtregeln erfüllt – nicht abgelegt")
    (out / "figuren.json").write_text(json.dumps({"ergebnis": ergebnis, "nutzung": dict(BP.NUTZUNG)}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    BP.melde("Porträts: " + "; ".join(f"{k} {v}" for k, v in ergebnis.items()))
    return bericht


def trocken(a):
    """Ohne API: Aufträge und Regeln ausgeben; mit --platzhalter zusätzlich die Ablage mit Platzhalterbildern durchspielen
    (Stil-Datensatz, Generator, Validator). Platzhalter nie committen."""
    c = cfg()
    eintr = eintraege()
    ids = wahl(eintr, a.szenen, erzwingen=a.erzwingen)
    n_bilder = 0
    for fid in ids:
        e = eintr[fid]
        rg = regeln(e, c)
        print(f"\n## {fid} ({e['art']}; Vorlagen: {', '.join(p.name for p in vorlagen(e))}; {len(rg)} Regeln, "
              f"davon {sum(r['stufe'] == 'pflicht' for r in rg)} Pflicht; Fingerabdruck {fingerabdruck(e, c)})")
        print(auftrag(e, c) + (f"\n\nADDITIONAL INSTRUCTION FOR THIS RUN: {a.hinweis}" if a.hinweis else ""))
        print("Regeln: " + "; ".join(f"{r['id']} [{r['stufe']}]" for r in rg))
        n_bilder += a.varianten
    pruef = 3 + 0  # Blind, Regeln, Kern je Variante (Zweitmeinung zusätzlich 2 je verfehlter Pflichtregel-Runde)
    print(f"\n{len(ids)} Einträge; erste Runde {n_bilder} Bilder und etwa {n_bilder * pruef} Prüfanfragen "
          f"(höchstens {n_bilder * a.runden} Bilder bei {a.runden} Runden).")
    if not a.platzhalter:
        return
    from PIL import Image, ImageDraw
    for fid in ids:
        im = Image.new("RGB", (1024, 1536), (251, 248, 241))
        d = ImageDraw.Draw(im)
        d.ellipse((412, 300, 612, 520), outline=(98, 102, 93), width=6)
        d.rectangle((362, 560, 662, 1300), outline=(189, 128, 103), width=6)
        d.text((40, 40), f"PLATZHALTER {fid}", fill=(98, 102, 93))
        buf = io.BytesIO()
        im.save(buf, "PNG")
        pr = {"ergebnis": "bestanden", "punkte": 0, "kern": 2, "kern_fehlt_de": "", "modell": "trocken",
              "regeln": [{**r, "ergebnis": "ok", "antwort": None, "grund": "trocken"} for r in regeln(eintr[fid], c)], "blind": {"action": "Platzhalter"}}
        ablegen(fid, buf.getvalue(), pr, eintr[fid], {"modell": "trocken", "lauf": "trocken", "variante": "r1v1", "runden": 1, "trocken": True}, c)
        print("Platzhalter abgelegt", fid)
    subprocess.run([sys.executable, str(ROOT / "scripts/authoring/bilder_aquarell.py")], check=True)
    v = subprocess.run([sys.executable, str(ROOT / "scripts/validate.py")], capture_output=True, text=True)
    print("\n".join(l for l in v.stdout.splitlines() if l.startswith(("ERROR", "FAIL", "PASS")))[:3000])
    print("Validator:", "PASS" if v.returncode == 0 else "FEHLER")


if __name__ == "__main__":
    sys.exit("Aufruf über bilder_aquarell_lauf.py figuren (mit --trocken ohne API) bzw. bilder_aquarell_gen.py figuren")
