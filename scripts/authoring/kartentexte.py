#!/usr/bin/env python3
"""Kartentexte und Bilder der Strukturbilder (Entscheid Andi Neck 2026-11-24: «vieles schaut nach Platzhalter aus»).

Allgemeine Regeln für jede Karte eines Strukturbilds (strukturgeruest.py):
  1. Keine Karte ohne Bild. Die Bilder kommen aus dem Bildlexikon (nur Einträge mit geprüftem Bild, keine Personen ohne
     Wiederkehr): zuerst aus dem Bildauftrag des Feldes, sonst aus den Lexikon-Einträgen, die der Text des Feldes nennt,
     sonst aus dem ganzen Bildauftrag. Höchstens drei: die handelnden Personen und, wenn vorhanden, ein Zeichen oder
     Gegenstand, der die Aussage trägt.
  2. Der Kartentext ist ein kurzer, vollständiger Ausdruck (höchstens 42 Zeichen), kein abgeschnittenes Satzstück aus dem
     Vers: «Jesus heilt en Glähmte» statt «wo Jesus ire Glaube gseh hät». Züritüütsch nach docs/ZUERITUEUETSCH.md (Gott und
     Jesus ohne Artikel; zusammenhängend), geprüft mit scripts/mundart.py.
Die Auswahl trifft eine KI-Instanz aus einer festen Kandidatenliste; das Werkzeug prüft Länge, Kandidaten und Mundart und
legt das Ergebnis mit Fingerabdruck der Eingaben ab (strukturgeruest_daten/karten.json). Ändert sich der Bildauftrag,
gilt der Eintrag als veraltet und wird neu erzeugt.

    python3 scripts/authoring/kartentexte.py erzeugen [BRIEF-…]   # fehlende oder veraltete Karten (claude -p)
    python3 scripts/authoring/kartentexte.py pruefen               # Regeln prüfen, ohne zu erzeugen
"""
import hashlib
import json
import pathlib
import re
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
sys.path.insert(0, str(ROOT / "scripts"))
import personen as P  # noqa: E402
import vignetten as V  # noqa: E402

BRIEFS = ROOT / "data/illustrations/briefs"
LEX = ROOT / "data/illustrations/lexicon"
ABLAGE = ROOT / "scripts/authoring/strukturgeruest_daten/karten.json"
MAX_BILDER = 3
MAX_TEXT = 42
MODELL = "claude-sonnet-4-6"
_lex = None


def lade(p):
    return json.loads(pathlib.Path(p).read_text(encoding="utf-8"))


def lexikon():
    """ID → (Name, Art) für alle Einträge mit geprüftem Bild, ohne Personen nur mit Namensschild."""
    global _lex
    if _lex is None:
        _lex = {}
        for p in LEX.glob("FIG-*.json"):
            lx = lade(p)
            f = lx["id"]
            if (f == "FIG-GOTT" or V.bild(f)) and not P.nur_namensschild(f):
                _lex[f] = ((lx.get("names") or {}).get("de", f), lx.get("kind", ""))
    return _lex


def _stamm(w):
    w = w.lower()
    return w[:max(4, len(w) - 2)] if len(w) > 4 else w


def im_text(text):
    """Lexikon-Einträge, deren Name (Wortstamm) im Text vorkommt."""
    woerter = {_stamm(w) for w in re.findall(r"[A-Za-zÄÖÜäöüß]{4,}", text)}
    out = []
    for f, (name, _) in lexikon().items():
        teile = [t for t in re.findall(r"[A-Za-zÄÖÜäöüß]{4,}", re.sub(r"\(.*?\)", "", name.split("/")[0]))]
        if teile and all(_stamm(t) in woerter for t in teile):
            out.append(f)
    return out


