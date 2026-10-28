"""Weiterdenken zum 1. Johannesbrief (Entscheid Andi Neck 2026-10-28): Fragen zum Weiterdenken und «Wie man es gelesen
hat» für alle Abschnitte, Kapitel und das Buch. KI-Entwürfe ohne fachliche Prüfung; Quellen in frei zugänglichen Ausgaben
nachgeschlagen (source_check), soweit möglich.

Prüfvermerk (PROC-WEITERDENKEN@1.0, Schritte 3 und 4): Am 2026-10-29 von einer weiteren Instanz (getrennte KI-Prüfung,
Claude) gegen die hochdeutsche Arbeitsübersetzung geprüft: alle 40 Fragen und Hintergrundsätze (offen, nicht suggestiv,
am Text belegt, Zitate per Skript wörtlich verglichen, Stellenmarken), Mundart nach pruefe_mundart; Kernaussagen (gist_de)
der Kernanalysen gegen den Text;
Quellen von 3 der 5 Einträge «Wie man es gelesen hat» erneut
nachgeschlagen (Vermerk im source_check). Grenzen: nicht gegen den Urtext geprüft; Zitate aus Büchern ohne
Arbeitsübersetzung nicht verglichen; Mundart-Zitate nicht an die Mundart-Übersetzungsschicht angeglichen; keine fachliche
und keine muttersprachliche Prüfung durch eine Person."""
DATE = "2026-10-28"
PROCESS = "PROC-WEITERDENKEN@1.0"
TAGS = ["TAG-JOHANNINE"]
AUTHORSHIP_DE = "KI-Entwurf (Claude) vom 2026-10-28 (Weiterdenken 1. Johannesbrief, Entscheid Andi Neck); keine fachliche Prüfung."

