"""Weiterdenken zu Rut (Entscheid Andi Neck 2026-10-28): Fragen zum Weiterdenken und «Wie man es gelesen hat» für alle
Abschnitte, Kapitel und das Buch. KI-Entwürfe ohne fachliche Prüfung; Quellen in frei zugänglichen Ausgaben nachgeschlagen
(source_check), soweit möglich.

Prüfvermerk (PROC-WEITERDENKEN@1.0, Schritte 3 und 4): Am 2026-10-29 von einer weiteren Instanz (getrennte KI-Prüfung,
Claude) gegen die hochdeutsche Arbeitsübersetzung geprüft: alle 34 Fragen und Hintergrundsätze (offen, nicht suggestiv,
am Text belegt, Zitate per Skript wörtlich verglichen, Stellenmarken), Mundart nach pruefe_mundart; Kernaussagen (gist_de)
der Kernanalysen gegen den Text;
Quellen von 2 der 7 Einträge «Wie man es gelesen hat» erneut
nachgeschlagen (Vermerk im source_check). Grenzen: nicht gegen den Urtext geprüft; Zitate aus Büchern ohne
Arbeitsübersetzung nicht verglichen; Mundart-Zitate nicht an die Mundart-Übersetzungsschicht angeglichen; keine fachliche
und keine muttersprachliche Prüfung durch eine Person."""
DATE = "2026-10-28"
PROCESS = "PROC-WEITERDENKEN@1.0"
TAGS = ["TAG-RUTH"]
AUTHORSHIP_DE = "KI-Entwurf (Claude) vom 2026-10-28 (Weiterdenken Rut, Entscheid Andi Neck); keine fachliche Prüfung."
METHOD = "KI-Prüfung (Claude): Angaben mit Websuche in frei zugänglichen Ausgaben bzw. Darstellungen nachgeschlagen; keine fachliche Prüfung."