def kandidaten(b, i):
    pa = b["panels"][i]
    lx = lexikon()
    eigene = [f for f in pa.get("figures", []) + pa.get("objects", []) + pa.get("signs", []) if f in lx]
    text = [f for f in im_text(pa.get("action_de", "")) if f not in eigene]
    rest = [f for q in b["panels"] for f in q.get("figures", []) + q.get("objects", []) + q.get("signs", []) if f in lx]
    return list(dict.fromkeys(eigene + text + rest))


def fingerabdruck(b, i, gsw):
    pa = b["panels"][i]
    return hashlib.sha256(json.dumps([pa.get("action_de"), gsw, pa.get("reference"), kandidaten(b, i)], ensure_ascii=False)
                          .encode()).hexdigest()[:16]


def gsw_aktionen(b):
    loc = ROOT / f"data/localizations/gsw-u-sd-chzh/{b['id']}.json"
    return ((lade(loc).get("fields") or {}).get("actions_de") or []) if loc.exists() else []


AUFTRAG = """Du gestaltest Karten für Übersichtsbilder einer Bibel-App (Deutsch und Zürichdeutsch). Jede Karte steht für einen Abschnitt
eines Bibeltexts und zeigt bis zu drei kleine Bilder aus einem Bildlexikon und einen kurzen Text.

Regeln für jede Karte:
- «bilder»: 1 bis 3 IDs, NUR aus der Kandidatenliste der Karte, in der Reihenfolge links→rechts. Wähle, was die Handlung der
  Karte am besten zeigt: zuerst die handelnden Personen oder Gruppen, dazu wenn passend EIN Zeichen oder Gegenstand, der die
  Aussage trägt. Nichts, was in dieser Karte nicht vorkommt. Gott (FIG-GOTT) nur, wenn Gott selbst handelt oder angesprochen ist.
- «de» und «gsw»: kurzer, vollständiger Ausdruck, höchstens 42 Zeichen, ohne Schlusspunkt, beginnt gross. Kein abgeschnittenes
  Satzstück («wo Jesus …», «dass …», «und …»), kein Zitat mitten aus einem Satz. Gut: «Jesus heilt en Glähmte», «Petrus verleugnet Jesus»,
  «D Pharisäer wänd es Zeiche». Sachlich, nah am Text, keine Deutung über den Text hinaus.
- Zürichdeutsch wie in den gegebenen Handlungen: Gott und Jesus ohne Artikel («Jesus heilt», «vo Gott»), andere Namen mit
  Artikel («de Petrus», «d Maria»), «de Heilig Geischt», einfache Wortstellung, Schweizer Schreibung (ss, kein ß).
  Nimm für «gsw» die Wörter und Formen aus der gegebenen zürichdeutschen Handlung der Karte; erfinde keine eigenen
  Formen. Fehlt sie, übertrage «de» schlicht. Dativ vor männlichen Namen «em» («Gott git em Mose», «Jesus seit em Petrus»). Prüfregeln (Fehler → richtig): {regeln}.

Antworte nur mit JSON: {{"BRIEF-ID": [{{"bilder": [...], "de": "…", "gsw": "…"}}, … je Karte in Reihenfolge], …}}

{daten}"""


def regeln():
    """Die Prüfregeln von scripts/mundart.py mit der richtigen Form, damit der Auftrag sie von Anfang an kennt."""
    import mundart
    return "; ".join(f"{m[1]} → {m[3]}" for m in mundart.MUSTER if len(m) > 3)


def frage(prompt):
    import subprocess
    r = subprocess.run(["claude", "-p", prompt, "--model", MODELL, "--disallowedTools", "Bash,Grep,Glob,WebFetch,WebSearch,Edit,Write,Read"],
                       capture_output=True, text=True, timeout=1500)
    m = re.search(r"\{.*\}", r.stdout, re.S)
    try:
        return json.loads(m.group(0)) if m else {}
    except json.JSONDecodeError:
        return {}


