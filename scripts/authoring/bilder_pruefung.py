#!/usr/bin/env python3
"""Automatische Bildprüfung für gemalte Bilder (docs/BILDSTIL.md, «Automatische Prüfung»).

Ein Bildprüfmodell (OpenAI, mit Bildeingang; nicht dasselbe Modell wie der Maler) prüft jedes Bild in drei Schritten:

1. Blind: Es sieht nur das Bild und beschreibt Personen (mit Kopfposition), Gegenstände, Handlung und rät die
   biblische Szene. Es kennt weder Auftrag noch Text.
2. Regeln: Es beantwortet die Prüffragen der drei Ebenen (allgemein: pruefregeln.json; Figur: figuren.json «pruef»;
   Feld: Szenenplan «pruefung») einzeln mit ja / nein / unklar und Begründung, zählt verlangte Gegenstände und ordnet
   die erwarteten Figuren den Personen aus Schritt 1 zu (Kopf als Rahmen, für die Sprechblasen).
3. Kern: Ein Textvergleich (ohne Bild) bewertet, ob die Blindbeschreibung den Moment des Bildfelds trifft (0–2).

Auf der fertigen Kachel (Bild mit Blasen und Stichwortband) folgt die Schlussprüfung: Spitze jeder Blase beim richtigen
Sprecher, keine Blase über einem Gesicht, Text lesbar, und die Blindbeschreibung trifft den Moment.

Ergebnis je Bild: «bestanden» (alle Pflichtregeln erfüllt), «unklar» (eine Pflichtregel unklar) oder «durchgefallen».
Die Punkte (erfüllte Soll-Regeln, Kernpunkte) entscheiden unter mehreren brauchbaren Varianten.

Das Modul wird von bilder_aquarell_lauf.py benutzt. Ohne OPENAI_API_KEY lassen sich mit --trocken die Anfragen ansehen:
  python3 scripts/authoring/bilder_pruefung.py --trocken JHN-002-K2
"""
import base64
import hashlib
import io
import json
import os
import pathlib
import sys
import time
import urllib.error
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[2]
DATEN = ROOT / "scripts/authoring/bilder_aquarell_daten"
API = "https://api.openai.com/v1"
VORZUG = ["gpt-6.1-terra", "gpt-5.5", "gpt-5.2", "gpt-5.1", "gpt-5", "gpt-4.1", "gpt-4o"]   # erste Instanz: alle Prüfschritte
VORZUG_ZWEIT = ["gpt-5.5", "gpt-5.2", "gpt-5.1", "gpt-5", "gpt-4.1", "gpt-4o"]   # zweite Instanz: nur wenn eine Pflichtregel nicht besteht
# Aufteilung nach Kalibrierung 2026-10-28 (20 Fälle): gpt-5.5 17/20 richtig, ≈ $0.19 je Feld; gpt-6.1-terra 15/20, ≈ $0.02 je Feld,
# seine Fehler waren überwiegend Fehlalarme bei Pflichtregeln. Die günstige Instanz prüft alles, die genauere entscheidet nur Streitfälle.
_modell = {}
NUTZUNG = {"anfragen": 0, "eingabe": 0, "ausgabe": 0}   # Tokens aller Anfragen dieses Laufs (für den Kostenvergleich)
VERFAHREN = "2026-10-28d"   # Stand des Prüfverfahrens; ändert er sich, gelten alle Prüfungen als veraltet
PROZESS = "PROC-BILD-AQUARELL@2.3"   # Prozessfassung (scripts/authoring/prozesse.py) zu diesem Verfahren; bei neuer Fassung beides ändern


def lade(p):
    return json.loads(pathlib.Path(p).read_text(encoding="utf-8"))


def sha(daten):
    return hashlib.sha256(daten if isinstance(daten, bytes) else json.dumps(daten, ensure_ascii=False, sort_keys=True).encode()).hexdigest()[:16]


# ---------------------------------------------------------------- Regeln

