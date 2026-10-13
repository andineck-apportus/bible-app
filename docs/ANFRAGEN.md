# Anfragen an Rechteinhaber

Stand 13. Oktober 2026. Gehört zum Quellenkatalog (`data/sources/`, Quellenkarte `app/quellenkarte/index.html`). Hier stehen die Quellen der Klasse «auf Anfrage», bei denen sich eine Anfrage lohnt, mit Kontakt und Entwurf. Gesendete Anfragen und Antworten bitte unten im Protokoll eintragen; eine Zusage wird erst nach schriftlicher Bestätigung im Katalog als Recht vermerkt.

## «Anfrage» und «Erlaubnis»: kein Unterschied

Beides meint dasselbe: Die Daten sind nicht offen lizenziert, eine Übernahme braucht eine schriftliche Erlaubnis des Rechteinhabers. Im Katalog heisst es jetzt einheitlich «Anfrage». Innerhalb dieser Klasse gibt es drei Fälle:

| Fall | Beispiele | Was eine Anfrage bringen kann |
|---|---|---|
| Lizenz verhandelbar | Deutsche Bibelgesellschaft, United Bible Societies, Crossway (Tyndale House GNT) | Nutzungsrecht für Daten, oft für Gemeinnützige günstiger oder gratis |
| Nur lesen | Editio Critica Maior online, PHI-Inschriften, Biblindex | Erlaubnis, Daten zu übernehmen; sonst bleibt es beim Zitieren |
| Bilder von Handschriften | Israel Antiquities Authority (Qumran), CSNTM, Cambridge (Geniza), Vatikan | Erlaubnis, einzelne Abbildungen zu zeigen |

Nicht in diese Klasse gehört CATSS (Septuaginta): Dort genügt eine unterschriebene Nutzungserklärung, keine Verhandlung.

## Liste nach Nutzen für das Projekt