REFLECTIONS = [
    # Buch
    {"id": "REFL-RUT-0001", "subject": "SUM-BOOK-RUT", "order": 1,
     "question_de": "Wer ist die Hauptperson dieses Buches – Rut, Noomi oder Boas?",
     "note_de": "Das Buch trägt Ruts Namen, beginnt und endet aber bei Noomi: «Ein Sohn ist Noomi geboren!» ([[RUT.4.17]]).",
     "gsw": {"question_de": "Wär isch d Hauptperson vo dem Buech – d Rut, d Noomi oder de Boas?",
             "note_de": "S Buech treit de Name vo de Rut, fangt aber bi de Noomi aa und hört bi ire uf: «D Noomi hät en Sohn übercho!» ([[RUT.4.17]])."}},
    {"id": "REFL-RUT-0002", "subject": "SUM-BOOK-RUT", "order": 2,
     "question_de": "Was bedeutet es, dass eine Moabiterin zu den Vorfahren Davids gehört?",
     "note_de": "Das Buch nennt Rut immer wieder «die Moabiterin» ([[RUT.2.2]]; [[RUT.4.10]]) und endet mit dem Stammbaum bis zu David ([[RUT.4.22]]).",
     "gsw": {"question_de": "Was bedüütet s, dass e Moabiterin zu de Vorfahre vom David ghört?",
             "note_de": "S Buech nännt d Rut immer wider «d Moabiterin» ([[RUT.2.2]]; [[RUT.4.10]]) und hört mit em Stammbaum bis zum David uf ([[RUT.4.22]])."}},
    {"id": "REFL-RUT-0003", "subject": "SUM-BOOK-RUT", "order": 3,
     "question_de": "Wo handelt in diesem Buch Gott – und wo handeln Menschen?",
     "note_de": "Ausdrücklich handelt JHWH nur zweimal: Er gibt dem Volk Brot und lässt Rut schwanger werden ([[RUT.1.6]]; [[RUT.4.13]]); sonst wird viel gesegnet.",
     "gsw": {"question_de": "Wo handlet i dem Buech Gott – und wo handled Mänsche?",
             "note_de": "Usdrücklich handlet JHWH nu zwei Mal: Er git em Volk Brot und laat d Rut schwanger wärde ([[RUT.1.6]]; [[RUT.4.13]]); susch wird vil gsägnet."}},
    # Kapitel
    {"id": "REFL-RUT-0004", "subject": "SUM-CH-RUT-001", "order": 1,
     "question_de": "Voll weggegangen, leer zurückgekommen – stimmt das, was Noomi sagt?",
     "note_de": "Noomi sagt: «Leer hat mich JHWH zurückgebracht» ([[RUT.1.21]]), während Rut neben ihr steht ([[RUT.1.22]]).",
     "gsw": {"question_de": "Voll wäggange, läär zruggchoo – stimmt das, was d Noomi seit?",
             "note_de": "D Noomi seit: «Läär hät mich JHWH zruggbracht» ([[RUT.1.21]]), und dänebe staat d Rut ([[RUT.1.22]])."}},
    {"id": "REFL-RUT-0005", "subject": "SUM-CH-RUT-002", "order": 1,
     "question_de": "Ist es Zufall, dass Rut auf das Feld des Boas kommt?",
     "note_de": "Der Erzähler sagt: «Es traf sich zufällig» ([[RUT.2.3]]) – und lässt Boas «gerade da» kommen ([[RUT.2.4]]).",
     "gsw": {"question_de": "Isch es Zuefall, dass d Rut uf s Fäld vom Boas chunnt?",
             "note_de": "De Erzähler seit: «Es hät sich zuefällig so gää» ([[RUT.2.3]]) – und laat de Boas «grad da» choo ([[RUT.2.4]])."}},
    {"id": "REFL-RUT-0006", "subject": "SUM-CH-RUT-003", "order": 1,
     "question_de": "Was riskiert Rut in dieser Nacht – und was riskiert Boas?",
     "note_de": "Boas sagt am Morgen: «Es darf nicht bekannt werden, dass die Frau zur Tenne gekommen ist» ([[RUT.3.14]]).",
     "gsw": {"question_de": "Was riskiert d Rut i dere Nacht – und was riskiert de Boas?",
             "note_de": "De Boas seit am Morge: «Es dörf nöd uschoo, dass d Frau uf d Tänn cho isch» ([[RUT.3.14]])."}},
    {"id": "REFL-RUT-0007", "subject": "SUM-CH-RUT-004", "order": 1,
     "question_de": "Warum bleibt der nähere Löser namenlos?",
     "note_de": "Boas spricht ihn nur mit «du Soundso» an ([[RUT.4.1]]); er verzichtet, um sein eigenes Erbteil nicht zu schädigen ([[RUT.4.6]]).",
     "gsw": {"question_de": "Wieso bliibt de nööcher Löser ohni Name?",
             "note_de": "De Boas redt en nu mit «du Soundso» aa ([[RUT.4.1]]); er verzichtet, damit er sis eiget Erbteil nöd schädiget ([[RUT.4.6]])."}},
    # 1,1–5
    {"id": "REFL-RUT-0008", "subject": "TU-RUT-001-001-005", "order": 1,
     "question_de": "Wie lebt es sich als Fremde in einem anderen Land?",
     "note_de": "Die Familie zieht wegen einer Hungersnot nach Moab, «um im Gebiet von Moab als Fremder zu wohnen» ([[RUT.1.1]]).",
     "gsw": {"question_de": "Wie läbt mer als Frömdi in eme andere Land?",
             "note_de": "D Familie zieht wäg ere Hungersnot uf Moab, «zum im Gebiet vo Moab als Frömde z wone» ([[RUT.1.1]])."}},
    {"id": "REFL-RUT-0009", "subject": "TU-RUT-001-001-005", "order": 2,
     "question_de": "Was bleibt einer Frau, die ohne Mann und ohne Kinder zurückbleibt?",
     "note_de": "Zweimal heisst es, Noomi «blieb zurück» ([[RUT.1.3]]; [[RUT.1.5]]).",
     "gsw": {"question_de": "Was bliibt ere Frau, wo ohni Maa und ohni Chind zrugg bliibt?",
             "note_de": "Zwei Mal heisst s, d Noomi «isch … zruggplibe» ([[RUT.1.3]]; [[RUT.1.5]])."}},
    # 1,6–18
    {"id": "REFL-RUT-0010", "subject": "TU-RUT-001-006-018", "order": 1,
     "question_de": "Orpa geht zurück, Rut bleibt – hat eine von beiden falsch gehandelt?",
     "note_de": "Noomi drängt beide zur Umkehr ([[RUT.1.8]]; [[RUT.1.11-RUT.1.12]]), zuletzt Rut allein ([[RUT.1.15]]); der Text tadelt Orpa nicht.",
     "gsw": {"question_de": "D Orpa gaat zrugg, d Rut bliibt – hät eini vo beide falsch ghandlet?",
             "note_de": "D Noomi drängt beidi zum Umchere ([[RUT.1.8]]; [[RUT.1.11-RUT.1.12]]), zletscht d Rut elei ([[RUT.1.15]]); de Text tadlet d Orpa nöd."}},
    {"id": "REFL-RUT-0011", "subject": "TU-RUT-001-006-018", "order": 2,
     "question_de": "Was gibt Rut alles auf mit ihrem Satz «Dein Volk ist mein Volk, und dein Gott ist mein Gott»?",
     "note_de": "Rut verbindet in ihrem Schwur Weg, Wohnort, Volk, Gott und Grab ([[RUT.1.16-RUT.1.17]]).",
     "gsw": {"question_de": "Was git d Rut alles uf mit irem Satz «Dis Volk isch mis Volk, und din Gott isch min Gott»?",
             "note_de": "D Rut verbindet i irem Schwur Wäg, Wonort, Volk, Gott und Grab ([[RUT.1.16-RUT.1.17]])."}},
    {"id": "REFL-RUT-0012", "subject": "TU-RUT-001-006-018", "order": 3,
     "question_de": "Warum drängt Noomi die beiden so hartnäckig zur Umkehr?",
     "note_de": "Noomi sagt: «Die Hand JHWHs hat sich gegen mich gewendet» ([[RUT.1.13]]).",
     "gsw": {"question_de": "Wieso drängt d Noomi die beide so hartnäckig zum Umchere?",
             "note_de": "D Noomi seit: «D Hand vo JHWH hät sich gäge mich gwändet» ([[RUT.1.13]])."}},
    # 1,19–22
    {"id": "REFL-RUT-0013", "subject": "TU-RUT-001-019-022", "order": 1,
     "question_de": "Darf man so offen gegen Gott klagen wie Noomi?",
     "note_de": "Noomi sagt vor den Frauen der Stadt, der Allmächtige habe ihr Böses angetan ([[RUT.1.20-RUT.1.21]]); der Erzähler widerspricht ihr nicht.",
     "gsw": {"question_de": "Dörf mer so offe gäge Gott chlage wie d Noomi?",
             "note_de": "D Noomi seit vor de Fraue vo de Stadt, de Allmächtig heb ire Böses aatue ([[RUT.1.20-RUT.1.21]]); de Erzähler widerspricht ire nöd."}},
    {"id": "REFL-RUT-0014", "subject": "TU-RUT-001-019-022", "order": 2,
     "question_de": "Was sagt der letzte Satz des Kapitels nach Noomis Klage?",
     "note_de": "Sie kommen «zu Beginn der Gerstenernte» nach Betlehem ([[RUT.1.22]]).",
     "gsw": {"question_de": "Was seit de letscht Satz vom Kapitel nach de Chlag vo de Noomi?",
             "note_de": "Si chömed «am Aafang vo de Gerschteernt» uf Betlehem ([[RUT.1.22]])."}},
    # 2,1–3
    {"id": "REFL-RUT-0015", "subject": "TU-RUT-002-001-003", "order": 1,
     "question_de": "Warum ergreift Rut hier selbst die Initiative?",
     "note_de": "Rut schlägt Noomi vor, Ähren aufzulesen «hinter dem, in dessen Augen ich Gunst finde» ([[RUT.2.2]]).",
     "gsw": {"question_de": "Wieso ergrifft d Rut da sälber d Initiative?",
             "note_de": "D Rut schlaat de Noomi vor, Ähre ufzläse «hinder dem här, bi dem ich Gnad find» ([[RUT.2.2]])."}},
    {"id": "REFL-RUT-0016", "subject": "TU-RUT-002-001-003", "order": 2,
     "question_de": "Was weiss der Leser über Boas, das Rut noch nicht weiss?",
     "note_de": "Schon im ersten Vers des Kapitels erfährt der Leser, dass Boas mit Elimelech verwandt ist ([[RUT.2.1]]).",
     "gsw": {"question_de": "Was weiss de Läser über de Boas, wo d Rut no nöd weiss?",
             "note_de": "Scho im erschte Vers vom Kapitel erfahrt de Läser, dass de Boas mit em Elimelech verwandt isch ([[RUT.2.1]])."}},
    # 2,4–17
    {"id": "REFL-RUT-0017", "subject": "TU-RUT-002-004-017", "order": 1,
     "question_de": "Warum beachtet Boas die Fremde?",
     "note_de": "Rut fragt genau das ([[RUT.2.10]]), und Boas antwortet mit dem, was man ihm über ihre Treue zu Noomi berichtet hat ([[RUT.2.11]]).",
     "gsw": {"question_de": "Wieso beachtet de Boas di Frömd?",
             "note_de": "D Rut fröget genau das ([[RUT.2.10]]), und de Boas antwortet mit dem, was mer ihm über iri Treui zur Noomi verzellt hät ([[RUT.2.11]])."}},
    {"id": "REFL-RUT-0018", "subject": "TU-RUT-002-004-017", "order": 2,
     "question_de": "Boas wünscht, dass JHWH Rut belohnt – und tut dann selbst etwas. Wie hängt beides zusammen?",
     "note_de": "Er wünscht ihr Lohn von JHWH, zu dem sie gekommen ist, «um unter seinen Flügeln Zuflucht zu suchen» ([[RUT.2.12]]), und lässt für sie Ähren aus den Bündeln ziehen ([[RUT.2.16]]).",
     "gsw": {"question_de": "De Boas wünscht, dass JHWH d Rut belohnt – und tuet dänn sälber öppis. Wie hanget beides zäme?",
             "note_de": "Er wünscht ire Lohn vo JHWH, zu dem si choo isch, «zum under sine Flügel Schutz z sueche» ([[RUT.2.12]]), und laat für si Ähre us de Büschel zie ([[RUT.2.16]])."}},
    {"id": "REFL-RUT-0019", "subject": "TU-RUT-002-004-017", "order": 3,
     "question_de": "Wovor muss Boas eine junge fremde Frau auf dem Feld schützen?",
     "note_de": "Boas hat den Knechten geboten, sie nicht anzurühren, und sagt: «Beschämt sie nicht» ([[RUT.2.9]]; [[RUT.2.15]]).",
     "gsw": {"question_de": "Vor was mues de Boas e jungi frömdi Frau uf em Fäld schütze?",
             "note_de": "De Boas hät de Chnächt befole, si nöd aazrüere, und seit: «beschämed si nöd» ([[RUT.2.9]]; [[RUT.2.15]])."}},
    # 2,18–23
    {"id": "REFL-RUT-0020", "subject": "TU-RUT-002-018-023", "order": 1,
     "question_de": "Was verändert sich bei Noomi, als sie den Namen Boas hört?",
     "note_de": "Die Frau, die «Mara» heissen wollte ([[RUT.1.20]]), sagt nun über Boas: «Gesegnet sei er von JHWH, der seine Treue den Lebenden und den Toten nicht entzogen hat!» ([[RUT.2.20]]).",
     "gsw": {"question_de": "Was veränderet sich bi de Noomi, wo si de Name Boas ghört?",
             "note_de": "D Frau, wo «Mara» hät wele heisse ([[RUT.1.20]]), seit jetzt über de Boas: «Gsägnet sig er vo JHWH, wo sini Tröii de Läbige und de Toote nöd entzoge hät!» ([[RUT.2.20]])."}},
    {"id": "REFL-RUT-0021", "subject": "TU-RUT-002-018-023", "order": 2,
     "question_de": "Was ist ein Löser – und wer kann heute für andere einstehen?",
     "note_de": "Noomi sagt von Boas: «Er ist einer von unseren Lösern» ([[RUT.2.20]]); was das heisst, zeigt erst Kapitel 4.",
     "gsw": {"question_de": "Was isch en Löser – und wär chan hüt für anderi iistaa?",
             "note_de": "D Noomi seit vom Boas: «Er isch eine vo öisne Löser» ([[RUT.2.20]]); was das heisst, zeigt erscht s Kapitel 4."}},
    # 3,1–5
    {"id": "REFL-RUT-0022", "subject": "TU-RUT-003-001-005", "order": 1,
     "question_de": "Noomi wollte Rut zuerst wegschicken, jetzt sucht sie ihr einen Ort der Ruhe. Was hat sich verändert?",
     "note_de": "Im ersten Kapitel wünschte Noomi den Schwiegertöchtern Ruhe im Haus eines Mannes in Moab ([[RUT.1.9]]); jetzt will sie selbst sie suchen ([[RUT.3.1]]).",
     "gsw": {"question_de": "D Noomi hät d Rut zerscht wele wägschicke, jetzt suecht si ire en Ort zum Rue finde. Was hät sich veränderet?",
             "note_de": "Im erschte Kapitel hät d Noomi de Schwigertöchtere Rue im Huus vo me Maa z Moab gwünscht ([[RUT.1.9]]); jetzt wott si sälber eini sueche ([[RUT.3.1]])."}},
    {"id": "REFL-RUT-0023", "subject": "TU-RUT-003-001-005", "order": 2,
     "question_de": "Warum sagt Rut zu diesem gewagten Plan ohne Widerspruch Ja?",
     "note_de": "Rut antwortet: «Alles, was du mir sagst, werde ich tun» ([[RUT.3.5]]).",
     "gsw": {"question_de": "Wieso seit d Rut zu dem gwagte Plan ohni Widerred Ja?",
             "note_de": "D Rut antwortet: «Alles, wo du mir seisch, mach ich» ([[RUT.3.5]])."}},
    # 3,6–15
    {"id": "REFL-RUT-0024", "subject": "TU-RUT-003-006-015", "order": 1,
     "question_de": "Rut sollte warten, bis Boas ihr sagt, was sie tun soll – stattdessen sagt sie es ihm. Warum?",
     "note_de": "Noomi hatte gesagt: «Er wird dir sagen, was du tun sollst» ([[RUT.3.4]]); Rut aber bittet: «Breite den Zipfel deines Gewandes über deine Dienerin aus» ([[RUT.3.9]]).",
     "gsw": {"question_de": "D Rut hett söle warte, bis de Boas ire seit, was si söll mache – statt dem seit si s ihm. Wieso?",
             "note_de": "D Noomi hät gseit: «Er wird dir säge, was du mache söllsch» ([[RUT.3.4]]); d Rut aber bittet: «So spreit de Zipfel vo dim Gwand über dini Dieneri uus» ([[RUT.3.9]])."}},
    {"id": "REFL-RUT-0025", "subject": "TU-RUT-003-006-015", "order": 2,
     "question_de": "Warum überlässt Boas dem näheren Löser den Vortritt, statt einfach zuzugreifen?",
     "note_de": "Boas schwört, Rut zu lösen, falls der nähere Löser nicht will ([[RUT.3.12-RUT.3.13]]).",
     "gsw": {"question_de": "Wieso laat de Boas em nööchere Löser de Vortritt, statt eifach zuezgriife?",
             "note_de": "De Boas schwört, er lös d Rut, wänn de nööcher Löser nöd wott ([[RUT.3.12-RUT.3.13]])."}},
    # 3,16–18
    {"id": "REFL-RUT-0026", "subject": "TU-RUT-003-016-018", "order": 1,
     "question_de": "«Komm nicht mit leeren Händen» – was bedeutet dieses Wort für Noomi?",
     "note_de": "Boas sagt es mit Blick auf die Schwiegermutter ([[RUT.3.17]]), die gesagt hatte, JHWH habe sie leer zurückgebracht ([[RUT.1.21]]).",
     "gsw": {"question_de": "«Chumm nöd mit lääre Händ» – was bedüütet das Wort für d Noomi?",
             "note_de": "De Boas seit s mit Blick uf d Schwigermueter ([[RUT.3.17]]), wo gseit hät, JHWH heb si läär zruggbracht ([[RUT.1.21]])."}},
    {"id": "REFL-RUT-0027", "subject": "TU-RUT-003-016-018", "order": 2,
     "question_de": "Wie fühlt sich das Warten an, wenn andere über die eigene Zukunft entscheiden?",
     "note_de": "Noomi sagt zu Rut: «Bleib sitzen, meine Tochter, bis du weisst, wie die Sache ausgeht» ([[RUT.3.18]]).",
     "gsw": {"question_de": "Wie fühlt sich s Warte aa, wänn anderi über di eiget Zuekunft entscheided?",
             "note_de": "D Noomi seit zur Rut: «Bliib sitze, mini Tochter, bis du weisch, wie d Sach usgaat» ([[RUT.3.18]])."}},
    # 4,1–12
    {"id": "REFL-RUT-0028", "subject": "TU-RUT-004-001-012", "order": 1,
     "question_de": "Rut ist bei der Verhandlung im Tor nicht dabei. Was bedeutet das?",
     "note_de": "Im Tor sitzen Boas, der Löser und zehn Älteste ([[RUT.4.1-RUT.4.2]]); über Rut wird gesprochen, sie selbst spricht nicht.",
     "gsw": {"question_de": "D Rut isch bi de Verhandlig im Tor nöd debii. Was bedüütet das?",
             "note_de": "Im Tor hocked de Boas, de Löser und zää Eltischti ([[RUT.4.1-RUT.4.2]]); über d Rut wird gredt, si sälber redt nöd."}},
    {"id": "REFL-RUT-0029", "subject": "TU-RUT-004-001-012", "order": 2,
     "question_de": "Warum ist es so wichtig, dass der Name eines Verstorbenen bleibt?",
     "note_de": "Boas sagt zweimal, er handle, «um den Namen des Verstorbenen auf seinem Erbteil aufrechtzuerhalten» ([[RUT.4.5]]; [[RUT.4.10]]).",
     "gsw": {"question_de": "Wieso isch es so wichtig, dass de Name vo me Verstorbne bliibt?",
             "note_de": "De Boas seit zwei Mal, er handli, «zum de Name vom Verstorbne uf sim Erbteil z erhalte» ([[RUT.4.5]]; [[RUT.4.10]])."}},
    {"id": "REFL-RUT-0030", "subject": "TU-RUT-004-001-012", "order": 3,
     "question_de": "Warum erinnert der Segen der Zeugen an Rahel, Lea und Tamar?",
     "note_de": "Die Leute im Tor wünschen, Rut werde wie Rahel und Lea, und das Haus des Boas wie das des Perez, den Tamar gebar ([[RUT.4.11-RUT.4.12]]).",
     "gsw": {"question_de": "Wieso erinneret de Sägä vo de Zügä a d Rahel, d Lea und d Tamar?",
             "note_de": "D Lüüt im Tor wünsched, d Rut wärdi wie d Rahel und d Lea, und s Huus vom Boas wie das vom Perez, wo d Tamar gebore hät ([[RUT.4.11-RUT.4.12]])."}},
    # 4,13–17
    {"id": "REFL-RUT-0031", "subject": "TU-RUT-004-013-017", "order": 1,
     "question_de": "Wer ist hier der Löser – Boas oder das Kind?",
     "note_de": "Die Frauen preisen JHWH, der Noomi «heute nicht an einem Löser hat fehlen lassen», und meinen das Neugeborene ([[RUT.4.14-RUT.4.15]]).",
     "gsw": {"question_de": "Wär isch da de Löser – de Boas oder s Chind?",
             "note_de": "D Fraue lobed JHWH, «wo dich hüt nöd ohni Löser glaa hät», und meined s Neugeborne ([[RUT.4.14-RUT.4.15]])."}},
    {"id": "REFL-RUT-0032", "subject": "TU-RUT-004-013-017", "order": 2,
     "question_de": "Was heisst es, dass eine Schwiegertochter für Noomi «besser ist als sieben Söhne»?",
     "note_de": "So reden die Frauen von Betlehem über Rut ([[RUT.4.15]]) – über die Fremde, mit der Noomi zurückgekommen war.",
     "gsw": {"question_de": "Was heisst es, dass e Schwigertochter für d Noomi «besser isch als sibe Söön»?",
             "note_de": "So redet d Fraue vo Betlehem über d Rut ([[RUT.4.15]]) – über di Frömd, wo mit de Noomi zruggchoo isch."}},
    # 4,18–22
    {"id": "REFL-RUT-0033", "subject": "TU-RUT-004-018-022", "order": 1,
     "question_de": "Welche Namen aus der Geschichte fehlen in diesem Stammbaum?",
     "note_de": "Der Stammbaum nennt nur Männer von Perez bis David ([[RUT.4.18-RUT.4.22]]); Rut, Noomi und Elimelech kommen darin nicht vor.",
     "gsw": {"question_de": "Weli Näme us de Gschicht fääled i dem Stammbaum?",
             "note_de": "De Stammbaum nännt nu Manne vom Perez bis zum David ([[RUT.4.18-RUT.4.22]]); d Rut, d Noomi und de Elimelech chömed nöd vor."}},
    {"id": "REFL-RUT-0034", "subject": "TU-RUT-004-018-022", "order": 2,
     "question_de": "Wie liest sich die ganze Geschichte anders, wenn man ihr Ende bei David kennt?",
     "gsw": {"question_de": "Wie list sich di ganz Gschicht andersch, wänn mer ires Änd bim David kännt?"}},
]