def regeln_fuer(sz, fig, allg):
    """Alle Prüfregeln für ein Feld, mit Ebene. Ausnahmen der Szene schalten allgemeine Regeln ab."""
    aus = {a["id"] for a in sz.get("ausnahmen", [])}
    ids = set(sz["depicts"]) | {x for sp in sz.get("speech", []) for x in (sp["from"], sp["to"])}
    out = []
    for r in allg["regeln"]:
        if r["id"] in aus or (r.get("wenn") and r["wenn"] not in ids):
            continue
        out.append({**r, "ebene": "allgemein"})
    for f in sz["depicts"]:
        for r in fig.get("pruef", {}).get(f, []):
            if r["id"] not in aus:
                out.append({**r, "ebene": "figur", "figur": f})
    for r in sz.get("pruefung", []):
        out.append({**r, "ebene": "feld"})
    return out


def figuren_fuer(sz, fig):
    """Figuren, die im Bild zu finden sind (Personen und Gruppen; Gegenstände prüfen die Regeln)."""
    ids = list(dict.fromkeys([*sz["depicts"], *[x for sp in sz.get("speech", []) for x in (sp["from"], sp["to"])]]))
    return [(f, fig["kenn_en"][f]) for f in ids if f in fig.get("kenn_en", {})]


def plan_fingerabdruck(sz, fig, allg):
    return sha({"verfahren": VERFAHREN, "regeln": regeln_fuer(sz, fig, allg), "speech": sz.get("speech", []), "evidence": sz.get("evidence", []),
                "bild_en": sz.get("bild_en"), "figuren": figuren_fuer(sz, fig)})


# ---------------------------------------------------------------- Modell

def melde(text):
    print(text, file=sys.stderr)
    if os.environ.get("GITHUB_ACTIONS"):
        print("::warning::" + text.replace("%", "%25").replace("\r", "%0D").replace("\n", "%0A"))


