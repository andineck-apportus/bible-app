# Züritüütsch: Schreibung, Formen, Wortwahl

Verbindliche Regeln für alle Züritüütsch-Texte der App: Bibeltext (Übersetzungsschicht `gsw-u-sd-chzh`), Titel,
Zusammenfassungen, Studieninhalte, Bildworte. Festgelegt am 2026-11-21 (KI-Entwurf, Claude, nach Entscheiden von
Andi Neck). Nicht von Mundart-Fachleuten geprüft.

Geprüft wird mit `scripts/mundart.py` (Regeln und Wortliste unten als Daten); `python3 scripts/mundart.py` zeigt die
Abweichungen je Buch.

## Grundlagen

- **Heinz Gallmann: Zürichdeutsches Wörterbuch**, 3., überarbeitete Auflage, Verlag NZZ. Einleitung Kap. 5
  (Lautsystem, Schreibung) und Kap. 6 (Abriss Grammatik) sowie Wörterbuchteil. Massgeblich für **Wortformen,
  Lautung, Grammatik und Wortschatz**.
- **Daniela Zimmermann: Empfehlungen für die zürichdeutsche Schreibung** (Merkblatt Radio SRF). Massgeblich für die
  **Buchstaben**: Schreibung nahe am Hochdeutschen, wie man heute Mundart schreibt.
- Zum Vergleich (nicht als Vorlage, nichts übernommen): Emil Weber, «s Nöi Teschtamänt Züritüütsch»; Josua Boesch,
  «s Johannes-Evangeelium Züritüütsch»; Viktor Schobinger, Zürichdeutsche Kurzgrammatik.

Die Bücher liegen als Fotos bei Andi (nicht im Repository, urheberrechtlich geschützt). Hier stehen nur die
abgeleiteten Regeln in eigenen Worten.

**Entscheide (Andi, 2026-11-21):** Schreiben, wie man heute Mundart schreibt, einfach und gut lesbar: keine
Sonderzeichen ausser ä, ö, ü; `ei` und Dehnungs-h wie im Hochdeutschen (nicht Gallmanns `äi`, `Jaar`); «Mänsch»
(nicht «Mäntsch»). Gallmanns lautnahe Dieth-Schreibung bestimmt also nicht die Buchstaben, wohl aber, welches Wort und
welche Form gilt.

**Im Zweifel** (Andi, 2026-11-21): so, wie man heute schreibt, nach der SRF-Regel nahe am Hochdeutschen (z. B.
`damit`, `Tempel`, `Erde`, `wieso`). Gallmanns Formen gelten für die häufigen Grundwörter (`hät`, `gää`, `gaat`,
`Dänn`, `öis`), nicht für jede seltene Lautung.

## 1 Schreibung

1. **Buchstaben:** nur a–z, ä, ö, ü. Kein è, é, ò, ù, ì, keine Unterstreichung. Gross- und Kleinschreibung wie im
   Hochdeutschen (Nomen gross). Die Anrede Gottes «du» klein.
2. **Lange Vokale doppelt, wo das Hochdeutsche keine Hilfe gibt:** wo hochdeutsch `au`, `ei`, `eu` steht, die
   Mundart aber einen langen Einzellaut hat: `Huus`, `Muur`, `Ziit`, `schriibe`, `Lüüt`, `tüür`, `Chrüüz`. Ebenso
   bei mundarteigenen Längen, die das Hochdeutsche nicht hat: `gaa`, `staa`, `choo`, `überchoo`, `gsii`, `haa`, `laa`,
   `nüüt`, `Aafang`, `Fiind`, `Fiischteri`.
3. **Sonst wie im Hochdeutschen:** Dehnungs-h und Doppelvokale nach hochdeutschem Vorbild, auch wenn kurz gesprochen:
   `ihm`, `ihn`, `ohni`, `Jahr`, `mehr`/`meh`, `gseh`, `Lehrer`, `wahr`, `Wahrheit`, `fehlt`, `Sohn`, `Söhn`. Bei
   einsilbigen Verben mit langem Vokal ebenfalls h: `gseh`, `gscheh`, `zieh`, `näh`. Hat das Hochdeutsche denselben
   langen Vokal ohne Zeichen, einfach schreiben: `Brot`, `Tür`, `Rat`, `Tag`, `Abig`, `Schlaf`, `Lüge`, `Ehe`, `Veh`,
   `Thron`, `schön`, `bös`, `höch`, `nöch` (nicht «Broot», «Tüür», «Raat», «Taag», «Aabig», «schöön», «nööch»).