REFLECTIONS = [
    # Buch
    {"id": "REFL-1JN-0001", "subject": "SUM-BOOK-1JN", "order": 1,
     "question_de": "Woran merkt man, dass jemand Gemeinschaft mit Gott hat?",
     "note_de": "Der Brief nennt immer wieder Prüfsteine: «Daran erkennen wir …» ([[1JN.2.3]]; [[1JN.3.24]]; [[1JN.4.13]]).",
     "gsw": {"question_de": "Wora merkt mer, dass öpper Gmeinschaft mit Gott hät?",
             "note_de": "De Brief nännt immer wider Prüefstei: «Dra erchänned mir …» ([[1JN.2.3]]; [[1JN.3.24]]; [[1JN.4.13]])."}},
    {"id": "REFL-1JN-0002", "subject": "SUM-BOOK-1JN", "order": 2,
     "question_de": "Wer ist mit «wir» gemeint – und gehörst du dazu?",
     "note_de": "Das «wir» der Zeugen, die gehört und gesehen haben ([[1JN.1.1]]), geht über in ein «wir» aller, die glauben ([[1JN.4.16]]).",
     "gsw": {"question_de": "Wär isch mit «mir» gmeint – und ghörsch du dezue?",
             "note_de": "S «mir» vo de Zügä, wo ghört und gseh händ ([[1JN.1.1]]), gaat über i es «mir» vo allne, wo glaubed ([[1JN.4.16]])."}},
    {"id": "REFL-1JN-0003", "subject": "SUM-BOOK-1JN", "order": 3,
     "question_de": "Wie kann ein Brief so von Liebe sprechen und zugleich so scharf trennen?",
     "note_de": "Neben «Gott ist Liebe» ([[1JN.4.8]]) stehen «Antichristen» und «Kinder des Teufels» ([[1JN.2.18]]; [[1JN.3.10]]).",
     "gsw": {"question_de": "Wie chan en Brief so vo Liebi rede und zgliich so scharf trenne?",
             "note_de": "Näbe «Gott isch Liebi» ([[1JN.4.8]]) stönd «Antichrischte» und «Chind vom Tüüfel» ([[1JN.2.18]]; [[1JN.3.10]])."}},
    # Kapitel
    {"id": "REFL-1JN-0004", "subject": "SUM-CH-1JN-001", "order": 1,
     "question_de": "Warum ist es so wichtig, dass man gehört, gesehen und betastet hat?",
     "note_de": "Der Brief beginnt mit Sinnen: hören, sehen, schauen, mit Händen betasten ([[1JN.1.1]]).",
     "gsw": {"question_de": "Wieso isch es so wichtig, dass mer ghört, gseh und aaglanget hät?",
             "note_de": "De Brief fangt mit de Sinn aa: ghöre, gseh, aaluege, mit de Händ aalange ([[1JN.1.1]])."}},
    {"id": "REFL-1JN-0005", "subject": "SUM-CH-1JN-002", "order": 1,
     "question_de": "Wie kann ein Gebot zugleich alt und neu sein?",
     "note_de": "«Nicht ein neues Gebot schreibe ich euch, sondern ein altes … Und doch schreibe ich euch ein neues Gebot» ([[1JN.2.7-1JN.2.8]]).",
     "gsw": {"question_de": "Wie chan es Gebot zgliich alt und nöi sii?",
             "note_de": "«Nöd es nöis Gebot schriib ich eu, sondern es alts … Und gliich schriib ich eu es nöis Gebot» ([[1JN.2.7-1JN.2.8]])."}},
    {"id": "REFL-1JN-0006", "subject": "SUM-CH-1JN-003", "order": 1,
     "question_de": "Was heisst Lieben «in Tat und Wahrheit»?",
     "note_de": "«Lasst uns nicht mit Worten lieben und auch nicht mit der Zunge, sondern in Tat und Wahrheit» ([[1JN.3.18]]).",
     "gsw": {"question_de": "Was heisst Liebe «i Tat und Wahrheit»?",
             "note_de": "«Mir wänd nöd mit Wort liebe und au nöd mit de Zunge, sondern i Tat und Wahrheit» ([[1JN.3.18]])."}},
    {"id": "REFL-1JN-0007", "subject": "SUM-CH-1JN-004", "order": 1,
     "question_de": "Was verändert der Satz «Gott ist Liebe»?",
     "note_de": "Er steht zweimal in diesem Kapitel ([[1JN.4.8]]; [[1JN.4.16]]) und wird mit der Sendung des Sohnes begründet ([[1JN.4.9-1JN.4.10]]).",
     "gsw": {"question_de": "Was veränderet de Satz «Gott isch Liebi»?",
             "note_de": "Er staat zwei Mal i dem Kapitel ([[1JN.4.8]]; [[1JN.4.16]]) und wird mit de Sändig vom Sohn begründet ([[1JN.4.9-1JN.4.10]])."}},
    {"id": "REFL-1JN-0008", "subject": "SUM-CH-1JN-005", "order": 1,
     "question_de": "Warum endet ein Brief über die Liebe mit einer Warnung vor Götzen?",
     "note_de": "Der letzte Satz lautet: «Kinder, hütet euch vor den Götzen!» ([[1JN.5.21]]); von Götzen war vorher nicht die Rede.",
     "gsw": {"question_de": "Wieso hört en Brief über d Liebi mit ere Warnig vor Götze uf?",
             "note_de": "De letscht Satz heisst: «Chind, hüeted eu vor de Götze!» ([[1JN.5.21]]); vo Götze isch vorher nöd d Red gsii."}},
    # 1,1–4
    {"id": "REFL-1JN-0009", "subject": "TU-1JN-001-001-004", "order": 1,
     "question_de": "Kann man Gemeinschaft mit jemandem haben, den man nicht selbst gesehen hat?",
     "note_de": "Die Zeugen verkündigen, was sie gesehen haben, «damit auch ihr Gemeinschaft habt mit uns» ([[1JN.1.3]]).",
     "gsw": {"question_de": "Chan mer Gmeinschaft ha mit öpperem, wo mer nöd sälber gseh hät?",
             "note_de": "D Zügä verchünded, was si gseh händ, «demit au ir Gmeinschaft händ mit üs» ([[1JN.1.3]])."}},
    {"id": "REFL-1JN-0010", "subject": "TU-1JN-001-001-004", "order": 2,
     "question_de": "Wessen Freude soll vollkommen werden – die der Schreiber oder die der Leser?",
     "note_de": "«Und das schreiben wir, damit unsere Freude vollkommen sei» ([[1JN.1.4]]).",
     "gsw": {"question_de": "Wem sini Fröid söll volkomme wärde – die vo de Schriiber oder die vo de Läser?",
             "note_de": "«Und das schriibed mir, demit öisi Fröid vollkomme isch» ([[1JN.1.4]])."}},
    # 1,5–10
    {"id": "REFL-1JN-0011", "subject": "TU-1JN-001-005-010", "order": 1,
     "question_de": "Was ändert sich, wenn man Sünde bekennt, statt sie zu leugnen?",
     "note_de": "Dreimal heisst es «Wenn wir sagen …» ([[1JN.1.6]]; [[1JN.1.8]]; [[1JN.1.10]]); dazwischen steht: «Wenn wir unsere Sünden bekennen» ([[1JN.1.9]]).",
     "gsw": {"question_de": "Was änderet sich, wänn mer Sünd bekännt, statt si z leugne?",
             "note_de": "Drüü Mal heisst s «Wänn mir säged …» ([[1JN.1.6]]; [[1JN.1.8]]; [[1JN.1.10]]); dezwüsche staat: «Wänn mir öisi Sünde bekänned» ([[1JN.1.9]])."}},
    {"id": "REFL-1JN-0012", "subject": "TU-1JN-001-005-010", "order": 2,
     "question_de": "Was bedeutet das Bild vom Licht, in dem keinerlei Finsternis ist?",
     "note_de": "«Gott ist Licht, und in ihm ist keinerlei Finsternis» ([[1JN.1.5]]).",
     "gsw": {"question_de": "Was bedüütet s Bild vom Liecht, wo kei Fiischteri drin isch?",
             "note_de": "«Gott isch Liecht, und in ihm isch überhaupt kei Fiischteri» ([[1JN.1.5]])."}},
    # 2,1–6
    {"id": "REFL-1JN-0013", "subject": "TU-1JN-002-001-006", "order": 1,
     "question_de": "Was braucht jemand, der versagt hat?",
     "note_de": "«Wenn jemand sündigt, haben wir einen Fürsprecher beim Vater» ([[1JN.2.1]]) – direkt nach der Mahnung, nicht zu sündigen.",
     "gsw": {"question_de": "Was bruucht öpper, wo versait hät?",
             "note_de": "«Wänn öpper sündiget, händ mir en Fürspräch bim Vatter» ([[1JN.2.1]]) – diräkt nach de Mahnig, nöd z sündige."}},
    {"id": "REFL-1JN-0014", "subject": "TU-1JN-002-001-006", "order": 2,
     "question_de": "Was hiesse es für dich, zu leben, «wie jener gelebt hat»?",
     "note_de": "«Wer sagt, er bleibe in ihm, muss auch selbst leben, wie jener gelebt hat» ([[1JN.2.6]]).",
     "gsw": {"question_de": "Was würd s für dich heisse, z läbe, «wie dä gläbt hät»?",
             "note_de": "«Wär seit, er bliibi in ihm, muess au sälber läbe, wie dä gläbt hät» ([[1JN.2.6]])."}},
    # 2,7–11
    {"id": "REFL-1JN-0015", "subject": "TU-1JN-002-007-011", "order": 1,
     "question_de": "Wie macht Hass blind?",
     "note_de": "Wer seinen Bruder hasst, «weiss nicht, wohin er geht; denn die Finsternis hat seine Augen blind gemacht» ([[1JN.2.11]]).",
     "gsw": {"question_de": "Wie macht Hass blind?",
             "note_de": "Wär sin Brueder hasst, «weiss nöd, wohii er gaat; dänn d Fiischteri hät sini Auge blind gmacht» ([[1JN.2.11]])."}},
    {"id": "REFL-1JN-0016", "subject": "TU-1JN-002-007-011", "order": 2,
     "question_de": "Wer ist hier mit «Bruder» gemeint – und wer nicht?",
     "note_de": "Ob nur Glaubende oder auch Aussenstehende gemeint sind, sagt der Brief hier nicht ([[1JN.2.9-1JN.2.10]]); an anderer Stelle stehen die «Brüder und Schwestern» der Welt gegenüber ([[1JN.3.13]]).",
     "gsw": {"question_de": "Wär isch da mit «Brueder» gmeint – und wär nöd?",
             "note_de": "Öb nu Gläubigi oder au Ussestehendi gmeint sind, seit de Brief da nöd ([[1JN.2.9-1JN.2.10]]); anderswo stönd d «Brüeder und Schwöschtere» de Wält gägenüber ([[1JN.3.13]])."}},
    # 2,12–17
    {"id": "REFL-1JN-0017", "subject": "TU-1JN-002-012-017", "order": 1,
     "question_de": "Warum spricht der Brief Kinder, Väter und junge Männer getrennt an?",
     "note_de": "Jede Gruppe wird zweimal angeredet, jedes Mal mit einem Zuspruch, nicht mit einer Mahnung ([[1JN.2.12-1JN.2.14]]).",
     "gsw": {"question_de": "Wieso redt de Brief Chind, Vätter und jungi Manne einzeln aa?",
             "note_de": "Jedi Gruppe wird zwei Mal aagredt, jedes Mal mit eme Zuespruch, nöd mit ere Mahnig ([[1JN.2.12-1JN.2.14]])."}},
    {"id": "REFL-1JN-0018", "subject": "TU-1JN-002-012-017", "order": 2,
     "question_de": "Was ist mit der «Welt» gemeint, die man nicht lieben soll?",
     "note_de": "Der Brief nennt die Begierde des Fleisches, die Begierde der Augen und das Prahlen mit dem Besitz ([[1JN.2.16]]); anderswo heisst es, Gott habe den Sohn «als Retter der Welt» gesandt ([[1JN.4.14]]).",
     "gsw": {"question_de": "Was isch mit de «Wält» gmeint, wo mer nöd söll liebe?",
             "note_de": "De Brief nännt d Begierd vom Fleisch, d Begierd vo de Auge und s Plagiere mit em Bsitz ([[1JN.2.16]]); anderswo heisst s, Gott heb de Sohn «als Retter vo de Wält» gschickt ([[1JN.4.14]])."}},
    # 2,18–27
    {"id": "REFL-1JN-0019", "subject": "TU-1JN-002-018-027", "order": 1,
     "question_de": "Wie fühlt sich eine Gemeinschaft an, aus der Menschen weggegangen sind?",
     "note_de": "«Von uns sind sie ausgegangen, aber sie gehörten nicht zu uns» ([[1JN.2.19]]); der Brief deutet den Weggang aus seiner Sicht.",
     "gsw": {"question_de": "Wie fühlt sich e Gmeinschaft aa, wo Lüüt devo wäggange sind?",
             "note_de": "«Vo üs sind si furtgange, aber si händ nöd zu üs ghört» ([[1JN.2.19]]); de Brief düütet de Wäggang us sinere Sicht."}},
    {"id": "REFL-1JN-0020", "subject": "TU-1JN-002-018-027", "order": 2,
     "question_de": "Die Leser brauchen niemanden, der sie belehrt – warum schreibt der Brief dann trotzdem?",
     "note_de": "«Ihr habt es nicht nötig, dass jemand euch belehrt» ([[1JN.2.27]]); geschrieben hat er, «weil ihr sie kennt» ([[1JN.2.21]]).",
     "gsw": {"question_de": "D Läser bruuched niemer, wo si lehrt – wieso schriibt de Brief dänn glich?",
             "note_de": "«Ir händ es nöd nötig, dass öpper eu öppis lehrt» ([[1JN.2.27]]); gschribe hät er, «wil ir si känned» ([[1JN.2.21]])."}},
    # 2,28–29
    {"id": "REFL-1JN-0021", "subject": "TU-1JN-002-028-029", "order": 1,
     "question_de": "Was gibt Zuversicht, wenn man an das Kommen Christi denkt?",
     "note_de": "Die Kinder sollen in ihm bleiben, damit sie bei seinem Kommen «nicht beschämt vor ihm zurückweichen müssen» ([[1JN.2.28]]).",
     "gsw": {"question_de": "Was git Zueversicht, wänn mer as Choo vo Christus dänkt?",
             "note_de": "D Chind söled in ihm bliibe, demit mir üs bi sim Choo «nöd vor ihm müend schäme» ([[1JN.2.28]])."}},
    {"id": "REFL-1JN-0022", "subject": "TU-1JN-002-028-029", "order": 2,
     "question_de": "Kann man an jemandes Tun erkennen, woher er kommt?",
     "note_de": "Der Brief sagt, «dass jeder, der die Gerechtigkeit tut, aus ihm geboren ist» ([[1JN.2.29]]).",
     "gsw": {"question_de": "Chan mer am Tue vo öpperem erchänne, won er herchunnt?",
             "note_de": "De Brief seit, «dass jede, wo d Grächtigkeit tuet, us ihm gebore isch» ([[1JN.2.29]])."}},
    # 3,1–10
    {"id": "REFL-1JN-0023", "subject": "TU-1JN-003-001-010", "order": 1,
     "question_de": "Was macht der Nachsatz «und wir sind es!» aus?",
     "note_de": "Der Brief sagt, «dass wir Kinder Gottes heissen – und wir sind es!» ([[1JN.3.1]]), und zugleich: «Es ist noch nicht offenbar geworden, was wir sein werden» ([[1JN.3.2]]).",
     "gsw": {"question_de": "Was macht de Nachsatz «und mir sinds!» us?",
             "note_de": "De Brief seit, «dass mir Chind vo Gott heissed – und mir sinds!» ([[1JN.3.1]]), und zgliich: «es isch no nöd sichtbar worde, was mir sii wärded» ([[1JN.3.2]])."}},
    {"id": "REFL-1JN-0024", "subject": "TU-1JN-003-001-010", "order": 2,
     "question_de": "Wie passen «Jeder, der aus Gott geboren ist, tut keine Sünde» und «Wenn wir sagen, dass wir keine Sünde haben, führen wir uns selbst in die Irre» zusammen?",
     "note_de": "Der Brief sagt beides ([[1JN.3.9]]; [[1JN.1.8]]) und löst die Spannung nicht auf.",
     "gsw": {"question_de": "Wie passed «Jede, wo us Gott gebore isch, tuet kei Sünd» und «Wänn mir säged, dass mir kei Sünd händ, verfüered mir üs sälber» zäme?",
             "note_de": "De Brief seit beides ([[1JN.3.9]]; [[1JN.1.8]]) und löst d Spannig nöd uf."}},
    # 3,11–18
    {"id": "REFL-1JN-0025", "subject": "TU-1JN-003-011-018", "order": 1,
     "question_de": "Warum wird ausgerechnet Kain als Gegenbild genannt?",
     "note_de": "Genannt wird Kain, der «seinen Bruder ermordete», weil seine Werke böse waren ([[1JN.3.12]], vgl. [[GEN.4.8]]); wer seinen Bruder hasst, heisst ein Mörder ([[1JN.3.15]]).",
     "gsw": {"question_de": "Wieso wird usgrächnet de Kain als Gägebild gnännt?",
             "note_de": "Gnännt wird de Kain, wo «sin Brueder umbracht hät», wil sini Wärch bös gsii sind ([[1JN.3.12]], vgl. [[GEN.4.8]]); wär sin Brueder hasst, heisst en Mörder ([[1JN.3.15]])."}},
    {"id": "REFL-1JN-0026", "subject": "TU-1JN-003-011-018", "order": 2,
     "question_de": "Was hat die Liebe mit dem zu tun, was man besitzt?",
     "note_de": "«Wer aber die Güter der Welt hat und seinen Bruder Not leiden sieht und sein Herz vor ihm verschliesst – wie bleibt die Liebe Gottes in ihm?» ([[1JN.3.17]]).",
     "gsw": {"question_de": "Was hät d Liebi mit dem z tue, was mer bsitzt?",
             "note_de": "«Wär aber de Bsitz vo de Wält hät und sin Brueder Not liide gseht und sis Härz vor ihm zuetuet – wie bliibt d Liebi vo Gott in ihm?» ([[1JN.3.17]])."}},
    # 3,19–24
    {"id": "REFL-1JN-0027", "subject": "TU-1JN-003-019-024", "order": 1,
     "question_de": "Was tröstet, wenn das eigene Herz einen verurteilt?",
     "note_de": "«Gott ist grösser als unser Herz und weiss alles» ([[1JN.3.20]]).",
     "gsw": {"question_de": "Was tröschtet, wänn s eiget Härz eim verurteilt?",
             "note_de": "«Gott isch grösser als öises Härz und weiss alles» ([[1JN.3.20]])."}},
    {"id": "REFL-1JN-0028", "subject": "TU-1JN-003-019-024", "order": 2,
     "question_de": "Warum werden Glauben und Lieben hier ein einziges Gebot genannt?",
     "note_de": "«Das ist sein Gebot: dass wir dem Namen seines Sohnes Jesus Christus glauben und einander lieben» ([[1JN.3.23]]).",
     "gsw": {"question_de": "Wieso wärded Glaube und Liebe da es einzigs Gebot gnännt?",
             "note_de": "«Und das isch sis Gebot: dass mir a de Name vo sim Sohn Jesus Christus glaubed und enand liebed» ([[1JN.3.23]])."}},
    # 4,1–6
    {"id": "REFL-1JN-0029", "subject": "TU-1JN-004-001-006", "order": 1,
     "question_de": "Woran prüfst du, ob eine Stimme vertrauenswürdig ist?",
     "note_de": "«Glaubt nicht jedem Geist, sondern prüft die Geister» ([[1JN.4.1]]); der Brief nennt als Prüfstein das Bekenntnis zu Jesus Christus im Fleisch ([[1JN.4.2]]).",
     "gsw": {"question_de": "Wora prüefsch du, öb e Stimm vertrauenswürdig isch?",
             "note_de": "«Glaubed nöd jedem Geischt, sondern prüefed d Geischter» ([[1JN.4.1]]); de Brief nännt als Prüefstei s Bekänntnis zu Jesus Christus im Fleisch ([[1JN.4.2]])."}},
    {"id": "REFL-1JN-0030", "subject": "TU-1JN-004-001-006", "order": 2,
     "question_de": "Woran lässt sich prüfen, wer die Wahrheit sagt, wenn sich beide Seiten auf Gott berufen?",
     "note_de": "«Wer Gott kennt, hört auf uns» ([[1JN.4.6]]) – kurz nachdem es von den Gegnern heisst: «die Welt hört auf sie» ([[1JN.4.5]]).",
     "gsw": {"question_de": "Wora chan mer prüefe, wär d Wahrheit seit, wänn sich beidi Siite uf Gott berüefed?",
             "note_de": "«Wär Gott kännt, lost uf üs» ([[1JN.4.6]]) – churz nachdem s vo de Gägner heisst: «d Wält lost uf si» ([[1JN.4.5]])."}},
    # 4,7–12
    {"id": "REFL-1JN-0031", "subject": "TU-1JN-004-007-012", "order": 1,
     "question_de": "Was ändert sich, wenn Liebe nicht bei uns anfängt?",
     "note_de": "«Nicht dass wir Gott geliebt haben, sondern dass er uns geliebt hat» ([[1JN.4.10]]).",
     "gsw": {"question_de": "Was änderet sich, wänn d Liebi nöd bi üs aafangt?",
             "note_de": "«Nöd dass mir Gott gliebt händ, sondern dass er üs gliebt hät» ([[1JN.4.10]])."}},
    {"id": "REFL-1JN-0032", "subject": "TU-1JN-004-007-012", "order": 2,
     "question_de": "Wie wird der unsichtbare Gott sichtbar?",
     "note_de": "«Gott hat niemand je geschaut. Wenn wir einander lieben, bleibt Gott in uns» ([[1JN.4.12]]).",
     "gsw": {"question_de": "Wie wird de unsichtbar Gott sichtbar?",
             "note_de": "«Gott hät niemer je gseh. Wänn mir enand liebed, bliibt Gott in üs» ([[1JN.4.12]])."}},
    # 4,13–21
    {"id": "REFL-1JN-0033", "subject": "TU-1JN-004-013-021", "order": 1,
     "question_de": "Wovor hast du Angst – und was würde die Liebe daran ändern?",
     "note_de": "«Furcht ist nicht in der Liebe, sondern die vollkommene Liebe treibt die Furcht aus» ([[1JN.4.18]]).",
     "gsw": {"question_de": "Vor was häsch du Angscht – und was würd d Liebi dra ändere?",
             "note_de": "«Angscht isch nöd i de Liebi, sondern di vollkomme Liebi tribt d Angscht uus» ([[1JN.4.18]])."}},
    {"id": "REFL-1JN-0034", "subject": "TU-1JN-004-013-021", "order": 2,
     "question_de": "Kann man Gott lieben und einen Menschen hassen?",
     "note_de": "«Wer seinen Bruder nicht liebt, den er gesehen hat, kann Gott nicht lieben, den er nicht gesehen hat» ([[1JN.4.20]]).",
     "gsw": {"question_de": "Chan mer Gott liebe und en Mänsch hasse?",
             "note_de": "«Wär sin Brueder nöd liebt, wo er gseh hät, cha Gott nöd liebe, wo er nöd gseh hät» ([[1JN.4.20]])."}},
    # 5,1–5
    {"id": "REFL-1JN-0035", "subject": "TU-1JN-005-001-005", "order": 1,
     "question_de": "«Seine Gebote sind nicht schwer» – stimmt das für dich?",
     "note_de": "Der Brief begründet es damit, dass alles, was aus Gott geboren ist, die Welt besiegt ([[1JN.5.3-1JN.5.4]]).",
     "gsw": {"question_de": "«Sini Gebot sind nöd schwär» – stimmt das für dich?",
             "note_de": "De Brief begründet s demit, dass alles, wo us Gott gebore isch, d Wält besiegt ([[1JN.5.3-1JN.5.4]])."}},
    {"id": "REFL-1JN-0036", "subject": "TU-1JN-005-001-005", "order": 2,
     "question_de": "Was für ein Sieg ist gemeint, wenn der Glaube «die Welt besiegt»?",
     "note_de": "«Das ist der Sieg, der die Welt besiegt hat: unser Glaube» ([[1JN.5.4]]); von Kampf oder Gewalt spricht der Text nicht.",
     "gsw": {"question_de": "Was für en Sieg isch gmeint, wänn de Glaube «d Wält besiegt»?",
             "note_de": "«Das isch de Sieg, wo d Wält besiegt hät: öise Glaube» ([[1JN.5.4]]); vo Kampf oder Gwalt redt de Text nöd."}},
    # 5,6–12
    {"id": "REFL-1JN-0037", "subject": "TU-1JN-005-006-012", "order": 1,
     "question_de": "Wem glaubst du, wenn es um das Wichtigste geht?",
     "note_de": "«Wenn wir das Zeugnis der Menschen annehmen, so ist das Zeugnis Gottes grösser» ([[1JN.5.9]]).",
     "gsw": {"question_de": "Wem glaubsch du, wänn s um s Wichtigscht gaat?",
             "note_de": "«Wänn mir s Zügnis vo de Mänsche aanämed, so isch s Zügnis vo Gott grösser» ([[1JN.5.9]])."}},
    {"id": "REFL-1JN-0038", "subject": "TU-1JN-005-006-012", "order": 2,
     "question_de": "Was könnte «durch Wasser und Blut gekommen» bedeuten?",
     "note_de": "Der Text sagt «nicht im Wasser allein, sondern im Wasser und im Blut» ([[1JN.5.6]]) und erklärt das Bild nicht.",
     "gsw": {"question_de": "Was chönt «dur Wasser und Bluet cho» bedüüte?",
             "note_de": "De Text seit «nöd im Wasser elei, sondern im Wasser und im Bluet» ([[1JN.5.6]]) und erchlärt s Bild nöd."}},
    # 5,13–21
    {"id": "REFL-1JN-0039", "subject": "TU-1JN-005-013-021", "order": 1,
     "question_de": "Wie viel Gewissheit verträgt ein Glaube?",
     "note_de": "Der Brief ist geschrieben, «damit ihr wisst, dass ihr ewiges Leben habt» ([[1JN.5.13]]); dreimal folgt «Wir wissen» ([[1JN.5.18-1JN.5.20]]).",
     "gsw": {"question_de": "Wie vil Gwüssheit vertreit en Glaube?",
             "note_de": "De Brief isch gschribe, «demit ir wüssed, dass ir ewigs Läbe händ» ([[1JN.5.13]]); drüü Mal chunnt «Mir wüssed» ([[1JN.5.18-1JN.5.20]])."}},
    {"id": "REFL-1JN-0040", "subject": "TU-1JN-005-013-021", "order": 2,
     "question_de": "Für wen würdest du bitten, wenn du ihn sündigen siehst?",
     "note_de": "Der Brief ermutigt zur Fürbitte und nennt zugleich eine «Sünde zum Tod», ohne sie zu erklären ([[1JN.5.16-1JN.5.17]]).",
     "gsw": {"question_de": "Für wän würdsch du bitte, wänn d en gsächsch sündige?",
             "note_de": "De Brief ermuetiget zur Fürbitt und nännt zgliich e «Sünd zum Tod», ohni si z erchläre ([[1JN.5.16-1JN.5.17]])."}},
]

