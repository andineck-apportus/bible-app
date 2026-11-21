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

Angleichung an docs/ZUERIDUEUETSCH.md (2026-11-21, zweiter Durchgang): Aus MUNDART gestrichen, was dem Regelwerk
widerspricht: «sterbe» -> «stärbe» (Regel 1.6: «sterbe»), «cho» -> «choo» (Abschnitt 2 Infinitiv: «cho luege» bei
Bewegung bleibt); «werdi» zeigt jetzt auf «wärd» (Abschnitt 2, indirekte Rede «er wärd»). MUNDART und pruefe_mundart
behalten ihre Schnittstelle (kernanalyse.py nutzt sie für alle Bücher).
Fehlalarm (FEHLALARM, nur in pruefe_mundart ausgenommen): Die Wortliste von scripts/mundart.py führt «häb» -> «heb» für
die indirekte Rede (Konjunktiv «er heb»). Der Imperativ von «haa» heisst aber «häb» («Häb kei Angscht», «häb Erbarme»;
«heb» ist der Imperativ von «hebe», halten). Imperative in festen Wendungen werden deshalb nicht gemeldet, ebenso der
Apostroph in englischen Buchtiteln («The Preface to Luke's Gospel») und Datensatz-IDs im Text («FIND-LUK-0008» als Wort
«FIND»); Regelvorschläge in der Rückmeldung vom 2026-11-21.
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
IDOU_GSW = ("ἰδού isch im ganze Lukas gliich widergää: i de Erzählig «lueg», i de direkte Red nach de Zahl vo de "
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
    "ufglääse": "ufgläse", "ufträte": "uftrete", "umchehr": "umkehr", "unglöubig": "ungläubig",
    "uussändig": "ussendig", "uusfüerlich": "usfüerlich", "uusgaat": "usgaat", "uusrichte": "usrichte",
    "uustriibed": "ustriibed", "verdoret": "verdorret", "verdoreti": "verdorreti", "verdorete": "verdorrete",
    "verriisse": "verrisse", "vilicht": "villicht", "weggange": "wäggange", "wägg": "wäg", "wen": "wän",
    "werdi": "wärd", "werfed": "wärfed", "zruggange": "zrugggange", "zruggcho": "zruggchoo", "anecho": "anechoo",
    "züügnis": "zügnis", "bööse": "böse", "bööses": "böses", "schnäll": "schnell", "jaar": "jahr",
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
    # Zweiter Durchgang 2026-11-21 (Anwendung der Regeln 1.3, 1.5–1.8, Abschnitte 2 und 3 auf Formen, die in Lukas
    # vorkamen; Kontextfälle wie «naa» = nach/nah, «root» = Rat/rät, «mer» = man/wir von Hand gelöst)
    "aabigmahl": "abigmahl", "aagaab": "aagab", "aagaabe": "aagabe", "gaab": "gab", "gaabe": "gabe", "aasaag":
    "aasag", "aanaam": "aanahm", "aateilnaam": "aateilnahm", "ufnaam": "ufnahm", "ufenaam": "ufenahm", "gfangenaam":
    "gfangenahm", "brootbräche": "brotbräche", "fladebroot": "fladebrot", "johannisbroot": "johannisbrot", "daar":
    "dar", "daarstelle": "darstelle", "daarstellig": "darstellig", "daarstellt": "darstellt", "daarzstelle":
    "darzstelle", "daate": "date", "einzaal": "einzahl", "zaal": "zahl", "zaale": "zahle", "zaalt": "zahlt",
    "zaalzeiche": "zahlzeiche", "meerzaal": "mehrzahl", "värszaale": "värszahle", "erchläärt": "erchlärt",
    "erkläärig": "erklärig", "erkläärige": "erklärige", "erfaart": "erfahrt", "faarplan": "fahrplan", "himmelfaart":
    "himmelfahrt", "widerfaare": "widerfahre", "gfaar": "gfahr", "fleet": "fleht", "frööge": "fröge", "fääled":
    "fehled", "fäälentwicklige": "fehlentwicklige", "fääler": "fehler", "verfäält": "verfehlt", "gleerte": "glehrte",
    "gläägeheit": "glägeheit", "gnaad": "gnad", "graabe": "grabe", "groosszügig": "grosszügig", "gseend": "gsehnd",
    "gseet": "gseht", "gsehned": "gsehnd", "aagsee": "aagseh", "gstraaft": "gstraft", "gwöönlich": "gwöhnlich",
    "gwöönliche": "gwöhnliche", "gwöönlichs": "gwöhnlichs", "ungwöönlich": "ungwöhnlich", "hööred": "höred",
    "iicheert": "iichehrt", "umgcheert": "umgchehrt", "iiglaadne": "iigladne", "iiglaadni": "iigladni", "laadt":
    "ladt", "klaagfrau": "klagfrau", "klaagfraue": "klagfraue", "klaaglieder": "klaglieder", "kolleege": "kollege",
    "laag": "lag", "laage": "lage", "leewort": "lehnwort", "loond": "lohnd", "maal": "mahl", "maalziit": "mahlziit",
    "maalziite": "mahlziite", "passamaal": "passamahl", "maanig": "mahnig", "maant": "mahnt", "usgmaalt": "usgmalt",
    "usmaalt": "usmalt", "mee": "meh", "meerere": "mehreri", "meereri": "mehreri", "meermaals": "mehrmals", "määntig":
    "mäntig", "naach": "nöch", "denaa": "dernach", "dernaa": "dernach", "naalaat": "nachlaat", "naazgää": "nachzgää",
    "nööche": "nöche", "nööchschte": "nöchschte", "erhööcht": "erhöcht", "erhööhe": "erhöhe", "erhööht": "erhöht",
    "plaage": "plage", "raame": "rahme", "raamt": "rahmt", "rääge": "räge", "saame": "same", "schaarfi": "scharfi",
    "schlaafed": "schlafed", "schlaafende": "schlafende", "spoot": "spot", "spoote": "spote", "spööte": "spöte",
    "spööter": "spöter", "spöötere": "spötere", "spööteri": "spöteri", "spraachaagab": "sprachaagab",
    "spraachgebruuch": "sprachgebruuch", "säät": "sät", "sääit": "säit", "sääed": "säed", "taat": "tat", "taate":
    "tate", "taglöön": "taglöhn", "toose": "tose", "troon": "thron", "tröön": "thrön", "ufgheebti": "ufghebti",
    "ufhööre": "ufhöre", "ussaag": "ussag", "usreede": "usrede", "uswaal": "uswahl", "waal": "wahl", "verraat":
    "verrat", "verraate": "verrate", "verroot": "verrat", "verrääter": "verräter", "verdrääti": "verdrähti",
    "versööne": "versöhne", "versöönig": "versöhnig", "versöönigstag": "versöhnigstag", "voruussaag": "voruussag",
    "wäält": "wählt", "zuesaag": "zuesag", "zäänechnirsche": "zähnechnirsche", "zäätuusig": "zähtuusig",
    "ältischteraat": "ältischterat", "ungefäär": "ungefähr", "ungfääri": "ungfähri", "unternäämer": "unternehmer",
    "erwäänt": "erwähnt", "bloosgstellt": "blossgstellt", "bewaared": "bewahred", "bewaart": "bewahrt", "abgleent":
    "abglehnt", "chliivee": "chliiveh", "nadelööhr": "nadelöhr", "gwonte": "gwohnte", "lidet": "liidet", "ziitaagaab":
    "ziitaagab", "ortsaagaab": "ortsaagab", "ortsaagaabe": "ortsaagabe", "werkaagaab": "werkaagab", "rückgaab":
    "rückgab", "ufgaab": "ufgab", "ufgaabe": "ufgabe", "usgaab": "usgab", "widergaab": "widergab", "hingaab":
    "hingab", "süschteem": "süschtem", "riichssüschteem": "riichssüschtem", "schwääre": "schwäre", "schwääri":
    "schwäri", "zieed": "ziehnd", "zied": "ziehnd", "mitzie": "mitzieh", "bezie": "bezieh", "usezie": "usezieh",
    "wiiterzie": "wiiterzieh", "zruggziet": "zruggzieht", "iigloo": "iiglaa", "wäggloo": "wägglaa", "wiederholti":
    "widerholti", "barmhärzig": "barmherzig", "barmhärzige": "barmherzige", "barmhärzigkeit": "barmherzigkeit",
    "ärnted": "ernted", "ärntisch": "erntisch", "priester": "prieschter", "hohepriester": "hoheprieschter",
    "verdienst": "verdienscht", "königin": "chönigin", "königliche": "chönigliche", "königriich": "chönigriich",
    "königsherrschaft": "chönigsherrschaft", "königslinie": "chönigslinie", "königspalascht": "chönigspalascht",
    "königspaläscht": "chönigspalascht", "königspalääscht": "chönigspalascht", "königswürde": "chönigswürde",
    "königswürdi": "chönigswürdi", "dreikönigstag": "dreichönigstag", "gottesknächt": "gotteschnächt", "diräkter":
    "direkter", "diräkts": "direkts", "indiräkt": "indirekt", "drüümal": "drümal", "sölled": "söled", "welles":
    "weles", "sigid": "seiged", "chöntsch": "chönntsch", "kein": "kei", "dem": "däm", "achtzää": "achtzäh", "achzää":
    "achtzäh", "drizää": "drizäh", "föifzää": "füfzäh", "nüünzää": "nüünzäh", "siebezää": "siebezäh", "dezueggää":
    "dezuegää", "mitggää": "mitgää", "zruggzale": "zruggzahle", "heuchler": "hüüchler", "aposchtelgschicht":
    "apostelgschicht", "jaarhundert": "jahrhundert", "jaarzähnt": "jahrzähnt", "tämpelbezirk": "tempelbezirk",
    "tämpelgäld": "tempelgäld", "tämpelhuus": "tempelhuus", "tämpelreinigig": "tempelreinigig", "tämpelvorhang":
    "tempelvorhang", "tämpelvorhof": "tempelvorhof", "gfüelt": "gfühlt", "überlieferet": "überliferet",
    "überliefered": "überlifered", "überlieferig": "überliferig", "uslieferig": "usliferig", "uszliefere": "uszlifere",
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


# Imperativ «häb» (von «haa») in festen Wendungen; scripts/mundart.py meldet «häb» als Konjunktiv (-> «heb»).
# Auszeichnungsfest ([Häb]{3} [kei Angscht]{4,5}). Dazu englische Buchtitel mit Genitiv-Apostroph («Luke's Gospel»), die
# das Apostroph-Muster (Regel 1.11) sonst meldet.
FEHLALARM = re.compile(r"\b([Hh])äb(?=(?:\]\{[^}]*\})?\s+\[?(?:kei|keis|keini|Erbarme|Geduld|Sorg|Acht|Vertroue|Muet)\b)")
FEHLALARM_TITEL = re.compile(r"\b(Luke|Mark|Matthew|John)['’]s (?=Gospel\b)")
# Datensatz-IDs im Text (FIND-LUK-0008): «FIND» ist kein Mundartwort (Wortliste: «find» -> «fiind»).
FEHLALARM_ID = re.compile(r"\b[A-Z]{2,}(?:-[A-Z0-9]+)+\b")


def _ohne_fehlalarm(t):
    return FEHLALARM_ID.sub("", FEHLALARM_TITEL.sub(r"\1s ", FEHLALARM.sub(r"\1aa", t)))


def pruefe_mundart(texte, wo, streng=True):
    """Bricht ab, wenn ein Mundart-Text eine abgelöste Form der Lukas-Liste (MUNDART) oder – mit streng (Vorgabe) – einen
    Fund von scripts/mundart.py (docs/ZUERIDUEUETSCH.md) enthält. Ausgenommen sind die Fehlalarme in FEHLALARM."""
    texte = list(_flach(list(texte)))
    alt = sorted({w for t in texte for w in _WORT.findall(t) if w.lower() in MUNDART})
    funde = sorted({f"{g} -> {neu} [{regel}]" for t in texte
                    for g, regel, neu in mundart.pruefe(_ohne_fehlalarm(t))}) if streng else []
    if alt or funde:
        raise SystemExit(f"{wo}: Mundart nach docs/ZUERIDUEUETSCH.md: abgelöst {alt} {funde} "
                         "(scripts/mundart.py, scripts/authoring/lukas_einheitlich.py)")