4. **`ei`, `au`, `öi`:** Der Zürcher ei-Laut wird `ei` geschrieben (`zwei`, `gseit`, `Geischt`, `heilig`, `kei`).
   `au` bleibt (`Frau`, `Baum`, `glaube`), `öi` bleibt (`nöi`, `Fröid`, `Höi`).
5. **`ie`, `ue`, `üe` nur für Zwielaute:** `lieb`, `Liecht`, `Chrieg`, `guet`, `Bluet`, `Brüeder`, `früe`. Nie `ie`
   für ein langes i: `wider` (nicht «wieder»), `vil` (nicht «viel»), `spile`.
6. **e oder ä:** `ä`, wo ä gesprochen wird und das Hochdeutsche e oder ä hat (`Mänsch`, `Wält`, `Läbe`, `läse`,
   `schlächt`, `Bärg`, `wäg`). Gallmanns offenes `è`: `e`, wo das Hochdeutsche e hat (`Herr`, `Herz`, `Erde`, `Ernte`,
   `gern`, `sterbe`, `fertig`, `merke`); `ä` nur in den häufigen Grundwörtern, wo das heute allgemein so geschrieben
   wird: `dä`, `däm`, `wär`, `wäm`, `gää`, `wärde`, `här`. Das unbetonte e (Schwa) immer `e` (`säge`, `luege`).
7. **sp, st:** am Wort- und Stammanfang wie im Hochdeutschen (`Stei`, `Stimm`, `spile`, `verstaa`); im Wortinnern und
   am Ende `scht`, `schp` (`Geischt`, `Prieschter`, `fescht`, `Fänschter`).
8. **k und ch:** `ch`, wo ch gesprochen wird (`Chind`, `chunnt`, `Chrüüz`, `Chile`); `k`/`ck` wie im Hochdeutschen,
   wo kch gesprochen wird; `gg`, wo ein weiches k gesprochen wird (`Schnägg`, `Schoggi`). Also `Chönig`, `Chnächt`,
   `Chrankheit` (nicht «König», «Knecht»).
9. **Mitlaute** (b, p, d, t, m, n, l, r): wie im Hochdeutschen, auch wenn anders gesprochen. Doppelmitlaut im
   Wortinnern nach Hochdeutsch (`Sunne`, `Himmel`, `alli`), nie am Wortanfang.
10. **Partizip:** kein `gg-` oder `gch-` für die Vorsilbe ge-: `gange`, `gää`, `gässe`, `kauft`, `bracht`, `treit`
    (nicht «ggange», «ggää», «ggässe», «gchauft», «praacht»). Verben, die in der Mundart mit ch anfangen, behalten es
    nach g-: `gchrüüziget`, `umgchehrt`, `gchochet`, `aagchündet`; einzige Ausnahme ist `kauft`/`verkauft`
    (Merkblatt-Beispiel, allgemein üblich).