_MANN = None
# Verben mit Dativ der Person: «Gott git em Mose», «Jesus seit em Petrus» (docs/ZUERITUEUETSCH.md: Dativ vor Personennamen em)
DATIV_VERBEN = r"(?:git|gänd|seit|säged|zeigt|antwortet|hilft|dankt|befiehlt|verheisst|verzellt|erschiint)"


def maennliche_namen():
    """Namen aus dem Bildlexikon (Personen, Rollen), die im Bibeltext mit «em» und nie mit «d» stehen: männliche Einzahl."""
    global _MANN
    if _MANN is None:
        em, d = set(), set()
        for p in ROOT.glob("data/translations/*GSW*.json"):
            t = p.read_text(encoding="utf-8")
            em.update(re.findall(r"\bem ([A-ZÄÖÜ][a-zäöü]+)\b", t))
            d.update(re.findall(r"\b[Dd] ([A-ZÄÖÜ][a-zäöü]+)\b", t))   # weiblich oder Mehrzahl («d Jünger»): «de» ist dort Dativ
        em -= d
        namen = set()
        for p in LEX.glob("FIG-*.json"):
            lx = lade(p)
            if lx.get("kind") in ("person", "role"):
                namen.update(re.findall(r"[A-ZÄÖÜ][a-zäöü]+", (lx.get("names") or {}).get("de", "")))
        _MANN = sorted((namen & em) - {"Jesus", "Gott"})
    return _MANN


def dativ_fehler(text):
    """Nur wenn das Subjekt vor dem Verb steht («Gott git de Mose …»); bei Umstellung ist «de X» oft Subjekt
    («Drüümal seit de Pilatus»)."""
    namen = "|".join(maennliche_namen())
    rx = re.compile(rf"(?:^|[:;] )(?:Gott|Jesus|[DS]e? [A-ZÄÖÜ][a-zäöü]+|{namen}) ({DATIV_VERBEN} de (?:{namen}))\b")
    return [m.group(1) for m in rx.finditer(text)]


def befunde(karte, kand):
    import mundart
    f = []
    for x in dativ_fehler(karte.get("gsw", "")):
        f.append(f"Mundart: Dativ vor Personennamen em («{x}» → «… em …»)")
    if not karte.get("bilder"):
        f.append("ohne Bild")
    if len(karte.get("bilder", [])) > MAX_BILDER:
        f.append("mehr als drei Bilder")
    for x in karte.get("bilder", []):
        if x not in kand:
            f.append(f"{x} nicht in den Kandidaten")
    for sp in ("de", "gsw"):
        t = karte.get(sp, "")
        if not t or len(t) > MAX_TEXT:
            f.append(f"{sp}: Länge {len(t)}")
        if t[:1].islower():
            f.append(f"{sp}: beginnt klein")
    for _, regel, *_ in mundart_funde(mundart, karte.get("gsw", "")):
        f.append(f"Mundart: {regel}")
    return f


def mundart_funde(mundart, text):
    out = []
    for m in mundart.MUSTER:
        rx, name = m[0], m[1]
        if rx.search(text):
            out.append((text, name))
    return out


def daten_fuer(briefs, alt=None):
    """Kartendaten für den Auftrag; bei einer verworfenen früheren Fassung steht der Grund dabei."""
    alt = alt or {}
    teile = []
    for b in briefs:
        akt = gsw_aktionen(b)
        karten = []
        for i, pa in enumerate(b["panels"]):
            kand = kandidaten(b, i)
            karten.append(f"  Karte {i + 1} ({pa.get('reference', '')}): Handlung: {pa.get('action_de', '')}"
                          + (f" | Zürichdeutsch: {akt[i]}" if i < len(akt) else "")
                          + "\n    Kandidaten: " + "; ".join(f"{f} = {lexikon()[f][0]}" for f in kand)
                          + "".join(f"\n    Verworfen: «{k['gsw']}» / «{k['de']}» – {', '.join(k['befunde'])}"
                                    for k in (alt.get(b["id"]) or [])[i:i + 1] if k.get("befunde")))
        teile.append(f"{b['id']} ({b.get('reference', '')}):\n" + "\n".join(karten))
    return "\n\n".join(teile)