| Rang | Stelle | Was | Wozu | Kontakt | Kontakt geprüft |
|---|---|---|---|---|---|
| 1 | Deutsche Bibelgesellschaft (DBG), Stuttgart | Apparat NA28, BHS-Apparat, Rahlfs-Hanhart, Stuttgarter Vulgata; ggf. kommerzielle BHSA-Nutzung | Kuratierter textkritischer Apparat, die grösste Lücke | Formular <https://www.die-bibel.de/en/permission-enquiry-form>; für ganze Testamente schriftlich an Ilona Raiser, raiser@dbg.de, +49 711 7181-244 (<https://die-bibel.de/en/rights>) | 2026-10-09 (docs/QUELLEN.md) |
| 2 | Institut für Neutestamentliche Textforschung (INTF), Münster | Daten der digitalen Editio Critica Maior (Markus, Apostelgeschichte; Varianten, Zeugen, CBGM), Nutzung der NTVMR-Schnittstelle | Bewertete Handschriftenbelege statt maschineller Zuordnung | intf@uni-muenster.de, +49 251 83-22581; Pferdegasse 1, 48143 Münster; Leitung Prof. Dr. Holger Strutwolf (<https://www.uni-muenster.de/INTF/impressum.html>) | 2026-10-13 |
| 3 | CATSS / CCAT, University of Pennsylvania | Nutzungserklärung für die Septuaginta-Daten (Rahlfs mit Morphologie) | Septuaginta im Vergleich und in der Textkritik (in `data-nc/`) | Laut Readme per Post an CCAT (R. Kraft), 201 Logan Hall, 249 S. 36th Street, University of Pennsylvania, Philadelphia, PA 19104-6304; kraft@ccat.sas.upenn.edu (<https://ccat.sas.upenn.edu/gopher/text/religion/biblical/lxxvar/0-readme.txt>). Das Readme ist alt; vorher per E-Mail fragen, ob die Adresse noch gilt | 2026-10-13 (Angabe veraltet möglich) |
| 4 | United Bible Societies | Semantic Dictionary of Biblical Hebrew (SDBH) und MARBLE/Louw-Nida-Bedeutungen in MACULA | Wortbedeutungen nach Bedeutungsfeldern im Wort-Blatt | info@biblesocieties.org bzw. Kontaktformular <https://translation.bible/contact/>; ob dort Lizenzanfragen bearbeitet werden, ist nicht angegeben | 2026-10-13 (Zuständigkeit ungeprüft) |
| 5 | Crossway / Tyndale House, Cambridge | Text des Tyndale House GNT als Daten | Weitere moderne Edition im Vergleich | Rechte bei Crossway («Used by permission of Crossway»); Kontakt über <https://www.crossway.org> (Rubrik Permissions), Adresse vor Versand prüfen | ungeprüft |
| 6 | Israel Antiquities Authority (Leon Levy Dead Sea Scrolls Digital Library) | Abbildungen biblischer Qumranrollen | Faksimile zu Lesarten im AT | contact@deadseascrolls.org.il (<https://www.deadseascrolls.org.il/terms>) | 2026-10-13 |
| 7 | CSNTM, Plano (Texas) | Abbildungen von NT-Handschriften | Faksimile zu Lesarten im NT; braucht zusätzlich die Erlaubnis der besitzenden Bibliothek | manuscripts@csntm.org (<https://www.csntm.org/terms-of-use-copyright/>) | 2026-10-13 |
| 8 | Cambridge University Library (Taylor-Schechter Genizah) | Abbildungen von Geniza-Fragmenten | Masoretische Textgeschichte, später | genizah@lib.cam.ac.uk | 2026-10-09 (docs/QUELLEN.md) |

Keine Anfrage nötig oder sinnvoll: Göttinger Septuaginta, BHQ, HALOT, BDAG, moderne deutsche Bibeln (nur zitieren); ECM-Druck (über DBG, siehe Rang 1).

## Würde ein gemeinnütziger Verein helfen?

Ja, in drei Punkten:

1. **Nicht kommerzielle Lizenzen** (CC BY-NC, CATSS) setzen voraus, dass die Nutzung nicht auf Gewinn zielt. Ein Verein mit gemeinnützigem Zweck macht das nach aussen klar und bindet es in den Statuten fest. Der Grundsatz in [LIZENZEN.md](../LIZENZEN.md) geht bereits von einem solchen Verein als Betreiber aus.
2. **Anfragen** an Bibelgesellschaften und Institute haben mehr Gewicht, wenn eine Körperschaft mit klarem Zweck anfragt, etwa «die Bibel für das Studium verständlicher machen, frei zugänglich». Die DBG und die UBS geben Daten für gemeinnützige Bibelarbeit oft günstiger oder gratis ab; Zusagen sind aber Einzelfälle.
3. **Verantwortung:** Lizenzverträge und Nutzungserklärungen braucht es mit einer Vertragspartei. Ein Verein trägt sie statt einer Privatperson.

Was ein Verein nicht ändert: Geschützte Werke (NA28, BHQ, BDAG) bleiben geschützt. Auch für einen Verein gilt «nicht kommerziell» nur, solange kein Erwerbszweck verfolgt wird; Werbung oder bezahlte Funktionen in der App können das gefährden, Spenden in der Regel nicht.

In der Schweiz entsteht ein Verein mit schriftlichen Statuten und einer Gründungsversammlung (Art. 60 ff. ZGB); ein Eintrag ins Handelsregister ist meist nicht nötig. Für eine Steuerbefreiung wegen Gemeinnützigkeit entscheidet die kantonale Steuerverwaltung. Keine Rechtsberatung; für Statuten und Steuerfragen eine Fachperson beiziehen.

Die Entwürfe unten sind so geschrieben, dass sie mit oder ohne Verein passen: `[Absender]` ist entweder der Verein oder Andi Neck als Projektverantwortlicher.

## Entwürfe

Platzhalter: `[Absender]`, `[Adresse]`, `[Link]` (Lesestrom oder GitHub `andineck-apportus/bible-app`), `[Datum]`.

### 1. Deutsche Bibelgesellschaft (Deutsch)

> **Betreff:** Anfrage Nutzungsrecht: Apparatdaten NA28/BHS für ein gemeinnütziges Bibelstudienprojekt
>
> Sehr geehrte Frau Raiser
>
> [Absender] entwickelt eine frei zugängliche Studien-App, die die Bibel aus dem Urtext erschliesst: eigene Übersetzungen aus dem Hebräischen und Griechischen mit Wortzuordnung, Lesarten mit Bewertung ihrer Gesichertheit und Hintergrund zur Entstehung. Ziel ist, die Bibel für das Studium verständlicher zu machen; das Projekt ist gemeinnützig und verfolgt keinen Erwerbszweck. Eine Vorschau: [Link].
>
> Wir verwenden bisher nur offen lizenzierte Daten (SBLGNT mit Apparat, Westminster Leningrad Codex, MACULA). Die grösste Lücke ist ein kuratierter textkritischer Apparat. Wir fragen deshalb an, ob und zu welchen Bedingungen wir folgende Daten in der App verwenden dürfen:
>
> 1. Apparat des Novum Testamentum Graece (NA28) in maschinenlesbarer Form, zunächst für einzelne Bücher (Markus, Philipper, Titus);
> 2. Apparat der Biblia Hebraica Stuttgartensia für einzelne Bücher (Rut, Obadja);
> 3. Text des Rahlfs-Hanhart als Vergleich zum hebräischen Text.
>
> Die Daten würden getrennt von unseren frei lizenzierten Inhalten gespeichert, mit vollständiger Quellenangabe angezeigt und nicht an Dritte weitergegeben. Gerne beschreiben wir Umfang und technische Umsetzung genauer.
>
> Freundliche Grüsse
> [Absender], [Adresse]

### 2. INTF Münster (Deutsch)

> **Betreff:** Anfrage: Nutzung der ECM-Daten (Markus, Apostelgeschichte) und der NTVMR-Schnittstelle in einer gemeinnützigen Studien-App
>
> Sehr geehrter Herr Professor Strutwolf
> Sehr geehrte Damen und Herren
>
> [Absender] entwickelt eine frei zugängliche Studien-App zum Neuen Testament, die Lesarten bis zu den Handschriften nachvollziehbar macht ([Link]). Bisher ordnen wir Handschriften maschinell aus den CNTR-Transkriptionen den Variantenstellen des SBLGNT-Apparats zu und kennzeichnen das als ungeprüft.
>
> Wir möchten stattdessen auf die Daten der digitalen Editio Critica Maior zurückgreifen, zuerst für Markus: Variantenstellen, Lesarten und Zeugen. Dürfen wir diese Daten in der App anzeigen und speichern, und unter welcher Lizenz? Ausserdem möchten wir wissen, ob die Transkriptionen über die NTVMR-Schnittstelle unter CC BY 4.0 genutzt werden dürfen und ob es Regeln für die Zahl der Abfragen gibt.
>
> Das Projekt ist gemeinnützig; alle Daten erscheinen mit Quellenangabe, und Korrekturen melden wir gerne zurück.
>
> Freundliche Grüsse
> [Absender], [Adresse]

### 3. CATSS (Englisch, Vorabfrage per E-Mail)

> **Subject:** CATSS LXX user declaration: current procedure?
>
> Dear Professor Kraft,
>
> We are building a free, non-commercial Bible study application that explains the biblical text from the original languages ([Link]). We would like to use the CATSS LXX morphological text, under the terms of the CCAT user declaration, to show the Septuagint alongside the Hebrew text.
>
> Could you tell us whether the user declaration is still to be sent to the address in the readme (201 Logan Hall), or whether there is a current form or e-mail procedure? We will acknowledge CATSS in the application and keep the data separate from our openly licensed content.
>
> With kind regards,
> [Absender], [Adresse]

### 4. United Bible Societies (Englisch)

> **Subject:** Permission request: SDBH and MARBLE domains in a non-profit Bible study app
>
> Dear Sir or Madam,
>
> [Absender] is developing a free, non-profit Bible study application that translates directly from the Hebrew and Greek, with word-by-word alignment and explanations for readers without the biblical languages ([Link]). We use MACULA Hebrew and MACULA Greek (CC BY 4.0).
>
> The MACULA files also contain data from the Semantic Dictionary of Biblical Hebrew and the MARBLE semantic domains, marked "used with permission". We have left these fields out. May we use them in our application, and under what conditions? They would be shown with full attribution and not passed on to third parties.
>
> If this address is not the right one, we would be grateful for a pointer to the responsible office.
>
> With kind regards,
> [Absender], [Adresse]

### 5. Crossway / Tyndale House (Englisch)

> **Subject:** Permission request: Tyndale House Greek New Testament as comparison text
>
> Dear Sir or Madam,
>
> [Absender] is developing a free, non-profit Bible study application that shows textual variants of the Greek New Testament with the editions that support each reading ([Link]). We currently compare the SBLGNT, Westcott-Hort, Robinson-Pierpont and others. We would like to add the Tyndale House Greek New Testament as a comparison text, word by word. May we use the text for this purpose, and under what conditions?
>
> With kind regards,
> [Absender], [Adresse]

### 6. Bilder: Israel Antiquities Authority, CSNTM (Englisch, Vorlage)

> **Subject:** Image permission request: [Handschrift, Fragment, Stelle]
>
> Dear Sir or Madam,
>
> [Absender] is developing a free, non-profit Bible study application ([Link]). Where manuscripts differ, readers can trace a reading back to the manuscript. We would like to show the following image(s) next to our transcription:
>
> - [Handschrift / Inventarnummer, Seite, Bibelstelle, Bild-ID oder Link]
>
> The images would be shown at screen resolution with full credit as you specify, not offered for download, and not passed on. Please let us know whether this is possible and what conditions or fees apply. [Nur CSNTM: We understand that the owning institution's permission is also needed; please let us know whom to contact.]
>
> With kind regards,
> [Absender], [Adresse]

## Protokoll

| Datum | Stelle | Gesendet von | Antwort | Folge im Katalog |
|---|---|---|---|---|
| – | – | – | – | – |