11. **Wortgrenzen und Apostroph:** Wörter getrennt schreiben, auch Einbuchstabenwörter: `s Wort`, `d Frau`, `i de
    Wält`, `hät s gseh`, `z Jerusalem`. Kein Apostroph (`s Huus`, nicht «'s Huus»). Zusammen nur, was nicht mehr zu
    trennen ist: `gömmer`, `wämmer`, `hämmer`, `simmer`; sonst getrennt: `sind s`, `soll s`, `isch s` (nicht «sinds»).
12. **Gleit-n:** nach `wo`, `wie`, `zue`, `cha` vor `er`, `es`, `em`, `en` (Fürwort oder Artikel) ans Wort davor:
    `won er`, `won en Maa`, `wien es Chind`, `zuen em`, `chan er`. Nicht vor `ich`, `si`, `me`, `mer`, `ir`.
13. **Endung -ung** wird `-ig`: `Wohnig`, `Beerdigig`, `Chrüüzigig`, `Ussag`, `Überliferig` (nicht «-ung»).

## 2 Formen (nach Gallmann, Kap. 6)

**Artikel:** `de Maa`, `d Frau`, `s Chind`; Dativ `em Maa`, `de Frau`, `em Chind`; Plural `d Manne`, Dativ `de
Manne`. Unbestimmt `en Maa`, `e Frau`, `es Chind`; Dativ `eme Maa`, `ere Frau`, `eme Chind`. Zusammengezogen: `vom`,
`im`, `am`, `ufem`, `bim`, `zum`, `zur`; `amene`, `imene`, `vomene`, `zumene`.

**Adjektiv:** nach bestimmtem Artikel schwach (`de guet Maa`, `di schön Frau`, `s lieb Chind`, Dativ `em guete
Maa`), nach unbestimmtem stark (`en guete Maa`, `e gueti Frau`, `es chliises Chind`). Steigerung `schöner`,
`am schönschte`; `guet – besser – bescht`, `vil – meh – am meischte`.

**Persönliche Fürwörter** (betont / unbetont):

| | Nominativ | Dativ | Akkusativ |
|---|---|---|---|
| ich | ich / i | mir / mer | mich / mi |
| du | du / de | dir / der | dich / di |
| er | er | ihm / em | ihn / en |
| sie (Einzahl) | si | ire / ere | si |
| es | es / s | ihm / em | es / s |
| wir | mir / mer | öis | öis |
| ihr | ir / er | öi | öi |
| sie (Mehrzahl) | si | ine / ene | si |

- `öis`, `öise`, `öisi` (nicht «üs», «üse»; `üüs` ist nur nördliches Weinland).
- Besitz: `min`, `din`, `sin`, `mini`, `dini`, `sini`; `öise`,
  `öisi`, `öises`; `öie`, `öii`; `ire`, `iri`, `ires`. Dativ `minere`, `sinere`.
- Höflichkeitsform `Si` (3. Person Mehrzahl), nicht «Ir».
- Hinweisend: `dä`, `die`, `das` (betont `dää`, `daas` nur zur Betonung).
- Fragend: `wär`, `wäm`, `was`, `wele`, `weli`, `weles`.
- **Bezugswort immer `wo`:** `de Maa, wo chunnt`; `d Frau, wo mer gseh händ`; mit Fall: `de Maa, won em s Huus
  ghört` bzw. `de Maa, wo s Huus vo ihm isch`. Nie «der», «die», «welcher» als Relativpronomen.
- Unbestimmt: `öpper` (jemand), `öppis` (etwas), `niemer` (niemand), `nüüt` (nichts), `mänge`, `jede`, `alli`,
  `es paar`, `me` (man), `kei`, `keini` (kein).

**Zahlen:** `eis`, `zwei`, `drü`, `vier`, `föif`; vor Nomen unveränderlich `zwei Manne`, `zwei Fraue`, `zwei Chind`.
Ordnungszahl `erscht`, `zweit`, `dritt`. Nach Zahl Einzahl bei Massen: `zwei Glas Wii`, `drü Jahr`.

**Verb:**
- **Kein Präteritum.** Vergangenes im Perfekt: `er isch choo`, `si händ gseit`. Formen wie «war», «hatte», «kam»,
  «sagte», «ging» kommen im Mundarttext nicht vor. Vorvergangenheit (Doppelperfekt) sparsam: `won er choo gsii
  isch`.
- Perfekt mit `sii` auch bei `staa`, `sitze`, `ligge`: `er isch gstande`, `si isch gsässe`, `es isch gläge`.
- Mehrzahl Gegenwart auf `-ed` (alle drei Personen gleich): `mir mached`, `ir mached`, `si mached`; Kurzverben `händ`,
  `sind`, `gönd`, `stönd`, `chömed`, `gänd`, `nämed`, `lönd`, `tüend`, `wänd`, `chönd`, `müend`, `söled`, `dörfed`,
  `wüssed`.
- Häufige Verben: `gaa` (gaat, gönd, gange), `staa` (staat, stönd, gstande), `choo` (chunnt, chömed, choo), `haa` (hät,
  händ, ghaa), `sii` (isch, sind, gsii), `tue` (tuet, tüend, taa), `gää` (git, gänd, gää), `näh` (nimmt, nämed, gnoo),
  `laa` (laat, lönd, glaa), `säge` (seit, säged, gseit), `gseh` (gseht, gsehnd, gseh), `wärde` (wird, wärded, worde),
  `chöne` (cha, chönd), `wele` (wott, wänd), `müese` (mues, müend), `söle` (söll, söled), `dörfe` (darf, dörfed),
  `wüsse` (weiss, wüssed, gwüsst).
- **Zukunft** meist im Präsens mit Zeitangabe (`er chunnt bald`, `dänn gsehnd er`); `wärde` + Infinitiv nur für
  Vermutung oder wo der Urtext das Künftige betont und es sonst unklar bliebe.
- **Passiv** sparsam; die Mundart zieht das Aktiv vor (`me hät en …`). Beim göttlichen Passiv des Urtexts (Gott als
  verschwiegener Täter) bleibt das Passiv (`si wärded tröschtet`), damit nichts hineingedeutet wird.
- **Konjunktiv:** indirekte Rede `er seig`, `si hebed`, `es gäb`; Unwirkliches `wär`, `hett`, `chäm`, `gieng`, sonst
  `würd` + Infinitiv.
- **Infinitiv:** `go` und `cho` bei Bewegung (`er gaat go bätte`, `si chömed cho luege`); `z` statt «zu» (`er hät
  aagfange z rede`); kein «um zu», sondern `zum` oder `damit`.
- Fusionen schreiben wie gesprochen und üblich: `hät s`, `isch es`, `gömmer`, `wämmer`.

**Kein Genitiv** (ausser in festen Wendungen): `s Huus vo mim Vatter` oder `em Vatter sis Huus`, `s Riich vo Gott`,
nicht «des Vaters», «Gottes Riich». In Namen von Personen und festen Begriffen ist `Gottes` zulässig, wo es ein
Eigenname ist (z. B. Buchtitel); im Bibeltext nicht.

**Weitere Festlegungen (Neuübersetzung 2026-11-21, aus allen Büchern zusammengeführt):**
- Fürwörter: `öi`, `öie`, `öii` (nicht «eu», «eui»); Dativ der Besitzwörter `minere`, `irere`, `öiere`, `öiem`;
  Mehrzahl `ire`, `öise` (nicht «irne», «öisne»); Fragewort und verallgemeinerndes `wär`; `me` für «man», `mer` nur für
  «wir»/«mir»; `niemer`, Dativ `niemerem`; `alli` (nicht «ali»).
- Zahlen: `zwei` für alle Geschlechter (nicht «zwee», «zwo»), `drü`, `drümal`, `drühundert`, `föif`, `zäh`, `vierzäh`,
  `füfzäh`, `zähtuusig`; Zahlen im Dativ unverändert (`zwei vo ine`).
- Nomen: `Manne` (Mehrzahl von Maa), `Brüeder` (Ein- und Mehrzahl), `Schriftglehrte` (mit Artikel) / `Schriftglehrti`,
  `Hüüchler`, `Fiind`, `Chönig`, `Tempel`, `Erde`, `Ernte`, `Herz`, `Brot`, `Lohn`, `Himmel`, `Himmelriich`.
- Verben: `damit` (nicht «demit»); `bracht`, `ghaa`, `überchoo`; `han` (ich habe) und `haa` (haben); `wele`, `söle`
  (nicht «welle», «sölle»); `chönnt`, `chönnted`; Mehrzahl auf `-ed` auch im Konjunktiv (`seiged`, `wüssed`); indirekte
  Rede `er seig`, `si seiged`, `er heb`, `si hebed`, `er wärd`; `wieso` (nicht «werum»); `zum` + Infinitiv ohne `z`
  (`zum s Gsetz ufhebe`); nach Bewegung Absicht mit `go` (`isch ine gange, go öppis hole`).
- Zukunft mit `wärde` bleibt, wo eine Lesart sich nur in der Zeitform unterscheidet oder der Urtext das Künftige
  betont; sonst Präsens. Passiv bleibt beim göttlichen Passiv und wo eine Lesart sonst nicht unterscheidbar wäre; sonst
  Aktiv mit `me`.
- Matthäus: βασιλεία τῶν οὐρανῶν `s Himmelriich`; Erfüllungsformel `damit sich erfüllt, was (vom Herr) dur de Prophet …
  gseit worde isch`.

**Festlegungen Runde 3 (2026-11-21, aus den Rückmeldungen aller Bereiche):**
- Länge: Hat die Mundart einen anderen Vokal als das Hochdeutsche, die Länge aber dieselbe, einfach schreiben:
  `spät`, `spöter`, `fröge`, `höch`, `nöch`, `schön`. Langes i, das hochdeutsch `ie` geschrieben wird, als `ii`
  (`Ziil`, `Spiil` als Nomen), kurzes als `i` (`spile`, `wider`, `vil`). `leer` (nicht «läär»), `Häggli`, `eher`.
- Dehnungs-h auch bei Verben auf -h: `dräht`, `umdräht`, `chräht`, `gchräht` (nicht «dräit», «chräit»); `chehrt`.
- Vorsilben `us-`, `uf-` kurz (`usliefere` nicht, sondern `uslifere`; `Ufstand`, `Ussag`); allein stehende betonte
  Partikel `uus`, `uuf`, `voruus` (`er schlüüsst si uus`).
- `säie`, Partizip `gsäit` (gesät; nicht «gsät»), `gseit` (gesagt).
- `öi` in Mundartwörtern (`nöi`, `nöii`, `tröi`, `Fröid`, `fröie`); in gelehrten Wörtern bleibt `eu` (`verleugne`,
  `Betreuig`).
- 1. Person Einzahl auf -e (`ich säge`, `ich mache`; aber `ich gaa`, `ich chume`, `ich han`); `ich wird`. Konjunktiv I
  ausser `seig`/`heb`/`wärd` mit -i erlaubt (`er chömi`, `er wüssi`); Mehrzahl immer -ed, nie -id.
- Dativ vor Personennamen `em` (`em Titus`), nicht «am»; `däm` (nicht «dem») als hinweisendes Wort; `kei` auch vor
  Vokal.
- `cho` nur vor Infinitiv (`cho luege`), sonst `choo`.
- Wortschatz: `Chile` (nicht «Chilche»), `Volk`, `Ängel`, `Frömd`, `Chnü`, `chnüle`, `Stern`, `Fäscht` (Fest) /
  `fescht` (fest), `Zahn`/`Zäh` (Zähne), `zäh` (zehn), `Wortluut`, `ränned`, `Umkehr`.

**Festlegungen Runde 4 (2026-11-21, Angleichung zwischen den Büchern):**
- `vorus-` in Zusammensetzungen kurz wie jede Vorsilbe (`vorussetze`, `Vorussag`, `vorusgseit`); allein `voruus`.
- Hochdeutsches `ie` in Lehn- und Fachwörtern bleibt (`Sieg`, `Siegel`, `Gier`, `Trieb`, `Papier`, `-iere`); gelehrte
  `eu`-Wörter bleiben (`ungeheuer`, `beteuere`). Nach `bi` kein Gleit-n (`bi ich`).
- Einheitlich: `Züügnis`, `züüge` (eu → üü, Regel 1.2), `elei`, `dört`, `fürchte`, `gfürchtet`, `verrisse`,
  `umchehre`, `umgchehrt`, `chrähe`, `ernidrige`, `aagchündet`, `Stern`.
- Werktitel und wörtliche fremdsprachige Zitate bleiben in ihrer Sprache und Schreibung.
- `am` bleibt, wo es `a` + `em` ist (`Brief am Titus`, `am Jona handle`); reiner Dativ vor Namen `em`. Nomen auf -kehr mit
  k wie `Umkehr` (`Heimkehr`, `Rückkehr`); Adjektiv zu Chile `chirchlich`. Nachgestellte betonte Partikel lang (`vo dört
  uus`). Kein Gleit-n nach Verben ausser `cha` vor er/es/em/en.

**Name (Andi, 2026-11-21):** `Züritüütsch`, `tüütsch`, `Hochtüütsch` mit t (Gallmann; so heissen auch die Zürcher
Bibelausgaben von Weber und Boesch und Schobingers Grammatik). Fester Name, geht der Regel 1.9 vor.

**Verneinung:** `nöd` (betont `nööd`), doppelte Verneinung ist Mundart und erlaubt (`er hät nie nüüt gseit`).

### Gott, Jesus und der Heilige Geist (Entscheid Andi Neck 2026-11-24)

- **Gott und Jesus ohne Artikel**, wie man in der Schweiz von ihnen spricht: «Jesus hät gseit», «Gott hät d Wält gmacht», «vo Jesus», «zu Gott», «bi Jesus» (nicht «de Jesus», «em Jesus», «vom Jesus»). Die übrigen Personennamen behalten den Artikel (de Petrus, d Maria).
- **De Heilig Geischt** mit Artikel.

### Satzbau: zusammenhängend erzählen (Entscheid Andi Neck 2026-11-24)

Eine zu genaue Übernahme der Satzstellung ist in Mundart schwer verständlich. Sätze werden so umgeformt, dass sie zusammenhängend und mit wenigen Kommas fliessen, wie man es erzählen würde; die Bedeutung bleibt (Treue zum Urtext in `decisions`).
Beispiel: «Ir aber, wär, säged ir, seig ich?» → «Was säged ir, wer ich bin?»
Prüfung: Sätze mit vorangestelltem, durch Kommas abgetrenntem Satzglied oder mehr als drei Kommas werden gemeldet (`scripts/mundart.py`, Regel «Satzbau») und von einer weiteren Instanz umformuliert.

## 3 Wortwahl

- Mundartwörter vor hochdeutschen Wörtern mit Mundart-Endung: `luege` (schauen), `lose` (zuhören), `ghöre` (hören),
  `poschte`, `öppe`, `glii` (bald), `geschter`, `moorn`, `hüt`, `jetzt`, `nachane`, `zerscht`, `äntli`, `gäge`,
  `wäge`, `dur` (durch), `ohni`, `zwüsche`, `ane`, `abe`, `ufe`, `use`, `ine`, `ume`, `füre`.
- Keine **falschen Vermundartlichungen** (Gallmann 5.6): hochdeutsches langes `ü`/`u` wird nicht zu `üe`/`ue`, wo
  die Mundart keinen Zwielaut hat: `Gfühl` (nicht «Gfüel»), `Stufe` (nicht «Stuefe»). Umgekehrt nicht `ii`/`uu`, wo
  die Mundart einen Zwielaut hat (`Liecht`, `guet`).
- Biblische Begriffe einheitlich: `Riich vo Gott` / `Himmelriich`, `Mänschesohn`, `Heilig Geischt`, `Herr`, `Sünd`,
  `Gnad`, `Erbarme`, `Gsetz`, `Prophet`, `Tempel`, `Synagoge`, `Jünger`, `Apostel`, `Hoheprieschter`, `Schriftglehrti`,
  `Pharisäer`, `Zöllner`, `Sabbat`, `Passa`, `selig` → `selig`, `Amen`.
- **Namen** in der hochdeutschen Form (`Jesus`, `Christus`, `Johannes`, `Mose`), mit Mundart-Artikel (`de Jesus`, `d
  Maria`, `em Petrus`).
- Zeitgemäss, nicht altertümlich: Gallmanns ältere oder archaische Formen (z. B. `Fäischter`, `Waret`, Dativ Plural
  `de Chinde`) nur, wo sie heute noch üblich sind.

## 4 Übersetzen

- Immer aus dem Urtext (AGENTS.md); die hochdeutsche Fassung ist nur Kontrolle. Mundart-Satzbau statt
  hochdeutschem Satzbau: Perfekt statt Präteritum, `wo` statt Relativpronomen, Nebensätze nicht verschachteln,
  lieber zwei Sätze.
- Gleich bleibt: Bedeutung, Personen, Zeitstufe (Vergangenheit bleibt Vergangenheit), Satzart, Wortzuordnung.
- Erzähltext darf das historische Präsens des Urtexts im Perfekt wiedergeben; direkte Rede wie gesprochen.

## 5 Prüfung

`scripts/mundart.py` prüft maschinell, was sich maschinell prüfen lässt: Sonderzeichen, Wortliste (abgelöste Form →
gültige Form), hochdeutsche Präteritumformen, «um z», Apostroph, Genitiv-Endungen in häufigen Wörtern. Alles Übrige
(Wortwahl, Satzbau, Idiomatik) prüft eine getrennte Instanz gegen dieses Dokument. Wortliste ergänzen, wo eine Prüfung
eine neue Form festlegt (mit Quelle: Gallmann-Seite oder Merkblatt-Regel).

Ersetzt die Mehrheitsentscheide in `scripts/authoring/lukas_einheitlich.py` (Stand 2026-10-26); wo diese einer Regel
hier widersprechen (z. B. «fäält», «Söön»), gilt dieses Dokument.