RECEPTIONS = [
    {"id": "RCPT-RUT-0001", "subject": "SUM-BOOK-RUT", "tradition": "liturgy", "period_de": "seit dem Frühmittelalter",
     "text_de": "In der Synagoge wird das Buch Rut am Wochenfest (Schawuot) gelesen. Als Gründe werden genannt: die Erntezeit, Ruts Bindung an Israels Gott als Bild für die Annahme der Tora am Sinai und David, mit dessen Stammbaum das Buch endet.",
     "sources_de": ["Traktat Soferim 14,16 (in anderen Ausgaben 14,18; frühester Beleg)"],
     "confidence": "high",
     "gsw": {"period_de": "sit em Früemittelalter",
             "text_de": "I de Synagoge list mer s Buech Rut am Wuchefescht (Schawuot). Als Gründ nännt mer: d Ärnteziit, dass sich d Rut a Israels Gott bindet, als Bild für d Aanaam vo de Tora am Sinai, und de David, mit dem sim Stammbaum s Buech uufhört."}},
    {"id": "RCPT-RUT-0002", "subject": "SUM-BOOK-RUT", "tradition": "jewish", "period_de": "Spätantike (Midrasch)",
     "text_de": "Der Midrasch Rut Rabba fragt, wozu das Buch geschrieben ist, da es nichts über rein und unrein, verboten und erlaubt lehrt. Rabbi Seira antwortet: um zu lehren, wie gross der Lohn derer ist, die Güte (Chesed) üben.",
     "sources_de": ["Rut Rabba 2,14"],
     "confidence": "high",
     "gsw": {"period_de": "Spätantike (Midrasch)",
             "text_de": "De Midrasch Rut Rabba fröget, für was s Buech gschribe isch, wil s nüüt über rein und unrein, verbotte und erlaubt lehrt. De Rabbi Seira antwortet: zum lehre, wie gross de Lohn vo dene isch, wo Güeti (Chesed) üebed."}},
    {"id": "RCPT-RUT-0003", "subject": "TU-RUT-001-006-018", "tradition": "jewish", "period_de": "Babylonischer Talmud, etwa 3.–6. Jahrhundert",
     "text_de": "Der Talmud liest Ruts Schwur als Antworten in einem Gespräch: Noomi nennt ihr Gebote, die sie als Israelitin halten müsste, und Rut antwortet jeweils mit einem Satz aus [[RUT.1.16-RUT.1.17]]. Daraus werden Regeln abgeleitet, wie man Menschen begegnet, die zum Judentum übertreten wollen; Rut gilt seither als Vorbild dafür.",
     "sources_de": ["Babylonischer Talmud, Jevamot 47b"],
     "confidence": "high",
     "gsw": {"period_de": "Babylonische Talmud, öppe 3.–6. Jahrhundert",
             "text_de": "De Talmud list de Schwur vo de Rut als Antworte i me Gspräch: D Noomi nännt ire Gebot, wo si als Israelitin müessti halte, und d Rut antwortet jedes Mal mit eme Satz us [[RUT.1.16-RUT.1.17]]. Drus leitet mer Regle ab, wie mer Mänsche begägnet, wo zum Judetum übertrete wänd; d Rut gilt sitdem als Vorbild defür."}},
    {"id": "RCPT-RUT-0004", "subject": "SUM-BOOK-RUT", "tradition": "jewish", "period_de": "Babylonischer Talmud, etwa 3.–6. Jahrhundert",
     "text_de": "Eine Überlieferung im Talmud nennt Samuel als Verfasser seines Buches sowie der Bücher Richter und Rut und stellt Rut an den Anfang der «Schriften», noch vor die Psalmen. In christlichen Bibeln steht Rut dagegen nach dem Buch der Richter, weil die Erzählung «in den Tagen, als die Richter richteten» spielt ([[RUT.1.1]]).",
     "sources_de": ["Babylonischer Talmud, Bava Batra 14b"],
     "confidence": "high",
     "gsw": {"period_de": "Babylonische Talmud, öppe 3.–6. Jahrhundert",
             "text_de": "E Überliferig im Talmud nännt de Samuel als Verfasser vo sim Buech und vo de Büecher Richter und Rut und stellt d Rut a de Aafang vo de «Schrifte», no vor d Psalme. I chrischtliche Bible staat d Rut dagäge nach em Buech vo de Richter, wil d Gschicht «i de Ziit, wo d Richter grichtet händ» spillt ([[RUT.1.1]])."}},
    {"id": "RCPT-RUT-0005", "subject": "TU-RUT-002-004-017", "tradition": "art", "period_de": "1660–1664",
     "text_de": "Nicolas Poussin malt in seinem Zyklus der vier Jahreszeiten den Sommer als Erntefeld, auf dem Boas Rut beim Ährenlesen begegnet; auch die anderen Jahreszeiten zeigen biblische Szenen.",
     "sources_de": ["Nicolas Poussin, «Der Sommer» (Rut und Boas), Zyklus «Die vier Jahreszeiten», Louvre, Paris"],
     "confidence": "high",
     "gsw": {"period_de": "1660–1664",
             "text_de": "De Nicolas Poussin malt i sim Zyklus vo de vier Jahresziite de Summer als Ärntefäld, wo de Boas d Rut bim Ähreläse aatrifft; au di andere Jahresziite zeiged biblischi Szene."}},
    {"id": "RCPT-RUT-0006", "subject": "TU-RUT-002-004-017", "tradition": "literature", "period_de": "1819",
     "text_de": "John Keats lässt in seiner «Ode an eine Nachtigall» das Lied des Vogels auch durch das traurige Herz Ruts gehen, die voll Heimweh «in Tränen im fremden Korn» stand. Von Ruts Heimweh oder Tränen erzählt das Buch selbst nichts; der Dichter füllt eine Leerstelle.",
     "sources_de": ["John Keats, «Ode to a Nightingale», Verse 65–67"],
     "confidence": "high",
     "gsw": {"period_de": "1819",
             "text_de": "De John Keats laat i sinere «Ode a e Nachtigall» s Lied vom Vogel au dur s trurig Härz vo de Rut gaa, wo voll Heiweh «mit Träne im frömde Chorn» gstande isch. Vom Heiweh oder vo Träne vo de Rut verzellt s Buech sälber nüüt; de Dichter füllt e Läärstell."}},
    {"id": "RCPT-RUT-0007", "subject": "TU-RUT-003-006-015", "tradition": "literature", "period_de": "1859",
     "text_de": "Victor Hugo widmet dem schlafenden Boas das Gedicht «Booz endormi» («Der schlafende Boas») im ersten Teil seiner Gedichtsammlung «La Légende des siècles»; es malt die Nacht auf der Tenne ([[RUT.3.7-RUT.3.8]]) dichterisch aus.",
     "sources_de": ["Victor Hugo, «Booz endormi», in: La Légende des siècles, 1. Reihe (1859)"],
     "confidence": "high",
     "gsw": {"period_de": "1859",
             "text_de": "De Victor Hugo widmet em Boas, wo schlaaft, s Gedicht «Booz endormi» («De schlafend Boas») im erschte Teil vo sinere Gedichtsammlig «La Légende des siècles»; es malt d Nacht uf de Tänne ([[RUT.3.7-RUT.3.8]]) dichterisch us."}},
]

