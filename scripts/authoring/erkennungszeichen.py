"""Erkennungszeichen je Bild gegen den Verstext prüfen (Entscheid Andi Neck 2026-10-26, Punkt 8).
Listet je Feld die gezeigten Erkennungszeichen der Figuren (figuren.py/bilder_anime CHAR attr) und prüft mit einem Muster je
Zeichen, ob der Text der Stelle (hochdeutsche Arbeitsübersetzung, Versbereich des Felds) es stützt. Mit --anwenden: nicht
gestützte Zeichen per stage.hold "LEER" entfernen, Legende (de/gsw) nachführen, Namensschild ergänzen, wenn die Figur im Bild
sonst nirgends benannt ist.

    python3 scripts/authoring/erkennungszeichen.py [--anwenden] [--ohne LUK.json,LUK-3.json]

Bericht: reports/erkennungszeichen.json (je Feld Bild, Feld, Versbereich, Figur, Zeichen, gestützt). Felder, in denen der Auftrag
die Hand schon festlegt (stage.hold), werden nicht verändert. KI-Entwurf (Claude) vom 2026-10-26; die Suchmuster sind grob
(ein Treffer im Versbereich genügt) und ersetzen kein Lesen der Stelle."""
import sys, json, re, pathlib, glob, collections
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts")); sys.path.insert(0, str(ROOT / "scripts/authoring"))
import bilder_anime as A
A_DIR = ROOT / "scripts/authoring/bildauftraege_daten"
SKIP = {"_wortzeichen.json"}
if "--ohne" in sys.argv:
    SKIP |= set(sys.argv[sys.argv.index("--ohne") + 1].split(","))
# Muster, die das Zeichen im Text stützen; None = traditionelles Attribut ohne Anhalt im Text (nie zeigen)
SUPPORT = {
    "schluessel": r"Schlüssel", "x-kreuz": None, "messer": None, "walkerstange": None, "saege": None, "keule": None,
    "stabkreuz": None, "jakobsmuschel": None, "kelch": None, "kreuzstab": None, "feuerwagen": r"feurige[rn]? Wagen|Feuerwagen",
    "hirtenstab": r"Hirte|Schafe", "alabaster": r"Alabaster|wohlriechende|Salböl|salben", "buch-muenzen": r"Zöllner|Zoll",
    "muenzen": r"Zöllner|Zoll", "kelle": r"dient|bedient|Bedienen", "salbt-fuss": r"salbt|Salböl|Nard|Füsse",
    "hammer": r"Zimmermann", "kasse": r"Kasse|Geldbeutel", "wundmal": r"Wunde|Nägel|Seite|Male?\b", "feigenbaum": r"Feigenbaum",
    "grab-offen": r"Grab|Gruft|Toten|auferweck|Stein", "lampe": r"Nacht", "richterstuhl": r"Richterstuhl",
    "raeucheraltar": r"Räucher|Rauchopfer|Altar", "garbe": r"Ähre|Garbe|Gerste|Ernte|Feld|aufles|Schnitter",
    "worfel": r"worfel|Tenne|Gerste", "herz": r"liebte|lieb hatte|geliebt", "ohr-schwert": r"Ohr|Schwert",
    "kette-gesprengt": r"Kette|Fessel|gefesselt|Grabhöhlen|Gräbern", "schale": r"dient|bediente", "hund-brot": r"Hund|Krümel|Brot",
    "tamburin": r"tanz", "gabenkorb": r"Gabe|geschickt|empfangen|Opfer|Bedürfnis|Not", "oelkrug": r"wohlriechend|Öl|salben|Spezereien",
    "netz": r"Netz|Boot|Fischer|Tagelöhner", "sandale": r"Schuh|Sandale", "acker": r"Erbteil|Feld|Acker|Name", "jesuskind": r"in die Arme|Arme",
    "insel": r"Kreta", "schuessel-kelle": r"dient|bedien|Bedienen",
}
# Wörter der Legende je Zeichen (de, gsw)
WORDS = {
    "schluessel": ("Schlüssel", "Schlüssel"), "x-kreuz": ("schräges Kreuz|X-Kreuz", "schrägs Chrüüz|X-Chrüüz|schräge Chrüüz"),
    "messer": ("Messer", "Mässer"), "walkerstange": ("Walkerstange", "Walkerstange"), "saege": ("Säge", "Sagi|Saagi|Säge"),
    "keule": ("Keule", "Chüüle|Keule"), "stabkreuz": ("Stabkreuz", "Stabchrüüz"), "jakobsmuschel": ("Jakobsmuschel", "Jakobsmuschle"),
    "kelch": ("Kelch mit Schlange|Kelch", "Chelch mit Schlange|Chelch"), "kreuzstab": ("Kreuzstab", "Chrüüzstab"),
    "feuerwagen": ("Feuerwagen", "Füürwage"), "alabaster": ("Alabastergefäss|Alabaster", "Alabaschtergfäss|Alabastergfäss|Alabaster"),
    "hammer": ("Hammer", "Hammer"), "kasse": ("Kasse", "Kasse"), "buch-muenzen": ("Buch und Münzen|Buch", "Buech und Münze|Buech"),
    "muenzen": ("Münzen", "Münze"), "wundmal": ("Wundmal", "Wundmal"), "feigenbaum": ("Feigenbaum", "Feigebaum"),
    "lampe": ("Öllampe|Lampe", "Öllampe|Lampe"), "richterstuhl": ("Richterstuhl", "Richterstuel"), "grab-offen": ("offenes Grab", "offnigs Grab|offes Grab"),
    "raeucheraltar": ("Räucheraltar", "Räucheraltar"), "garbe": ("Garbe|Ährengarbe", "Garbe|Ährigarbe"), "worfel": ("Worfelgabel", "Worfelgable"),
    "kelle": ("Schöpfkelle", "Schöpfchelle"), "salbt-fuss": ("Nardenfläschchen|Fläschchen", "Nardefläschli|Fläschli"),
    "oelkrug": ("Ölkrug", "Ölchrueg"), "herz": ("Herz", "Härz"), "netz": ("Netz", "Netz"), "jesuskind": ("Kind", "Chind"),
}
texts = {}
for f in glob.glob(str(ROOT / "data/translations/TRANS-*-DE-WORKING.json")):
    texts.update(json.loads(pathlib.Path(f).read_text()).get("text_by_reference") or {})
