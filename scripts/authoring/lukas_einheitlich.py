"""Gemeinsame Festlegungen für die sechs Lukas-Werkzeuge (lukas_text_01_04.py … lukas_text_22_24.py).

Kein eigenes Werkzeug: Die Teile importieren von hier die gleichlautenden Entscheidungs- und Hinweistexte und prüfen ihre
Mundart gegen die festgelegte Schreibung (pruefe_mundart). Festgelegt bei der Vereinheitlichung vom 2026-10-26
(KI-Entwurf, Claude), damit Lukas wie aus einem Guss liest; [[LUK.11.1-LUK.11.4]] (vaterunser.py, zueridueuetsch.py)
bleibt unverändert und ist Bezugspunkt.

Wiederkehrende Wendungen (Hochdeutsch / Züridüütsch):
- ἐγένετο als Erzählformel: wiedergegeben, wo sie einen Abschnitt eröffnet (Erzähleinschnitt, wie [[LUK.11.1]]):
  καὶ ἐγένετο «Und es geschah» / «Und es isch gsii», ἐγένετο δέ «Es geschah aber» / «Es isch aber gsii». Innerhalb eines
  Abschnitts, wo sie nur den nächsten Erzählschritt anschliesst, nicht eigens wiedergegeben (~n mit EGEN_SKIP_*).
  Wo ἐγένετο ein eigenes Verb ist («wurde», «kam», «war», «es gab»), ist es als solches übersetzt.
- ἰδού: in der Erzählung «siehe» / «lueg»; in direkter Rede nach Zahl der Angesprochenen «sieh» / «seht»
  bzw. «lueg» / «lueged».
- μὴ φοβοῦ / μὴ φοβεῖσθε / μὴ φοβηθῆτε: «Fürchte dich nicht» / «Fürchtet euch nicht»; Mundart «Häb kei Angscht» /
  «Händ kei Angscht» (wie in Markus und Johannes mehrheitlich).
- οἱ ὄχλοι «die Menschenmengen» (wie Matthäus), ὄχλος «die Menge»; Mundart «d Lüüt» bzw. «d Mängi».
- νομικός «Gesetzeslehrer» / «Gsetzeslehrer» (wie Matthäus; ebenso νομοδιδάσκαλος, [[LUK.5.17]]).
- οὐαί «Weh» / «Weh»; ἀληθῶς «Wahrhaftig»; ἀποκριθεὶς … εἶπεν ohne vorausgehende Frage «ergriff das Wort» /
  «hät s Wort gnoo»; εὐθέως «sofort» / «grad», παραχρῆμα «sofort» / «sofort»; πλήν Mundart «aber» (Hochdeutsch je nach
  Satz «doch», «vielmehr»).
- Bereits einheitlich und so belassen: ἀμὴν λέγω ὑμῖν «Amen, ich sage euch» / «Amen, ich säg eu»; ὁ υἱὸς τοῦ ἀνθρώπου
  «der Menschensohn» / «de Mänschesohn»; ἐπιστάτα «Meister» / «Meischter»; διδάσκαλε «Lehrer»; κύριε «Herr»;
  μακάριος «selig» / «sälig»; γενεά «Geschlecht» / «Generation»; ἡ βασιλεία τοῦ θεοῦ «das Reich Gottes» / «s Riich vo
  Gott»; ὑποκριταί «Heuchler» / «Hüüchler»; Rede-Ebenen « » / ‹ › / „ “.

Mundart-Schreibung (MUNDART): Mehrheitsform in markus_text_*.py und johannes_text_*.py, gezählt am 2026-10-26 über alle
Mundart-Texte dieser Werkzeuge (Bibeltext, Abschnittstitel und -zusammenfassungen, Entscheidungen, Hinweise, Lesarten);
in Klammern Markus+Johannes festgelegte Form : abgelöste Form. Zusammengehörige Formen eines Wortes sind gemeinsam
gezählt; ohne Beleg in Markus/Johannes gilt die Mehrheit in Lukas bzw. die Form des Grundworts.
  userwählt, userwählte (8:6 uuserwäält-) · lehre, lehrt, glehrt, Lehr (44:16 leere, leert, gleert, Leer; das Nomen
  «Schriftgleerte» bleibt) · dört (87:14 det) · Chnü (4:2 Chnüü; das Verb «chnüüle» bleibt) · usggää, Partizip
  (Grundwort ggää) · gantwortet, Partizip (in Lukas 1–4 «antwortet») · gscheh (13:0 gschee) · Mueterliib (Mueter) ·
  wiitergange (2:0) · fürchte, fürchted, fürcht, gfürchtet (5:2 förcht-) · elei (30:0 ellei) · frömde (3:1 fremde) ·
  ggässe (17:0 gässe) · ghöre, ghöred (42:5 ghööre, ghööred) · ghüratet, hüratet, verhüratet (5:0 -hüraat-) · glöst
  (1:0) · gmäldet, mäldet (2:0) · Höchi, gröscht, Grössi (7:0 hööchi, grööscht) · Herde (9:0 Härde) · iigschlaafe (3:0)
  · chöm, chömende (3:1) · chönt, chönted (15:9 chönnt, chönnted) · Fälder (7:0) · riitet (2:0) · Schaf (42:0 Schaaf) ·
  Städt (2:1) · stärbe (22:4 sterbe) · strited (6:0) · Tüüre (5:1 Türe) · ufgläse (3:1) · uftrete (6:0) · Umkehr (6:1
  Umchehr) · ungläubig (2:0) · us- statt uus- in Zusammensetzungen (Ussendig, usfüerlich, usgaat, usrichte, ustriibed;
  7:0) · verdorret, verdorreti, verdorrete (9:2 verdoret-) · verrisse (4:2) · villicht (3:2) · wäg, wäggange (86:0 wägg,
  weggange) · wem (12:2 wäm) · wän (8:3 wen) · wärdi, wärfed (25:0) · zrugggange (Lukas 4:2) · choo, auch in
  Zusammensetzungen (zruggchoo, anechoo, s Choo; Grundwort 221:8, obwohl Markus «anecho» 2 hat) · Zügnis (69:5) ·
  böse, böses (10:6 bööse, bööses) · Greber (5:2 Gräber) · schnell (3:2 schnäll) · Jahr (14:0 Jaar) · Ohre (9:0 Oore) ·
  Lohn (4:2 Loon) · Söhn (5:4 Söön) · glähmt, glähmte (9:0 gläämt-) · zie, ziend, zieht (18:0 zieh, ziehnd, ziet) ·
  Wonige (4:0) · fahr, fahred, fahrt, gfahre (11:6 faar-) · befole (12:0) · fäält (26:14 fehlt) · nöi (14:2 nöii) · da
  (daa) · häre (25:0 here) · liide (11:0 lide) · legged (8:3 leged) · söle (7:0 sölle) · nöch, Nöchi (22:7 nööch-) ·
  Fäschtässe (Grundwort Fäscht; Markus/Johannes «Feschtässe» 3:1, das aber wie «fest» aussieht).
Bewusst nicht vereinheitlicht (eigene Wörter oder Formen, nicht Schreibvarianten): bliibe (Infinitiv) / blibe
(Partizip), triibe / tribe / tribt, gää (Infinitiv) / ggää (Partizip), «fiind» (feind), «Lischte» und «Liischte»
(je ein Beleg), «Schaubroot» (Grundwort Broot), und alles in [[LUK.11.1-LUK.11.4]] (dort «leer üs bätte», «gleert»).
"""
import re

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
            "[[LUK.11.1]] (" + _marken(ABSCHNITTSBEGINN) + "). Innerhalb vom Abschnitt, wo si nu de nööchscht Schritt "
            "aahänkt, isch si nöd eigens widergää, wil si de Satz dört nu schwärfällig macht (" + _marken(INNERHALB) + "). "
            "Wo ἐγένετο es eigets Verb isch («isch worde», «isch choo», «isch gsii»), isch es eso übersetzt.")