def _anfrage(pfad, schluessel, body=None, timeout=300):
    req = urllib.request.Request(f"{API}/{pfad}", data=json.dumps(body).encode() if body is not None else None,
                                 headers={"Authorization": f"Bearer {schluessel}", "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read())


def modell(schluessel, rolle="haupt"):
    """Prüfmodell der ersten (rolle «haupt») oder der zweiten Instanz (rolle «zweit»). Vorgabe aus VORZUG bzw. VORZUG_ZWEIT,
    übersteuerbar mit OPENAI_VISION_MODEL bzw. OPENAI_VISION_MODEL_ZWEIT (genauer Name oder Teil davon, z. B. «terra»)."""
    if rolle in _modell:
        return _modell[rolle]
    wunsch = os.environ.get("OPENAI_VISION_MODEL" + ("_ZWEIT" if rolle == "zweit" else ""))
    vorzug = VORZUG_ZWEIT if rolle == "zweit" else VORZUG
    try:
        da = sorted(m["id"] for m in _anfrage("models", schluessel)["data"])
    except Exception as ex:
        melde(f"Modellliste nicht lesbar ({ex})")
        da = []
    if wunsch:  # dann der passende Name aus der Modellliste des Kontos
        if wunsch in da or not da:
            gewaehlt = wunsch
        else:
            treffer = [m for m in da if wunsch.lower() in m.lower()]
            if not treffer:
                raise RuntimeError(f"Kein Modell zu «{wunsch}». Vorhanden: {', '.join(m for m in da if m.startswith(('gpt', 'o')))}")
            import re as _re
            def _vers(m):
                z = _re.search(r"(\d+(?:\.\d+)*)", m)
                return tuple(int(x) for x in z.group(1).split(".")) if z else ()
            datiert = lambda m: bool(_re.search(r"\d{4}-\d{2}-\d{2}", m))  # noqa: E731
            gewaehlt = sorted(treffer, key=lambda m: (_vers(m), not datiert(m), -len(m)))[-1]   # neueste Fassung, ohne Datumsendung
            melde(f"Treffer für «{wunsch}»: {', '.join(treffer)}")
    else:
        gewaehlt = next((m for m in vorzug if m in da), vorzug[0] if not da else vorzug[-1])
    _modell[rolle] = gewaehlt
    melde(f"Prüfmodell ({'zweite' if rolle == 'zweit' else 'erste'} Instanz): {gewaehlt}")
    return gewaehlt


def modelle(schluessel):
    """Beschreibung für den Prüfdatensatz: erste Instanz, bei Streitfällen zweite."""
    a, b = modell(schluessel), modell(schluessel, "zweit")
    return a if a == b else f"{a} + {b}"


def bild_url(pfad_oder_bytes, breite=1024):
    from PIL import Image
    daten = pfad_oder_bytes if isinstance(pfad_oder_bytes, bytes) else pathlib.Path(pfad_oder_bytes).read_bytes()
    im = Image.open(io.BytesIO(daten)).convert("RGB")
    if im.width > breite:
        im = im.resize((breite, round(im.height * breite / im.width)), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=90)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()


def gitter(pfad_oder_bytes):
    """Kopie des Bildes mit feinem Koordinatengitter (0–1000) für den Ortungsschritt (nur dort, damit die Regelfragen ein
    unverändertes Bild sehen). Ohne Gitter lagen die Kopfrahmen bis zu einer Kopfhöhe daneben (Lauf 15, Lk 15 L3, Joh 2 T2)."""
    from PIL import Image, ImageDraw
    daten = pfad_oder_bytes if isinstance(pfad_oder_bytes, bytes) else pathlib.Path(pfad_oder_bytes).read_bytes()
    im = Image.open(io.BytesIO(daten)).convert("RGB")
    im = im.resize((1200, round(im.height * 1200 / im.width)), Image.LANCZOS)
    d = ImageDraw.Draw(im, "RGBA")
    for k in range(0, 1001, 50):
        x, y = k * (im.width - 1) / 1000, k * (im.height - 1) / 1000
        st = (200, 0, 120, 150 if k % 100 == 0 else 60)
        d.line([(x, 0), (x, im.height)], fill=st, width=1)
        d.line([(0, y), (im.width, y)], fill=st, width=1)
        if k % 100 == 0 and 0 < k < 1000:
            d.text((x + 2, 2), str(k), fill=(200, 0, 120, 255))
            d.text((2, y + 2), str(k), fill=(200, 0, 120, 255))
    buf = io.BytesIO()
    im.save(buf, "PNG")
    return buf.getvalue()


SYS_ORT = ("You locate people in a picture precisely. The picture has a magenta coordinate grid: lines every 50 units, labelled every 100, "
           "from 0 to 1000 in x (left to right) and y (top to bottom). Read coordinates from the grid. Answer in JSON.")


def txt_ort(figuren):
    fg = "\n".join(f"- {f}: {k}" for f, k in figuren) or "- (none)"
    return f"""1. List EVERY person (also small or faint ones), left to right: {{"nr", "who": short description, "head": [x0, y0, x1, y1] tight box around the head including hair and head covering, read from the grid}}.
2. For each expected figure give the nr of the matching person (for a group: the member who speaks or the most prominent one), or null:
{fg}
Return JSON: {{"persons": [...], "figures": {{id: nr or null}}}}"""


def orte(schluessel, bild, figuren):
    r = frage(schluessel, SYS_ORT, txt_ort(figuren), gitter(bild), breite=1200)
    pers = [p for p in r.get("persons", []) if isinstance(p.get("head"), list) and len(p["head"]) == 4]
    nach_nr = {p.get("nr"): p for p in pers}
    zu = {}
    for f, _ in figuren:
        n = (r.get("figures") or {}).get(f)
        if n in nach_nr:
            zu[f] = {"kopf": [round(v) for v in nach_nr[n]["head"]], "sicher": "gitter"}
    return pers, zu


def frage(schluessel, system, text, bild=None, versuche=3, breite=1024, rolle="haupt"):
    inhalt = [{"type": "text", "text": text}]
    if bild is not None:
        inhalt.append({"type": "image_url", "image_url": {"url": bild_url(bild, breite), "detail": "high"}})
    body = {"model": modell(schluessel, rolle), "response_format": {"type": "json_object"},
            "messages": [{"role": "system", "content": system}, {"role": "user", "content": inhalt}]}
    letzter = None
    for k in range(versuche):
        try:
            d = _anfrage("chat/completions", schluessel, body)
            u = d.get("usage") or {}
            NUTZUNG["anfragen"] += 1
            NUTZUNG["eingabe"] += u.get("prompt_tokens", 0)
            NUTZUNG["ausgabe"] += u.get("completion_tokens", 0)
            return json.loads(d["choices"][0]["message"]["content"])
        except urllib.error.HTTPError as e:
            letzter = f"HTTP {e.code}: {e.read().decode(errors='replace')[:400]}"
            if e.code not in (429, 500, 502, 503):
                break
        except (json.JSONDecodeError, KeyError, urllib.error.URLError, TimeoutError) as e:
            letzter = str(e)
        time.sleep(4 * (k + 1))
    raise RuntimeError(f"Bildprüfung fehlgeschlagen: {letzter}")


# ---------------------------------------------------------------- Schritte

SYS_BLIND = ("You are a careful, sceptical picture analyst. You describe only what is actually visible. "
             "Coordinates are integers from 0 to 1000 relative to the picture width (x) and height (y), origin top left. Answer in JSON.")

TXT_BLIND = """Look at this picture. You get no other information.
Return JSON with:
- "persons": list of every person, left to right: {"nr": 1.., "description": apparent age, sex, hair, beard, clothing colours, pose, facial expression, what the hands do, "looking_at": nr of the person this one faces or null, "head": [x0, y0, x1, y1] box around the head}
- "objects": list of {"what", "count", "where"}
- "action": what is happening, in two or three sentences
- "setting": place and time hints
- "text_in_picture": any letters or words you can see, else ""
- "cut_off": people or objects cut off by the picture edge, else ""
- "story_guess": if this illustrates a Bible story, which one and which moment exactly
- "style": one sentence on the drawing style and how detailed it is"""

SYS_REGELN = ("You are a strict picture checker for a Bible app. You check a painting against questions. Be literal and sceptical: "
              "answer \"yes\" or \"no\" only if it is clearly visible; otherwise \"unclear\". Do not assume what the painter intended. Answer in JSON.")


def txt_regeln(regeln, figuren, blind):
    fr = "\n".join(f'- {r["id"]}: {"COUNT the " + r["en"] if r.get("typ") == "anzahl" else r["en"]}' for r in regeln)
    fg = "\n".join(f"- {f}: {k}" for f, k in figuren) or "- (none)"
    return f"""A first, independent look at this picture found these persons (numbering left to right):
{json.dumps(blind.get("persons", []), ensure_ascii=False)}

1. QUESTIONS – answer each one separately:
{fr}
For each id return {{"answer": "yes" | "no" | "unclear", "reason": short reason}}; for COUNT questions return {{"count": number or null, "reason"}}.

2. FIGURES – for each expected figure, find the matching person (use the numbers above; a different person may also be correct if the first look missed someone):
{fg}
For each id return {{"person": nr or null, "head": [x0, y0, x1, y1] (0–1000, the head of that person; for a group the member who is speaking or the most prominent one) or null, "certainty": "high" | "medium" | "low"}}.

Return JSON: {{"questions": {{id: ...}}, "figures": {{id: ...}}}}"""


SYS_KERN = "You compare a blind description of a picture with the intended moment of a Bible illustration. Answer in JSON."


def txt_kern(moment_de, blind):
    return f"""Intended moment (German): {moment_de}

Blind description by someone who saw only the picture:
action: {blind.get("action")}
story guess: {blind.get("story_guess")}
persons: {json.dumps(blind.get("persons", []), ensure_ascii=False)}

Score: 2 = the description clearly captures the intended moment (who does what, to whom); 1 = partly (the situation fits but an essential element is missing or ambiguous); 0 = does not capture it or contradicts it.
Return JSON: {{"score": 0 | 1 | 2, "missing_de": what is missing or wrong, in German, short}}"""


def bewerte(regeln, antworten):
    out = []
    for r in regeln:
        a = antworten.get(r["id"], {})
        if r.get("typ") == "anzahl":
            z = a.get("count")
            erg = "unklar" if z is None else ("ok" if z == r["soll"] else "fehler")
            out.append({"id": r["id"], "ebene": r["ebene"], "stufe": r["stufe"], "de": r["de"], "ergebnis": erg, "antwort": z, "grund": a.get("reason", "")})
            continue
        ant = (a.get("answer") or "unclear").lower()
        erwartet = "yes" if r["art"] == "muss" else "no"
        erg = "ok" if ant == erwartet else ("unklar" if ant == "unclear" else "fehler")
        out.append({"id": r["id"], "ebene": r["ebene"], "stufe": r["stufe"], "de": r["de"], "ergebnis": erg, "antwort": ant, "grund": a.get("reason", "")})
    return out


def zweitmeinung(schluessel, bild, regeln, erg, figuren, blind, runden=2):
    """Verfehlte Pflichtregeln noch zweimal einzeln fragen, und zwar die zweite Instanz; es gilt die Mehrheit der drei Antworten.
    Dasselbe Bild bestand im einen Lauf und war im nächsten «unklar» (Lauf 15, Mk 4 S1): ein einzelnes Urteil ist nicht stabil genug.
    Weil die zweite Instanz zwei der drei Stimmen hat, entscheidet sie, sobald sie sich einig ist (Verfahren 2026-10-28d)."""
    offen = [e["id"] for e in erg if e["stufe"] == "pflicht" and e["ergebnis"] != "ok"]
    if not offen:
        return erg
    nach = [r for r in regeln if r["id"] in offen]
    stimmen = {i: [next(e for e in erg if e["id"] == i)] for i in offen}
    for _ in range(runden):
        r = frage(schluessel, SYS_REGELN, txt_regeln(nach, [], blind), bild, rolle="zweit")
        for e in bewerte(nach, r.get("questions", {})):
            stimmen[e["id"]].append(e)
    out = []
    for e in erg:
        if e["id"] in stimmen:
            st = stimmen[e["id"]]
            ok = [x for x in st if x["ergebnis"] == "ok"]
            nein = [x for x in st if x["ergebnis"] == "fehler"]
            wahl = ok[0] if len(ok) * 2 > len(st) else (nein[0] if len(nein) * 2 > len(st) else next(x for x in st if x["ergebnis"] != "ok"))
            e = {**wahl, "stimmen": [x["ergebnis"] for x in st]}
        out.append(e)
    return out


def gesamt(ergebnisse, kern=None, kern_pflicht=None):
    pfl = [e for e in ergebnisse if e["stufe"] == "pflicht"]
    if any(e["ergebnis"] == "fehler" for e in pfl) or (kern_pflicht is not None and kern is not None and kern < kern_pflicht):
        erg = "durchgefallen"
    elif any(e["ergebnis"] == "unklar" for e in pfl):
        erg = "unklar"
    else:
        erg = "bestanden"
    punkte = sum(e["ergebnis"] == "ok" for e in ergebnisse if e["stufe"] == "soll") + (kern or 0)
    return erg, punkte


def pruefe_feld(schluessel, bild, sz, fig, allg, moment_de):
    """Schritte 1–3 für ein gemaltes Bildfeld (ohne Blasen). bild: Pfad oder Bytes."""
    blind = frage(schluessel, SYS_BLIND, TXT_BLIND, bild)
    regeln = regeln_fuer(sz, fig, allg)
    figuren = figuren_fuer(sz, fig)
    r = frage(schluessel, SYS_REGELN, txt_regeln(regeln, figuren, blind), bild)
    erg = zweitmeinung(schluessel, bild, regeln, bewerte(regeln, r.get("questions", {})), figuren, blind)
    personen, koepfe = orte(schluessel, bild, figuren)
    fehlt = []
    for f, _ in figuren:
        if f not in koepfe:
            x = (r.get("figures") or {}).get(f) or {}
            if x.get("head") and len(x["head"]) == 4:
                koepfe[f] = {"kopf": [round(v) for v in x["head"]], "sicher": x.get("certainty")}
            else:
                fehlt.append(f)
    for f in fehlt:  # Sprecher und Angesprochene müssen gefunden werden
        pfl = any(f in (sp["from"], sp["to"]) for sp in sz.get("speech", []))
        erg.append({"id": f"FIG-GEFUNDEN:{f}", "ebene": "figur", "stufe": "pflicht" if pfl else "soll", "de": f"Figur im Bild gefunden: {f}",
                    "ergebnis": "fehler", "antwort": None, "grund": "nicht zugeordnet"})
    k = frage(schluessel, SYS_KERN, txt_kern(moment_de, blind))
    kern = k.get("score")
    e, punkte = gesamt(erg, kern)
    bytes_ = bild if isinstance(bild, bytes) else pathlib.Path(bild).read_bytes()
    return {"ergebnis": e, "punkte": punkte, "kern": kern, "kern_fehlt_de": k.get("missing_de", ""), "regeln": erg, "koepfe": koepfe,
            "blind": {k_: blind.get(k_) for k_ in ("action", "story_guess", "cut_off", "text_in_picture", "style")},
            "personen": personen or blind.get("persons", []), "modell": modelle(schluessel), "bild_sha": sha(bytes_)}


SYS_SCHLUSS = ("You are a strict checker of a finished comic panel for a Bible app (painting with speech bubbles and a caption band). "
               "Be literal: answer \"yes\" or \"no\" only if clearly visible, else \"unclear\". Answer in JSON.")


def txt_schluss(sprech, fig):
    fr = []
    for n, sp in enumerate(sprech, 1):
        wer = fig["kenn_en"].get(sp["from"], sp["from"])
        if sp.get("denken"):
            fr.append(f'- B{n}: Is the bubble with the words «{sp["de"]}» a thought bubble (rounded, with a trail of small circles instead of a pointed tail), and do the circles lead to {wer}?')
        else:
            fr.append(f'- B{n}: Does the tail of the speech bubble with the words «{sp["de"]}» point clearly at {wer}?')
    fr.append("- S-GESICHT: Does any speech bubble cover a face, a gesturing hand, an object someone holds (for example a whip, a cup, a jug), or the main action of the scene? (Touching the tip of a mast, a roof, a tree or the sky does not count.)")
    fr.append("- S-LESBAR: Is all lettering (bubbles and caption band) complete and readable, not cut off or overlapping?")
    return "\n".join(fr)


def pruefe_kachel(schluessel, png, sprech, fig, moment_de):
    """Schlussprüfung auf der fertigen Kachel (Hochdeutsch)."""
    blind = frage(schluessel, SYS_BLIND, TXT_BLIND.replace('"text_in_picture": any letters or words you can see, else ""',
                                                          '"text_in_picture": all words you can read, and for each speech bubble who it belongs to'), png)
    q = frage(schluessel, SYS_SCHLUSS, "Answer each question separately:\n" + txt_schluss(sprech, fig)
              + '\nReturn JSON: {"questions": {id: {"answer": "yes" | "no" | "unclear", "reason"}}}', png)
    regeln = [{"id": f"B{n}", "art": "muss", "stufe": "pflicht", "de": f"Blase {n} zeigt auf den Sprecher ({sp['from']})", "ebene": "kachel"} for n, sp in enumerate(sprech, 1)]
    regeln += [{"id": "S-GESICHT", "art": "nicht", "stufe": "pflicht", "de": "Keine Blase über Gesicht, Geste oder Haupthandlung", "ebene": "kachel"},
               {"id": "S-LESBAR", "art": "muss", "stufe": "pflicht", "de": "Alle Worte vollständig und lesbar", "ebene": "kachel"}]
    erg = bewerte(regeln, q.get("questions", {}))
    offen = [e["id"] for e in erg if e["ergebnis"] != "ok"]
    if offen:  # Zweitmeinung (Mehrheit aus drei)
        stimmen = {i: [next(e for e in erg if e["id"] == i)] for i in offen}
        nur = "\n".join(l for l in txt_schluss(sprech, fig).split("\n") if l.split(":")[0].strip("- ") in offen)
        for _ in range(2):
            q2 = frage(schluessel, SYS_SCHLUSS, "Answer each question separately:\n" + nur
                       + '\nReturn JSON: {"questions": {id: {"answer": "yes" | "no" | "unclear", "reason"}}}', png, rolle="zweit")
            for e in bewerte([r for r in regeln if r["id"] in offen], q2.get("questions", {})):
                stimmen[e["id"]].append(e)
        neu = []
        for e in erg:
            if e["id"] in stimmen:
                st = stimmen[e["id"]]
                ok = [x for x in st if x["ergebnis"] == "ok"]
                e = {**(ok[0] if len(ok) * 2 > len(st) else next(x for x in st if x["ergebnis"] != "ok")), "stimmen": [x["ergebnis"] for x in st]}
            neu.append(e)
        erg = neu
    k = frage(schluessel, SYS_KERN, txt_kern(moment_de, blind))
    e, punkte = gesamt(erg, k.get("score"), kern_pflicht=1)
    return {"ergebnis": e, "punkte": punkte, "kern": k.get("score"), "kern_fehlt_de": k.get("missing_de", ""), "regeln": erg,
            "blind": {k_: blind.get(k_) for k_ in ("action", "story_guess", "text_in_picture")}, "modell": modelle(schluessel), "bild_sha": sha(png)}


def hinweis_aus(pruefung):
    """Zusatzanweisung für einen neuen Malversuch aus den verfehlten Regeln (Englisch)."""
    teile = []
    for e in pruefung["regeln"]:
        if e["ergebnis"] == "ok" or e["stufe"] != "pflicht":
            continue
        teile.append(f"- {e['de']} (check {e['id']} failed: {e['grund']})")
    return ("A previous attempt failed these checks; make sure this time:\n" + "\n".join(teile)) if teile else ""


# ---------------------------------------------------------------- Kachel rendern

def rendere(svg_text, basis, skala=2):
    """SVG (mit relativen Bildpfaden) als PNG im Browser rendern."""
    import re
    from playwright.sync_api import sync_playwright

    def inline(m):
        p = basis / m.group(1)
        typ = "image/webp" if p.suffix == ".webp" else "image/png"
        return f'href="data:{typ};base64,{base64.b64encode(p.read_bytes()).decode()}"'
    svg = re.sub(r'href="(img/[^"]+)"', inline, svg_text)
    vb = [float(v) for v in re.search(r'viewBox="([^"]+)"', svg).group(1).split()]
    w, h = int(vb[2]), int(vb[3])
    svg = svg.replace("<svg ", f'<svg width="{w}" height="{h}" ', 1)
    seite = ('<!doctype html><html><head><style>html,body{margin:0;background:#fff} .lw-gsw{display:none}</style></head>'
             f'<body>{svg}</body></html>')
    with sync_playwright() as p:
        try:
            b = p.chromium.launch()
        except Exception:
            b = p.chromium.launch(channel="chrome")
        s = b.new_page(viewport={"width": w, "height": h}, device_scale_factor=skala)
        s.set_content(seite)
        s.wait_for_timeout(300)
        png = s.screenshot(clip={"x": 0, "y": 0, "width": w, "height": h})
        b.close()
    return png


def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("szene")
    ap.add_argument("--plan", default="szenen-jhn-002.json")
    ap.add_argument("--trocken", action="store_true")
    a = ap.parse_args()
    plan, fig, allg = lade(DATEN / a.plan)["szenen"], lade(DATEN / "figuren.json"), lade(DATEN / "pruefregeln.json")
    sz = plan[a.szene]
    regeln = regeln_fuer(sz, fig, allg)
    if a.trocken:
        print(TXT_BLIND, "\n\n", txt_regeln(regeln, figuren_fuer(sz, fig), {"persons": ["…"]}))
        print("\nSchluss:\n" + txt_schluss(sz.get("speech", []), fig))
        print(f"\n{len(regeln)} Regeln, Fingerabdruck {plan_fingerabdruck(sz, fig, allg)}")
        return
    sys.exit("Ohne --trocken nur über bilder_aquarell_lauf.py")


if __name__ == "__main__":
    main()
