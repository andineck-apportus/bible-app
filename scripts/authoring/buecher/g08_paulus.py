"""Hintergrund damals je Buch: Paulusbriefe (ohne Titus, der bereits besteht).

KI-Entwurf (Claude) vom 2026-10-13 auf Wunsch von Andi Neck; keine fachliche Prüfung erfolgt.
"""
from hintergrund_buecher import T

EC = "CTX-HIST-EARLY-CHRISTIANITY"

NOTES = [
 # ---------------------------------------------------------------- Römer
 {"id": "BG-ROM-BOOK-0001", "book": "ROM", "context": EC, "confidence": "probable",
  "topic": "Ein Brief an eine Gemeinde, die Paulus nicht gegründet hatte",
  "text": "Rom war die Hauptstadt des Reiches und mit vielleicht einer Million Einwohnern die grösste Stadt der "
          "Mittelmeerwelt; dort lebte auch eine grosse jüdische Gemeinschaft. Die christliche Gemeinde entstand ohne "
          "Paulus und traf sich in mehreren Hausgemeinden ([[ROM.16.3-ROM.16.5]]; [[ROM.16.14-ROM.16.15]]). Paulus "
          "schrieb wahrscheinlich um 56/57 n. Chr. aus Korinth: Er empfiehlt Phöbe aus dem nahen Hafenort Kenchreä "
          "([[ROM.16.1-ROM.16.2]]) und grüsst von seinem Gastgeber Gaius ([[ROM.16.23]]). Er stand vor der Reise nach "
          "Jerusalem mit der Sammlung ([[ROM.15.25-ROM.15.26]]) und wollte danach über Rom nach Spanien weiterziehen "
          "([[ROM.15.24]]; [[ROM.15.28]]). So stellt sich Paulus der Gemeinde vor und legt seine Botschaft ausführlich "
          "dar. Dass er den Brief geschrieben hat, ist unbestritten.",
  "uncertain": "Das Jahr schwankt in der Forschung zwischen etwa 55 und 58 n. Chr.; die Einwohnerzahl Roms ist eine "
               "Schätzung. Umstritten ist, ob Kapitel 16 mit seinen vielen Grüssen ursprünglich zum Brief gehörte oder an "
               "eine andere Gemeinde (etwa Ephesus) gerichtet war; der Schlusslobpreis ([[ROM.16.25-ROM.16.27]]) steht in "
               "alten Handschriften an verschiedenen Stellen.",
  "evidence_refs": ["ROM.1.7", "ROM.1.13", "ROM.15.24-ROM.15.28", "ROM.16.1-ROM.16.2", "ROM.16.23"],
  "sources": [], "terms": [],
  "gsw": {"topic": "En Brief a e Gmeind, wo de Paulus nöd gründet gha hät",
          "text": "Rom isch d Hauptstadt vom Riich gsii und mit vilicht ere Million Iiwoner di gröscht Stadt vo de "
                  "Mittelmeerwält; det hät au e grossi jüdischi Gmeinschaft gläbt. D christlich Gmeind isch ohni de Paulus "
                  "entstande und hät sich i meerere Husgmeinde troffe ([[ROM.16.3-ROM.16.5]]; [[ROM.16.14-ROM.16.15]]). De "
                  "Paulus hät wahrschiinli um 56/57 n. Chr. vo Korinth us gschribe: Er empfiilt d Phöbe us em nööche "
                  "Hafeort Kenchreä ([[ROM.16.1-ROM.16.2]]) und grüesst vo sim Gaschtgeber Gaius ([[ROM.16.23]]). Er isch "
                  "vor de Reis uf Jerusalem mit de Sammlig gstande ([[ROM.15.25-ROM.15.26]]) und hät dänn über Rom wiiter "
                  "uf Spanie wele ([[ROM.15.24]]; [[ROM.15.28]]). So stellt sich de Paulus de Gmeind vor und leit sini "
                  "Botschaft usfüerlich dar. Dass er de Brief gschribe hät, isch unbestritte.",
          "uncertain": "S Jaar schwankt i de Forschig zwüsche öppe 55 und 58 n. Chr.; d Iiwonerzaal vo Rom isch e "
                       "Schätzig. Umstritte isch, öb s Kapitel 16 mit sine vile Grüess ursprünglich zum Brief ghört hät oder "
                       "a en anderi Gmeind (öppe Ephesus) grichtet gsii isch; de Schlusslobpriis ([[ROM.16.25-ROM.16.27]]) "
                       "staat i alte Handschrifte a verschidene Stelle.",
          "terms": []}},
 {"id": "BG-ROM-BOOK-0002", "book": "ROM", "context": EC, "confidence": "possible",
  "topic": "Juden und Nichtjuden in Rom nach dem Erlass des Claudius",
  "text": "Der römische Schriftsteller Sueton berichtet, Kaiser Claudius habe Juden aus Rom vertrieben, weil sie «auf "
          "Anstiften des Chrestus» ständig Unruhe stifteten. Viele Forscher sehen darin einen Streit in den Synagogen "
          "über Jesus als Christus. Die Apostelgeschichte erwähnt Aquila und Priszilla, die wegen dieses Erlasses nach "
          "Korinth kamen ([[ACT.18.2]]); im Römerbrief grüsst Paulus die beiden wieder in Rom ([[ROM.16.3]]). Nach dem "
          "Tod des Claudius (54 n. Chr.) konnten Juden wohl zurückkehren. Manche lesen den Brief vor diesem Hintergrund: Eine "
          "inzwischen stärker nichtjüdisch geprägte Gemeinde und zurückkehrende jüdische Christen mussten zusammenfinden. "
          "Das könnte die Mahnungen zur gegenseitigen Annahme erklären ([[ROM.11.13-ROM.11.18]]; [[ROM.14.1]]; "
          "[[ROM.15.7]]).",
  "uncertain": "Ob «Chrestus» Christus meint, ist nicht sicher; es war auch ein gewöhnlicher Personenname. Das Jahr des "
               "Erlasses (meist 49 n. Chr., nach dem späteren Geschichtsschreiber Orosius) und sein Umfang (alle Juden oder "
               "nur einzelne Gruppen) sind umstritten. Wie stark diese Lage den Römerbrief prägt, wird unterschiedlich "
               "beurteilt; andere sehen in ihm vor allem eine grundsätzliche Darlegung der Botschaft des Paulus.",
  "evidence_refs": ["ACT.18.2", "ROM.16.3", "ROM.14.1", "ROM.15.7"],
  "sources": ["Sueton, Claudius 25,4", "Orosius, Historien gegen die Heiden 7,6,15"],
  "terms": [T("lat", "Chrestus", "Chrestus (Personenname; oft als «Christus» gedeutet)", "chrestus")],
  "gsw": {"topic": "Jude und Nichtjude z Rom nach em Erlass vom Claudius",
          "text": "De römisch Schriftsteller Sueton bricht, de Kaiser Claudius heg Jude us Rom vertribe, wil si «uf "
                  "Aastifte vom Chrestus» immer wider Unrue gstiftet heged. Vili Forscher gsend drin en Striit i de "
                  "Synagoge über de Jesus als Christus. D Apostelgschicht erwäänt de Aquila und d Priszilla, wo wäge däm "
                  "Erlass uf Korinth cho sind ([[ACT.18.2]]); im Römerbrief grüesst de Paulus di beide wider z Rom "
                  "([[ROM.16.3]]). Nach em Tod vom Claudius (54 n. Chr.) händ Jude wahrschiinli wider chöne zrugg cho. Es paar läsed de Brief "
                  "vor däm Hintergrund: E Gmeind, wo underdesse stärcher nichtjüdisch prägt gsii isch, und jüdischi "
                  "Chrischte, wo zrugg cho sind, händ müese zämefinde. Das chönnt d Maanige erkläre, enand aazneh "
                  "([[ROM.11.13-ROM.11.18]]; [[ROM.14.1]]; [[ROM.15.7]]).",
          "uncertain": "Öb «Chrestus» de Christus meint, isch nöd sicher; es isch au en gwöönliche Personename gsii. S Jaar "
                       "vom Erlass (meischtens 49 n. Chr., nach em spöötere Gschichtsschriiber Orosius) und sin Umfang (alli "
                       "Jude oder nu einzelni Gruppe) sind umstritte. Wie stark die Lag de Römerbrief prägt, wird "
                       "verschide beurteilt; anderi gsend i im vor allem e grundsätzlichi Darlegig vo de Botschaft vom "
                       "Paulus.",
          "terms": ["Chrestus (Personename; oft als «Christus» düütet)"]}},

 # ---------------------------------------------------------------- 1. Korinther
 {"id": "BG-1CO-BOOK-0001", "book": "1CO", "context": EC, "confidence": "probable",
  "topic": "Korinth: Hafenstadt und römische Kolonie",
  "text": "Korinth lag auf der Landenge zwischen zwei Meeren, besass zwei Häfen und war ein reicher Handelsplatz. Die "
          "Römer hatten die griechische Stadt 146 v. Chr. zerstört; Julius Caesar gründete sie 44 v. Chr. als römische "
          "Kolonie neu, vor allem mit Freigelassenen als Siedlern. Korinth war Hauptstadt der Provinz Achaia. Paulus "
          "gründete die Gemeinde um 50–52 n. Chr. während rund anderthalb Jahren ([[ACT.18.1-ACT.18.18]]); die "
          "Gallio-Inschrift aus Delphi hilft, diese Zeit zu datieren ([[ACT.18.12]]). Den 1. Korintherbrief schrieb er "
          "wohl um 54/55 n. Chr. aus Ephesus ([[1CO.16.8]]). Anlass waren Berichte von Leuten der Chloe über Spaltungen "
          "([[1CO.1.11]]) und ein Brief der Gemeinde mit Fragen ([[1CO.7.1]]). Ein früherer Brief des Paulus ist "
          "verloren ([[1CO.5.9]]). Die Verfasserschaft ist unbestritten.",
  "uncertain": "Das Abfassungsjahr wird zwischen etwa 53 und 57 n. Chr. angesetzt. Wie gross und wie sozial gemischt die "
               "Gemeinde war, wird nur aus Andeutungen erschlossen ([[1CO.1.26]]; [[1CO.11.21-1CO.11.22]]). Eine "
               "Bauinschrift in Korinth nennt einen Erastus als städtischen Beamten; ob er der Erastus aus [[ROM.16.23]] "
               "ist, ist umstritten.",
  "evidence_refs": ["ACT.18.1-ACT.18.18", "ACT.18.12", "1CO.1.11", "1CO.5.9", "1CO.7.1", "1CO.16.8"],
  "sources": ["Gallio-Inschrift, Delphi (um 52 n. Chr.)", "Erastus-Inschrift, Korinth"], "terms": [],
  "gsw": {"topic": "Korinth: Hafestadt und römischi Kolonie",
          "text": "Korinth isch uf de Landängi zwüsche zwei Meer gläge, hät zwei Häfe gha und isch en riiche "
                  "Handelsplatz gsii. D Römer händ di griechisch Stadt 146 v. Chr. zerstört; de Julius Caesar hät si 44 v. "
                  "Chr. als römischi Kolonie nöi gründet, vor allem mit Freiglassne als Siidler. Korinth isch d Hauptstadt "
                  "vo de Provinz Achaia gsii. De Paulus hät d Gmeind um 50–52 n. Chr. während öppe andertalb Jaar gründet "
                  "([[ACT.18.1-ACT.18.18]]); d Gallio-Inschrift us Delphi hilft, die Ziit z datiere ([[ACT.18.12]]). De 1. "
                  "Korintherbrief hät er wahrschiinli um 54/55 n. Chr. vo Ephesus us gschribe ([[1CO.16.8]]). Aalass sind "
                  "Bricht vo Lüüt vo de Chloe über Spaltige gsii ([[1CO.1.11]]) und en Brief vo de Gmeind mit Frage "
                  "([[1CO.7.1]]). En früenere Brief vom Paulus isch verlore ([[1CO.5.9]]). Dass er vom Paulus isch, isch "
                  "unbestritte.",
          "uncertain": "S Jaar wird zwüsche öppe 53 und 57 n. Chr. aagsetzt. Wie gross und wie sozial gmischt d Gmeind gsii "
                       "isch, cha me nu us Aadüütige erschliesse ([[1CO.1.26]]; [[1CO.11.21-1CO.11.22]]). E Bauinschrift z "
                       "Korinth nännt en Erastus als städtische Beamte; öb er de Erastus us [[ROM.16.23]] isch, isch "
                       "umstritte.",
          "terms": []}},

 # ---------------------------------------------------------------- 2. Korinther
 {"id": "BG-2CO-BOOK-0001", "book": "2CO", "context": EC, "confidence": "probable",
  "topic": "Ein gespanntes Verhältnis zu Korinth",
  "text": "Nach dem 1. Korintherbrief verschlechterte sich das Verhältnis zwischen Paulus und der Gemeinde. Er machte "
          "einen schmerzlichen Zwischenbesuch ([[2CO.2.1]]) und schrieb danach einen Brief «unter vielen Tränen» "
          "([[2CO.2.4]]). Titus überbrachte ihn wohl und kam mit guten Nachrichten zurück, als Paulus in Makedonien auf ihn "
          "wartete ([[2CO.2.12-2CO.2.13]]; [[2CO.7.5-2CO.7.7]]). Von dort schrieb Paulus wahrscheinlich um 55/56 n. Chr. "
          "den 2. Korintherbrief. Er wirbt darin für die Sammlung für Jerusalem ([[2CO.8.1-2CO.9.15]]) und setzt sich mit "
          "Gegnern auseinander, die er spöttisch «Überapostel» nennt ([[2CO.11.5]]). Zugleich kündigt er einen dritten "
          "Besuch an ([[2CO.12.14]]; [[2CO.13.1]]). Dass der Brief von Paulus stammt, ist unbestritten.",
  "uncertain": "Ob der Tränenbrief verloren ist oder in den Kapiteln 10–13 erhalten blieb, ist umstritten (siehe die "
               "zweite Notiz). Wer die Gegner waren (judenchristliche Missionare, begeisterte Wanderprediger oder andere), "
               "lässt sich nur aus der Polemik des Paulus erschliessen. Das Jahr schwankt zwischen etwa 55 und 57 n. Chr.",
  "evidence_refs": ["2CO.2.1", "2CO.2.4", "2CO.2.12-2CO.2.13", "2CO.7.5-2CO.7.7", "2CO.12.14", "2CO.13.1"],
  "sources": [], "terms": [],
  "gsw": {"topic": "Es gspannts Verhältnis zu Korinth",
          "text": "Nach em 1. Korintherbrief isch s Verhältnis zwüsche em Paulus und de Gmeind schlächter worde. Er hät en "
                  "schmerzliche Zwüschebsuech gmacht ([[2CO.2.1]]) und dänn en Brief «under vile Träne» gschribe "
                  "([[2CO.2.4]]). De Titus hät en wahrschiinli überbracht und isch mit guete Nachrichte zrugg cho, wo de Paulus z "
                  "Makedonie uf en gwartet hät ([[2CO.2.12-2CO.2.13]]; [[2CO.7.5-2CO.7.7]]). Vo det us hät de Paulus "
                  "wahrschiinli um 55/56 n. Chr. de 2. Korintherbrief gschribe. Er wirbt drin für d Sammlig für Jerusalem "
                  "([[2CO.8.1-2CO.9.15]]) und setzt sich mit Gägner usenand, won er spöttisch «Überapostel» nännt "
                  "([[2CO.11.5]]). Glichziitig chündt er en dritte Bsuech aa ([[2CO.12.14]]; [[2CO.13.1]]). Dass de Brief "
                  "vom Paulus stammt, isch unbestritte.",
          "uncertain": "Öb de Tränebrief verlore isch oder i de Kapitel 10–13 erhalte blibe isch, isch umstritte (lueg di "
                       "zweit Notiz). Wär d Gägner gsii sind (judechristlichi Missionar, begeischtereti Wanderprediger oder "
                       "anderi), cha me nu us de Polemik vom Paulus erschliesse. S Jaar schwankt zwüsche öppe 55 und 57 n. "
                       "Chr.",
          "terms": []}},
 {"id": "BG-2CO-BOOK-0002", "book": "2CO", "context": EC, "confidence": "possible",
  "topic": "Ein Brief oder mehrere?",
  "text": "Viele Ausleger halten den 2. Korintherbrief für eine Sammlung mehrerer Briefe oder Briefteile, die später "
          "zusammengefügt wurden. Gründe sind deutliche Brüche: Nach der Versöhnung in [[2CO.7.5-2CO.7.16]] schlägt der "
          "Ton in [[2CO.10.1-2CO.13.14]] plötzlich in scharfe Verteidigung um; die Kapitel 8 und 9 behandeln die "
          "Sammlung zweimal, als stünden sie je für sich; und [[2CO.6.14-2CO.7.1]] unterbricht den Gedankengang. Andere "
          "halten den Brief für eine Einheit: Paulus könnte über längere Zeit diktiert oder auf neue Nachrichten "
          "reagiert haben, und auch andere antike Briefe kennen solche Stimmungswechsel. Diese App entscheidet die "
          "Frage nicht.",
  "uncertain": "Die Teilungshypothesen unterscheiden sich stark (zwei bis fünf Teilbriefe); keine alte Handschrift "
               "bezeugt eine andere Form als die heutige. Ob die Kapitel 10–13 der Tränenbrief sind oder nach den Kapiteln "
               "1–9 geschrieben wurden, ist offen.",
  "evidence_refs": ["2CO.6.14-2CO.7.1", "2CO.7.5-2CO.7.16", "2CO.8.1-2CO.9.15", "2CO.10.1-2CO.13.14"],
  "sources": [], "terms": [],
  "gsw": {"topic": "En Brief oder meereri?",
          "text": "Vili Usleger halted de 2. Korintherbrief für e Sammlig vo meerere Brief oder Briefteil, wo spööter "
                  "zämegfüegt worde sind. Gründ sind tüütlichi Brüch: Nach de Versöönig i [[2CO.7.5-2CO.7.16]] schlaat de "
                  "Ton i [[2CO.10.1-2CO.13.14]] plötzlich i e scharfi Verteidigig um; d Kapitel 8 und 9 behandled d "
                  "Sammlig zwei Mal, wie wänn si jedes für sich stüended; und [[2CO.6.14-2CO.7.1]] underbricht de "
                  "Gedankegang. Anderi halted de Brief für e Einheit: De Paulus chönnt über e längeri Ziit diktiert oder "
                  "uf nöii Nachrichte reagiert ha, und au anderi antiki Brief kenned sonig Stimmigswächsel. Die App "
                  "entscheidet d Frag nöd.",
          "uncertain": "D Teiligshypothese underscheided sich stark (zwei bis füüf Teilbrief); kei alti Handschrift "
                       "bezüügt en anderi Form als di hütig. Öb d Kapitel 10–13 de Tränebrief sind oder nach de Kapitel 1–9 "
                       "gschribe worde sind, isch offe.",
          "terms": []}},

 # ---------------------------------------------------------------- Galater
 {"id": "BG-GAL-BOOK-0001", "book": "GAL", "context": EC, "confidence": "probable",
  "topic": "Ein Kampfbrief an die Gemeinden in Galatien",
  "text": "Die Galater waren keltische Stämme, die sich im 3. Jahrhundert v. Chr. in Zentralanatolien um das heutige "
          "Ankara niedergelassen hatten. Ab 25 v. Chr. war Galatien eine römische Provinz, zu der auch südlichere Städte "
          "wie Ikonion, Lystra und Derbe gehörten. Paulus schreibt an mehrere Gemeinden ([[GAL.1.2]]), die er selbst "
          "gegründet hatte, nach eigenen Worten während einer Krankheit ([[GAL.4.13-GAL.4.14]]). Nun warben andere "
          "Lehrer dafür, dass sich die nichtjüdischen Christen beschneiden lassen und das jüdische Gesetz übernehmen "
          "([[GAL.5.2-GAL.5.3]]; [[GAL.6.12-GAL.6.13]]). Paulus reagiert ungewöhnlich scharf, ohne den sonst üblichen "
          "Dank am Briefanfang ([[GAL.1.6-GAL.1.9]]), und schliesst mit eigener Hand ([[GAL.6.11]]). Dass er den Brief "
          "geschrieben hat, ist unbestritten.",
  "uncertain": "Ort und Zeit der Abfassung sind unsicher: Vorgeschlagen werden unter anderem Antiochia, Ephesus, "
               "Makedonien und Korinth, Datierungen zwischen etwa 48 und 55 n. Chr. Sie hängen davon ab, welche Galater "
               "gemeint sind (siehe die zweite Notiz). Wer die Gegner genau waren, lässt sich nur aus dem Brief selbst "
               "erschliessen.",
  "evidence_refs": ["GAL.1.2", "GAL.1.6-GAL.1.9", "GAL.4.13-GAL.4.14", "GAL.5.2-GAL.5.3", "GAL.6.11-GAL.6.13"],
  "sources": [], "terms": [],
  "gsw": {"topic": "En Kampfbrief a d Gmeinde z Galatie",
          "text": "D Galater sind keltischi Stämm gsii, wo sich im 3. Jaarhundert v. Chr. z Zentralanatolie um s hütig "
                  "Ankara niderglaa händ. Ab 25 v. Chr. isch Galatie e römischi Provinz gsii, zu dere au südlicheri Stedt "
                  "wie Ikonion, Lystra und Derbe ghört händ. De Paulus schriibt a meereri Gmeinde ([[GAL.1.2]]), won er "
                  "sälber gründet gha hät, nach sine eigene Wort während ere Chranket ([[GAL.4.13-GAL.4.14]]). Jetzt händ "
                  "anderi Leerer defür gworbe, dass sich di nichtjüdische Chrischte beschniide lönd und s jüdisch Gsetz "
                  "übernämed ([[GAL.5.2-GAL.5.3]]; [[GAL.6.12-GAL.6.13]]). De Paulus reagiert ungwöönlich scharf, ohni de "
                  "suscht üblich Dank am Briefaafang ([[GAL.1.6-GAL.1.9]]), und schlüsst mit eigener Hand ([[GAL.6.11]]). "
                  "Dass er de Brief gschribe hät, isch unbestritte.",
          "uncertain": "Ort und Ziit, wo de Brief entstande isch, sind unsicher: Vorgschlage wärded under anderem "
                       "Antiochia, Ephesus, Makedonie und Korinth, Datierige zwüsche öppe 48 und 55 n. Chr. Si hanged devo "
                       "ab, weli Galater gmeint sind (lueg di zweit Notiz). Wär d Gägner gnau gsii sind, cha me nu us em "
                       "Brief sälber erschliesse.",
          "terms": []}},
 {"id": "BG-GAL-BOOK-0002", "book": "GAL", "context": EC, "confidence": "possible",
  "topic": "Nordgalatien oder Südgalatien?",
  "text": "Mit «Galatien» kann die Landschaft der keltischen Galater im Norden gemeint sein oder die ganze römische "
          "Provinz. Nach der Nordgalatien-These schrieb Paulus an Gemeinden im Gebiet um Ankara, die er erst auf der "
          "zweiten Reise gründete ([[ACT.16.6]]; [[ACT.18.23]]); der Brief entstünde dann um 53–55 n. Chr., in der Nähe "
          "des Römerbriefs, mit dem er viele Themen teilt. Nach der Südgalatien-These sind die Gemeinden in Antiochia in "
          "Pisidien, Ikonion, Lystra und Derbe gemeint, deren Gründung die Apostelgeschichte ausführlich erzählt "
          "([[ACT.13.14-ACT.14.23]]); dann kann der Brief früh sein, nach manchen sogar vor dem Apostelkonzil "
          "([[ACT.15.1-ACT.15.29]]) um 48/49 n. Chr. Die Frage hängt eng damit zusammen, welchen Besuch in Jerusalem "
          "[[GAL.2.1-GAL.2.10]] beschreibt.",
  "uncertain": "Beide Thesen haben gewichtige Vertreter; im deutschsprachigen Raum war die Nordgalatien-These lange "
               "vorherrschend, im englischsprachigen ist die Südgalatien-These verbreitet. Ob [[GAL.2.1-GAL.2.10]] dem "
               "Apostelkonzil oder dem Besuch aus [[ACT.11.27-ACT.11.30]] entspricht, ist umstritten. Diese App entscheidet "
               "die Frage nicht.",
  "evidence_refs": ["ACT.13.14-ACT.14.23", "ACT.16.6", "ACT.18.23", "GAL.2.1-GAL.2.10", "ACT.15.1-ACT.15.29"],
  "sources": [], "terms": [],
  "gsw": {"topic": "Nordgalatie oder Südgalatie?",
          "text": "Mit «Galatie» cha d Landschaft vo de keltische Galater im Norde gmeint sii oder di ganz römisch Provinz. "
                  "Nach de Nordgalatie-These hät de Paulus a Gmeinde im Gebiet um Ankara gschribe, won er erscht uf de "
                  "zweite Reis gründet hät ([[ACT.16.6]]; [[ACT.18.23]]); de Brief wär dänn um 53–55 n. Chr. entstande, i "
                  "de Nööchi vom Römerbrief, mit dem er vili Theme teilt. Nach de Südgalatie-These sind d Gmeinde z "
                  "Antiochia z Pisidie, Ikonion, Lystra und Derbe gmeint, vo dene d Apostelgschicht usfüerlich verzellt, "
                  "wie si gründet worde sind ([[ACT.13.14-ACT.14.23]]); dänn cha de Brief früe sii, nach es paar sogar vor "
                  "em Apostelkonzil ([[ACT.15.1-ACT.15.29]]) um 48/49 n. Chr. D Frag hangt äng demit zäme, weli Bsuech z "
                  "Jerusalem [[GAL.2.1-GAL.2.10]] beschriibt.",
          "uncertain": "Beidi These händ gwichtigi Vertreter; im düütschsprachige Ruum isch d Nordgalatie-These lang "
                       "vorherrschend gsii, im änglischsprachige isch d Südgalatie-These verbreitet. Öb [[GAL.2.1-GAL.2.10]] "
                       "em Apostelkonzil oder em Bsuech us [[ACT.11.27-ACT.11.30]] entspricht, isch umstritte. Die App "
                       "entscheidet d Frag nöd.",
          "terms": []}},

 # ---------------------------------------------------------------- Epheser
 {"id": "BG-EPH-BOOK-0001", "book": "EPH", "context": EC, "confidence": "probable",
  "topic": "Ephesus: Metropole der Provinz Asia",
  "text": "Ephesus war eine der grössten Städte im Osten des Reiches, eine Hafen- und Handelsstadt und der wichtigste Ort "
          "der Provinz Asia, wo der römische Statthalter häufig residierte. Berühmt war der Tempel der Artemis, eines der "
          "sieben Weltwunder; um ihren Kult blühte ein Gewerbe, das sich durch die Predigt des Paulus bedroht sah "
          "([[ACT.19.23-ACT.19.41]]). Auch eine jüdische Gemeinde lebte in der Stadt ([[ACT.19.8]]). Paulus wirkte nach "
          "der Apostelgeschichte zwei bis drei Jahre dort ([[ACT.19.10]]; [[ACT.20.31]]), wohl um 52–55 n. Chr.; von "
          "hier aus entstanden Gemeinden in der ganzen Region. Später gilt Ephesus als Wirkungsort des Timotheus "
          "([[1TI.1.3]]) und erscheint unter den sieben Gemeinden der Offenbarung ([[REV.2.1-REV.2.7]]).",
  "uncertain": "Ob Ephesus formell Hauptstadt der Provinz war oder diese Rolle mit Pergamon teilte, ist nicht ganz klar; "
               "Einwohnerzahlen sind blosse Schätzungen. Die Dauer des Aufenthalts des Paulus kennen wir nur aus der "
               "Apostelgeschichte. Eine Haft des Paulus in Ephesus wird vermutet, ist aber nicht belegt.",
  "evidence_refs": ["ACT.19.1-ACT.19.41", "ACT.20.17-ACT.20.38", "1TI.1.3", "REV.2.1-REV.2.7"],
  "sources": [], "terms": [],
  "gsw": {"topic": "Ephesus: Metropole vo de Provinz Asia",
          "text": "Ephesus isch eini vo de gröschte Stedt im Oschte vom Riich gsii, e Hafe- und Handelsstadt und de wichtigscht "
                  "Ort vo de Provinz Asia, wo de römisch Statthalter oft residiert hät. Berüemt isch de Tempel vo de "
                  "Artemis gsii, eis vo de sibe Wältwunder; um iren Kult umme hät es Gwärb blüet, wo sich dur d Predig vom "
                  "Paulus bedroht gfüült hät ([[ACT.19.23-ACT.19.41]]). Au e jüdischi Gmeind hät i de Stadt gläbt "
                  "([[ACT.19.8]]). De Paulus hät nach de Apostelgschicht zwei bis drüü Jaar det gwürkt ([[ACT.19.10]]; "
                  "[[ACT.20.31]]), wahrschiinli um 52–55 n. Chr.; vo da us sind i de ganze Region Gmeinde entstande. "
                  "Spööter gilt Ephesus als de Ort, wo de Timotheus gwürkt hät ([[1TI.1.3]]), und erschiint under de sibe "
                  "Gmeinde vo de Offebarig ([[REV.2.1-REV.2.7]]).",
          "uncertain": "Öb Ephesus förmlich d Hauptstadt vo de Provinz gsii isch oder die Rolle mit Pergamon teilt hät, isch "
                       "nöd ganz klar; Iiwonerzaale sind bloossi Schätzige. Wie lang de Paulus det gsii isch, wüssed mer nu "
                       "us de Apostelgschicht. E Haft vom Paulus z Ephesus wird vermuetet, isch aber nöd bleit.",
          "terms": []}},
 {"id": "BG-EPH-BOOK-0002", "book": "EPH", "context": EC, "confidence": "possible",
  "topic": "An wen und von wem?",
  "text": "Die Worte «in Ephesus» ([[EPH.1.1]]) fehlen in einigen der ältesten Handschriften. Zudem klingt der Brief "
          "auffallend unpersönlich für eine Gemeinde, in der Paulus lange gewirkt hatte ([[EPH.1.15]]; [[EPH.3.2]]); "
          "viele denken daher an ein Rundschreiben an mehrere Gemeinden Kleinasiens. Als Verfasser nennt sich Paulus im "
          "Gefängnis ([[EPH.3.1]]; [[EPH.6.20]]). Wer ihm den Brief zuschreibt, datiert ihn meist in die römische Haft um "
          "60–62 n. Chr. Viele Forscher halten ihn dagegen für die Schrift eines Paulusschülers um 80–90 n. Chr.: wegen "
          "des Stils mit sehr langen Sätzen, einer weiterentwickelten Sicht der Kirche als weltweiter Grösse und der "
          "engen Anlehnung an den Kolosserbrief; die Notiz über den Boten Tychikus ([[EPH.6.21-EPH.6.22]]) gleicht fast "
          "wörtlich [[COL.4.7-COL.4.8]].",
  "uncertain": "Offen ist, ob die Ortsangabe ursprünglich ist und ob der Brief ein Rundschreiben oder vielleicht der in "
               "[[COL.4.16]] erwähnte Brief nach Laodizea ist. Die Verfasserfrage hängt davon ab, wie man Stil, Theologie "
               "und die Nähe zum Kolosserbrief gewichtet; manche rechnen auch mit einem Mitarbeiter, der im Auftrag des "
               "Paulus schrieb.",
  "evidence_refs": ["EPH.1.1", "EPH.1.15", "EPH.3.1-EPH.3.2", "EPH.6.20-EPH.6.22", "COL.4.7-COL.4.8", "COL.4.16"],
  "sources": [], "terms": [],
  "gsw": {"topic": "A wän und vo wäm?",
          "text": "D Wort «z Ephesus» ([[EPH.1.1]]) fääled i es paar vo de ältischte Handschrifte. Zuedem tönt de Brief "
                  "uffällig unpersönlich für e Gmeind, wo de Paulus lang gwürkt gha hät ([[EPH.1.15]]; [[EPH.3.2]]); vili "
                  "dänked drum a es Rundschriibe a meereri Gmeinde z Chliiasie. Als Verfasser nännt sich de Paulus im "
                  "Gfängnis ([[EPH.3.1]]; [[EPH.6.20]]). Wär im de Brief zueschriibt, datiert en meischtens i di römisch "
                  "Haft um 60–62 n. Chr. Vili Forscher halted en defür für d Schrift vo me Paulusschüeler um 80–90 n. Chr.: "
                  "wäge em Stil mit sehr lange Sätz, ere wiiterentwicklete Sicht vo de Chile als wältwiiti Gröössi und de "
                  "ängen Aalehnig a de Kolosserbrief; d Notiz über de Bott Tychikus ([[EPH.6.21-EPH.6.22]]) gliicht fascht "
                  "wörtlich [[COL.4.7-COL.4.8]].",
          "uncertain": "Offe isch, öb d Ortsaagaab ursprünglich isch und öb de Brief es Rundschriibe oder vilicht de i "
                       "[[COL.4.16]] erwäänt Brief uf Laodizea isch. D Verfasserfrag hangt devo ab, wie me Stil, Theologie "
                       "und d Nööchi zum Kolosserbrief gwichtet; es paar rächned au mit eme Mitarbeiter, wo im Uftrag vom "
                       "Paulus gschribe hät.",
          "terms": []}},

 # ---------------------------------------------------------------- Philipper
 {"id": "BG-PHP-BOOK-0001", "book": "PHP", "context": EC, "confidence": "probable",
  "topic": "Philippi: eine römische Kolonie in Makedonien",
  "text": "Philippi wurde von König Philipp II. von Makedonien gegründet und nach ihm benannt. Nach der Schlacht bei "
          "Philippi (42 v. Chr.) und erneut nach 31 v. Chr. siedelten die Römer dort Veteranen an; die Stadt wurde "
          "römische Kolonie mit römischem Recht und Latein als Amtssprache ([[ACT.16.12]]). Sie lag an der Via Egnatia, "
          "der grossen Strasse von der Adria nach Osten. Die Apostelgeschichte erzählt die Gründung der Gemeinde mit "
          "Lydia und anderen um 49/50 n. Chr. als ersten Schritt des Paulus nach Europa ([[ACT.16.9-ACT.16.40]]). Die "
          "Gemeinde unterstützte ihn wiederholt mit Geld ([[PHP.4.15-PHP.4.16]]). Anlass des Briefes war eine neue Gabe, "
          "die Epaphroditus zu Paulus ins Gefängnis brachte ([[PHP.2.25]]; [[PHP.4.18]]). Die Verfasserschaft des Paulus "
          "ist unbestritten.",
  "uncertain": "Wann und wo der Brief entstand, hängt vom Ort der Haft ab (siehe die zweite Notiz). Manche halten den "
               "Brief wegen des abrupten Übergangs in [[PHP.3.1-PHP.3.2]] für eine Zusammenstellung aus zwei oder drei "
               "Briefen, andere für eine Einheit. Das Gründungsjahr ist aus der Chronologie der Apostelgeschichte "
               "erschlossen.",
  "evidence_refs": ["ACT.16.11-ACT.16.40", "PHP.2.25", "PHP.4.15-PHP.4.18"],
  "sources": [], "terms": [],
  "gsw": {"topic": "Philippi: e römischi Kolonie z Makedonie",
          "text": "Philippi isch vom König Philipp II. vo Makedonie gründet und nach im benännt worde. Nach de Schlacht bi "
                  "Philippi (42 v. Chr.) und nomal nach 31 v. Chr. händ d Römer det Veterane aagsidlet; d Stadt isch e "
                  "römischi Kolonie worde, mit römischem Rächt und Latiin als Amtssprach ([[ACT.16.12]]). Si isch a de Via "
                  "Egnatia gläge, de groosse Strass vo de Adria Richtig Oschte. D Apostelgschicht verzellt d Gründig vo de "
                  "Gmeind mit de Lydia und andere um 49/50 n. Chr. als erschte Schritt vom Paulus uf Europa "
                  "([[ACT.16.9-ACT.16.40]]). D Gmeind hät en mee als eimal mit Gäld understützt ([[PHP.4.15-PHP.4.16]]). "
                  "Aalass vom Brief isch e nöii Gaab gsii, wo de Epaphroditus em Paulus is Gfängnis bracht hät "
                  "([[PHP.2.25]]; [[PHP.4.18]]). Dass de Brief vom Paulus isch, isch unbestritte.",
          "uncertain": "Wänn und wo de Brief entstande isch, hangt vom Ort vo de Haft ab (lueg di zweit Notiz). Es paar "
                       "halted de Brief wäge em abrupte Überggang i [[PHP.3.1-PHP.3.2]] für e Zämestellig us zwei oder drüü "
                       "Brief, anderi für e Einheit. S Gründigsjaar isch us de Chronologie vo de Apostelgschicht "
                       "erschlosse.",
          "terms": []}},
 {"id": "BG-PHP-BOOK-0002", "book": "PHP", "context": EC, "confidence": "possible",
  "topic": "Aus welchem Gefängnis?",
  "text": "Paulus schreibt als Gefangener ([[PHP.1.7]]; [[PHP.1.13]]) und grüsst von Leuten «aus dem Haus des Kaisers» "
          "([[PHP.4.22]]). Traditionell denkt man an die Haft in Rom um 60–62 n. Chr. ([[ACT.28.16]]; [[ACT.28.30]]): "
          "Dafür sprechen das Prätorium, das hier die kaiserliche Garde meinen kann, und der kaiserliche Haushalt. Viele "
          "Forscher vermuten dagegen eine sonst nicht bezeugte Haft in Ephesus um 54/55 n. Chr. ([[2CO.1.8-2CO.1.9]]; "
          "[[2CO.11.23]]): Die vielen Botengänge zwischen Paulus und Philippi ([[PHP.2.19-PHP.2.30]]) wären von dort aus "
          "leichter möglich, und Amtssitze des Statthalters wie kaiserliche Sklaven und Freigelassene gab es auch in den "
          "Provinzen. Eine dritte Möglichkeit ist die Haft in Cäsarea um 57–59 n. Chr. ([[ACT.23.33-ACT.24.27]]).",
  "uncertain": "Keine der drei Annahmen ist gesichert. Eine Haft in Ephesus wird nur erschlossen; die Apostelgeschichte "
               "erwähnt sie nicht. Die Wahl beeinflusst die Datierung und die Einordnung des Briefes unter die übrigen "
               "Paulusbriefe; dieselbe Frage stellt sich beim Philemonbrief und, falls von Paulus, beim Kolosserbrief.",
  "evidence_refs": ["PHP.1.7", "PHP.1.13", "PHP.4.22", "ACT.28.16", "ACT.28.30", "2CO.1.8-2CO.1.9", "ACT.23.33-ACT.23.35"],
  "sources": [],
  "terms": [T("grc", "πραιτώριον", "Prätorium: Amtssitz eines Statthalters oder die kaiserliche Garde")],
  "gsw": {"topic": "Us welem Gfängnis?",
          "text": "De Paulus schriibt als Gfangne ([[PHP.1.7]]; [[PHP.1.13]]) und grüesst vo Lüüt «us em Huus vom Kaiser» "
                  "([[PHP.4.22]]). Traditionell dänkt me a d Haft z Rom um 60–62 n. Chr. ([[ACT.28.16]]; [[ACT.28.30]]): "
                  "Defür reded s Prätorium, wo da di kaiserlich Garde cha meine, und de kaiserlich Huushalt. Vili Forscher "
                  "vermueted defür e Haft z Ephesus um 54/55 n. Chr., wo suscht nöd bezüügt isch ([[2CO.1.8-2CO.1.9]]; "
                  "[[2CO.11.23]]): Di vile Botegäng zwüsche em Paulus und Philippi ([[PHP.2.19-PHP.2.30]]) wäred vo det us "
                  "liechter möglich gsii, und Amtssitz vom Statthalter wie au kaiserlichi Sklave und Freiglassni hät s au i "
                  "de Provinze gää. E dritti Möglichkeit isch d Haft z Cäsarea um 57–59 n. Chr. ([[ACT.23.33-ACT.24.27]]).",
          "uncertain": "Kei vo de drüü Aanaame isch gsicheret. E Haft z Ephesus wird nu erschlosse; d Apostelgschicht "
                       "erwäänt si nöd. D Waal beiiflusst d Datierig und d Iiornig vom Brief under di andere Paulusbrief; di "
                       "gliich Frag stellt sich bim Philemonbrief und, falls vom Paulus, bim Kolosserbrief.",
          "terms": ["Prätorium: Amtssitz vo me Statthalter oder di kaiserlich Garde"]}},

 # ---------------------------------------------------------------- Kolosser
 {"id": "BG-COL-BOOK-0001", "book": "COL", "context": EC, "confidence": "possible",
  "topic": "Kolossä und die Gemeinden im Lykostal",
  "text": "Kolossä war eine alte Stadt in Phrygien im Westen Kleinasiens, zur Zeit des Paulus kleiner als die nahen "
          "Nachbarstädte Laodizea und Hierapolis, mit denen die Gemeinde verbunden war ([[COL.4.13]]; [[COL.4.16]]). "
          "Gegründet hatte sie nicht Paulus, sondern Epaphras ([[COL.1.7]]; [[COL.2.1]]). Anlass ist eine Lehre, die der "
          "Brief «Philosophie» nennt, mit Vorschriften über Speisen und Feste und mit Engelverehrung ([[COL.2.8]]; "
          "[[COL.2.16-COL.2.18]]). Als Absender nennt der Brief Paulus, der in Haft ist, und Timotheus ([[COL.1.1]]; "
          "[[COL.4.18]]). Wer ihn Paulus zuschreibt, denkt an die Haft in Ephesus (um 54/55) oder in Rom (um 60–62 n. "
          "Chr.); dafür spricht die enge Verbindung zum Philemonbrief mit denselben Namen ([[COL.4.9-COL.4.14]]; "
          "[[PHM.1.23-PHM.1.24]]). Viele Forscher halten den Brief wegen Stil und weiterentwickelter Theologie für das "
          "Werk eines Schülers um 70–80 n. Chr.",
  "uncertain": "Die Verfasserschaft ist offen; vorgeschlagen wird auch, Timotheus habe den Brief noch zu Lebzeiten des "
               "Paulus formuliert. Tacitus berichtet für das Jahr 60 n. Chr. ein Erdbeben, das Laodizea zerstörte; ob es "
               "auch Kolossä traf und ob der Brief davor oder danach entstand, ist unklar. Was die «Philosophie» genau "
               "lehrte (jüdisch, heidnisch-mystisch oder gemischt), ist umstritten.",
  "evidence_refs": ["COL.1.1", "COL.1.7", "COL.2.1", "COL.2.8", "COL.2.16-COL.2.18", "COL.4.9-COL.4.18"],
  "sources": ["Tacitus, Annalen 14,27"],
  "terms": [T("grc", "φιλοσοφία", "Philosophie, Weisheitslehre")],
  "gsw": {"topic": "Kolossä und d Gmeinde im Lykostal",
          "text": "Kolossä isch en alti Stadt z Phrygie im Weschte vo Chliiasie gsii, zur Ziit vom Paulus chliiner als d "
                  "nööche Nachberstedt Laodizea und Hierapolis, mit dene d Gmeind verbunde gsii isch ([[COL.4.13]]; "
                  "[[COL.4.16]]). Gründet hät si nöd de Paulus, sondern de Epaphras ([[COL.1.7]]; [[COL.2.1]]). Aalass isch "
                  "e Leer, wo de Brief «Philosophie» nännt, mit Vorschrifte über Ässe und Fescht und mit Ängelverehrig "
                  "([[COL.2.8]]; [[COL.2.16-COL.2.18]]). Als Absänder nännt de Brief de Paulus, wo i de Haft isch, und de "
                  "Timotheus ([[COL.1.1]]; [[COL.4.18]]). Wär en em Paulus zueschriibt, dänkt a d Haft z Ephesus (um 54/55) "
                  "oder z Rom (um 60–62 n. Chr.); defür redt di äng Verbindig zum Philemonbrief mit de gliiche Näme "
                  "([[COL.4.9-COL.4.14]]; [[PHM.1.23-PHM.1.24]]). Vili Forscher halted de Brief wäge em Stil und ere "
                  "wiiterentwicklete Theologie für s Wärch vo me Schüeler um 70–80 n. Chr.",
          "uncertain": "D Verfasserschaft isch offe; vorgschlage wird au, de Timotheus heg de Brief no zu Läbziite vom "
                       "Paulus formuliert. De Tacitus bricht für s Jaar 60 n. Chr. es Ärdbebe, wo Laodizea zerstört hät; öb "
                       "s au Kolossä troffe hät und öb de Brief vorher oder nachher entstande isch, isch unklar. Was d "
                       "«Philosophie» gnau gleert hät (jüdisch, heidnisch-mystisch oder gmischt), isch umstritte.",
          "terms": ["Philosophie, Wiisheitsleer"]}},

 # ---------------------------------------------------------------- 1. Thessalonicher
 {"id": "BG-1TH-BOOK-0001", "book": "1TH", "context": EC, "confidence": "probable",
  "topic": "Thessalonich: der wohl älteste erhaltene Paulusbrief",
  "text": "Thessalonich wurde um 316 v. Chr. von König Kassander gegründet und nach seiner Frau benannt. Die Hafenstadt "
          "an der Via Egnatia war Hauptstadt der römischen Provinz Makedonien und seit 42 v. Chr. eine freie Stadt mit "
          "eigener Verwaltung. Ihre obersten Beamten hiessen Politarchen ([[ACT.17.6]]); der Titel ist durch Inschriften "
          "aus der Stadt bezeugt. Paulus gründete die Gemeinde um 49/50 n. Chr., musste aber bald fliehen "
          "([[ACT.17.1-ACT.17.10]]). Viele Mitglieder hatten sich von den Götterbildern abgewandt ([[1TH.1.9]]). Besorgt "
          "schickte Paulus Timotheus von Athen aus zurück; nach dessen gutem Bericht schrieb er den Brief, wohl um 50/51 "
          "n. Chr. aus Korinth ([[1TH.3.1-1TH.3.6]]). Der Brief ist unbestritten von Paulus und gilt meist als älteste "
          "erhaltene Schrift des Neuen Testaments.",
  "uncertain": "Die Dauer des Aufenthalts ist umstritten: Die Apostelgeschichte nennt drei Sabbate ([[ACT.17.2]]), die "
               "mehrfache Unterstützung aus Philippi ([[PHP.4.16]]) lässt eher an einige Monate denken. Ob der 1. "
               "Thessalonicherbrief oder der Galaterbrief älter ist, hängt von der Datierung des Galaterbriefs ab.",
  "evidence_refs": ["ACT.17.1-ACT.17.10", "ACT.17.6", "1TH.1.9", "1TH.3.1-1TH.3.6", "ACT.18.5"],
  "sources": [],
  "terms": [T("grc", "πολιτάρχης", "Politarch: oberster Beamter einer Stadt")],
  "gsw": {"topic": "Thessalonich: de wahrschiinli ältischt erhalte Paulusbrief",
          "text": "Thessalonich isch um 316 v. Chr. vom König Kassander gründet und nach sinere Frau benännt worde. D "
                  "Hafestadt a de Via Egnatia isch d Hauptstadt vo de römische Provinz Makedonie gsii und sit 42 v. Chr. e "
                  "freii Stadt mit eigener Verwaltig. Iri oberschte Beamte händ Politarche gheisse ([[ACT.17.6]]); de "
                  "Titel isch dur Inschrifte us de Stadt bezüügt. De Paulus hät d Gmeind um 49/50 n. Chr. gründet, hät aber "
                  "bald müese flüüche ([[ACT.17.1-ACT.17.10]]). Vili Mitglider händ sich vo de Götterbilder abgwändt gha "
                  "([[1TH.1.9]]). Bsorgt hät de Paulus de Timotheus vo Athen us zrugg gschickt; nach sim guete Bricht hät "
                  "er de Brief gschribe, wahrschiinli um 50/51 n. Chr. vo Korinth us ([[1TH.3.1-1TH.3.6]]). De Brief isch "
                  "unbestritte vom Paulus und gilt meischtens als di ältischt erhalte Schrift vom Nöie Teschtamänt.",
          "uncertain": "Wie lang de Paulus det gsii isch, isch umstritte: D Apostelgschicht nännt drüü Sabbat "
                       "([[ACT.17.2]]), d Understützig us Philippi, wo mee als eimal cho isch ([[PHP.4.16]]), laat eender a "
                       "es paar Mönet dänke. Öb de 1. Thessalonicherbrief oder de Galaterbrief elter isch, hangt devo ab, "
                       "wie me de Galaterbrief datiert.",
          "terms": ["Politarch: oberschte Beamte vo ere Stadt"]}},

 # ---------------------------------------------------------------- 2. Thessalonicher
 {"id": "BG-2TH-BOOK-0001", "book": "2TH", "context": EC, "confidence": "possible",
  "topic": "Ein zweiter Brief nach Thessalonich – von wem?",
  "text": "Der 2. Thessalonicherbrief richtet sich an eine bedrängte Gemeinde, in der einige meinten, der «Tag des "
          "Herrn» sei schon da, und manche nicht mehr arbeiteten ([[2TH.2.1-2TH.2.2]]; [[2TH.3.6-2TH.3.12]]). Er nennt "
          "Paulus, Silvanus und Timotheus als Absender ([[2TH.1.1]]) und ähnelt im Aufbau stark dem 1. "
          "Thessalonicherbrief. Wer ihn Paulus zuschreibt, datiert ihn kurz nach dem ersten Brief, um 50/51 n. Chr. aus "
          "Korinth; Paulus hätte dann ein Missverständnis korrigiert. Andere halten ihn für eine spätere Schrift (etwa "
          "80–100 n. Chr.) im Namen des Paulus: Die Erwartung von Vorzeichen vor dem Ende ([[2TH.2.3-2TH.2.12]]) wirke "
          "anders als das plötzliche Kommen in [[1TH.5.1-1TH.5.3]], und die Warnung vor einem Brief, «als ob er von uns "
          "sei», samt eigenhändigem Gruss ([[2TH.2.2]]; [[2TH.3.17]]) falle auf.",
  "uncertain": "Die Verfasserschaft ist in der Forschung stark umstritten. Die Ähnlichkeit zum 1. Thessalonicherbrief "
               "deuten die einen als Zeichen zeitlicher Nähe, die anderen als Nachahmung. Eine Minderheit hält den 2. "
               "Thessalonicherbrief sogar für den früheren der beiden.",
  "evidence_refs": ["2TH.1.1", "2TH.2.1-2TH.2.12", "2TH.3.6-2TH.3.12", "2TH.3.17", "1TH.5.1-1TH.5.3"],
  "sources": [], "terms": [],
  "gsw": {"topic": "En zweite Brief uf Thessalonich – vo wäm?",
          "text": "De 2. Thessalonicherbrief richtet sich a e bedrängti Gmeind, wo es paar gmeint händ, de «Tag vom Herr» "
                  "sei scho da, und es paar nüme gschaffet händ ([[2TH.2.1-2TH.2.2]]; [[2TH.3.6-2TH.3.12]]). Er nännt de "
                  "Paulus, de Silvanus und de Timotheus als Absänder ([[2TH.1.1]]) und gliicht im Ufbau stark em 1. "
                  "Thessalonicherbrief. Wär en em Paulus zueschriibt, datiert en churz nach em erschte Brief, um 50/51 n. "
                  "Chr. vo Korinth us; de Paulus hett dänn es Missverständnis korrigiert. Anderi halted en für e spööteri "
                  "Schrift (öppe 80–100 n. Chr.) im Name vom Paulus: D Erwartig vo Vorzeiche vor em Änd "
                  "([[2TH.2.3-2TH.2.12]]) würki anders als s plötzlich Cho i [[1TH.5.1-1TH.5.3]], und d Warnig vor eme "
                  "Brief, «wie wänn er vo eus wär», mitsamt em eigehändige Gruess ([[2TH.2.2]]; [[2TH.3.17]]) fall uf.",
          "uncertain": "D Verfasserschaft isch i de Forschig stark umstritte. D Äänlichkeit zum 1. Thessalonicherbrief "
                       "düüted di einte als Zeiche vo ziitlicher Nööchi, di andere als Nachamig. E Minderheit haltet de 2. "
                       "Thessalonicherbrief sogar für de früener vo de beide.",
          "terms": []}},

 # ---------------------------------------------------------------- 1. Timotheus
 {"id": "BG-1TI-BOOK-0001", "book": "1TI", "context": EC, "confidence": "possible",
  "topic": "Timotheus in Ephesus",
  "text": "Timotheus stammte aus Lystra in Kleinasien, Sohn einer jüdischen Mutter und eines griechischen Vaters "
          "([[ACT.16.1-ACT.16.3]]). Er war einer der engsten Mitarbeiter des Paulus und wird in sechs Briefen als "
          "Mitabsender genannt (z. B. [[2CO.1.1]]; [[PHP.1.1]]; [[1TH.1.1]]). Nach dem Brief liess Paulus ihn in Ephesus "
          "zurück, um gegen falsche Lehren vorzugehen ([[1TI.1.3-1TI.1.7]]; [[1TI.6.20]]). Der Brief ordnet das "
          "Gemeindeleben: Aufgaben der Aufseher (griechisch episkopos, woraus «Bischof» wurde) und der Diakone "
          "([[1TI.3.1-1TI.3.13]]), Versorgung der Witwen ([[1TI.5.3-1TI.5.16]]). Wie beim Titusbrief ist die "
          "Verfasserschaft umstritten: Paulus selbst um 63–65 n. Chr. nach einer Freilassung, Paulus mit Hilfe eines "
          "Sekretärs oder ein Schüler um 80–110 n. Chr. Die vorausgesetzte Reise nach Makedonien ([[1TI.1.3]]) lässt sich "
          "in der Apostelgeschichte nicht unterbringen.",
  "uncertain": "Die Verfasserfrage hängt davon ab, wie man Wortschatz, Stil und die entwickelte Gemeindeordnung "
               "gewichtet und ob man eine Freilassung des Paulus nach der ersten römischen Haft annimmt, die erst spätere "
               "Überlieferung berichtet. Gegen welche Lehre sich der Brief richtet (jüdisch geprägt, frühe Gnosis oder "
               "anderes), ist umstritten.",
  "evidence_refs": ["ACT.16.1-ACT.16.3", "1TI.1.3-1TI.1.7", "1TI.3.1-1TI.3.13", "1TI.5.3-1TI.5.16", "1TI.6.20"],
  "sources": [],
  "terms": [T("grc", "ἐπίσκοπος", "Aufseher (daraus «Bischof»)")],
  "gsw": {"topic": "De Timotheus z Ephesus",
          "text": "De Timotheus isch us Lystra z Chliiasie cho, de Soon vo ere jüdische Mueter und eme griechische Vater "
                  "([[ACT.16.1-ACT.16.3]]). Er isch eine vo de ängschte Mitarbeiter vom Paulus gsii und wird i sächs Brief "
                  "als Mitabsänder gnännt (z. B. [[2CO.1.1]]; [[PHP.1.1]]; [[1TH.1.1]]). Nach em Brief hät de Paulus en z "
                  "Ephesus zrugglaa, zum gäge falschi Leere vorzgaa ([[1TI.1.3-1TI.1.7]]; [[1TI.6.20]]). De Brief ornet s "
                  "Gmeindsläbe: d Ufgabe vo de Ufseher (griechisch episkopos, wo drus «Bischof» worde isch) und vo de "
                  "Diakon ([[1TI.3.1-1TI.3.13]]), d Versorgig vo de Witwe ([[1TI.5.3-1TI.5.16]]). Wie bim Titusbrief isch "
                  "umstritte, wär en gschribe hät: de Paulus sälber um 63–65 n. Chr. nach ere Freilassig, de Paulus mit "
                  "Hilf vo me Sekretär oder en Schüeler um 80–110 n. Chr. D Reis uf Makedonie, wo voruusgsetzt isch "
                  "([[1TI.1.3]]), passt nöd i d Apostelgschicht.",
          "uncertain": "D Verfasserfrag hangt devo ab, wie me Wortschatz, Stil und di entwicklet Gmeindsornig gwichtet und "
                       "öb me e Freilassig vom Paulus nach de erschte römische Haft aanimmt, vo dere erscht e spööteri "
                       "Überlieferig bricht. Gäge weli Leer sich de Brief richtet (jüdisch prägt, früei Gnosis oder anders), "
                       "isch umstritte.",
          "terms": ["Ufseher (drus isch «Bischof» worde)"]}},

 # ---------------------------------------------------------------- 2. Timotheus
 {"id": "BG-2TI-BOOK-0001", "book": "2TI", "context": EC, "confidence": "possible",
  "topic": "Das Vermächtnis eines Gefangenen",
  "text": "Der 2. Timotheusbrief ist als Abschiedsbrief gestaltet: Paulus liegt in Rom in Ketten ([[2TI.1.8]]; "
          "[[2TI.1.16-2TI.1.17]]), rechnet mit seinem nahen Tod ([[2TI.4.6-2TI.4.8]]) und bittet Timotheus, vor dem "
          "Winter zu kommen und Mantel und Schriftrollen aus Troas mitzubringen ([[2TI.4.13]]; [[2TI.4.21]]). Viele "
          "Mitarbeiter haben ihn verlassen ([[2TI.4.10-2TI.4.11]]; [[2TI.4.16]]). Nach alter Überlieferung starb Paulus "
          "unter Kaiser Nero in Rom als Märtyrer. Wer den Brief Paulus zuschreibt, datiert ihn in eine zweite römische "
          "Haft um 64–67 n. Chr. Andere sehen ihn wie die übrigen Pastoralbriefe als Schrift eines Schülers (um 80–110 n. "
          "Chr.), die das Erbe des Paulus in Form eines Testaments bewahrt. Eine vermittelnde These rechnet mit echten "
          "persönlichen Notizen des Paulus, die in einen späteren Brief eingearbeitet wurden.",
  "uncertain": "Ob Paulus nach der in [[ACT.28.30-ACT.28.31]] erwähnten Haft freikam und ein zweites Mal gefangen war, "
               "berichtet erst spätere Überlieferung (Eusebius); die Apostelgeschichte schweigt darüber. Todesjahr und "
               "Umstände sind nicht genau bekannt. Die persönlichen Angaben gelten den einen als Zeichen der Echtheit, "
               "den anderen als bewusst gestaltete Erinnerung.",
  "evidence_refs": ["2TI.1.8", "2TI.1.16-2TI.1.17", "2TI.4.6-2TI.4.8", "2TI.4.9-2TI.4.21"],
  "sources": ["1. Clemensbrief 5,5-7", "Eusebius, Kirchengeschichte 2,22", "Eusebius, Kirchengeschichte 2,25"],
  "terms": [],
  "gsw": {"topic": "S Vermächtnis vo me Gfangne",
          "text": "De 2. Timotheusbrief isch als Abschiidsbrief gstaltet: De Paulus liit z Rom i Chette ([[2TI.1.8]]; "
                  "[[2TI.1.16-2TI.1.17]]), rächnet mit sim nööche Tod ([[2TI.4.6-2TI.4.8]]) und bittet de Timotheus, vor em "
                  "Winter z cho und Mantel und Schriftrolle us Troas mitzbringe ([[2TI.4.13]]; [[2TI.4.21]]). Vili "
                  "Mitarbeiter händ en verlaa ([[2TI.4.10-2TI.4.11]]; [[2TI.4.16]]). Nach alter Überlieferig isch de "
                  "Paulus under em Kaiser Nero z Rom als Märtyrer gstorbe. Wär de Brief em Paulus zueschriibt, datiert en i "
                  "e zweiti römischi Haft um 64–67 n. Chr. Anderi gsend en wie di andere Pastoralbrief als Schrift vo me "
                  "Schüeler (um 80–110 n. Chr.), wo s Erb vom Paulus i de Form vo me Teschtamänt bewaart. E vermittlendi "
                  "These rächnet mit ächte persönliche Notize vom Paulus, wo i en spöötere Brief iigarbeitet worde sind.",
          "uncertain": "Öb de Paulus nach de Haft, wo i [[ACT.28.30-ACT.28.31]] erwäänt isch, freicho isch und es zweits Mal "
                       "gfange gsii isch, bricht erscht e spööteri Überlieferig (Eusebius); d Apostelgschicht schwiigt "
                       "drüber. Todesjaar und Umständ sind nöd gnau bekannt. Di persönliche Aagabe gälted de einte als "
                       "Zeiche vo Ächtheit, de andere als bewusst gstalteti Erinnerig.",
          "terms": []}},

 # ---------------------------------------------------------------- Philemon
 {"id": "BG-PHM-BOOK-0001", "book": "PHM", "context": EC, "confidence": "probable",
  "topic": "Ein Brief über einen Sklaven",
  "text": "Der kürzeste Paulusbrief richtet sich an Philemon und die Hausgemeinde, die sich bei ihm traf "
          "([[PHM.1.1-PHM.1.2]]), wohl in Kolossä, wie gleiche Namen im Kolosserbrief nahelegen ([[COL.4.9]]; "
          "[[COL.4.17]]). Paulus schreibt als Gefangener ([[PHM.1.9-PHM.1.10]]). Bei ihm ist Onesimus, ein Sklave "
          "Philemons, der durch Paulus Christ geworden ist. Paulus schickt ihn zurück und bittet Philemon, ihn als Bruder "
          "aufzunehmen ([[PHM.1.15-PHM.1.17]]); einen allfälligen Schaden will er selbst ersetzen "
          "([[PHM.1.18-PHM.1.19]]). Dabei spielt er mit dem Namen Onesimus, der «nützlich» bedeutet ([[PHM.1.11]]). "
          "Sklaverei war im Römischen Reich alltäglich; auch christliche Haushalte besassen Sklaven. Der Brief stammt "
          "unbestritten von Paulus, je nach Haftort um 54/55 (Ephesus) oder um 60–62 n. Chr. (Rom).",
  "uncertain": "Ob Onesimus entlaufen war oder Paulus bewusst als Fürsprecher bei seinem Herrn aufsuchte, ist umstritten; "
               "der Brief sagt es nicht ausdrücklich. Ein Vergleichsfall ist ein Brief des jüngeren Plinius, der bei einem "
               "Freund für dessen Freigelassenen bittet. Offen ist auch, ob Paulus die Freilassung erbittet. Für Ephesus "
               "spricht der geplante baldige Besuch ([[PHM.1.22]]), für Rom die verbreitete kirchliche Überlieferung.",
  "evidence_refs": ["PHM.1.1-PHM.1.2", "PHM.1.9-PHM.1.19", "PHM.1.22", "COL.4.9", "COL.4.17"],
  "sources": ["Plinius der Jüngere, Briefe 9,21"],
  "terms": [T("grc", "Ὀνήσιμος", "Onesimus: «nützlich»")],
  "gsw": {"topic": "En Brief über en Sklav",
          "text": "De chürzischt Paulusbrief richtet sich a de Philemon und d Husgmeind, wo sich bi im troffe hät "
                  "([[PHM.1.1-PHM.1.2]]), wahrschiinli z Kolossä, wie gliichi Näme im Kolosserbrief nooleged ([[COL.4.9]]; "
                  "[[COL.4.17]]). De Paulus schriibt als Gfangne ([[PHM.1.9-PHM.1.10]]). Bi im isch de Onesimus, en Sklav "
                  "vom Philemon, wo dur de Paulus Christ worde isch. De Paulus schickt en zrugg und bittet de Philemon, en "
                  "als Brueder ufznee ([[PHM.1.15-PHM.1.17]]); en allfällige Schade wott er sälber ersetze "
                  "([[PHM.1.18-PHM.1.19]]). Debii spilt er mit em Name Onesimus, wo «nützlich» heisst ([[PHM.1.11]]). "
                  "Sklaverei isch im Römische Riich alltäglich gsii; au christlichi Hushält händ Sklave gha. De Brief "
                  "stammt unbestritte vom Paulus, je nach Haftort um 54/55 (Ephesus) oder um 60–62 n. Chr. (Rom).",
          "uncertain": "Öb de Onesimus devoglaufe gsii isch oder de Paulus bewusst als Fürsprecher bi sim Herr ufgsuecht hät, "
                       "isch umstritte; de Brief seit s nöd usdrücklich. En Verglichsfall isch en Brief vom jüngere Plinius, "
                       "wo bi me Fründ für dä sin Freiglassne bittet. Offe isch au, öb de Paulus um d Freilassig bittet. "
                       "Für Ephesus redt de planti baldig Bsuech ([[PHM.1.22]]), für Rom di verbreitet chirchlich Überlieferig.",
          "terms": ["Onesimus: «nützlich»"]}},
]