EGEN_SKIP_DE = "ἐγένετο «es geschah»: Erzählformel innerhalb des Abschnitts; nicht eigens wiedergegeben"
EGEN_SKIP_GSW = "ἐγένετο «es isch gsii»: Erzählformle innerhalb vom Abschnitt; nöd eigens widergää"

IDOU_DE = ("ἰδού ist in ganz Lukas gleich wiedergegeben: in der Erzählung «siehe», in direkter Rede nach der Zahl der "
           "Angesprochenen «sieh» oder «seht».")
IDOU_GSW = ("ἰδού isch im ganze Lukas gliich widergää: i de Verzellig «lueg», i de diräkte Red nach de Zaal vo de "
            "Aagredete «lueg» oder «lueged».")
FURCHT_GSW = ("μὴ φοβοῦ / μὴ φοβεῖσθε isch im ganze Lukas «Häb kei Angscht» / «Händ kei Angscht», wie bim Markus und "
              "Johannes meischtens.")
OCHLOI_DE = ("οἱ ὄχλοι ist in ganz Lukas «die Menschenmengen» (wie bei Matthäus), ὄχλος «die Menge»; λαός ist «das Volk».")

# Mundart: abgelöste Form -> festgelegte Form (klein geschrieben; Grossschreibung am Wortanfang wird übernommen).
MUNDART = {
    "uuserwäält": "userwählt", "uuserwäälte": "userwählte", "uuserwählt": "userwählt", "leert": "lehrt", "gleert": "glehrt", "leere": "lehre", "leer": "lehr", "det": "dört",
    "chnüü": "chnü", "usgää": "usggää", "gschee": "gscheh", "muetterliib": "mueterliib", "witergange": "wiitergange",
    "förchte": "fürchte", "förchted": "fürchted", "förcht": "fürcht", "gförchtet": "gfürchtet", "ellei": "elei",
    "fremde": "frömde", "gässe": "ggässe", "ghööre": "ghöre", "ghööred": "ghöred", "ghüraatet": "ghüratet",
    "hüraatet": "hüratet", "verhüraatet": "verhüratet", "glööst": "glöst", "gmeldet": "gmäldet", "meldet": "mäldet",
    "hööchi": "höchi", "grööscht": "gröscht", "gröössi": "grössi", "härde": "herde", "iigschlafe": "iigschlaafe",
    "chömm": "chöm", "chömmende": "chömende", "chönnt": "chönt", "chönnted": "chönted", "felder": "fälder",
    "rittet": "riitet", "schaaf": "schaf", "stedt": "städt", "sterbe": "stärbe", "striited": "strited", "türe": "tüüre",
    "ufglääse": "ufgläse", "ufträte": "uftrete", "umchehr": "umkehr", "unglöubig": "ungläubig", "uussändig": "ussendig",
    "uusfüerlich": "usfüerlich", "uusgaat": "usgaat", "uusrichte": "usrichte", "uustriibed": "ustriibed",
    "verdoret": "verdorret", "verdoreti": "verdorreti", "verdorete": "verdorrete", "verriisse": "verrisse",
    "vilicht": "villicht", "weggange": "wäggange", "wägg": "wäg", "wäm": "wem", "wen": "wän", "werdi": "wärdi",
    "werfed": "wärfed", "zruggange": "zrugggange", "zruggcho": "zruggchoo", "anecho": "anechoo", "cho": "choo",
    "züügnis": "zügnis", "bööse": "böse", "bööses": "böses", "gräber": "greber", "schnäll": "schnell", "jaar": "jahr",
    "oore": "ohre", "loon": "lohn", "söön": "söhn", "gläämt": "glähmt", "gläämte": "glähmte", "zieh": "zie",
    "ziehnd": "ziend", "ziet": "zieht", "wohnige": "wonige", "faar": "fahr", "faared": "fahred", "faart": "fahrt",
    "gfaare": "gfahre", "befohle": "befole", "fehlt": "fäält", "nöii": "nöi", "daa": "da", "here": "häre", "lide": "liide",
    "leged": "legged", "sölle": "söle", "nööch": "nöch", "nööchi": "nöchi", "feschtässe": "fäschtässe",
}
_WORT = re.compile(r"[A-Za-zÄÖÜäöüéèà]+")


def mundart_schreibung(text):
    """Ersetzt abgelöste Mundart-Formen durch die festgelegten (Grossschreibung am Wortanfang bleibt)."""
    def repl(m):
        w = m.group(0)
        neu = MUNDART.get(w.lower())
        if neu is None:
            return w
        return neu[0].upper() + neu[1:] if w[0].isupper() else neu
    return _WORT.sub(repl, text)


def pruefe_mundart(texte, wo):
    """Bricht ab, wenn ein Mundart-Text noch eine abgelöste Form enthält."""
    alt = sorted({w for t in texte for w in _WORT.findall(t) if w.lower() in MUNDART})
    if alt:
        raise SystemExit(f"{wo}: abgelöste Mundart-Schreibung {alt} (siehe scripts/authoring/lukas_einheitlich.py)")