RECEPTIONS = [
    {"id": "RCPT-1JN-0001", "subject": "TU-1JN-004-001-006", "tradition": "church_fathers", "period_de": "erste Hälfte 2. Jahrhundert",
     "text_de": "Polykarp von Smyrna schreibt in seinem Brief an die Philipper fast wörtlich wie [[1JN.4.2-1JN.4.3]]: Jeder, der nicht bekennt, dass Jesus Christus im Fleisch gekommen ist, ist ein Antichrist. Das gilt als eines der frühesten Zeugnisse dafür, dass der 1. Johannesbrief bekannt war.",
     "sources_de": ["Polykarp, Brief an die Philipper 7,1"],
     "confidence": "high",
     "gsw": {"period_de": "erschti Hälfti 2. Jahrhundert",
             "text_de": "De Polykarp vo Smyrna schriibt i sim Brief a d Philipper fascht wörtlich wie [[1JN.4.2-1JN.4.3]]: Jede, wo nöd bekännt, dass Jesus Christus im Fleisch choo isch, isch en Antichrischt. Das gilt als eis vo de früenschte Zügnis defür, dass mer de 1. Johannesbrief kännt hät."}},
    {"id": "RCPT-1JN-0002", "subject": "TU-1JN-004-007-012", "tradition": "church_fathers", "period_de": "um 407",
     "text_de": "Augustinus legt den 1. Johannesbrief in zehn Predigten aus. Darin fällt der oft zitierte Satz «Liebe, und tu, was du willst»: Wo die Wurzel die Liebe ist, könne nur Gutes wachsen. Aus dem Zusammenhang gelöst, wird der Satz manchmal als Freibrief missverstanden.",
     "sources_de": ["Augustinus, Abhandlungen über den 1. Johannesbrief (Tractatus in epistolam Ioannis ad Parthos) 7,8"],
     "confidence": "high",
     "gsw": {"period_de": "um 407",
             "text_de": "De Augustinus leit de 1. Johannesbrief i zää Predige us. Drin fallt de vil zitiert Satz «Lieb, und tue, was d wotsch»: Wo d Wurzle d Liebi isch, chönn nu Guets wachse. Us em Zämehang glöst, wird de Satz mängisch als Freibrief falsch verstande."}},
    {"id": "RCPT-1JN-0003", "subject": "TU-1JN-005-006-012", "tradition": "modern_scholarship", "period_de": "16. bis 19. Jahrhundert",
     "text_de": "In späten lateinischen Handschriften steht in [[1JN.5.7-1JN.5.8]] ein Zusatz über drei, die im Himmel Zeugnis geben: Vater, Wort und Heiliger Geist («Comma Johanneum»). Erasmus liess ihn in seinen griechischen Ausgaben von 1516 und 1519 weg und nahm ihn erst 1522 auf; so kam er in viele spätere Bibeln. Die Textforschung hält ihn heute für einen späteren Zusatz, weil er in den alten griechischen Handschriften fehlt; die Übersetzung hier folgt ihnen.",
     "sources_de": ["Erasmus, Novum Instrumentum (1516) und 3. Auflage (1522)"],
     "confidence": "high",
     "gsw": {"period_de": "16. bis 19. Jahrhundert",
             "text_de": "I spaate latiinische Handschrifte staat i [[1JN.5.7-1JN.5.8]] en Zuesatz über drei, wo im Himmel Zügnis gänd: Vatter, Wort und Heilige Geischt («Comma Johanneum»). De Erasmus hät en i sine griechische Usgabe vo 1516 und 1519 wäggla und erscht 1522 ufgnoo; so isch er i vil speteri Bible choo. D Textforschig haltet en hüt für en spetere Zuesatz, wil er i de alte griechische Handschrifte fäält; d Übersetzig da folgt dene."}},
    {"id": "RCPT-1JN-0004", "subject": "TU-1JN-004-013-021", "tradition": "liturgy", "period_de": "um 800; bis heute",
     "text_de": "Der lateinische Gesang «Ubi caritas et amor, Deus ibi est» («Wo Güte und Liebe ist, da ist Gott»), der Paulinus von Aquileia zugeschrieben wird, erinnert an [[1JN.4.16]]. Er wurde lange zur Fusswaschung am Gründonnerstag gesungen, heute in der Abendmahlsmesse dieses Tages; als Gesang aus Taizé ist er auch ökumenisch verbreitet.",
     "sources_de": ["Hymnus «Ubi caritas» (Paulinus von Aquileia zugeschrieben, um 796)", "Römisches Messbuch, Messe vom Letzten Abendmahl"],
     "confidence": "high",
     "gsw": {"period_de": "um 800; bis hüt",
             "text_de": "De latiinisch Gsang «Ubi caritas et amor, Deus ibi est» («Wo Güeti und Liebi isch, isch Gott»), wo mer em Paulinus vo Aquileia zueschriibt, erinneret a [[1JN.4.16]]. Mer hät en lang zur Fuesswäschig am Grüendonschtig gsunge, hüt i de Abedmaalsmäss vo dem Tag; als Gsang us Taizé isch er au ökumenisch verbreitet."}},
    {"id": "RCPT-1JN-0005", "subject": "TU-1JN-002-018-027", "tradition": "church_fathers", "period_de": "um 180",
     "text_de": "Irenäus von Lyon zitiert [[1JN.2.18-1JN.2.22]] als Wort von «Johannes, dem Jünger des Herrn», im Streit mit Lehrern, die Jesus und Christus voneinander trennten. Damit beginnt die lange Lesart, die die «Antichristen» des Briefes mit bestimmten Irrlehren gleichsetzt; der Brief selbst nennt keine Namen.",
     "sources_de": ["Irenäus, Gegen die Häresien 3,16,5"],
     "confidence": "high",
     "gsw": {"period_de": "um 180",
             "text_de": "De Irenäus vo Lyon zitiert [[1JN.2.18-1JN.2.22]] als Wort vo «Johannes, em Jünger vom Herr», im Striit mit Lehrer, wo Jesus und Christus vonenand trännt händ. Demit fangt di lang Läsart aa, wo d «Antichrischte» vom Brief mit bstimmte Irrlehre gliichsetzt; de Brief sälber nännt kei Näme."}},
]