def zu_bearbeiten(nur=None):
    import strukturgeruest as S
    ab = lade(ABLAGE) if ABLAGE.exists() else {}
    fertig = S.schon_aquarell()
    out = []
    for p in sorted(BRIEFS.glob("BRIEF-*.json")):
        b = lade(p)
        if b.get("level") not in S.EBENEN or b["id"] in fertig or not b.get("panels") or (nur and b["id"] not in nur):
            continue
        akt = gsw_aktionen(b)
        fp = [fingerabdruck(b, i, akt[i] if i < len(akt) else "") for i in range(len(b["panels"]))]
        alt = ab.get(b["id"])
        if not alt or [k.get("fp") for k in alt] != fp or any(k.get("befunde") for k in alt):
            out.append(b)
    return out, ab


def erzeugen(nur=None):
    briefs, ab = zu_bearbeiten(nur)
    briefs = [b for b in briefs if any(kandidaten(b, i) for i in range(len(b["panels"])))]   # ohne jedes Bild: bleibt beim bisherigen Bild
    print(f"{len(briefs)} Bildaufträge zu bearbeiten")
    pakete = [briefs[i:i + 8] for i in range(0, len(briefs), 8)]
    ABLAGE.parent.mkdir(exist_ok=True)
    with ThreadPoolExecutor(10) as ex:
        laeufe = {ex.submit(frage, AUFTRAG.format(daten=daten_fuer(pk, ab), regeln=regeln())): pk for pk in pakete}
        for n, fu in enumerate(as_completed(laeufe), 1):
            pk, a = laeufe[fu], fu.result()
            if not a:
                print(f"Paket ohne Antwort: {pk[0]['id']} …", flush=True)
                continue
            uebernehmen(pk, a, ab)
            ABLAGE.write_text(json.dumps(dict(sorted(ab.items())), ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
            print(f"{n}/{len(pakete)} Pakete", flush=True)
    pruefen()


def uebernehmen(pk, a, ab):
    """Antwort eines Pakets prüfen und in die Ablage übernehmen (laufend gespeichert, ein Abbruch verliert nichts)."""
    for b in pk:
        akt = gsw_aktionen(b)
        ks = a.get(b["id"]) or []
        out = []
        for i in range(len(b["panels"])):
            k = ks[i] if i < len(ks) and isinstance(ks[i], dict) else {}
            kand = kandidaten(b, i)
            k = {"bilder": [x for x in k.get("bilder", []) if x in kand][:MAX_BILDER], "de": (k.get("de") or "").strip().rstrip("."),
                 "gsw": (k.get("gsw") or "").strip().rstrip(".")}
            import mundart
            k["gsw"] = mundart.ersetze(k["gsw"])   # eindeutige Mundartregeln (Gleit-n, Wortliste) wie im Bibeltext
            if not k["bilder"] and kand:
                k["bilder"] = kand[:1]
            k["befunde"] = befunde(k, kand)
            k["fp"] = fingerabdruck(b, i, akt[i] if i < len(akt) else "")
            out.append(k)
        ab[b["id"]] = out


def pruefen():
    ab = lade(ABLAGE) if ABLAGE.exists() else {}
    n = sum(len(v) for v in ab.values())
    schlecht = {f"{b} {i + 1}": k["befunde"] for b, v in ab.items() for i, k in enumerate(v) if k.get("befunde")}
    for k, v in list(schlecht.items())[:40]:
        print(k, v)
    print(f"{'PASS' if not schlecht else 'FEHLER'}: Kartentexte – {len(ab)} Bilder, {n} Karten, {len(schlecht)} mit Befund")
    return not schlecht


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "erzeugen":
        erzeugen(set(sys.argv[2:]) or None)
    elif cmd == "pruefen":
        sys.exit(0 if pruefen() else 1)
    else:
        print(__doc__)
