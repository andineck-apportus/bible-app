"""Autorenwerkzeug: Züridüütsch-Fassung der Studieninhalte (Befunde, Deutungen, Grundsätze, Anwendungen,
Fragen, Hintergrund, Zusammenfassungen aller Ebenen, Wortbedeutungen und Erklärungen zu den Lesarten).

Aufruf: python3 scripts/authoring/zueridueuetsch_inhalte.py

Schreibt pro übersetztem Datensatz eine eigene Lokalisierung `data/localizations/gsw-u-sd-chzh/<ID>.json`
(Typ `localization`, siehe docs/DATENMODELL.md): `localizes` verweist auf den Originaldatensatz, `fields` trägt
dieselben Feldnamen wie das hochdeutsche Original (z. B. `claim_de`, `text_de`; bei `terms` eine Liste der
Bedeutungen in derselben Reihenfolge), `source_fingerprint` hält fest, von welchem Stand des Originals übersetzt
wurde. Der Originaldatensatz wird nicht verändert. Idempotent.
KI-Entwurf (Claude) vom 2026-10-13; Prüfung der Mundart durch eine muttersprachliche Person vorgesehen.
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
D = ROOT / "data"
LANG = "gsw-u-sd-chzh"
DATE = "2026-10-13"
AUTH = f"KI-Entwurf (Claude) vom {DATE}; aus dem Hochdeutschen und dem Urtext in Züridüütsch gefasst; Mundart noch nicht muttersprachlich geprüft."

I18N = {
 # ---------------------------------------------------------------- Befunde
 "FIND-LP-0001": {"claim_de": "Nach de Aared folged bim Matthäus drüü Bitte mit «diin» (Name, Riich, Wile) und nachhär vier Bitte mit «üs» bzw. «öise» (Broot, Schulde, Versuechig, Rettig).",
                  "confidence_rationale_de": "Beobachtig am Wortluut; wie me d Bitte zellt (sächs oder sibe), wird i de Tradition verschide ghandhabt."},
 "FIND-LP-0002": {"claim_de": "De Lukas hät e chürzeri Fassig: d Aared isch nu «Vatter», ohni d Bitt um Gottes Wile und ohni d Bitt um Rettig vor em Bööse. Statt «Schulde» seit er «Sünde», bhaltet aber im zweite Satzteil s Bild vom Schuldner.",
                  "confidence_rationale_de": "Vergliich vo de SBLGNT-Text; i vilne spöötere Handschrifte isch d Lukasfassig a de Matthäus aaglichet (lueg Läsarte)."},
 "FIND-LP-0003": {"claim_de": "S griechische Wort, wo me meischtens mit «täglich» übersetzt (ἐπιούσιος), chunnt im Nöie Teschtamänt nu im Vatterunser vor (Mt 6,11; Lk 11,3). De Origenes hät im 3. Jaarhundert gmerkt, dass es bi de Grieche süscht nöd bruucht wird.",
                  "confidence_rationale_de": "Origenes, Über s Gebät 27,7; spööteri Fund vo einzelne Beleg sind umstritte. Drum isch d Bedüütig unsicher."},
 "FIND-LP-0004": {"claim_de": "Vo allne Bitte vom Vatterunser nimmt de Matthäus nu d Bitt um Vergäbig nachhär nomal uf (6,14–15).",
                  "confidence_rationale_de": "Beobachtig am Wortluut."},
 "FIND-LP-0005": {"claim_de": "De Lobpriis «Dänn diin isch s Riich …» fäält bim Matthäus i de eltischte erhaltene Handschrifte (Sinaiticus, Vaticanus, Bezae) und staat im Washingtonianus (4./5. Jh.) und i de Meerheit vo de spöötere Handschrifte.",
                  "confidence_rationale_de": "Nach de importierte CNTR-Transkriptione und de maschinelle Zuordnig (WREAD-CNTR-MAT-006-005-015); nöd am Faksimile prüeft."},
 "FIND-LP-0006": {"claim_de": "D churz Lukasfassig (Aared «Vatter», ohni Wilesbitt und ohni «sondern rett üs») staat im 𝔓75 und im Vaticanus; de Sinaiticus hät d churz Aared, aber d Wilesbitt. Alexandrinus, Ephraemi, Bezae und Washingtonianus händ die längere Forme, wo a de Matthäus aaglichet sind.",
                  "confidence_rationale_de": "Nach de CNTR-Transkriptione (WREAD-CNTR-LUK-011-001-004); maschinelli Zuordnig, nöd am Faksimile prüeft."},
 "FIND-MRK-0001": {"claim_de": "Mk 3,30 begründet d Warnig vom Jesus demit, dass d Schriftgleerte gseit händ, er heig en unreine Geischt."},
 "FIND-MRK-0002": {"claim_de": "D Red verbindt de Beelzebul-Vorwurf mit de Antwort vom Jesus über de Satan und d Läschterig vom Heilige Geischt."},
 "FIND-MRK-0003": {"claim_de": "De Schluss vo Mk 3,29 isch i verschidene Läsarte überliferet (Sünd/Gricht).",
                   "confidence_rationale_de": "D Variante sind us de bisherige Vorarbet bekannt; d Zuordnig vo de Züüge mues no a de Primärquelle prüeft wärde."},
 "FIND-MRK-0004": {"claim_de": "Mk 3,22 nännt de Vorwurf; 3,23–27 enthaltet d Gägenargumänt vom Jesus und 3,28–30 d Warnig samt Begründig."},
 "FIND-MRK-0005": {"claim_de": "I 3,21 mached sich d Aaghörige vom Jesus (οἱ παρʼ αὐτοῦ) uf, zum en hole; i 3,31 chömed sini Mueter und sini Brüeder aa. Dezwüsche staat d Usenandersetzig mit de Schriftgleerte us Jerusalem (3,22–30).",
                   "confidence_rationale_de": "Beobachtig am Wortluut; öb οἱ παρʼ αὐτοῦ die gliiche Lüüt sind wie d Mueter und d Brüeder i 3,31, seit de Text nöd usdrückli."},
 # ---------------------------------------------------------------- Deutungen
 "INT-LP-0001": {"claim_de": "«Broot für de nööchscht Taag»: S Wort (ἐπιούσιος) wird vom griechische Usdruck für «de nööchscht Taag» (ἡ ἐπιοῦσα ἡμέρα) abgleitet. Me bittet hüt um s Broot für morn, demit me nöd i Sorg läbe mues. De Hieronymus brichtet, im Hebräerevangelium stöng da «mahar» (für morn).",
                 "caveat_de": "Staat i Spannig zu Mt 6,34 («Sorged nöd für morn»), wänn me s als Vorsorg verstaat.",
                 "counterarguments_de": ["D Bitt «gib üs hüt s Broot für morn» cha grad das Vertroue usdrucke, wo 6,34 verlangt: Me leit de nööchscht Taag i Gottes Hand.",
                                         "D Notiz vom Hieronymus bezieht sich uf es Evangelium, wo nöd erhalte isch, und cha e spööteri Rucküebersetzig sii."]},
 "INT-LP-0002": {"claim_de": "«S Broot, wo me zum Läbe bruucht»: S Wort (ἐπιούσιος) wird vo «für» (ἐπί) und «Daasii, Läbesunterhalt» (οὐσία) abgleitet. Me bittet um das, wo me zum Läbe bruucht, nöd um Überfluss (vgl. Spr 30,8).",
                 "caveat_de": "Sprachlich isch die Wortbildig ungwöhnli; me wür e chli e anderi Form erwarte (ἐπούσιος).",
                 "counterarguments_de": ["D Tradition «täglich» (latiinisch cotidianum) und s lukanische «Taag für Taag» passed guet zu dere Bedüütig."]},
 "INT-LP-0003": {"claim_de": "«S Broot vo de chünftige Wält»: Mängi Chilevätter händ s Wort geischtlich verstande, als Broot vom Gottesriich oder als Abigmaal; de Hieronymus hät im Matthäus mit supersubstantialem («überwäsentlich») übersetzt.",
                 "caveat_de": "Die Düütig liit wiiter wägg vom Alltagsbroot, a das d Zuehörer vom Jesus zerscht dänkt händ.",
                 "counterarguments_de": ["D Bitt um s Riich (6,10) und d Maalgmeinschafte vom Jesus verbinded Alltagsbroot und s erwartete Feschtmaal; beides mues sich nöd usschlüüsse."]},
 "INT-LP-0004": {"claim_de": "«Füer üs nöd i d Versuechig» bittet drum, nöd in e Prüefig ine z choo, wo me de Glaube verlüürt. Vili dänked debii a di groossi Bedrängnis vo de Ändziit, anderi a alltäglichi Versuechige.",
                 "caveat_de": "Öb Gott sälber als dä dänkt isch, wo i d Versuechig füert, isch umstritte; Jak 1,13 seit, Gott versuechi niemert.",
                 "counterarguments_de": ["S Griechische isch e Bitt a Gott und setzt vorus, dass au Prüefige i siner Hand liged (vgl. Gen 22,1). D Bitt widerspricht Jak 1,13 nöd, wänn me «Prüefig» und «Verfüerig zum Bööse» usenand haltet.",
                                         "Einigi Chile händ d Formulierig i de letschte Ziit gänderet (z. B. Frankriich 2017: «lass üs nöd i d Versuechig ine trätte»; Italie 2020: «überlass üs nöd de Versuechig»), anderi, etwa d tüütschsprachige katholische Bistüemer 2018, händ si bhalte."]},
 "INT-LP-0005": {"claim_de": "D Bitt um Vergäbig isch bim Matthäus mit de eigene Bereitschaft zum Vergää verknüpft: Wär sälber nöd vergit, verschlüüsst sich de Vergäbig vo Gott (6,14–15; vgl. Mt 18,23–35).",
                 "caveat_de": "Öb s eigene Vergää Bedingig oder Folg vo de empfangene Vergäbig isch, wird verschide gsee.",
                 "counterarguments_de": ["Im Gliichnis Mt 18,23–35 gaat d Vergäbig vom Herr vora; s eigene Vergää isch d Antwort druf, nöd e Leischtig.",
                                         "D Vergangeheitsform «wie mir vergää händ» (6,12) cha me als Usdruck vo de Bereitschaft verstaa, nöd als Vorleischtig."]},
 "INT-LP-0006": {"claim_de": "«Vor em Bööse» meint de Böös als Person (de Tüüfel), wie i Mt 13,19.38.",
                 "caveat_de": "S Griechische laat «s Bööse» (Neutrum) und «de Böös» (Maskulinum) zue; d Chile vom Oschte bätted meischtens «vor em Bööse» im persönliche Sinn, vili weschtlichi Übersetzige neutral.",
                 "counterarguments_de": ["«S Bööse» im allgemeine Sinn (Unheil, Bosheit) passt gnau so zum Zämehang und zu jüdische Gebät um Bewaarig vor Böösem."]},
 "INT-LP-0007": {"claim_de": "De Lukas überliferet en elteri, chürzeri Form, wo de Matthäus für de Bruuch i siner Gmeind erwiiteret hät.",
                 "caveat_de": "Weli Fassig nööcher bim Jesus liit, cha me nöd sicher entscheide; vilicht hät de Jesus s Gebät i verschidene Forme gleert.",
                 "counterarguments_de": ["De Matthäus chönnt di ursprünglicheri Wortwaal bhalte haa (z. B. «Schulde» statt «Sünde»), während de Lukas für nödjüdischi Läser vereifacht.",
                                         "Beidi Fassige chönd uf verschideni Gmeindstraditione zruggaa, ohni dass eini vo de andere abhängt."]},
 "INT-MRK-0001": {"claim_de": "D Warnig bezieht sich im Verzellzämehang druf, dass s befreiende Wirke vom Jesus ere unreine Macht zuegschribe wird.",
                  "caveat_de": "De Text seit nöd usdrückli, dass d Schriftgleerte di göttlich Herkunft sicher erkännt händ."},
 "INT-MRK-0002": {"claim_de": "D Warnig cha me stercher als Beschriibig vo ere duurhafte Verhertig läse; d Duurhaftigkeit laat sich aber nöd elei us de Värbform bewiise."},
 "INT-MRK-0003": {"claim_de": "De Markus verschachtlet die zwei Szene bewusst: Aaghörigi («er isch nüme bi Troscht», 3,21) und Schriftgleerti («er hät de Beelzebul», 3,22) beurteiled de Jesus jede uf sini Art falsch. 3,35 bestimmt d Zueghörigkeit zum Jesus nöi über s Tue vom Wile vo Gott.",
                  "caveat_de": "Öb οἱ παρʼ αὐτοῦ i 3,21 d Familie vom Jesus meint (so di meischte Übersetzige) oder allgemeiner sini Lüüt, isch umstritte; gnau so, wär i 3,21 «si händ gseit» redt (d Aaghörige oder unbestimmt «me»). Je nach Entscheidig wird d Parallele schwächer.",
                  "counterarguments_de": ["D Verschachtelig cha au verzellerisch d Ziit überbrugge, bis d Aaghörige aachömed, ohni dass e Vergliich beabsichtigt isch."]},
 # ---------------------------------------------------------------- Grundsätze, Anwendungen, Fragen
 "PRIN-LP-0001": {"statement_de": "Bätte nach de Aaleitig vom Jesus faat mit ere vertrouensvolle Aared vo Gott und mit Gottes Sach aa und bringt dänn di eigene Grundbedürfnis vor: Broot, Vergäbig und Bewaarig. Empfangeni und gschänkti Vergäbig ghööred zäme."},
 "PRIN-MRK-0001": {"statement_de": "Behauptige über s Wirke vo Gott mues me verantwortigsvoll beurteile; s bewusste Verdrääje vo Guet und Böös isch nöd s Gliiche wie gwöhnliche Zwiifel."},
 "APP-LP-0001": {"statement_de": "Wär s Vatterunser hüt bättet, cha s langsam bätte und bi einzelne Bitte inehalte: Wo bruuch ich würkli «Broot für hüt»? Wem mues ich no vergää? In eme Land mit Überfluss cha d Broot-Bitt au a die erinnere, wo s Nötige fäält, dänn si heisst «öises» Broot, nöd «miis» Broot.",
                 "limitations_de": "Das isch e hüttigi Übertragig, kei Befund am Text. S Vatterunser händ zu siner Ziit Mänsche bättet, für wo s tägliche Broot oft unsicher gsii isch; das laat sich nöd eifach uf hüttigi Läbesverhältnis übertrage."},
 "APP-MRK-0001": {"statement_de": "E behaupteti Geischteswirkig dörf me kritisch prüefe; das isch nöd automatisch Läschterig vom Heilige Geischt.",
                  "limitations_de": "Hüttigi religiösi Behauptige cha me nöd eifach so mit em Wirke vom Jesus im Markus gliichsetze."},
 "QUESTION-LP-0001": {"question_de": "Was bedüütet ἐπιούσιος gnau: «täglich», «für de nööchscht Taag», «zum Läbe nötig» oder öppis anders?",
                      "finding_de": "S Wort isch usserhalb vom Vatterunser praktisch nöd belait; d Düütige stütze sich uf d Wortbildig, alti Übersetzige und früeji Usleger."},
 "QUESTION-LP-0002": {"question_de": "Weli Fassig vom Vatterunser staat em Jesus nööcher, und isch es ursprünglich uf Aramäisch bättet worde?",
                      "finding_de": "Beidi Fassige sind nu griechisch überliferet. Rucküebersetzige is Aramäische sind Rekonstruktione."},
 "QUESTION-MRK-0001": {"question_de": "Setzt de Vorwurf vo de Schriftgleerte vorus, dass si s Wirke vom Heilige Geischt bewusst als söttigs erkännt händ?",
                       "finding_de": "Mk 3,22–30 belait d Zueschriibig a de Beelzebul, nöd usdrückli s innere Wüsse vo dene, wo reded."},
 # ---------------------------------------------------------------- Hintergrund Vaterunser
 "BG-LP-0001": {"topic_de": "Zwei Fassige, zwei Läserchreis",
                "text_de": "De Matthäus stellt s Vatterunser i d Bärgpredigt, zwüsche Aawiisige zu Almose, Bätte und Faschte (6,1–18), wie si für d jüdisch Frömmigkeit typisch gsii sind. De Lukas verzellt, dass en Jünger de Jesus drum bittet, wie de Johannes de Töifer sini Jünger s Bätte gleert hät. Beidi händ Jaarzäänt nach em Jesus für verschideni Gmeinde gschribe, wo s Gebät wahrschiinli scho regelmässig bättet händ.",
                "uncertain_de": "Öb de Jesus s Gebät bi einere oder bi meerere Glägeheite gleert hät, isch offe."},
 "BG-LP-0002": {"topic_de": "Bätte im Judetum dozmal",
                "text_de": "Frommi Jude händ zu feschte Ziite bättet, oft drüümal am Taag (vgl. Dan 6,11; Ps 55,18), dezue s Schma Israel. Wär zur Gebätsziit underwägs gsii isch, hät dört bättet, wo n er grad gstande isch. De Jesus kritisiert nöd s Bätte i de Öffentlichkeit a sich, sondern s Bätte, zum gsee wärde.",
                "uncertain_de": "Wie fescht d Gebätsziite und d Gebätstext zur Ziit vom Jesus scho greglet gsii sind, isch i de Forschig umstritte."},
 "BG-LP-0003": {"topic_de": "Hüüchler, Chammer, Heide",
                "text_de": "S griechische Wort für Hüüchler hät ursprünglich Schauspiler uf de Büni bezeichnet. D «Chammer» isch e Vorrats- oder Inneruum gsii, i eifache Hüüser oft de einzig Ruum ohni Fänschter und mit Tür. I heidnische Gebät hät me d Gottheite mit vilne Näme und Biiname aagrüeft, demit me di richtig Aared troffe hät und erhört worde isch (vgl. 1 Kön 18,26).",
                "terms": ["Schauspiler, Hüüchler", "Vorratsruum, Chammer", "plappere, läär Wort mache"]},
 "BG-LP-0004": {"topic_de": "Gott als Vatter aarede",
                "text_de": "Au d hebräisch Bible und jüdischi Gebät nänned Gott Vatter (Jes 63,16; 64,7; Sir 23,1). Dass de Jesus Gott ganz direkt mit «Vatter» aaredt, uf Aramäisch «Abba» (Mk 14,36), und sini Jünger dezue aaleitet, wird oft als bsunders vertrout beschribe. S früeje Chrischtetum hät s aramäische Wort sogar i griechische Brief bhalte (Röm 8,15; Gal 4,6).",
                "uncertain_de": "Di verbreiteti Erkläärig, «Abba» seig d Chindersprach «Papi», gilt hüt als übertribe; s Wort händ au Erwachseni gägenüber irem Vatter bruucht.",
                "terms": ["Vatter", "Vatter"]},
 "BG-LP-0005": {"topic_de": "De Name heilige",
                "text_de": "De «Name» staat i de Bible für d Person sälber. Nach Ez 36,23 heiliget Gott sin Name, indäm er a siim Volk handlet. Es jüdischs Gebät, s Kaddisch, faat ähnlich aa: «Erhobe und gheiliget wärdi sin groosse Name … er lassi sis Riich choo.»",
                "uncertain_de": "S Kaddisch isch i siner hüttige Form düütli spööter belait; wie alt sini Chärnsätz sind, isch umstritte.",
                "terms": ["Name", "heilige", "heilig (Name vom Gebät)"]},
 "BG-LP-0006": {"topic_de": "S Riich vo Gott",
                "text_de": "Vili Jude händ erwartet, dass Gott sini Herrschaft sichtbar ufrichtet und Unrächt und frömdi Herrschaft beändet (vgl. Dan 2,44). Im Galiläa under römischer Oberherrschaft isch das au politisch brisant gsii. «Riich vo Gott» isch s zentrale Thema vo de Verkündigung vom Jesus (Mk 1,15).",
                "terms": ["Chünigsherrschaft, Riich"]},
 "BG-LP-0007": {"topic_de": "Broot für de Taag",
                "text_de": "Vili Mänsche händ vo de Hand i de Mund gläbt: Taglööner händ ire Loon am Aabig übercho und dervo s Ässe für de nööchscht Taag kauft (vgl. Mt 20,1–16; Dtn 24,15). I de Wüeschti hät Israel s Manna Taag für Taag übercho und hät kei Vorrat dörfe aalegge (Ex 16,4.19–20).",
                "uncertain_de": "Was s griechische Wort für «täglich» gnau bedüütet, isch unsicher (lueg Düütige).",
                "terms": ["meischtens «täglich»; Bedüütig unsicher", "morn"]},
 "BG-LP-0008": {"topic_de": "Schulde und Sünde",
                "text_de": "Im Aramäische, wo de Jesus gredt hät, bezeichnet s gliiche Wort (ḥôbā) e Gäldschuld und e Sünd. Verschuldig isch im Galiläa verbreitet gsii und hät bis zur Schuldchnächtschaft chöne füere. S Gsetz hät en Schuldeerlass i jedem sibte Jaar kännt (Dtn 15,1–2). De Matthäus bhaltet s Bild vo de Schulde, de Lukas seit «Sünde», redt aber im gliiche Värs vom Schuldner.",
                "terms": ["Schuld, Sünd", "Schuld"]},
 "BG-LP-0009": {"topic_de": "Versuechig und Prüefig",
                "text_de": "S griechische Wort meint beides: Versuechig zum Bööse und Prüefig vo de Tröi. D Bible verzellt vo Prüefige, etwa vom Abraham (Gen 22,1) oder vo Israel i de Wüeschti (Dtn 8,2). Vili Jude händ vor em Choo vom Riich e Ziit vo groosser Bedrängnis erwartet.",
                "terms": ["Versuechig, Prüefig"]},
 "BG-LP-0010": {"topic_de": "De Lobpriis am Schluss",
                "text_de": "Jüdischi Gebät händ oft mit eme Lobpriis vo Gott ufghört; es Vorbild isch s Gebät vom David i 1 Chr 29,11. D Didache, e früechrischtlichi Gmeindsordnig us de Ziit um 100, git s Vatterunser fascht wie de Matthäus wider, mit em Schluss «dänn diin isch d Chraft und d Herrlichkeit i Ewigkeit», und raatet, es drüümal am Taag z bätte.",
                "uncertain_de": "D Datierig vo de Didache isch umstritte (meischtens um 100)."},
 "BG-LP-0011": {"topic_de": "S Vatterunser uf Amulett",
                "text_de": "Us em 3. bis 6. Jaarhundert sind meereri chliini Papyrusblätter und e Tonschärbe mit em Vatterunser erhalte, oft als Schutz-Amulett traage. Si zeiged, wie verbreitet s Gebät gsii isch, und dass eifachi Lüüt es nach em Ghöör ufgschribe händ, mit vilne Schriibvariante.",
                "uncertain_de": "D Iiordnig als Amulett beruet uf em Format und em Fundzämehang; nöd jedes Stuck isch sicher eis."},
 "BG-LP-0012": {"topic_de": "De Johannes und sini Jünger",
                "text_de": "Leerer und iri Schüelerchreis händ eigeni Gebät gha; au vo de Jünger vom Johannes em Töifer wird verzellt, dass si gfaschtet und bättet händ (Lk 5,33). Es eigets Gebät hät ere Gruppe Zämehalt und es Erkännigszeiche gää."},
 # ---------------------------------------------------------------- Hintergrund Markus
 "BG-MRK-0001": {"topic_de": "Ziit und Ort",
                 "text_de": "D Szene spilt um s Jaar 30 im Galiläa, im Norde vom Land. Dört hät de Herodes Antipas als vo Rom abhängige Fürscht regiert; Jerusalem mit em Tämpel isch im Judäa gläge, wo en römische Statthalter verwaltet hät. D Lüüt im Galiläa händ im Alltag Aramäisch gredt, händ meischtens vo Landwirtschaft, Handwärch und Fischerei gläbt und sind i Dorf und Groossfamilie iibunde gsii.",
                 "uncertain_de": "S gnaue Jaar isch nöd bekannt."},
 "BG-MRK-0002": {"topic_de": "Für wän de Markus gschribe hät",
                 "text_de": "De Markus verzellt die Ereignis es paar Jaarzäänt spööter uf Griechisch. Sini Läser händ jüdischi Brüüch offebar nöd alli kännt, dänn er erkläärt si a andere Stell (Mk 7,3–4). Wär d Szene list, sött also zwei Ziite im Blick haa: d Situation um de Jesus und d Frage vo de erschte chrischtliche Gmeinde, für wo de Markus verzellt.",
                 "uncertain_de": "Ort und Ziitpunkt, wo s gschribe worde isch, sind umstritte."},
 "BG-MRK-0003": {"topic_de": "Es volls Huus",
                 "text_de": "Hüüser im Galiläa sind meischtens eifach gsii: es paar Rüüm us Basaltstei um en offne Hof, wo me kochet und gschaffet hät. Scho es paar Dotzed Lüüt händ Huus und Iigang gfüllt. Im Kafarnaum, wo de Jesus nach em Markus gwont hät, sind söttigi Wonhüüser usgrabe worde.",
                 "uncertain_de": "Öb s Huus da im Kafarnaum staat und wem s ghört, seit de Text nöd."},
 "BG-MRK-0004": {"topic_de": "Familie und Ruef",
                 "text_de": "D Familie isch dozmal nöd Privatsach gsii, sondern di wichtigscht Läbes- und Schutzgmeinschaft. Was eis Mitglid taa hät, isch uf alli zruggfalle. Wänn öpper für «nüme bi Troscht» ghalte worde isch, isch es d Ufgab vo de Aaghörige gsii, en hei z hole. Verwirrtheit hät me oft mit eme bööse Geischt i Verbindig bracht.",
                 "uncertain_de": "Wär mit «sini Lüüt» gmeint isch, isch umstritte (lueg «Wie cha me s verstaa?»).",
                 "terms": ["die vo ihm her, sini Aaghörige", "er isch nüme bi Troscht"]},
 "BG-MRK-0005": {"topic_de": "Schriftgleerti us Jerusalem",
                 "text_de": "Schriftgleerti sind Känner und Leerer vo de heilige Schrifte und vom Gsetz gsii. Jerusalem mit em Tämpel isch s religiöse Zentrum gsii. Bis is Galiläa sind s öppe 120 Kilometer gsii, meereri Taag z Fuess. Dass Schriftgleerti vo dört chömed, zeigt: Was de Jesus macht, beschäftiget me au im Zentrum.",
                 "uncertain_de": "Öb si im Uftrag vo ere Behörde choo sind, isch offe.",
                 "terms": ["Schriftgleerti"]},
 "BG-MRK-0006": {"topic_de": "Beelzebul",
                 "text_de": "De Name erinneret a «Baal-Sebub», en Gott vo de Philischterstadt Ekron (2 Kön 1,2). «Baal» heisst «Herr»; «Sebub» bedüütet «Flüüge», was wahrschiinli e spöttisch verdrääjte Name isch. «Sebul» cha «Wonig» oder «erhabeni Wonig» heisse. Zur Ziit vom Jesus hät de Name de Aafüerer vo de bööse Geischter bezeichnet. D Düütig «Herr vom Huus» wür zu de Bilder vom Huus i 3,25–27 passe; au Mt 10,25 spilt mit «Huusherr» und «Beelzebul».",
                 "uncertain_de": "Herkunft und Bedüütig vom Name sind nöd sicher kläärt.",
                 "terms": ["Beelzebul", "Herr vo de Flüüge (2 Kön 1,2)", "Wonig, erhabeni Wonig"]},
 "BG-MRK-0007": {"topic_de": "Geischter ustriibe",
                 "text_de": "Dass me böösi Geischter cha ustriibe, hät me dozmal allgemein aagnaa; au anderi jüdischi Heiler händ das gmacht. De jüdisch Gschichtsschriiber Josephus verzellt vo eme Eleazar, wo vor em spöötere Kaiser Vespasian mit Formle, wo me uf de Chünig Salomo zruggfüert hät, en Dämon ustribe hät. D Gägner bestriited im Text au nöd, dass de Jesus Geischter ustribt; si fraged, us welere Macht er s macht. De Vorwurf, de Jesus seig en Zauberer gsii, findt me spööter au bi jüdische und andere Gägner vom Chrischtetum.",
                 "terms": ["usewärfe, ustriibe"]},
 "BG-MRK-0008": {"topic_de": "De Starch binde",
                 "text_de": "S Bild vom Starche, wo me sini Büüti wägnimmt, erinneret a Jes 49,24–25: Gott sälber nimmt em Starche d Gfangene ab. I jüdische Schrifte vo dere Ziit wärded böösi Mächt «bunde», etwa im Buech Tobit (8,3) oder im äthiopische Henochbuech (10,4). Zuehörer händ s Bild drum als Hiiwiis chöne verstaa, dass Gottes Sieg über s Bööse aafaat.",
                 "uncertain_de": "Wie wiit de Jesus und de Markus a die Text dänkt händ, isch e Düütig, kei Befund.",
                 "terms": ["starch; de Starch", "binde"]},
 "BG-MRK-0009": {"topic_de": "«Amen» am Aafang",
                 "text_de": "«Amen» heisst «so isch es, es gilt». Im Gottesdienscht isch es d Antwort vo de Gmeind uf es Gebät oder en Säge gsii (Dtn 27,15–26; Neh 8,6). De Jesus setzt s degäge a de Aafang vo sine Wort. Die ungwöhnlich Redwiis isch i de Evangelie typisch für ihn und understriicht, was folgt.",
                 "terms": ["so isch es, es gilt", "Amen"]},
 "BG-MRK-0010": {"topic_de": "Läschterig",
                 "text_de": "Läschterig hät bedüütet, verächtlich gäge Gott oder Heiligs z rede; nach em Gsetz isch d Läschterig vom Gottesname es schwärs Vergää gsii (Lev 24,15–16). Bekannt isch au d Underscheidig gsii zwüsche Versee und Sünd «mit erhobener Hand», also bewusster Uflenig, für wo s kei Opfer gää hät (Num 15,30–31). Vor dem Hintergrund fallt uf, wie wiit de Jesus d Vergäbig fasst: Alli Läschterige vo de Mänsche chönd vergää wärde, mit einere Usnaam.",
                 "uncertain_de": "Öb de Jesus bewusst a Num 15 aaknüpft, isch offe.",
                 "terms": ["Läschterig"]},
 "BG-MRK-0011": {"topic_de": "D Brüeder vom Jesus",
                 "text_de": "De Markus nännt a anderer Stell vier Brüeder, Jakobus, Joses, Judas und Simon, und Schwöschtere (Mk 6,3). Wie si mit em Jesus verwandt sind, wird i de Chile sit em 4. Jaarhundert verschide verstande: als jüngeri Chind vo de Maria und em Josef, als Chind vom Josef us ere früenere Ehe oder als Cousins. S griechische Wort für «Brueder» cha au wiiteri Verwandti meine. De Josef wird nöd erwäänt; vili vermueted, dass er scho gstorbe gsii isch.",
                 "uncertain_de": "D Verwandtschaftsfrag isch zwüsche de Konfessione umstritte; de Text sälber entscheidet si nöd.",
                 "terms": ["Brueder, au Verwandte"]},
 "BG-MRK-0012": {"topic_de": "Dine sitze, dusse staa",
                 "text_de": "Um en Leerer ume z sitze isch d Haltig vo Schüeler gsii (vgl. Lk 10,39; Apg 22,3). En früeje jüdische Spruch raatet: «Setz dich i de Staub vo irne Füess», gmeint sind d Leerer. D Familie degäge staat dusse und laat en rüefe. In ere Kultur, wo d Familie Aaspruch uf iri Mitglider gha hät, isch das e starchi Bitt gsii."},
 "BG-MRK-0013": {"topic_de": "E nöii Familie",
                 "text_de": "Wil d Familie Läbesgrundlag, Altersvorsorg und Eer bedüütet hät, isch es uffällig gsii, Mänsche usserhalb vo de Verwandtschaft «Mueter» und «Brüeder» z nänne. Gliichziitig hät s Gebot golte, d Eltere z eere (Ex 20,12). De Markus chunnt spööter druf zrugg: Wär wäge em Jesus d Familie verlaat, überchunnt e nöii Gmeinschaft (Mk 10,29–30). Für di erschte Gmeinde, wo mängi wäge irem Glaube mit de eigene Familie broche händ, isch das wichtig gsii.",
                 "uncertain_de": "Wie scharf de Gägesatz zur liibliche Familie gmeint isch, wird verschide beurteilt."},
}

# ---------------------------------------------------------------- Zusammenfassungen (alle Ebenen)
SUM = {
 "SUM-BIBLE": "D Bible versammlet Verzellige, Gebät, Wiisheit, prophetischi Stimme und Brief. I chrischtlicher Läsart verbindt si d Gschicht vo Gott mit Israel mit em Läbe, em Tod und de Uferstehig vom Jesus und mit de Hoffnig uf e ernöiereti Schöpfig.",
 "SUM-OT": "D Schrifte vo Israel verzelled vo Schöpfig, Befreiig, Bund und em Läbe vo eme Volk vor Gott. Gschicht, Chlag und Wiisheit stönd näbe prophetischer Kritik und de Hoffnig uf Ernöierig. Iri underschidliche Stimme träged Erfaarige vo Vertroue, Schiitere, Exil und Nöiaafang zäme.",
 "SUM-NT": "S Nöie Teschtamänt verzellt vom Läbe, Stärbe und de Uferstehig vom Jesus, vo de erschte Gmeinde und vo de Hoffnig uf d Vollendig. Vier Evangelie, d Apostelgschicht, Brief und d Offebarig lueged das us verschidene Blickwinkel aa.",
}

# Buchgruppen, Bücher und Kapitel: Zusammenfassungen werden unten aus SUM_GROUPS/SUM_BOOKS/SUM_CH ergänzt
SUM_GROUPS = {
 "SUM-GROUP-01": "Di föif Büecher vom Mose: Schöpfig, Erzvätter, Uszug us Ägypte, Bund am Sinai und d Weisige für s Läbe als Gottes Volk, bis a d Gränze vom verheissene Land.",
 "SUM-GROUP-02": "D Gschichtsbüecher verzelled vo de Landnaam, de Richter, de Chünig, vom Exil und vo de Ruckkeer. Si zeiged, wie s Volk mit Gott und sine Gebot umgaat, und frööged nach Tröi und Schuld.",
 "SUM-GROUP-03": "Poesie und Wiisheit: Hiob ringt mit em Leide, d Psalme bätted i allne Laage, d Sprüch sammled Läbenswiisheit, de Prediger fröögt nach em Sinn, s Hoheslied singt vo de Liebi.",
 "SUM-GROUP-04": "Di groosse Prophete Jesaja, Jeremia, Ezechiel und Daniel (mit de Chlagelieder) reded i Kriise vo Gricht und Hoffnig: Si warne, trööschte und zeiged Gottes Plan über d Völker.",
 "SUM-GROUP-05": "Zwölf chürzeri Prophetebüecher, vo Hosea bis Maleachi: Rüef zur Umkeer, Gricht über Unrächt, Hoffnig uf Ernöierig und de Taag vom Herr.",
 "SUM-GROUP-06": "Vier Verzellige vom Jesus: Matthäus, Markus, Lukas und Johannes. Jedi zeigt sis Wirke, sini Wort, sin Tod und sini Uferstehig us em eigene Blickwinkel und für eigeni Läser.",
 "SUM-GROUP-07": "D Apostelgschicht verzellt, wie d Botschaft vom Jesus vo Jerusalem über Samaria bis Rom chunnt: Pfingschte, di erschti Gmeind, Petrus und Paulus.",
 "SUM-GROUP-08": "Brief vom Paulus a Gmeinde und Mitarbeiter: Si erkläred de Glaube, löösed Striit, ermuetiged und zeiged, wie Chrischte zäme läbe söled.",
 "SUM-GROUP-09": "Wiiteri Brief, vom Hebräerbrief bis zum Judasbrief: Duurehalte im Glaube, Glaube und Werk, Liebi, Warnig vor Irrleerer und Hoffnig i de Bedrängnis.",
 "SUM-GROUP-10": "D Offebarig vom Johannes: Bilder vo Gricht und Rettig, Trooscht für verfolgti Gmeinde und d Hoffnig uf de nöie Himel und di nöii Ärde.",
}
SUM_CH = {
 "SUM-CH-GEN-001": "Gott erschafft i sibe Taag Himel und Ärde, Liecht, Land, Pflanze, Tier und de Mänsch als sis Abbild; am sibte Taag rueet er.",
 "SUM-CH-GEN-002": "De Mänsch im Garte Eden: Gott setzt en als Gärtner ii, git em s Gebot wäge em Baum und schafft em d Frau als Gägenüber.",
 "SUM-CH-GEN-003": "D Schlange verfüert de Mänsch, er isst vom verbotne Baum; Scham, Schuld und d Vertriibig us em Garte folged, aber Gott sorgt wiiter für d Mänsche.",
 "SUM-CH-MRK-003": "Heilig am Sabbat füert zu Konflikt. De Jesus berüeft di Zwölf, begägnet em Vorwurf, er wirki mit dämonischer Vollmacht, und beschriibt sini Familie vom Tue vom Gotteswile her.",
 "SUM-CH-MAT-006": "De Jesus redt über Almose, Bätte und Faschte: nöd vor de Lüüt, sondern vor Gott. I de Mitti staat s Vatterunser. Nachhär gaat s um Schätz im Himel und drum, sich nöd z sorge, sondern zerscht Gottes Riich z sueche.",
 "SUM-CH-LUK-011": "De Jesus leert bätte: s Vatterunser, es Gliichnis vom bittende Fründ und d Zuesag, dass Gott de Heilig Geischt git. Es folged Striitgspröch über sini Vollmacht und scharfi Wort a Pharisäer und Gsetzesleerer.",
}
SUM_BOOKS = {
 "GEN": "Vom Aafang vo de Wält bis zu de Familie vom Jakob in Ägypte: Schöpfig, Sündefall, Sintfluet, Abraham, Isaak, Jakob und Josef.",
 "EXO": "Israel wird us de Sklaverei in Ägypte befreit, zieht dur s Meer, überchunnt am Sinai d Gebot und baut s Heiligtum.",
 "LEV": "Weisige für Opfer, Prieschter, Reinheit und Feschttag: Wie es Volk vor eme heilige Gott läbt.",
 "NUM": "Israel wird zellt und zieht dur d Wüeschti; Murre, Uflenig und Gottes Fürsorg prääged de Wäg bis vor s verheissene Land.",
 "DEU": "De Mose hält Abschiedsrede: Er erinneret a de Wäg, wiederholt s Gsetz und stellt s Volk vor d Waal zwüsche Säge und Fluech.",
 "JOS": "Under em Josua überquert Israel de Jordan, nimmt s Land ii und teilt s under d Stämm uf.",
 "JDG": "I de Ziit vo de Richter wächsled Abfall, Bedrängnis, Hilferuef und Rettig dur Füerer wie Debora, Gideon und Simson.",
 "RUT": "D Ruth, e Moabiterin, hält zu irer Schwigermueter Noomi und wird dur de Boas zur Urgroossmueter vom David.",
 "1SA": "Vom Samuel über de Saul zum David: Wie Israel en Chünig überchunnt und wie Gott de David erwäält.",
 "2SA": "De David regiert über ganz Israel: Erfolg, Schuld mit de Batseba, Familiestriit und d Verheissig vo eme ewige Chünigshuus.",
 "1KI": "De Salomo baut de Tämpel, s Riich teilt sich, und de Prophet Elija stellt sich gäge de Baalskult.",
 "2KI": "Elischa wirkt, d Chünig vo Israel und Juda fale meischtens ab, s Nordriich und spööter Jerusalem gönd under.",
 "1CH": "Stammtafle und d Gschicht vom David, mit em Blick uf de Tämpel und de Gottesdienscht.",
 "2CH": "Vom Salomo bis zum Exil: d Chünig vo Juda, de Tämpel und d Hoffnig uf d Ruckkeer.",
 "EZR": "Di Ruckkeer us em Exil, de Nöibau vom Tämpel und d Ernöierig vom Volk under em Esra.",
 "NEH": "De Nehemia baut d Muur vo Jerusalem wider uf und ordnet s Läbe vo de Gmeinschaft nach em Gsetz.",
 "EST": "D Ester rettet als Chünigin im Persischriich iris Volk vor em Aaschlag vom Haman; s Purimfescht erinneret dra.",
 "JOB": "De Hiob verlüürt alles, ringt mit sine Fründ und mit Gott um d Frag nach em Leide und überchunnt Antwort us em Sturm.",
 "PSA": "150 Gebät und Lieder: Lob, Chlag, Dank, Vertroue und Wut, für de einzel Mänsch und für s ganze Volk.",
 "PRO": "Sprüch und Leere für es kluegs und grächts Läbe; d Furcht vor Gott isch de Aafang vo de Wiisheit.",
 "ECC": "De Prediger fröögt, was im Läbe bliibt, und findt: Alles isch flüchtig, aber me söll Gottes Gaabe mit Freud aanää.",
 "SNG": "Liebeslieder zwüsche zwei Liebende: Seensucht, Nööchi und Freud a de Liebi.",
 "ISA": "De Jesaja warnt Juda, kündt Gricht und Trooscht aa und redt vom Chnächt vo Gott und vo ere nöie Schöpfig.",
 "JER": "De Jeremia liidet under siner Botschaft: Er kündt de Undergang vo Jerusalem aa und verheisst en nöie Bund.",
 "LAM": "Föif Chlagelieder über s zerstörte Jerusalem: Trauer, Schuldbekänntnis und e Spur vo Hoffnig.",
 "EZK": "De Ezechiel gseet im Exil Visione: Gricht über Jerusalem, Gottes Herrlichkeit, Hoffnig für di dürre Bei und en nöie Tämpel.",
 "DAN": "De Daniel bliibt am Chünigshof tröi; Visione vo Riiche, wo vergönd, und vo Gottes Herrschaft, wo bliibt.",
 "HOS": "De Hosea zeigt mit siner eigene Ehe Gottes Liebi zu eme untröie Volk und rüeft zur Umkeer.",
 "JOL": "Nach ere Heuschreckeplag rüeft de Joel zur Umkeer und verheisst, dass Gott sin Geischt uf alli usgüsst.",
 "AMO": "De Amos klagt Unrächt und falschi Sicherheit aa: Gott wott Rächt und Grächtigkeit, nöd Opfer ohni Härz.",
 "OBA": "De Obadja kündt s Gricht über Edom aa, wil s a Juda nöd gholfe hät.",
 "JON": "De Jona flüchtet vor em Uftrag, landet im Fisch und erläbt, dass Gott au Ninive gnädig isch.",
 "MIC": "De Micha kritisiert d Mächtige und verheisst en Herrscher us Betlehem; Gott verlangt Rächt, Güeti und Demuet.",
 "NAM": "De Nahum kündt de Undergang vo Ninive aa: Gott duldet Gwalt nöd für immer.",
 "HAB": "De Habakuk fröögt, warum Gott s Unrächt zuelaat, und leert: De Grächt läbt us Glaube.",
 "ZEP": "De Zefanja warnt vor em Taag vom Herr und verheisst de Bliibende Freud und Ernöierig.",
 "HAG": "De Haggai ermuetiget s Volk, de Tämpel wider ufzboue.",
 "ZEC": "De Sacharja gseet Nachtvisione und redt vom chünftige Chünig, wo uf eme Esel chunnt.",
 "MAL": "De Maleachi mahnt Prieschter und Volk zur Tröi und verheisst de Bott vor em Taag vom Herr.",
 "MAT": "De Matthäus verzellt vom Jesus im Zämehang mit de Schrifte vo Israel. Sini Leer vom Himelriich, sin Tod und sini Uferstehig füered zum Uftrag, Mänsche us allne Völker zu Jünger z mache.",
 "MRK": "De Markus verzellt chnapp und dirääkt vom Jesus: Heilige, Striitgspröch, de Wäg nach Jerusalem und s Chrüüz. Wär de Jesus isch, zeigt sich für d Läser erscht ganz under em Chrüüz.",
 "LUK": "De Lukas verzellt sorgfältig vom Jesus, wo sich de Arme, de Fraue und de Usgstossne zuewändet; vili Gliichnis und d Freud über Gottes Barmherzigkeit prääged das Evangelium.",
 "JHN": "De Johannes zeigt de Jesus als s Wort vo Gott, wo Mänsch worde isch: Zeiche, Red über Liecht, Läbe und Liebi, und d Stund vo de Verherrlichig am Chrüüz.",
 "ACT": "Vo Pfingschte bis zum Paulus z Rom: Wie de Heilig Geischt d Gmeind verbreitet, mit Petrus, Stephanus, Philippus und Paulus.",
 "ROM": "De Paulus entfaltet s Evangelium: Alli sind schuldig, alli wärded us Glaube grächt gsproche; es nöis Läbe im Geischt, Israel und d Gmeind.",
 "1CO": "De Paulus antwortet uf Striit und Frage i Korinth: Einheit, Sexualität, Götzeopferfleisch, Abigmaal, Geischtesgaabe, Liebi und Uferstehig.",
 "2CO": "De Paulus verteidigt sin Dienscht, redt vo Trooscht im Leide, vo de Kollekte und vo siner Schwachheit, i dere Gottes Chraft wirkt.",
 "GAL": "De Paulus streitet für d Freiheit im Glaube: Nöd s Gsetz, sondern s Vertroue uf Chrischtus macht grächt; de Geischt bringt Frucht.",
 "EPH": "Gottes Plan, alles i Chrischtus z vereine; d Gmeind als Liib vo Chrischtus; es Läbe i Liebi, Familie und geischtlichem Kampf.",
 "PHP": "En Brief voll Freud us em Gfängnis: Chrischtus als Vorbild vo de Demuet, Warnig vor falscher Sicherheit, Dank für d Hilf.",
 "COL": "Chrischtus staat über allem; d Gmeind söll sich nöd vo frömde Leere verwirre laa und es nöis Läbe füere.",
 "1TH": "De Paulus dankt für de Glaube vo de Thessalonicher, ermuetiget zum heilige Läbe und trööschtet wäge de Verstorbne und de Widerkunft.",
 "2TH": "Duurehalte i de Verfolgig, Warnig vor Irrtum über de Taag vom Herr, Mahnig zum ornigliche Läbe.",
 "1TI": "Aawiisige für de Timotheus: Leer bewaare, Gmeindsordnig, Ämter, Umgang mit Riichtum.",
 "2TI": "De letscht Brief vom Paulus: Tröi bliibe, Liide erträge, d Schrift bruuche, de Lauf vollände.",
 "TIT": "Aawiisige für de Titus uf Kreta: Elteschti iisetze, gsundi Leer, guets Läbe us de Gnad.",
 "PHM": "De Paulus bittet de Philemon, de entloffe Sklav Onesimus als Brueder ufznää.",
 "HEB": "Chrischtus isch grösser als Ängel, Mose und Prieschtertum; de nöi Bund; Glaubenszüüge und d Mahnig, duurezhalte.",
 "JAS": "Glaube zeigt sich im Tue: Prüefige, Hööre und Tue, Umgang mit de Zunge, mit Arme und Riiche, Geduld und Gebät.",
 "1PE": "Hoffnig und Duurehalte für bedrängti Chrischte: als Frömdi i de Wält heilig läbe, Liide wie Chrischtus.",
 "2PE": "Warnig vor Irrleerer und Spötter; d Wiederkunft chunnt gwüss, drum heilig läbe und wachse i de Gnad.",
 "1JN": "Gott isch Liecht und Liebi: Im Liecht läbe, d Sünd bekänne, enand liebe, de Glaube a de Jesus als Chrischtus feschthalte.",
 "2JN": "E churze Brief: I de Liebi und i de Waarheit bliibe, Irrleerer nöd ufnää.",
 "3JN": "De Johannes lobt de Gaius für sini Gaschtfründschaft und tadlet de Diotrephes.",
 "JUD": "E scharfi Warnig vor Lüüt, wo d Gnad missbruuched, und d Ermuetigung, im Glaube feschtzhalte.",
 "REV": "Visione vom Johannes uf Patmos: Brief a sibe Gmeinde, Gricht über d Mächt vo de Wält, de Sieg vom Lamm und s nöie Jerusalem.",
}

# ---------------------------------------------------------------- Wortbedeutungen und Erklärungen zu den Lesarten (gsw-Übersetzungen)
ALT_I18N = {
 "VAR-SBLGNTAPP-MAT-006-005-01:R2": {"readings_de": {"R1": [["προσεύχησθε, οὐκ ἔσεσθε ὡς", "ir bätted, ir söled nöd sii wie", "Meerzaal"]], "R2": [["προσεύχῃ οὐκ ἔσῃ ὥσπερ", "du bätisch, du sollsch nöd sii wie", "Einzaal"]]},
   "origin_de": ["D Einzaal chönnt a d Umgäbig aaglichet sii: I 6,2–4 und 6,6 wird jewiils «du» aagredt.", "Umgekeert chönnt d Meerzaal a 6,7–9 aaglichet sii, wo «ir» aagredt wird."]},
 "VAR-SBLGNTAPP-MAT-006-006-01:R2": {"readings_de": {"R1": [["σοι", "dir", "ohni Zuesatz"]], "R2": [["σοι ἐν τῷ φανερῷ", "dir im Offne, öffentlich", "Zuesatz"]]},
   "origin_de": ["De Zuesatz bildet es Gägestuck zu «im Verborgne» und chönnt ergänzt worde sii, zum de Gägesatz z betone; de gliich Zuesatz findt sich i mängne Handschrifte au i 6,4 und 6,18.", "Wär de Zuesatz für ursprünglich haltet, mues erkläre, warum er i de eltischte Handschrifte fäält; dänkbar isch, dass er wäge em Gedanke a en öffentliche Loon bewusst wäggglaa worde isch."]},
 "VAR-SBLGNTAPP-MAT-006-008-01:R2": {"readings_de": {"R1": [["ὁ πατὴρ", "de Vatter", "ohni «Gott»"]], "R2": [["ὁ θεὸς ὁ πατὴρ", "Gott, de Vatter", "mit «Gott»"]]},
   "origin_de": ["«Gott» cha als Verdüütlichig dezuekoo sii, wie si au i de Liturgie üblich isch.", "Umgekeert cha «Gott» bim Abschriibe usgfalle sii, wil zwei Wortgruppe gliich mit «ὁ» aafanged."]},
 "VAR-SBLGNTAPP-MAT-006-012-01:R2": {"readings_de": {"R1": [["ἀφήκαμεν", "mir händ vergää", "Aorist: abgschlosseni Handlig"]], "R2": [["ἀφίεμεν", "mir vergänd", "Gägewart"]], "other": [["ἀφίομεν", "mir vergänd", "Näbeform vo de Gägewart, so au i Lk 11,4"]]},
   "origin_de": ["D Gägewart chönnt a de Lukas (11,4 «mir vergänd») und a s Gebät im Gottesdienscht aaglichet sii.", "D Vergangeheitsform cha e aramäischi Usdruckswiis widergää, wo en Akt meint, wo me grad jetzt vollzieht («hiemit vergänd mir»); dänn isch de Underschid chliiner, als er im Tüütsche ussgseet.", "Wär d Gägewart für ursprünglich haltet, verwiist uf iri Verbreitig i de Meerheit vo de spöötere Handschrifte."]},
 "VAR-SBLGNTAPP-MAT-006-013-01:R2": {"readings_de": {"R1": [["πονηροῦ", "(em) Bööse", "Änd vom Gebät ohni Lobpriis"]], "R2": [["ὅτι σοῦ ἐστιν ἡ βασιλεία καὶ ἡ δύναμις καὶ ἡ δόξα εἰς τοὺς αἰῶνας· ἀμήν", "dänn diin isch s Riich und d Chraft und d Herrlichkeit i Ewigkeit. Amen", "Lobpriis (Doxologie)"]]},
   "origin_de": ["Jüdischi Gebät händ oft mit eme Lobpriis ufghört; es Vorbild isch 1 Chr 29,11. Bim Bätte im Gottesdienscht hät me s Vatterunser wahrschiinli früe mit eme Lobpriis beändet, und dä isch vo dört i vili Handschrifte cho.", "D Didache, e früechrischtlichi Gmeindsordnig (um 100), git s Vatterunser mit em chürzere Schluss «dänn diin isch d Chraft und d Herrlichkeit i Ewigkeit» wider. Das zeigt, dass en Lobpriis seer früe bättet worde isch, aber i verschidene Forme.", "Wär de Lobpriis für ursprünglich haltet, verwiist uf sini Verbreitig i de groosse Meerheit vo de Handschrifte und im chilchliche Bruuch."]},
 "VAR-SBLGNTAPP-MAT-006-015-01:R2": {"readings_de": {"R1": [["ἀνθρώποις", "de Lüüt", "ohni Zuesatz"]], "R2": [["ἀνθρώποις τὰ παραπτώματα αὐτῶν", "de Lüüt iri Fääler", "Zuesatz wie i 6,14"]]},
   "origin_de": ["De Zuesatz cha us 6,14 übernaa sii, zum die zwei Sätz gliich z gstalte.", "Gnau so cha er bim Abschriibe usgfalle sii; d Usgabe sind da teilt."]},
 "VAR-SBLGNTAPP-LUK-011-002-01:R2": {"readings_de": {"R1": [["Πάτερ", "Vatter", "churzi Aared"]], "R2": [["Πάτερ ἡμῶν ὁ ἐν τοῖς οὐρανοῖς", "Öise Vatter i de Himel", "Aared wie bim Matthäus"]]},
   "origin_de": ["Wär s Vatterunser i de Matthäusfassig uswändig kännt und im Gottesdienscht bättet hät, hät bim Abschriibe di chürzer Lukasfassig liecht dra aaglichet. Vili Textforscher erkläred di längeri Aared bim Lukas so.", "Di chürzer Aared entspricht au em aramäische «Abba», mit däm de Jesus Gott nach Mk 14,36 aaredt."]},
 "VAR-SBLGNTAPP-LUK-011-002-02:R2": {"readings_de": {"R1": [["σου", "diis (Riich)", "ohni wiiteri Bitt"]], "R2": [["γενηθήτω τὸ θέλημά σου ὡς ἐν οὐρανῷ καὶ ἐπὶ τῆς γῆς", "diin Wile söll gschee, wie im Himel, eso uf de Ärde", "Bitt wie bim Matthäus"]]},
   "origin_de": ["Au da isch e Aagliichig a di vertrouti Matthäusfassig di hüüfigscht Erkläärig.", "Es paar wenigi spööteri Handschrifte und Chilevätter (brichtet für d Minuskle 700 und 162 und für de Gregor vo Nyssa) händ a dere Stell stattdesse e Bitt um de Heilig Geischt: «Diin Heilige Geischt söll über üs choo und üs reinige.» Die Aagab isch da nöd prüeft; si zeigt, wie frei s Gebät i mängne Chreis wiitergää worde isch."]},
 "VAR-SBLGNTAPP-LUK-011-004-01:R2": {"readings_de": {"R1": [["πειρασμόν", "Versuechig", "Änd vom Gebät"]], "R2": [["ἀλλὰ ῥῦσαι ἡμᾶς ἀπὸ τοῦ πονηροῦ", "sondern rett üs vor em Bööse", "Bitt wie bim Matthäus"]]},
   "origin_de": ["Au dä Zuesatz laat sich als Aagliichig a de Matthäus erkläre.", "Wär en für ursprünglich haltet, verwiist uf sini wiiti Verbreitig; dass er grad im 𝔓75, im Sinaiticus und im Vaticanus fäält, redt nach Aasicht vo vilne Textforscher eher für e spööteri Ergänzig."]},
 "VAR-SBLGNTAPP-MRK-003-020-01:R2": {"readings_de": {"R1": [["ἔρχεται", "er chunnt", "Einzaal, Gägewart"]], "R2": [["ἔρχονται", "si chömed", "Meerzaal, Gägewart"]]},
   "origin_de": ["D Meerzaal chönnt entstande sii, wil churz vorhär di zwölf Jünger ufzellt wärded (3,13–19): En Schriiber hät a de Jesus mit sine Jünger dänkt.", "Umgekeert chönnt d Einzaal e Vereifachig sii, wo de Jesus als Hauptperson i d Mitti stellt.", "Im gliiche Värs staat nachhär sowiso «si» i de Meerzaal («so dass si nöd emal händ chöne Broot ässe»); de Underschid betrifft nu, wär usdrückli is Huus chunnt."]},
 "VAR-SBLGNTAPP-MRK-003-025-01:R2": {"readings_de": {"R1": [["δυνήσεται", "wird chöne", "Zuekunft"]], "R2": [["δύναται", "cha", "Gägewart"]]},
   "origin_de": ["I 3,24 und 3,26 staat jewiils «cha» i de Gägewart. Schriiber chönnted 3,25 dra aaglichet haa.", "Gnau so dänkbar isch, dass d Zuekunftsform e stilistischi Abwächslig isch, wo spööter glättet worde isch, oder umgekeert."]},
 "VAR-SBLGNTAPP-MRK-003-026-01:R2": {"readings_de": {"R1": [["ἐμερίσθη", "isch gspalte worde", "Aorist: abgschlossnes Ereignis"]], "R2": [["μεμέρισται", "isch gspalte", "Perfekt: aaduurende Zuestand"]]},
   "origin_de": ["D Parallelstell Mt 12,26 hät «isch gspalte worde» (ἐμερίσθη). Die Form chönnt drum us em Matthäus übernaa sii.", "Umgekeert chönnt «isch gspalte» e sprachlichi Glättig sii, wil de Zuestand im Satz wichtiger isch als s Ereignis.", "Für de Sinn macht de Underschid wenig us."]},
 "VAR-SBLGNTAPP-MRK-003-029-01:R2": {"readings_de": {"R1": [["ἁμαρτήματος", "ere Verfäälig, Sünd", "ἁμάρτημα: einzelni Tat; im Nöie Teschtamänt sälte (im kritische Text nu Mk 3,28–29; Röm 3,25; 1 Kor 6,18; im byzantinische Text au Mk 4,12)"]], "R2": [["κρίσεως", "eme Gricht, Urteil", "κρίσις: Gricht, Entscheidig"]], "VAR-MRK-003-029-001:R3": [["ἁμαρτίας", "ere Sünd", "ἁμαρτία: s gläufige Wort für Sünd"]]},
   "origin_de": ["Vili Textforscher halted s sälte «ewigi Sünd» (ἁμαρτήματος) für ursprünglich: Schriiber händ de ungwöhnlich Usdruck eher dur s gläufigere Wort (ἁμαρτίας) oder dur di liecht verständlich Vorstellig vo eme ewige Gricht (κρίσεως) ersetzt als umgekeert.", "Wär em Text vo de Meerheit vo de spöötere Handschrifte de Vorzug git, haltet «ewigs Gricht» für ursprünglich; die Läsart isch i vilne byzantinische Handschrifte verbreitet.", "Di dritt Form «ewigi Sünd» mit em hüüfige Wort ἁμαρτία staat i meerere alte Handschrifte und liit sprachlich zwüsche de beide andere."]},
 "VAR-MRK-003-029-002:R2": {"readings_de": {"R1": [["ἐστιν", "isch", "Gägewart"]], "R2": [["ἔσται", "wird sii", "Zuekunft"]]},
   "origin_de": ["D Zuekunftsform chönnt a s vorusgaande «hät i Ewigkeit kei Vergäbig» und a de Gedanke a es chünftigs Gricht aagleent sii.", "Gnau so chönnt d Gägewart e Aagliichig a de übliche Sprachgebruuch sii. Beidi Forme stönd i seer alte Handschrifte."]},
 "VAR-SBLGNTAPP-MRK-003-032-03:R2": {"readings_de": {"R1": [["σου", "ohni Zuesatz", "De Satz hört mit «dini Brüeder» uf."]], "R2": [["καὶ αἱ ἀδελφαί σου", "und dini Schwöschtere", "Zuesatz"]]},
   "origin_de": ["En Schriiber cha d Schwöschtere us 3,35 («Brueder, Schwöschter und Mueter») da ergänzt haa.", "Umgekeert chönd si us Versee usgfalle sii: Beidi Wortgruppe höred uf «σου» (dini) uf. Springt s Aug vom erschte zum zweite «σου», fallt «und dini Schwöschtere» wägg; das passiert bim Abschriibe hüüfig.", "Au e bewussti Aagliichig a 3,31 und 3,34 und a de Matthäus und de Lukas, wo da kei Schwöschtere nänned, isch dänkbar."]},
}


# Wortbedeutungen (terms) der Deutungen, Reihenfolge wie im Original
for _rid, _terms in {'INT-LP-0001': ['meischtens «täglich»', 'de folgendi Tag', 'morn'], 'INT-LP-0002': ['meischtens «täglich»', 'Daasii, Läbesunderhalt'], 'INT-LP-0003': ['meischtens «täglich»', 'überwäsentlich'], 'INT-LP-0004': ['Versuechig, Prüefig', 'inebringe'], 'INT-LP-0005': ['vergää, erlaa', 'Schuld'], 'INT-LP-0006': ['bööse; de Bööse']}.items():
    I18N[_rid]["terms"] = _terms

import hashlib

OUT = D / "localizations" / LANG


def fingerprint(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()[:16]


def patch(path, fields):
    rec = json.loads(path.read_text(encoding="utf-8"))
    rid = rec["id"]
    out = OUT / f"{rid}.json"
    prev = json.loads(out.read_text(encoding="utf-8")) if out.exists() else None
    loc = {"id": "L10N-GSW-ZH-" + rid, "type": "localization", "status": "draft", "tags": [],
           "localizes": rid, "language": LANG, "target_context": "CTX-CH-ZH-GSW-2026",
           "fields": fields, "source_fingerprint": {k: fingerprint(rec.get(k)) for k in fields},
           "authorship_de": AUTH, "review_de": "Noch keine muttersprachliche Prüfung dokumentiert.",
           "knowledge": {"asserted_at": DATE, "supersedes": None},
           "revision_log": (prev or {}).get("revision_log") or [{"date": DATE, "change_de": "Erstfassung Züridüütsch",
                                                                  "reason_de": "Mundart-Schicht soll alle Inhalte umfassen"}]}
    if prev and (prev["fields"] != fields or prev["source_fingerprint"] != loc["source_fingerprint"]):
        loc["revision_log"] = prev["revision_log"] + [{"date": DATE, "change_de": "Fassung erneuert", "previous_fields": prev["fields"],
                                                       "previous_fingerprint": prev["source_fingerprint"]}]
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(loc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


n = 0
for rid, fields in I18N.items():
    hits = [h for h in D.rglob(f"{rid}.json") if "localizations" not in h.parts]
    assert len(hits) == 1, rid
    rec = json.loads(hits[0].read_text(encoding="utf-8"))
    for k, v in fields.items():
        if k == "terms":
            assert len(v) == len(rec.get("terms", [])), (rid, "terms")
        else:
            assert k in rec, (rid, k)
            assert type(v) is type(rec[k]), (rid, k)
            if isinstance(v, list):
                assert len(v) == len(rec[k]), (rid, k)
    patch(hits[0], fields); n += 1
for sid, text in {**SUM, **SUM_GROUPS, **SUM_CH, **{f"SUM-BOOK-{c}": t for c, t in SUM_BOOKS.items()}}.items():
    p = D / "summaries" / f"{sid}.json"
    assert p.exists(), sid
    patch(p, {"text_de": text}); n += 1
missing = sorted(p.stem for p in (D / "summaries").glob("*.json") if not (OUT / p.name).exists())
assert not missing, missing
# Lesarten: Wortbedeutungen/Erklärungen in die gsw-Übersetzungen
for p in (D / "translations").glob("TRANS-*-GSW-ZH-WORKING.json"):
    rec = json.loads(p.read_text(encoding="utf-8"))
    for a in rec.get("alternatives", []):
        x = ALT_I18N.get(a["reading"])
        assert x, a["reading"]
        a["readings_de"] = {k: [{"grc": g, "de": de, "note_de": nt} for g, de, nt in v] for k, v in x["readings_de"].items()}
        a["origin_de"] = x["origin_de"]
        if a["reading"] == "VAR-SBLGNTAPP-MRK-003-029-01:R2":
            a["related_variants"] = ["VAR-MRK-003-029-001"]
    log = rec.setdefault("revision_log", [])
    if not any("Wortbedeutungen und Entstehung" in x.get("change_de", "") for x in log):
        log.append({"date": DATE, "change_de": "Wortbedeutungen und Entstehung der Lesarten in Züridüütsch ergänzt (readings_de, origin_de); Übersetzungstext unverändert",
                    "reason_de": "Mundart-Schicht soll alle Inhalte umfassen"})
    rec["alternatives_origin_note_de"] = "Möglichi Erkläärige, wie d Underschid entstande sii chönnted. Si stönd näbenand; keini isch als richtig entschide. " + AUTH
    p.write_text(json.dumps(rec, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"); n += 1
print(f"PASS: {n} Datensätze mit Züridüütsch-Inhalten ergänzt")