# Quellenprüfung (docs/QUELLENPRUEFUNG.md)
SOURCE_CHECKS = {
 "RCPT-1JN-0001": {
  "date": "2026-10-29",
  "result": "confirmed",
  "method_de": "KI-Prüfung (Claude) vom 2026-10-29: Angaben mit Websuche in frei zugänglichen Textausgaben bzw. Nachschlagewerken nachgeschlagen; nur Fundstelle und eigene Zusammenfassung übernommen; keine fachliche Prüfung.",
  "checked": [
   {
    "source": "Polykarp, Brief an die Philipper, Kapitel 7",
    "found_at": "https://www.newadvent.org/fathers/0136.htm",
    "finding_de": "«Whosoever does not confess that Jesus Christ has come in the flesh, is antichrist»."
   }
  ]
 },
 "RCPT-1JN-0002": {
  "date": "2026-10-29",
  "result": "confirmed",
  "method_de": "KI-Prüfung (Claude) vom 2026-10-29: Angaben mit Websuche in frei zugänglichen Textausgaben bzw. Nachschlagewerken nachgeschlagen; nur Fundstelle und eigene Zusammenfassung übernommen; keine fachliche Prüfung.",
  "checked": [
   {
    "source": "Augustinus, Abhandlungen über den 1. Johannesbrief 7,8",
    "found_at": "https://newadvent.org/fathers/170207.htm",
    "finding_de": "«Love, and do what you will»; aus der Wurzel der Liebe kann nur Gutes wachsen."
   }
  ]
 },
 "RCPT-1JN-0003": {
  "date": "2026-10-29",
  "result": "corrected",
  "method_de": "KI-Prüfung (Claude) vom 2026-10-29: Angaben mit Websuche in frei zugänglichen Textausgaben bzw. Nachschlagewerken nachgeschlagen; nur Fundstelle und eigene Zusammenfassung übernommen; keine fachliche Prüfung.",
  "checked": [
   {
    "source": "Erasmus und das Comma Johanneum",
    "found_at": "https://dick.wursten.be/preken/Erasmus%20and%20the%20Comma%20Johanneum%20door%20H.J.%20de%20Jonge.htm (H. J. de Jonge)",
    "finding_de": "Erasmus liess den Zusatz 1516 und 1519 weg und nahm ihn 1522 auf; die von ihm geprüften griechischen Handschriften hatten ihn nicht. Vorher nur «1516» genannt; ergänzt."
   }
  ]
 },
 "RCPT-1JN-0004": {
  "date": "2026-10-29",
  "result": "corrected",
  "method_de": "KI-Prüfung (Claude) vom 2026-10-29: Angaben mit Websuche in frei zugänglichen Textausgaben bzw. Nachschlagewerken nachgeschlagen; nur Fundstelle und eigene Zusammenfassung übernommen; keine fachliche Prüfung.",
  "checked": [
   {
    "source": "Hymnus «Ubi caritas»",
    "found_at": "https://en.wikipedia.org/wiki/Ubi_caritas",
    "finding_de": "Paulinus von Aquileia zugeschrieben (um 796); lange zur Fusswaschung am Gründonnerstag, heute zur Gabenbereitung der Abendmahlsmesse; Taizé-Fassung. Vorher «seit dem Frühmittelalter» und «gehört zur Fusswaschung»; berichtigt. Der Bezug zu [[1JN.4.16]] ist eine eigene Beobachtung (nicht an der Fundstelle)."
   }
  ]
 },
 "RCPT-1JN-0005": {
  "date": "2026-10-29",
  "result": "confirmed",
  "method_de": "KI-Prüfung (Claude) vom 2026-10-29: Angaben mit Websuche in frei zugänglichen Textausgaben bzw. Nachschlagewerken nachgeschlagen; nur Fundstelle und eigene Zusammenfassung übernommen; keine fachliche Prüfung.",
  "checked": [
   {
    "source": "Irenäus, Gegen die Häresien 3,16,5",
    "found_at": "https://bkv.unifr.ch/en/works/cpg-1306/compare/gegen-die-haresien-bkv/492/against-heresies",
    "finding_de": "Irenäus zitiert [[1JN.2.18]] ff. als Brief des Johannes, des Jüngers des Herrn, gegen eine Lehre, die den Herrn teilt."
   }
  ]
 }
}
for _x in RECEPTIONS:
    _x["source_check"] = SOURCE_CHECKS[_x["id"]]