BOOKS = ["RUT", "OBA", "JON", "MAT", "MRK", "LUK", "JHN", "PHP", "TIT", "1JN", "2JN", "3JN"]
def key(r):
    b, c, v = r.split(".")
    return BOOKS.index(b), int(c), int(v)
def verses(ref):
    if not ref:
        return []
    out = []
    for part in ref.split(","):
        part = part.strip()
        if "-" in part:
            a, b = part.split("-")
            if a.count(".") == 1: a += ".1"
            if b.count(".") == 1: b += ".999"
            ka, kb = key(a), key(b)
            out += [t for r, t in texts.items() if r.split(".")[0] in BOOKS and ka <= key(r) <= kb]
        else:
            ps = part.split(".")
            out += [t for r, t in texts.items() if r.split(".")[:len(ps)] == ps]
    return out
NAMES = {}
for f in sorted(A_DIR.glob("*.json")):
    if f.name.startswith("_"):
        continue
    for b in json.loads(f.read_text()):
        for p in b["panels"]:
            for k, v in (p.get("names") or {}).items():
                NAMES.setdefault(k, v)
def strip_words(cap, words):
    w = f"(?:{words})"
    cap2 = re.sub(rf"\s*\({w}\)", "", cap)
    cap2 = re.sub(rf"\(({w}), ", "(", cap2)
    cap2 = re.sub(rf", ({w})(?=[,)])", "", cap2)
    return cap2
apply = "--anwenden" in sys.argv
rep = []
cnt = collections.Counter()
for f in sorted(A_DIR.glob("*.json")):
    if f.name in SKIP:
        continue
    data = json.loads(f.read_text())
    changed = False
    for b in data:
        named = {k for p in b["panels"] for k in (p.get("names") or {})}
        for p in b["panels"]:
            st = p.get("stage") or {}
            hold = st.get("hold") or {}
            ref = p.get("reference") or b.get("reference")
            txt = " ".join(verses(ref))
            for fid in p["figures"]:
                a = (A.CHAR.get(A.KEY.get(fid, ""), {}) or {}).get("attr")
                if not a or fid in hold:
                    continue
                a = a[5:]
                if a not in SUPPORT:
                    continue
                pat = SUPPORT[a]
                ok = bool(pat and txt and re.search(pat, txt))
                if not txt and pat:
                    ok = True  # obere Ebenen ohne Versbereich: nicht entscheidbar, bleibt
                rep.append({"bild": b["suffix"], "feld": p["n"], "ref": ref, "figur": fid, "zeichen": a, "gestuetzt": ok})
                cnt[(a, ok)] += 1
                if not ok and apply:
                    p.setdefault("stage", {}).setdefault("hold", {})[fid] = "LEER"
                    if a in WORDS:
                        p["caption_de"] = strip_words(p["caption_de"], WORDS[a][0])
                        p["caption_gsw"] = strip_words(p["caption_gsw"], WORDS[a][1])
                    if fid not in named and fid in NAMES and fid not in ("FIG-JESUS",):
                        p.setdefault("names", {})[fid] = NAMES[fid]
                        named.add(fid)
                    changed = True
    if changed:
        f.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n")
out = ROOT / "reports/erkennungszeichen.json"
out.write_text(json.dumps(rep, ensure_ascii=False, indent=1))
print("gestützt / nicht gestützt je Zeichen:")
for a in sorted({a for a, _ in cnt}):
    print(f"  {a}: {cnt[(a, True)]} / {cnt[(a, False)]}")
print("Felder gesamt", len(rep), "nicht gestützt", sum(1 for r in rep if not r["gestuetzt"]))
