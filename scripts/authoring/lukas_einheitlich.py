"""Gemeinsame Festlegungen für die sechs Lukas-Werkzeuge (lukas_text_01_04.py … lukas_text_22_24.py).

Kein eigenes Werkzeug: Die Teile importieren von hier die gleichlautenden Entscheidungs- und Hinweistexte und prüfen ihre
Mundart (pruefe_mundart). Festgelegt bei der Vereinheitlichung vom 2026-10-26 (KI-Entwurf, Claude), damit Lukas wie aus
einem Guss liest. Seit der Neuübersetzung vom 2026-11-21 gilt für die Mundart das Regelwerk docs/ZUERIDUEUETSCH.md
(Gallmann, SRF-Merkblatt; geprüft mit scripts/mundart.py); die frühere Mehrheitsschreibung aus Markus und Johannes
(z. B. «fäält», «Söön», «üs», «ggää», «demit») ist abgelöst.

Wiederkehrende Wendungen (Hochdeutsch / Züridüütsch):
- ἐγένετο als Erzählformel: wiedergegeben, wo sie einen Abschnitt eröffnet (Erzähleinschnitt, wie [[LUK.11.1]]):
  καὶ ἐγένετο «Und es geschah» / «Und es isch gsii», ἐγένετο δέ «Es geschah aber» / «Es isch aber gsii». Innerhalb eines
  Abschnitts, wo sie nur den nächsten Erzählschritt anschliesst, nicht eigens wiedergegeben (~n mit EGEN_SKIP_*).
  Wo ἐγένετο ein eigenes Verb ist («wurde», «kam», «war», «es gab»), ist es als solches übersetzt.
- ἰδού: in der Erzählung «siehe» / «lueg»; in direkter Rede nach Zahl der Angesprochenen «sieh» / «seht»
  bzw. «lueg» / «lueged».
- μὴ φοβοῦ / μὴ φοβεῖσθε / μὴ φοβηθῆτε: «Fürchte dich nicht» / «Fürchtet euch nicht»; Mundart «Häb kei Angscht» /
  «Händ kei Angscht».
- οἱ ὄχλοι «die Menschenmengen» (wie Matthäus), ὄχλος «die Menge»; Mundart «d Lüüt» bzw. «d Mängi».
- νομικός «Gesetzeslehrer» / «Gsetzeslehrer» (wie Matthäus; ebenso νομοδιδάσκαλος, [[LUK.5.17]]).
- οὐαί «Weh» / «Weh»; ἀληθῶς «Wahrhaftig»; εὐθέως «sofort» / «grad», παραχρῆμα «sofort» / «sofort»; πλήν Mundart «aber»
  oder «lieber» (Hochdeutsch je nach Satz «doch», «vielmehr»).
- Einheitlich: ἀμὴν λέγω ὑμῖν «Amen, ich sage euch» / «Amen, ich säge öi»; ὁ υἱὸς τοῦ ἀνθρώπου «der Menschensohn» /
  «de Mänschesohn»; ἐπιστάτα «Meister» / «Meischter»; διδάσκαλε «Lehrer»; κύριε «Herr»; μακάριος «selig» / «sälig»;
  γενεά «Geschlecht» / «Generation»; ἡ βασιλεία τοῦ θεοῦ «das Reich Gottes» / «s Riich vo Gott»; ὑποκριταί «Heuchler» /
  «Hüüchler»; Rede-Ebenen « » / ‹ › / „ “.

Mundart-Schreibung: verbindlich ist docs/ZUERIDUEUETSCH.md; pruefe_mundart prüft mit scripts/mundart.py (pruefe: Sonderzeichen,
Wortliste, Präteritum, «um z», Apostroph, Genitiv) und zusätzlich mit der Lukas-Liste MUNDART (abgelöste Form -> gültige
Form). MUNDART enthält Formen, die in Lukas vorkamen und nach docs/ZUERIDUEUETSCH.md nicht mehr gelten, aber (noch) nicht
in der allgemeinen Wortliste von scripts/mundart.py stehen; dazu die Festlegungen der Vereinheitlichung vom 2026-10-26,
soweit sie mit dem Regelwerk übereinstimmen. Neu am 2026-11-21 (Begründung jeweils Regel im Regelwerk): Brot (1.3, nicht
«Broot»), Ernte (Zweifel: nahe am Hochdeutschen), zwei auch vor männlichen Nomen (2 Zahlen, nicht «zwee»), Apostel (3),
seig (2 Konjunktiv, nicht «sig»), jetzt (3), wieso (Pilot), überchoo (1.2 wie choo), schlafe/gschlafe (1.3, kein
Doppelvokal, wo das Hochdeutsche die Länge schon trägt), Tür/Türe (1.3), chönnt/chönnted (1.9 Doppelmitlaut nach
Hochdeutsch), befohle, Wohnig (1.3 Dehnungs-h), usgää/gässe (1.10), wäm (2 Fragewort), Fiischteri (Pilot Johannes).
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import mundart  # noqa: E402  (scripts/mundart.py)

DATUM = "2026-10-26"
GRUND = "Vereinheitlichung Lukas 2026-10-26"

ABSCHNITTSBEGINN = ["LUK.2.1", "LUK.3.21", "LUK.5.1", "LUK.5.12", "LUK.5.17", "LUK.6.1", "LUK.6.6", "LUK.6.12", "LUK.7.11",
                    "LUK.8.1", "LUK.8.22", "LUK.9.18", "LUK.9.28", "LUK.9.37", "LUK.9.51", "LUK.11.1", "LUK.11.27",
                    "LUK.14.1", "LUK.17.11", "LUK.18.35", "LUK.20.1"]
INNERHALB = ["LUK.1.8", "LUK.1.23", "LUK.1.41", "LUK.1.59", "LUK.2.6", "LUK.2.15", "LUK.2.46", "LUK.9.33", "LUK.11.14",
             "LUK.16.22", "LUK.17.14", "LUK.19.15", "LUK.19.29", "LUK.24.4", "LUK.24.15", "LUK.24.30", "LUK.24.51"]


def _marken(refs):
    return ", ".join(f"[[{r}]]" for r in refs)


EGEN_DE = ("Erzählformel ἐγένετο («es geschah») nach dem Vorbild der griechischen Bibel (hebräisch wajehi). Regel für ganz "
           "Lukas: Wo sie einen Abschnitt eröffnet, ist sie wiedergegeben – καὶ ἐγένετο «Und es geschah», ἐγένετο δέ «Es "
           "geschah aber», wie in [[LUK.11.1]] (" + _marken(ABSCHNITTSBEGINN) + "). Innerhalb eines Abschnitts, wo sie "
           "nur den nächsten Erzählschritt anschliesst, ist sie nicht eigens wiedergegeben, weil sie den Satz dort nur "
           "schwerfällig macht (" + _marken(INNERHALB) + "). Wo ἐγένετο ein eigenes Verb ist («wurde», «kam», «war»), "
           "ist es als solches übersetzt.")
EGEN_GSW = ("Erzählformle ἐγένετο («es isch gsii») nach em Vorbild vo de griechische Bible. Regle für de ganz Lukas: Wo si "
            "en Abschnitt aafangt, isch si widergää – καὶ ἐγένετο «Und es isch gsii», ἐγένετο δέ «Es isch aber gsii», wie i "
            "[[LUK.11.1]] (" + _marken(ABSCHNITTSBEGINN) + "). Innerhalb vom Abschnitt, wo si nume de nächscht Schritt "
            "aahänkt, isch si nöd eigens widergää, wil si de Satz dört nume schwärfällig macht (" + _marken(INNERHALB) + "). "
            "Wo ἐγένετο es eigets Verb isch («isch worde», «isch choo», «isch gsii», «hät s gää»), isch es eso übersetzt.")
EGEN_SKIP_DE = "ἐγένετο «es geschah»: Erzählformel innerhalb des Abschnitts; nicht eigens wiedergegeben"
EGEN_SKIP_GSW = "ἐγένετο «es isch gsii»: Erzählformle innerhalb vom Abschnitt; nöd eigens widergää"

IDOU_DE = ("ἰδού ist in ganz Lukas gleich wiedergegeben: in der Erzählung «siehe», in direkter Rede nach der Zahl der "
           "Angesprochenen «sieh» oder «seht».")
IDOU_GSW = ("ἰδού isch im ganze Lukas gliich widergää: i de Erzählig «lueg», i de diräkte Red nach de Zahl vo de "
            "Aagredete «lueg» oder «lueged».")
FURCHT_GSW = ("μὴ φοβοῦ / μὴ φοβεῖσθε isch im ganze Lukas «Häb kei Angscht» / «Händ kei Angscht»; so seit me s hüt.")
OCHLOI_DE = ("οἱ ὄχλοι ist in ganz Lukas «die Menschenmengen» (wie bei Matthäus), ὄχλος «die Menge»; λαός ist «das Volk».")

# Mundart: abgelöste Form -> gültige Form nach docs/ZUERIDUEUETSCH.md (klein geschrieben; Grossschreibung am Wortanfang
# wird übernommen). Ergänzt die Wortliste in scripts/mundart.py um Formen, die in Lukas vorkamen.
MUNDART = {
    # Festlegungen vom 2026-10-26, die mit dem Regelwerk übereinstimmen
    "uuserwäält": "userwählt", "uuserwäälte": "userwählte", "uuserwählt": "userwählt", "leert": "lehrt",
    "gleert": "glehrt", "leere": "lehre", "leer": "lehr", "det": "dört", "chnüü": "chnü", "gschee": "gscheh",
    "muetterliib": "mueterliib", "witergange": "wiitergange", "förchte": "fürchte", "förchted": "fürchted",
    "förcht": "fürcht", "gförchtet": "gfürchtet", "ellei": "elei", "ghööre": "ghöre", "ghööred": "ghöred",
    "ghüraatet": "ghüratet", "hüraatet": "hüratet", "verhüraatet": "verhüratet", "glööst": "glöst", "gmeldet": "gmäldet",
    "meldet": "mäldet", "hööchi": "höchi", "grööscht": "gröscht", "gröössi": "grössi", "härde": "herde",
    "chömm": "chöm", "chömmende": "chömende", "felder": "fälder", "rittet": "riitet", "schaaf": "schaf", "stedt": "städt",
    "sterbe": "stärbe", "ufglääse": "ufgläse", "ufträte": "uftrete", "umchehr": "umkehr", "unglöubig": "ungläubig",
    "uussändig": "ussendig", "uusfüerlich": "usfüerlich", "uusgaat": "usgaat", "uusrichte": "usrichte",
    "uustriibed": "ustriibed", "verdoret": "verdorret", "verdoreti": "verdorreti", "verdorete": "verdorrete",
    "verriisse": "verrisse", "vilicht": "villicht", "weggange": "wäggange", "wägg": "wäg", "wen": "wän",
    "werdi": "wärdi", "werfed": "wärfed", "zruggange": "zrugggange", "zruggcho": "zruggchoo", "anecho": "anechoo",
    "cho": "choo", "züügnis": "zügnis", "bööse": "böse", "bööses": "böses", "schnäll": "schnell", "jaar": "jahr",
    "oore": "ohre", "loon": "lohn", "söön": "söhn", "gläämt": "glähmt", "gläämte": "glähmte", "faar": "fahr",
    "faared": "fahred", "faart": "fahrt", "gfaare": "gfahre", "nöii": "nöi", "daa": "da", "here": "häre", "lide": "liide",
    "leged": "legged", "sölle": "söle", "nööch": "nöch", "nööchi": "nöchi", "feschtässe": "fäschtässe",
    # Neu nach docs/ZUERIDUEUETSCH.md (2026-11-21); früher in Lukas festgelegt, jetzt abgelöst
    "fäält": "fehlt", "ziet": "zieht", "zie": "zieh", "ziend": "ziehnd", "wonige": "wohnige", "befole": "befohle",
    "usggää": "usgää", "ggässe": "gässe", "wem": "wäm", "chönt": "chönnt", "chönted": "chönnted",
    "iigschlaafe": "iigschlafe", "schlaaft": "schlaft", "gschlaafe": "gschlafe", "tüüre": "türe", "tüür": "tür",
    "broot": "brot", "schaubroot": "schaubrot", "zwee": "zwei", "aposchtel": "apostel", "sig": "seig", "jetz": "jetzt",
    "werum": "wieso", "übercho": "überchoo", "hüchler": "hüüchler", "ärnt": "ernte", "ärnte": "ernte",
    "fischter": "fiischter", "fischtere": "fiischtere", "fischternis": "fiischteri", "niemertem": "niemerem",
    "niemert": "niemer", "drüü": "drü", "Tämpel": "tempel", "schriftgleerte": "schriftglehrte", "schriftgleerti": "schriftglehrti",
}
MUNDART = {k.lower(): v for k, v in MUNDART.items()}
_WORT = re.compile(r"[A-Za-zÄÖÜäöüéèà]+")


def mundart_schreibung(text):
    """Ersetzt abgelöste Mundart-Formen der Lukas-Liste durch die gültigen (Grossschreibung am Wortanfang bleibt)."""
    def repl(m):
        w = m.group(0)
        neu = MUNDART.get(w.lower())
        if neu is None:
            return w
        return neu[0].upper() + neu[1:] if w[0].isupper() else neu
    return _WORT.sub(repl, text)


def _flach(x):
    """Texte aus Strings, Listen, Tupeln und Dicts; ein als str(…) übergebenes Tupel oder eine Liste wird wieder zerlegt,
    damit Python-Anführungszeichen nicht als Apostroph gelten."""
    if x is None:
        return
    if isinstance(x, str):
        if x[:1] in "([{" and x[-1:] in ")]}":
            try:
                import ast
                y = ast.literal_eval(x)
            except (ValueError, SyntaxError):
                y = None
            if isinstance(y, (list, tuple, dict)):
                yield from _flach(y)
                return
        yield x
    elif isinstance(x, dict):
        for v in x.values():
            yield from _flach(v)
    elif isinstance(x, (list, tuple)):
        for v in x:
            yield from _flach(v)


def pruefe_mundart(texte, wo, streng=True):
    """Bricht ab, wenn ein Mundart-Text eine abgelöste Form der Lukas-Liste (MUNDART) oder – mit streng (Vorgabe) – einen
    Fund von scripts/mundart.py (docs/ZUERIDUEUETSCH.md) enthält."""
    texte = list(_flach(list(texte)))
    alt = sorted({w for t in texte for w in _WORT.findall(t) if w.lower() in MUNDART})
    funde = sorted({f"{g} -> {neu} [{regel}]" for t in texte for g, regel, neu in mundart.pruefe(t)}) if streng else []
    if alt or funde:
        raise SystemExit(f"{wo}: Mundart nach docs/ZUERIDUEUETSCH.md: abgelöst {alt} {funde} "
                         "(scripts/mundart.py, scripts/authoring/lukas_einheitlich.py)")