# Zweite Quellenprüfung durch eine weitere Instanz (2026-10-29)
RECHECK_DE = " Am 2026-10-29 von einer weiteren Instanz (getrennte KI-Prüfung, Claude) erneut nachgeschlagen; keine fachliche Prüfung."
RECHECKED = ["RCPT-1JN-0002", "RCPT-1JN-0003", "RCPT-1JN-0004"]
RECHECK_EXTRA = {}
for _x in RECEPTIONS:
    if _x["id"] in RECHECKED:
        _sc = dict(_x["source_check"])
        _sc["method_de"] = _sc["method_de"] + RECHECK_DE
        if _x["id"] in RECHECK_EXTRA:
            _sc["checked"] = _sc["checked"] + [RECHECK_EXTRA[_x["id"]]]
        _x["source_check"] = _sc

# Prüfvermerk der Prüfrunde vom 2026-10-29 (getrennte Instanz; docs/WEITERDENKEN.md, Feld check)
CHECK = {"date": "2026-10-29", "by": "weitere Instanz (KI)", "limits_de": "Nicht gegen den Urtext geprüft, sondern gegen die hochdeutsche und die Mundart-Arbeitsübersetzung (Zitate per Skript wörtlich verglichen); Quellen der Rezeption nur in frei zugänglichen Ausgaben nachgeschlagen; keine fachliche und keine muttersprachliche Prüfung durch eine Person.", "process": "PROC-WEITERDENKEN@1.0"}
# in der Prüfung (oder bei der Zitat-Prüfung am selben Tag) berichtigt
CHECK_CORRECTED = ["RCPT-1JN-0002", "RCPT-1JN-0003", "RCPT-1JN-0004", "REFL-1JN-0004", "REFL-1JN-0005", "REFL-1JN-0009", "REFL-1JN-0010", "REFL-1JN-0011", "REFL-1JN-0012", "REFL-1JN-0013", "REFL-1JN-0015", "REFL-1JN-0016", "REFL-1JN-0019", "REFL-1JN-0020", "REFL-1JN-0021", "REFL-1JN-0022", "REFL-1JN-0023", "REFL-1JN-0024", "REFL-1JN-0025", "REFL-1JN-0026", "REFL-1JN-0027", "REFL-1JN-0028", "REFL-1JN-0030", "REFL-1JN-0032", "REFL-1JN-0033", "REFL-1JN-0034", "REFL-1JN-0037", "REFL-1JN-0038", "REFL-1JN-0039"]