# Quellenprüfung (docs/QUELLENPRUEFUNG.md)
SOURCE_CHECKS = {
 "RCPT-RUT-0001": {
  "date": "2026-10-29",
  "result": "confirmed",
  "method_de": "KI-Prüfung (Claude) vom 2026-10-29: Angaben mit Websuche in frei zugänglichen Textausgaben bzw. Nachschlagewerken nachgeschlagen; nur Fundstelle und eigene Zusammenfassung übernommen; keine fachliche Prüfung.",
  "checked": [
   {
    "source": "Traktat Soferim 14,16",
    "found_at": "https://www.myjewishlearning.com/article/why-do-we-read-the-book-of-ruth-on-shavuot/ (Darstellung mit Stellenangabe)",
    "finding_de": "Soferim 14,16 gilt als frühester Beleg für die Lesung von Rut an Schawuot; genannte Gründe: Annahme der Tora, David, Erntezeit."
   }
  ]
 },
 "RCPT-RUT-0002": {
  "date": "2026-10-29",
  "result": "confirmed",
  "method_de": "KI-Prüfung (Claude) vom 2026-10-29: Angaben mit Websuche in frei zugänglichen Textausgaben bzw. Nachschlagewerken nachgeschlagen; nur Fundstelle und eigene Zusammenfassung übernommen; keine fachliche Prüfung.",
  "checked": [
   {
    "source": "Rut Rabba 2,14",
    "found_at": "https://torahinmotion.org/sites/default/files/TIM5-6%20RUTH.pdf (Quellenblatt mit englischer Übersetzung)",
    "finding_de": "R. Seira: Die Rolle lehrt nichts über rein und unrein, verboten und erlaubt; sie lehrt, wie gross der Lohn derer ist, die Güte üben."
   }
  ]
 },
 "RCPT-RUT-0003": {
  "date": "2026-10-29",
  "result": "confirmed",
  "method_de": "KI-Prüfung (Claude) vom 2026-10-29: Angaben mit Websuche in frei zugänglichen Textausgaben bzw. Nachschlagewerken nachgeschlagen; nur Fundstelle und eigene Zusammenfassung übernommen; keine fachliche Prüfung.",
  "checked": [
   {
    "source": "Babylonischer Talmud, Jevamot 47b",
    "found_at": "https://hatanakh.com/sites/default/files/Ruth%2010.pdf (Darstellung mit Wiedergabe der Talmudstelle)",
    "finding_de": "Der Talmud liest Ruts Worte als Antworten auf Noomis Hinweise auf Gebote und leitet daraus Regeln für den Übertritt ab."
   }
  ]
 },
 "RCPT-RUT-0004": {
  "date": "2026-10-29",
  "result": "confirmed",
  "method_de": "KI-Prüfung (Claude) vom 2026-10-29: Angaben mit Websuche in frei zugänglichen Textausgaben bzw. Nachschlagewerken nachgeschlagen; nur Fundstelle und eigene Zusammenfassung übernommen; keine fachliche Prüfung.",
  "checked": [
   {
    "source": "Babylonischer Talmud, Bava Batra 14b",
    "found_at": "https://cojs.org/?p=4832 (englische Übersetzung von Bava Batra 14b–15a)",
    "finding_de": "Reihenfolge der Schriften beginnt mit Rut, Psalmen, Hiob, Sprüche; «Samuel schrieb sein Buch, Richter und Rut»."
   }
  ]
 },
 "RCPT-RUT-0005": {
  "date": "2026-10-29",
  "result": "confirmed",
  "method_de": "KI-Prüfung (Claude) vom 2026-10-29: Angaben mit Websuche in frei zugänglichen Textausgaben bzw. Nachschlagewerken nachgeschlagen; nur Fundstelle und eigene Zusammenfassung übernommen; keine fachliche Prüfung.",
  "checked": [
   {
    "source": "Nicolas Poussin, «Der Sommer» (Rut und Boas)",
    "found_at": "https://en.wikipedia.org/wiki/The_Four_Seasons_(Poussin)",
    "finding_de": "Zyklus der vier Jahreszeiten, 1660–1664 in Rom gemalt, im Louvre; der Sommer zeigt Boas, der Rut beim Ährenlesen findet; auch die übrigen Jahreszeiten zeigen biblische Szenen."
   }
  ]
 },
 "RCPT-RUT-0006": {
  "date": "2026-10-29",
  "result": "confirmed",
  "method_de": "KI-Prüfung (Claude) vom 2026-10-29: Angaben mit Websuche in frei zugänglichen Textausgaben bzw. Nachschlagewerken nachgeschlagen; nur Fundstelle und eigene Zusammenfassung übernommen; keine fachliche Prüfung.",
  "checked": [
   {
    "source": "John Keats, «Ode to a Nightingale», V. 65–67",
    "found_at": "https://rpo.library.utoronto.ca/poems/ode-nightingale",
    "finding_de": "«Through the sad heart of Ruth, when, sick for home, / She stood in tears amid the alien corn»; Mai 1819 verfasst, im Juli 1819 gedruckt."
   }
  ]
 },
 "RCPT-RUT-0007": {
  "date": "2026-10-29",
  "result": "confirmed",
  "method_de": "KI-Prüfung (Claude) vom 2026-10-29: Angaben mit Websuche in frei zugänglichen Textausgaben bzw. Nachschlagewerken nachgeschlagen; nur Fundstelle und eigene Zusammenfassung übernommen; keine fachliche Prüfung.",
  "checked": [
   {
    "source": "Victor Hugo, «Booz endormi»",
    "found_at": "https://en.wikipedia.org/wiki/La_L%C3%A9gende_des_si%C3%A8cles",
    "finding_de": "Das Gedicht steht in der ersten Reihe der «Légende des siècles» (1859), Teil «D’Ève à Jésus»."
   }
  ]
 }
}
for _x in RECEPTIONS:
    _x["source_check"] = SOURCE_CHECKS[_x["id"]]

# Zweite Quellenprüfung durch eine weitere Instanz (2026-10-29)
RECHECK_DE = " Am 2026-10-29 von einer weiteren Instanz (getrennte KI-Prüfung, Claude) erneut nachgeschlagen; keine fachliche Prüfung."
RECHECKED = ["RCPT-RUT-0001", "RCPT-RUT-0004"]
RECHECK_EXTRA = {
 "RCPT-RUT-0001": {
  "source": "Traktat Soferim 14 (zweite Prüfung)",
  "found_at": "https://jewishlink.news/the-origin-of-the-reading-of-the-chamesh-megillot/",
  "finding_de": "Dieselbe Bestimmung (Hoheslied an Pessach, Rut an Schawuot) wird dort als Soferim 14,18 gezählt; die Zählung der Halachot schwankt zwischen Ausgaben. Angabe in sources_de ergänzt."
 }
}
for _x in RECEPTIONS:
    if _x["id"] in RECHECKED:
        _sc = dict(_x["source_check"])
        _sc["method_de"] = _sc["method_de"] + RECHECK_DE
        if _x["id"] in RECHECK_EXTRA:
            _sc["checked"] = _sc["checked"] + [RECHECK_EXTRA[_x["id"]]]
        _x["source_check"] = _sc
