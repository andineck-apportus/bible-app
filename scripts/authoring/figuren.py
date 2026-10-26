#!/usr/bin/env python3
"""Figurenbaukasten: Aussehen der Personen, Rollen und Gruppen des Bildlexikons für alle Bildstile.

Je Lexikon-Eintrag Parameter (Gewand, Mantel, Haar, Bart, Kopfbedeckung, Alter, Attribut), abgeleitet aus den
Pflichtmerkmalen und der Palette des Lexikons (data/illustrations/lexicon/). Aus denselben Parametern entstehen
- im Stil «Symbol» ein Bauteil ``ill-p-<name>`` (Ganzfigur ohne Gesicht, viewBox 0 0 30 64),
- im Stil «Anime» eine Figur für das Brustbild (``CHAR`` in bilder_anime.py).
So sieht eine Figur in beiden Stilen gleich aus (gleiche Farben, gleiche Zeichen). Handgezeichnete Figuren
(ill-p-jesus, ill-p-maria …) bleiben unverändert; hier stehen nur die übrigen.

Attribute (ill-a-*) sind kleine Bauteile, die eine Figur trägt (Schlüssel, Ähren …); sie stehen nicht im Lexikon,
sondern gehören zur Figur. Gegenstände, die selbst handeln oder gezeigt werden, sind Lexikon-Einträge (bildsymbole.py).

KI-Entwurf (Claude) vom 2026-10-17 auf Wunsch von Andi Neck; eigene Zeichnungen (CC0), keine fachliche Prüfung.
"""
INK = "#3B3226"
SKIN = "#C89B72"

# ------------------------------------------------------------------ Attribute (klein, viewBox 0 0 16 16)
ATTR = {
    "schluessel": '<g fill="none" stroke="#C08A2A" stroke-width="1.8" stroke-linecap="round"><circle cx="5" cy="5" r="3.2"/><path d="M7.4 7.4l6.4 6.4M11 11l1.8-1.8M12.6 12.6l1.6-1.6"/></g>',
    "winkelmass": '<path d="M3 2v11h11" fill="none" stroke="#8C8070" stroke-width="2.4" stroke-linejoin="round"/>',
    "kreuzstab": '<path d="M8 1v15M4.5 4.5h7" stroke="#7A5A34" stroke-width="1.8" stroke-linecap="round"/>',
    "muschel": '<path d="M8 14L2 5q6-5 12 0z" fill="#F2E6CC" stroke="#3B3226" stroke-width=".8"/><path d="M8 14L5 4M8 14V3M8 14l3-10" stroke="#B4A98F" stroke-width=".7"/>',
    "buch": '<path d="M2 3h6v11H2zM8 3h6v11H8z" fill="#F4F1EA" stroke="#3B3226" stroke-width=".8"/><path d="M13 1l2 6" stroke="#3B3226" stroke-width="1"/>',
    "feigenblatt": '<path d="M8 15V8M8 8Q2 9 2 4q3 1 4-2 2 2 2 2 0 0 2-2 1 3 4 2 0 5-6 4z" fill="#5E7F3A" stroke="#3B3226" stroke-width=".7"/>',
    "aehren": '<g stroke="#B08A2A" stroke-width="1.1" stroke-linecap="round"><path d="M5 15L7 3M8 15V2M11 15L9 3"/></g><g fill="#E8B84A" stroke="#B08A2A" stroke-width=".5"><ellipse cx="7" cy="4" rx="1.4" ry="2.4"/><ellipse cx="8" cy="3" rx="1.4" ry="2.4"/><ellipse cx="9.2" cy="4" rx="1.4" ry="2.4"/></g>',
    # Worfelgabel: langer Stiel mit fünf Zinken, dazu Gerstenkörner (Rut 3,2); vorher Schaufelblatt, las sich als Hammer/Axt (Blindtest 2026-10-23)
    "worfel": '<path d="M2.2 15.6L9.4 6.4" stroke="#7A5A34" stroke-width="1.7" stroke-linecap="round"/><path d="M7 4.6Q9.4 6.9 11.8 8.2" fill="none" stroke="#7A5A34" stroke-width="1.5" stroke-linecap="round"/>'
              '<path d="M7 4.6L9.2.8M8.2 5.6l2.4-3.8M9.4 6.4l2.8-3.4M10.6 7.3l3.2-2.9M11.8 8.2L15.4 6" stroke="#7A5A34" stroke-width="1.05" stroke-linecap="round"/>'
              '<g fill="#E8B84A" stroke="#B08A2A" stroke-width=".35"><ellipse cx="3.6" cy="3.4" rx=".7" ry="1.1" transform="rotate(-30 3.6 3.4)"/><ellipse cx="5.4" cy="1.6" rx=".7" ry="1.1" transform="rotate(20 5.4 1.6)"/>'
              '<ellipse cx="2.2" cy="6.4" rx=".7" ry="1.1" transform="rotate(50 2.2 6.4)"/><ellipse cx="13.8" cy="11" rx=".7" ry="1.1" transform="rotate(-20 13.8 11)"/></g>',
    # Sandale (von oben): Sohle mit Riemen und Zehenriemen, gross (Rut 4,8); vorher kleiner Schuh von der Seite (Blindtest 2026-10-23)
    "schuh": '<g transform="rotate(28 8 8)"><path d="M8 .6Q11.6.6 11.6 4.6q0 2.8-.9 4.8-.6 1.8-.4 3.4.1 2.4-2.3 2.6-2.5.1-2.8-2.6-.2-2.2-.9-4Q3.6 6.8 4.3 4.2 5.1.6 8 .6z" fill="#C49A62" stroke="#3B3226" stroke-width=".8"/>'
             '<path d="M8 1.8q2.6.2 2.5 3" fill="none" stroke="#E2C08A" stroke-width=".6"/><path d="M4.6 5.2Q8 7.4 11.4 5.2M5 8.8Q8 10.8 10.8 8.8" fill="none" stroke="#5B3A20" stroke-width="1.5"/>'
             '<path d="M7.6 1.6l.5 4.6" stroke="#5B3A20" stroke-width="1"/><path d="M6.4 14.2q1.8 1 3.4 0" fill="none" stroke="#5B3A20" stroke-width="1.2"/></g>',
    "salbgefaess": '<path d="M5 6h6l1 8H4z" fill="#E9D8B4" stroke="#3B3226" stroke-width=".8"/><path d="M6 6V4h4v2" fill="#C9B48E" stroke="#3B3226" stroke-width=".8"/><path d="M5 3h6v1.4H5z" fill="#8E3B5E"/>',
    "flaeschchen": '<path d="M6.5 3h3v3l1.5 2v7h-6V8l1.5-2z" fill="#E9D8B4" stroke="#3B3226" stroke-width=".8"/><path d="M6.5 2h3v1.4h-3z" fill="#6B8E7A"/>',
    "kelle": '<path d="M12 2L6 9" stroke="#7A5A34" stroke-width="1.6" stroke-linecap="round"/><path d="M2 10a4 3 0 0 0 7 0z" fill="#8C8070" stroke="#3B3226" stroke-width=".8"/>',
    "lampe": '<path d="M2 10q6-5 11 0l2-1v2q-7 4-13-1z" fill="#B07A3E" stroke="#3B3226" stroke-width=".8"/><path d="M13 9q2-4 0-7-1 3 0 7z" fill="#F2B53A"/>',
    "netz": '<path d="M2 3h12l-2 11H4z" fill="none" stroke="#8A6A3A" stroke-width="1"/><path d="M2 3l10 11M6 3l8 8M10 3l4 4M14 3L4 14M10 3l-8 8M6 3L2 7" stroke="#8A6A3A" stroke-width=".6"/>',
    "laterne": '<path d="M8 1v2" stroke="#3B3226" stroke-width="1"/><path d="M4 3h8l-1 10H5z" fill="#F2B53A" stroke="#3B3226" stroke-width=".9"/><path d="M4 13h8v2H4z" fill="#5B4630"/>',
    "stab": '<path d="M9 1v15" stroke="#7A5A34" stroke-width="1.8" stroke-linecap="round"/>',
    "hirtenstab": '<path d="M9 16V5q0-4 3-4t3 3" fill="none" stroke="#7A5A34" stroke-width="1.8" stroke-linecap="round"/>',
    "kette": '<g fill="none" stroke="#6A6A6A" stroke-width="1.2"><ellipse cx="3" cy="8" rx="2.4" ry="1.6"/><ellipse cx="7" cy="8" rx="2.4" ry="1.6"/><ellipse cx="11" cy="8" rx="2.4" ry="1.6"/></g><path d="M13.6 8l1.8-2M13.6 8l1.8 2" stroke="#6A6A6A" stroke-width="1"/>',
    "leinentuch": '<path d="M2 3h12v11H2z" fill="#F6EBD9" stroke="#3B3226" stroke-width=".8"/><path d="M2 6h12M2 9h12" stroke="#D8CBB0" stroke-width=".8"/>',
    "beutel": '<path d="M5 5q-3 3-3 6 0 3 6 3t6-3q0-3-3-6z" fill="#7A8A5A" stroke="#3B3226" stroke-width=".8"/><path d="M5 5h6" stroke="#5B4630" stroke-width="1.4"/>',
    "brief": '<path d="M2 3h9l3 3v8H2z" fill="#F4F1EA" stroke="#3B3226" stroke-width=".8"/><path d="M4 7h7M4 10h8" stroke="#A79A80" stroke-width=".8"/><circle cx="11" cy="11.5" r="1.6" fill="#A33A2E"/>',
    "rolle": '<path d="M3 4h10v8H3z" fill="#F4F1EA" stroke="#3B3226" stroke-width=".7"/><rect x="1.5" y="3" width="2.6" height="10" rx="1.3" fill="#B07A3E" stroke="#3B3226" stroke-width=".6"/><rect x="11.9" y="3" width="2.6" height="10" rx="1.3" fill="#B07A3E" stroke="#3B3226" stroke-width=".6"/><circle cx="8" cy="11" r="1.4" fill="#A33A2E"/>',
    "feder": '<path d="M3 15Q6 6 14 2q-2 7-9 10" fill="#F4F1EA" stroke="#3B3226" stroke-width=".8"/><path d="M1 13h5v2H1z" fill="#2E2017"/>',
    "muenzen": '<circle cx="5" cy="10" r="3" fill="#D9A441" stroke="#9C6F1C" stroke-width=".7"/><circle cx="10" cy="9" r="3" fill="#D9A441" stroke="#9C6F1C" stroke-width=".7"/><circle cx="7.5" cy="5.5" r="3" fill="#C9C2B4" stroke="#8C8070" stroke-width=".7"/>',
    "zwei-muenzen": '<circle cx="5.5" cy="9" r="2.6" fill="#B07A3E" stroke="#6A4A2A" stroke-width=".7"/><circle cx="10.5" cy="9" r="2.6" fill="#B07A3E" stroke="#6A4A2A" stroke-width=".7"/>',
    "matte": '<path d="M1 9h14v4H1z" fill="#C9B48E" stroke="#3B3226" stroke-width=".8"/><path d="M3 9v4M6 9v4M9 9v4M12 9v4" stroke="#A79A80" stroke-width=".6"/>',
    "tuer": '<path d="M3 1h10v15H3z" fill="#8A6A3A" stroke="#3B3226" stroke-width=".9"/><circle cx="11" cy="9" r=".9" fill="#D9A441"/>',
    "tuer-offen": '<path d="M3 1h10v15H3z" fill="#3B3226"/><path d="M3 1l5 2v14l-5-1z" fill="#8A6A3A" stroke="#3B3226" stroke-width=".7"/>',
    "garbe": '<g stroke="#B08A2A" stroke-width="1" stroke-linecap="round"><path d="M4 15L7 4M8 15V3M12 15L9 4M6 15l2-11M10 15L8 4"/></g><path d="M5 11h6" stroke="#8A6A3A" stroke-width="1.6"/><g fill="#E8B84A"><ellipse cx="7" cy="4" rx="1.3" ry="2.2"/><ellipse cx="8" cy="3" rx="1.3" ry="2.2"/><ellipse cx="9" cy="4" rx="1.3" ry="2.2"/></g>',
    "tinte": '<path d="M4 8h7v6H4z" fill="#2E2017"/><path d="M9 9L14 1" stroke="#F4F1EA" stroke-width="1.2"/><path d="M9 9L14 1" stroke="#3B3226" stroke-width=".4"/>',
    "myrrhe": '<path d="M4 6h8v8H4z" fill="#C9B48E" stroke="#3B3226" stroke-width=".8"/><path d="M4 6l1-2h6l1 2" fill="#A07A44" stroke="#3B3226" stroke-width=".7"/>',
    "kind": '<circle cx="8" cy="4.6" r="3.2" fill="#C89B72" stroke="#3B3226" stroke-width=".7"/><path d="M4.8 4.4Q4.6 1 8 1t3.2 3.4Q10 2.6 8 2.6T4.8 4.4z" fill="#3A2618"/><path d="M4.4 15.6q-.4-6.4 3.6-7.2 4 .8 3.6 7.2z" fill="#E8B84A" stroke="#3B3226" stroke-width=".7"/><path d="M4.8 10.4l-2.4 2.4M11.2 10.4l2.4 2.4" stroke="#C89B72" stroke-width="1.3" stroke-linecap="round"/>',
    # Ergänzt nach dem Blindtest 2026-10-23 (reports/figuren-blindtest-2026-10-23.json): je Figur ein eigenes, im Text oder in der Tradition begründetes Zeichen
    "fisch": '<path d="M1.2 9.6Q5 3.2 11 6.6l3.6-3v9.4L11 10.4Q5 14.6 1.2 9.6z" fill="#5A8AB0" stroke="#3B3226" stroke-width=".8"/><path d="M8 7.2q1 1.8 0 4M5.6 10.6q1.6.8 3.4.2" fill="none" stroke="#2E5478" stroke-width=".6"/><circle cx="3.8" cy="8.4" r=".8" fill="#3B3226"/>',
    "brief-feder": '<path d="M1.5 4h8.5l2 2v9.5H1.5z" fill="#F4F1EA" stroke="#3B3226" stroke-width=".8"/><path d="M3.2 7.4h6M3.2 9.6h7M3.2 11.8h5" stroke="#A79A80" stroke-width=".8"/><path d="M8.6 13.6Q10 6 15.4.6q.6 5.4-5 9.6" fill="#FFFDF6" stroke="#3B3226" stroke-width=".7"/><path d="M8.6 13.6l3.4-7.4" stroke="#3B3226" stroke-width=".5"/>',
    "blind": '<path d="M.8 8.4Q8 1.4 15.2 8.4 8 15.4.8 8.4z" fill="#FFFDF6" stroke="#3B3226" stroke-width="1"/><circle cx="8" cy="8.4" r="2.4" fill="#3B3226"/><path d="M2.2 14.6L13.8 2.2" stroke="#A33A2E" stroke-width="2" stroke-linecap="round"/>',
    "rolle-feder": '<path d="M2.6 5h8v8.6h-8z" fill="#F4F1EA" stroke="#3B3226" stroke-width=".7"/><path d="M4 7.6h5M4 9.6h5M4 11.6h3.4" stroke="#A79A80" stroke-width=".7"/><rect x="1" y="4" width="2.6" height="10.6" rx="1.3" fill="#B07A3E" stroke="#3B3226" stroke-width=".6"/><rect x="9.6" y="4" width="2.6" height="10.6" rx="1.3" fill="#B07A3E" stroke="#3B3226" stroke-width=".6"/><path d="M11 13L15.4 1" stroke="#3B3226" stroke-width="1.6" stroke-linecap="round"/><path d="M11 13L15.4 1" stroke="#C9A86A" stroke-width=".8" stroke-linecap="round"/>',
    "alabaster": '<path d="M4.8 15.4Q1.8 12 3.2 8.4 4 6.6 6 6.4h4q2 .2 2.8 2 1.4 3.6-1.6 7z" fill="#F2EADA" stroke="#3B3226" stroke-width=".8"/><path d="M6.2 6.4V4.4h3.6v2" fill="#E2D6BE" stroke="#3B3226" stroke-width=".7"/><path d="M5 2.6h6v1.8H5z" fill="#8E3B5E" stroke="#3B3226" stroke-width=".6"/><circle cx="8" cy="1.8" r="1" fill="#8E3B5E" stroke="#3B3226" stroke-width=".5"/><path d="M4.4 10.6q3.6 1 7.2 0" fill="none" stroke="#C9B48E" stroke-width=".7"/>',
    "oelkrug": '<path d="M5 15q-3.6-1.4-3.2-5.2Q2.2 6.6 6 6.2h4q3.8.4 4.2 3.6.4 3.8-3.2 5.2z" fill="#B07A3E" stroke="#3B3226" stroke-width=".8"/><path d="M6 6.2l.4-2.6h3.2l.4 2.6" fill="#B07A3E" stroke="#3B3226" stroke-width=".7"/><path d="M5.6 2.6h4.8v1.2H5.6z" fill="#6E7F5A"/><path d="M3 10.4h10" stroke="#E8C98E" stroke-width=".9"/>',
    "wasserkrug": '<path d="M4.6 15.4Q2 11.4 3 7.6 3.8 5.4 5.8 5h4.4q2 .4 2.8 2.6 1 3.8-1.6 7.8z" fill="#B4643A" stroke="#3B3226" stroke-width=".8"/><path d="M6 5V2.6h4V5" fill="#B4643A" stroke="#3B3226" stroke-width=".7"/><path d="M5.6 6.4Q2 5.4 2.4 9M10.4 6.4q3.6-1 3.2 2.6" fill="none" stroke="#3B3226" stroke-width="1"/><path d="M3.4 10h9.2" stroke="#E8C98E" stroke-width=".8"/><path d="M6.6 1.4q1.4 1 2.8 0" fill="none" stroke="#6FA8D8" stroke-width="1"/>',
    "traube": '<path d="M8 4.6V1.4" stroke="#5B4630" stroke-width="1.2" stroke-linecap="round"/><path d="M8 3Q11 .4 14.4 2.4 12.6 5.6 8.6 4.4z" fill="#6E8B3D" stroke="#3B3226" stroke-width=".6"/><g fill="#6A3A6E" stroke="#3B3226" stroke-width=".5"><circle cx="5.6" cy="6.2" r="1.7"/><circle cx="8.8" cy="6.2" r="1.7"/><circle cx="4.4" cy="9" r="1.7"/><circle cx="7.2" cy="8.8" r="1.7"/><circle cx="10.2" cy="8.8" r="1.7"/><circle cx="5.8" cy="11.6" r="1.7"/><circle cx="8.8" cy="11.6" r="1.7"/><circle cx="7.4" cy="14.2" r="1.7"/></g>',
    "daemon": '<path d="M9 13Q3.4 12.6 3 7.6q-.2-3.2 2.2-5.4Q5 5 6.8 5.6 6.4 2.6 9 1q-.2 2.8 1.8 4 2.6 2 2.2 4.8Q12.6 13.2 9 13zM6 13.4q-1.4 1.4-3.4 1.2M10.4 13.4q.8 1.6 2.6 2" fill="#4A4050" stroke="#2A2430" stroke-width=".6" opacity=".9"/>',
    "muschelstab": '<path d="M12 1v15" stroke="#7A5A34" stroke-width="1.8" stroke-linecap="round"/><path d="M6 13.4L1.4 6.6Q2 2 6 1.6q4 .4 4.6 5z" fill="#F2C78E" stroke="#3B3226" stroke-width=".8"/><path d="M6 13.4L3 4.4M6 13.4l-1-10M6 13.4l1-10M6 13.4l3-9" stroke="#B07A3E" stroke-width=".7"/><path d="M4.6 12.4h2.8v1.8H4.6z" fill="#F2C78E" stroke="#3B3226" stroke-width=".6"/><path d="M7.2 9.4l4.8-3" stroke="#5B4630" stroke-width=".8"/>',
    "geldbeutel": '<path d="M5 6q-3.4 3-3.4 6.2 0 3 6.4 3t6.4-3Q14.4 9 11 6z" fill="#7A3E2A" stroke="#3B3226" stroke-width=".8"/><path d="M5 6q3-1.6 6 0M6 5.6L4.6 2.6M10 5.6l1.4-3" stroke="#D9A441" stroke-width="1.1" stroke-linecap="round" fill="none"/><circle cx="8" cy="11" r="2.4" fill="#E0B24E" stroke="#9C6F1C" stroke-width=".6"/><circle cx="12.6" cy="2.6" r="1.6" fill="#E0B24E" stroke="#9C6F1C" stroke-width=".5"/>',
    "gebetsriemen": '<path d="M2 12Q8 8 14 12" fill="none" stroke="#2E2017" stroke-width="1.6"/><path d="M5.2 3.2h5.6v5.6H5.2z" fill="#1E1610" stroke="#5B4630" stroke-width=".6"/><path d="M5.2 3.2l1-1.6h5.6l-1 1.6zM10.8 3.2l1-1.6v5.6l-1 1.6z" fill="#3B3226"/><path d="M8 8.8V11M3 11.4q-1 2 0 4.4M13 11.4q1 2 0 4.4" fill="none" stroke="#2E2017" stroke-width="1.2"/>',
    "feuerrad": '<path d="M3.6 9Q2 4.6 5 2q-.2 2.4 1.4 3Q6.6 1.4 9.8.6 8.8 3 10.6 4q1.6-1.6 1.2-3.4 3.2 3.2 1 8z" fill="#E8783A" stroke="#A3461E" stroke-width=".6"/><circle cx="8" cy="10.4" r="4.6" fill="none" stroke="#7A5A34" stroke-width="1.4"/><path d="M8 5.8v9.2M3.4 10.4h9.2M4.8 7.2l6.4 6.4M11.2 7.2l-6.4 6.4" stroke="#7A5A34" stroke-width=".8"/><circle cx="8" cy="10.4" r="1.2" fill="#5B4630"/>',
    "leinen": '<path d="M2 2.4h12l-.6 4.6 1 8.6-2.6-1.4-2.4 1.4-2.4-1.4-2.4 1.4-2.4-1.4L1.6 7z" fill="#F6EBD9" stroke="#3B3226" stroke-width=".8"/><path d="M2 2.4q6 3 12 0" fill="#E2D6BE" stroke="#3B3226" stroke-width=".6"/><path d="M5 5.4l-.4 8.6M8 5.8v8.6M11 5.4l.4 8.6" stroke="#D8CBB0" stroke-width=".7"/>',
    "stab-brief": '<path d="M3.4 1v15" stroke="#7A5A34" stroke-width="1.8" stroke-linecap="round"/><path d="M5.4 4.4h7.4l2 2v8.8H5.4z" fill="#F4F1EA" stroke="#3B3226" stroke-width=".8"/><path d="M7 8h5.6M7 10.4h6" stroke="#A79A80" stroke-width=".8"/><circle cx="12.4" cy="12.8" r="1.4" fill="#A33A2E"/>',
    "blatt-muenzen": '<path d="M1.6 1.6h9.6v10H1.6z" fill="#F4F1EA" stroke="#3B3226" stroke-width=".8"/><path d="M3.2 4.2h6.4M3.2 6.4h6.4M3.2 8.6h4" stroke="#A79A80" stroke-width=".8"/><circle cx="10.4" cy="12.4" r="2.6" fill="#E0B24E" stroke="#9C6F1C" stroke-width=".6"/><circle cx="13.4" cy="10" r="2.2" fill="#C9C2B4" stroke="#8C8070" stroke-width=".6"/>',
    "tafel-griffel": '<path d="M1.6 2.4h10v12.4h-10z" fill="#A07A44" stroke="#3B3226" stroke-width=".8"/><path d="M3 3.8h7.2v9.6H3z" fill="#3B3226"/><path d="M4.2 6h4.6M4.2 8.2h4.6M4.2 10.4h3" stroke="#C9B48E" stroke-width=".6"/><path d="M10.4 13.6L15.2 1.8" stroke="#8C8070" stroke-width="1.3" stroke-linecap="round"/>',
    "frage": '<path d="M1.6 2.4h12.8v9H7l-3.4 3.4v-3.4h-2z" fill="#FFFDF6" stroke="#3B3226" stroke-width=".8"/><path d="M6 5.4q0-1.8 2-1.8t2 1.6q0 1.2-1.4 1.8-.6.4-.6 1.4" fill="none" stroke="#2E5478" stroke-width="1.2" stroke-linecap="round"/><circle cx="8" cy="9.8" r=".7" fill="#2E5478"/>',
    "balken": '<path d="M.6 6.4L14 .8l1.4 3.4L2 9.8z" fill="#9A6A3A" stroke="#3B3226" stroke-width=".8"/><path d="M3 6.6l9.6-4M4.4 7.6l6-2.6" stroke="#6A4A2A" stroke-width=".5"/>',
    "ruder": '<path d="M2.4 15.6L11.6 4.4" stroke="#7A5A34" stroke-width="1.5" stroke-linecap="round"/><path d="M9.8 6.6Q10.4 2.4 13.6.8q2 .4 1.4 2.6-1 3.2-5.2 3.2z" fill="#A07A44" stroke="#3B3226" stroke-width=".7"/><path d="M1.2 12.6l3 2.6" stroke="#7A5A34" stroke-width="1.5" stroke-linecap="round"/>',
    "sack": '<path d="M4 6.4Q1 9 1.6 12.4 2.4 15.6 8 15.6t6.4-3.2Q15 9 12 6.4z" fill="#5E5A52" stroke="#2E2A24" stroke-width=".8"/><path d="M4 6.4q4-1.6 8 0" fill="none" stroke="#2E2A24" stroke-width="1"/><path d="M6 5.8Q6.2 2 8 1.6q1.8.4 2 4.2" fill="#5E5A52" stroke="#2E2A24" stroke-width=".7"/><path d="M5.4 4.8h5.2" stroke="#8A6A3A" stroke-width="1.2"/>',
    # ---- Runde 3 (2026-10-23, Hinweise Projektleiter und Blindtest Runde 2): je Figur ein eigenes, grosses Zeichen für die Brust
    # Hirte: grosses Schaf allein, ohne Stab (Schaf war zu klein, Stab überlud das Zeichen)
    "hirte": '<g fill="#FFFDF6" stroke="#3B3226" stroke-width=".7"><circle cx="5.6" cy="5.4" r="2.6"/><circle cx="8.8" cy="4.6" r="2.6"/><circle cx="12" cy="5.4" r="2.6"/>'
             '<circle cx="13.8" cy="8.4" r="2.4"/><circle cx="12" cy="11" r="2.6"/><circle cx="8.8" cy="11.6" r="2.6"/><circle cx="5.8" cy="11" r="2.6"/><circle cx="4.6" cy="8.2" r="2.4"/></g>'
             '<ellipse cx="9" cy="8.2" rx="5.2" ry="3.6" fill="#FFFDF6"/><path d="M6.6 13.4v2.4M9 13.6v2.2M11.6 13.4v2.4" stroke="#3B3226" stroke-width="1.2" stroke-linecap="round"/>'
             '<ellipse cx="2.8" cy="6.8" rx="2.1" ry="2.6" transform="rotate(-18 2.8 6.8)" fill="#3B3226"/><ellipse cx="4.2" cy="4.2" rx="1.4" ry=".6" transform="rotate(-30 4.2 4.2)" fill="#3B3226"/>'
             '<circle cx="2.2" cy="6.2" r=".45" fill="#FFFDF6"/><path d="M6.6 6.8q1.6-1.2 3.2 0M9.6 9.4q1.6-1 3 0" fill="none" stroke="#D8D2C4" stroke-width=".6"/>',
    # Jakobsmuschel allein, gross, mit Rippen, gewelltem Rand und Ohren am Schloss (vorher Muschel am Stab, las sich als Fächer)
    "jakobsmuschel": None,
    # gerollte Strohmatte: dicke Rolle mit Spirale an der Stirnseite, Geflecht, zwei Schnüren und Strohfransen (las sich als Schriftrolle)
    "matte-rolle": '<g transform="rotate(-24 8 8)"><path d="M1.4 4.4h10.8v7.4H1.4z" fill="#D8BC7A" stroke="#3B3226" stroke-width=".8"/>'
                   '<path d="M2.9 4.4v7.4M4.4 4.4v7.4M5.9 4.4v7.4M7.4 4.4v7.4M8.9 4.4v7.4M10.4 4.4v7.4" stroke="#A8884A" stroke-width=".5"/>'
                   '<path d="M1.4 6.3h10.8M1.4 8.1h10.8M1.4 9.9h10.8" stroke="#B89A5A" stroke-width=".5" stroke-dasharray="1.5 1.5"/>'
                   '<ellipse cx="12.2" cy="8.1" rx="2.6" ry="3.7" fill="#E2CA8E" stroke="#3B3226" stroke-width=".8"/>'
                   '<path d="M12.2 8.1m-.4 0a.5.6 0 1 1 .9.4a1.1 1.5 0 1 1-1.6-1.2a1.7 2.4 0 1 1 2.8 1.8" fill="none" stroke="#8A6A3A" stroke-width=".55"/>'
                   '<path d="M3.6 4.1v8M8.6 4.1v8" stroke="#6A4A2A" stroke-width="1.3"/>'
                   '<path d="M1.4 4.9H0M1.4 6.6H-.2M1.4 8.3H-.3M1.4 10H-.2M1.4 11.3H0" stroke="#B89A5A" stroke-width=".7" stroke-linecap="round"/></g>',
    # verdorrte Hand: fahl, Finger eingekrümmt, mit Falten (Mt 12,10)
    "hand-verdorrt": '<path d="M4.6 15.6V9.6q-.2-3 2.6-3.2h2.8q2.6.2 2.4 3.2v6z" fill="#B0A488" stroke="#3B3226" stroke-width=".8"/>'
                     '<path d="M5.6 7q-.6-2.8.8-3 1.4-.2 1.3 2.6M7.6 6.6q-.2-3.4 1.2-3.4t1.1 3.4M9.8 6.8q.2-2.8 1.5-2.6 1.2.4.5 3.2" fill="#B0A488" stroke="#3B3226" stroke-width=".7"/>'
                     '<path d="M4.8 11.2Q2.2 10.4 2.4 8.6q.6-1.2 1.8-.4l1 1.4" fill="#B0A488" stroke="#3B3226" stroke-width=".7"/>'
                     '<path d="M6.4 9.8l1 1.4-.6 1.6M9.4 9.6l.6 1.6-.8 1.4M11.2 11.4l.5 1.2M6 13.8h4.4" fill="none" stroke="#6E604A" stroke-width=".55" stroke-linecap="round"/>'
                     '<path d="M13.4 2.6q1.2 1.4.4 3M14.8 6.2q.8 1 .2 2.2" fill="none" stroke="#9A8C74" stroke-width=".8" stroke-linecap="round"/>',
    # Gabenbeutel mit Zugband und roter Kordel (Phil 4,18); vorher schalenförmig
    "gabenbeutel": '<path d="M4.6 7Q1.2 9.6 1.8 12.6 2.6 15.6 8 15.6t6.2-3Q14.8 9.6 11.4 7z" fill="#C9A06A" stroke="#3B3226" stroke-width=".8"/>'
                   '<path d="M5.2 6.8Q5 3.2 6.4 2.4l1.6 1.8 1.6-1.8q1.4.8 1.2 4.4" fill="#C9A06A" stroke="#3B3226" stroke-width=".7"/>'
                   '<path d="M4.6 7Q8 8.4 11.4 7" fill="none" stroke="#A33A2E" stroke-width="1.3"/><path d="M8 7.8q-2.6 1.6-2.4 4.2M8 7.8q2.4 1.6 2.8 3.8" fill="none" stroke="#A33A2E" stroke-width="1" stroke-linecap="round"/>'
                   '<path d="M4.2 10.6q.4 2.4-.2 4M11.8 10.6q-.4 2.4.2 4" fill="none" stroke="#A07A44" stroke-width=".6"/>',
    # Mensch (jemand): bekanntes Personen-Piktogramm auf runder Plakette
    "mensch": '<circle cx="8" cy="8" r="7.4" fill="#F4F1EA" stroke="#3B3226" stroke-width=".9"/><circle cx="8" cy="5.2" r="2.3" fill="#5B4630"/><path d="M3.8 13.6Q3.8 8.4 8 8.4t4.2 5.2z" fill="#5B4630"/>',
    # Hacke (Arbeitsgerät des Tagelöhners)
    "hacke": '<path d="M2 15.6L11.2 3.4" stroke="#7A5A34" stroke-width="1.7" stroke-linecap="round"/><path d="M9.6 2.2l2.6 1.6-.4.8z" fill="#5B4630"/>'
             '<path d="M10.4 2.6L12.8 4l2.6 5.4-3.6 1z" fill="#8C8070" stroke="#3B3226" stroke-width=".8" stroke-linejoin="round"/><path d="M12.4 6l1.4 3.4" stroke="#B4AA9A" stroke-width=".6"/>',
    # taub: Ohr, rot durchgestrichen (wie das Zeichen «blind»)
    "taub": '<path d="M5.4 13Q3.6 9.8 4 6.6 4.6 1.6 9 1.4q4.6.2 4.8 4.8.2 3-2.2 4.6-1.6 1-1.8 2.8-.4 2.6-2.8 2.8-1.2 0-1.6-1.6z" fill="#C89B72" stroke="#3B3226" stroke-width=".8"/>'
            '<path d="M7 6.4q.4-2.6 2.4-2.4 2 .4 1.8 2.6-.2 1.6-1.4 2.2-1 .6-.8 1.8" fill="none" stroke="#3B3226" stroke-width=".7"/><path d="M2.2 14.6L13.8 2.2" stroke="#A33A2E" stroke-width="2" stroke-linecap="round"/>',
    # Feuerwagen (2 Kön 2,11): Wagenkasten mit Rad und Deichsel, Flammen darüber; vorher Rad mit Flamme (brennendes Rad)
    "feuerwagen": '<path d="M2.6 8.8Q.8 5 3.2 2.4q.2 2 1.6 2.6Q4.8 2 7.8.4q-.8 2.6.8 3.8 1.4-1.6 1-3.6 3.6 2.2 2.8 5.8 1.2-.6 1.4-2.2 2.2 3 .4 4.6z" fill="#F08A3C" stroke="#C0502A" stroke-width=".6"/>'
                  '<path d="M5 8.4q.4-2.4 2.2-3.2-.2 1.6 1 2 .6-1.4 1.8-1.8-.2 1.8.8 3z" fill="#F2C76E"/>'
                  '<path d="M1.6 8.2h10.6l-1 3.8H3z" fill="#A0603A" stroke="#3B3226" stroke-width=".8"/><path d="M11.4 11l4.2-2.2" stroke="#7A5A34" stroke-width="1.3" stroke-linecap="round"/>'
                  '<circle cx="6.4" cy="12.4" r="3.1" fill="#C08A2A" stroke="#3B3226" stroke-width=".8"/><circle cx="6.4" cy="12.4" r="2" fill="none" stroke="#7A5A34" stroke-width=".6"/>'
                  '<path d="M6.4 9.3v6.2M3.3 12.4h6.2M4.2 10.2l4.4 4.4M8.6 10.2l-4.4 4.4" stroke="#7A5A34" stroke-width=".6"/>',
    # Reisebündel ohne Stab, verknotet (Orpa kehrt zu ihrem Volk zurück, Rut 1,14-15)
    "buendel-tuch": '<path d="M1.6 15.4Q.4 11.4 2.2 8.8 3.6 7.4 8 7.4t5.8 1.4q1.8 2.6.6 6.6z" fill="#E2CDA8" stroke="#3B3226" stroke-width=".8"/>'
                    '<path d="M1.4 11.4h13.2M1.6 13.6h12.8M5 7.8v7.6M11 7.8v7.6" stroke="#B4707A" stroke-width=".9"/>'
                    '<path d="M7 7.8Q3.4 6.6 2.4 3.6q3.2-.4 5.6 3 2.4-3.4 5.6-3-1 3-4.6 4.2" fill="#E2CDA8" stroke="#3B3226" stroke-width=".7"/>'
                    '<ellipse cx="8" cy="7.4" rx="1.8" ry="1.2" fill="#C9A27A" stroke="#3B3226" stroke-width=".6"/>',
    # Gaius: offene Tür, Licht fällt heraus (Gastfreundschaft, 3 Joh 5-8); vorher Haus, las sich als Hausmodell
    "tuer-offen-licht": '<path d="M3 15.6V6.6Q3 1.6 8 1.6t5 5v9z" fill="#F2C76E" stroke="#3B3226" stroke-width=".9"/>'
                        '<path d="M5.4 15.6V7.6Q5.4 4 8 4t2.6 3.6v8" fill="#FFF3C4"/>'
                        '<path d="M3 15.6V6.6L.4 5v11.4z" fill="#7A5A34" stroke="#3B3226" stroke-width=".7"/><circle cx="1.6" cy="10.6" r=".5" fill="#D9A441"/>'
                        '<path d="M13.8 4.6l1.8-1.2M14.2 8.6h1.8M13.8 12.4l1.8 1.2" stroke="#E0A030" stroke-width="1.1" stroke-linecap="round"/>',
    # Diotrephes: geschlossene, verriegelte Tür und abweisende Hand (3 Joh 10)
    "tuer-zu": '<path d="M1.4 15.6V5.4Q1.4 1.4 6 1.4t4.6 4v10.2z" fill="#6A4A2A" stroke="#3B3226" stroke-width=".9"/>'
               '<path d="M4.4 2.2v13.4M7.4 2.2v13.4" stroke="#4A3220" stroke-width=".6"/><path d="M1.4 9h9.2" stroke="#3B3226" stroke-width="1.5"/>'
               '<path d="M11 15.6v-4.4Q9.4 10.4 9.4 8.8l.5-.4 1.3 1.1V4.6q0-.8.7-.8t.7.8v3.2V3.2q0-.8.7-.8t.7.8v4.6V3.8q0-.8.7-.8t.7.8v4.4V5.4q0-.8.6-.8t.6.8v5.8q0 2.2-1.4 3.4v1z" fill="#C89B72" stroke="#3B3226" stroke-width=".6"/>',
    # Diener: Tablett mit Krug und Bechern (Joh 2,8 «bringt es»), über der Schürze
    "tablett": '<path d="M.8 11.8h14.4l-1.2 1.6H2z" fill="#B07A3E" stroke="#3B3226" stroke-width=".7"/>'
               '<path d="M4 11.8Q2.4 9.4 3.2 7.2 3.8 6 5.2 5.8V4.6h1.8v1.2q1.4.2 2 1.4.8 2.2-.6 4.6z" fill="#C2884A" stroke="#3B3226" stroke-width=".6"/>'
               '<path d="M9.8 8.4h2.6l-.4 3.4h-1.8zM12.8 8.8h2.2l-.3 3h-1.6z" fill="#F4F1EA" stroke="#3B3226" stroke-width=".6"/>',
    # Gerasener: gesprengte Kette mit Bruchstelle (Mk 5,4)
    "kette-gesprengt": '<g fill="none" stroke-linecap="round"><g stroke="#3B3226" stroke-width="2.4"><ellipse cx="2.4" cy="12.4" rx="2" ry="1.2" transform="rotate(-30 2.4 12.4)"/>'
                       '<ellipse cx="5" cy="10.6" rx="2" ry="1.2" transform="rotate(-30 5 10.6)"/><path d="M6.8 9.6q.8-1.6 0-2.4"/>'
                       '<ellipse cx="13.6" cy="12.4" rx="2" ry="1.2" transform="rotate(30 13.6 12.4)"/><ellipse cx="11" cy="10.6" rx="2" ry="1.2" transform="rotate(30 11 10.6)"/><path d="M9.2 9.6q-.8-1.6 0-2.4"/></g>'
                       '<g stroke="#A8A8A8" stroke-width="1.1"><ellipse cx="2.4" cy="12.4" rx="2" ry="1.2" transform="rotate(-30 2.4 12.4)"/>'
                       '<ellipse cx="5" cy="10.6" rx="2" ry="1.2" transform="rotate(-30 5 10.6)"/><path d="M6.8 9.6q.8-1.6 0-2.4"/>'
                       '<ellipse cx="13.6" cy="12.4" rx="2" ry="1.2" transform="rotate(30 13.6 12.4)"/><ellipse cx="11" cy="10.6" rx="2" ry="1.2" transform="rotate(30 11 10.6)"/><path d="M9.2 9.6q-.8-1.6 0-2.4"/></g>'
                       '<path d="M8 1.2v3M4.8 2.4l1.4 2M11.2 2.4l-1.4 2M3 5.4l1.8.8M13 5.4l-1.8.8" stroke="#D9A441" stroke-width="1.1"/></g>',
    # Natanaël: kleiner Feigenbaum mit gelappten Blättern und Feigen (Joh 1,48)
    "feigenbaum": '<path d="M6.8 15.6q1-3 .5-6.4h1.6q-.4 3.4.9 6.4z" fill="#7A5A34" stroke="#3B3226" stroke-width=".6"/>'
                  '<g fill="#5E7F3A" stroke="#3B3226" stroke-width=".6">'
                  '<path d="M8 10Q4.6 10.6 2.4 8.8q1-.2 1.2-.8-1.6-.8-1.6-2.6 1 .6 1.8.2-.4-1.8.6-2.8.8 1 1.6 1 .4-1.6 1.6-2.2.6 1.4.4 2.4z"/>'
                  '<path d="M8 10q3.4.6 5.6-1.2-1-.2-1.2-.8 1.6-.8 1.6-2.6-1 .6-1.8.2.4-1.8-.6-2.8-.8 1-1.6 1-.4-1.6-1.6-2.2-.6 1.4-.4 2.4z"/>'
                  '<path d="M8 9.4Q6 6.4 6.6 3.8q.8.6 1.4.2-.2-1.8.8-3 .9 1.2.8 3 .6.4 1.4-.2.6 2.6-1.4 5.6z"/></g>'
                  '<path d="M8 9.4V3M8 10L4 5.2M8 10l4-4.8" stroke="#3E5A22" stroke-width=".5"/>'
                  '<g fill="#6A3A6E" stroke="#3B3226" stroke-width=".4"><ellipse cx="4.6" cy="9.8" rx="1" ry="1.2"/><ellipse cx="11.6" cy="9.6" rx="1" ry="1.2"/><ellipse cx="9.8" cy="4.6" rx=".9" ry="1.1"/></g>',
    # Machlon: Erbteil (Feld), auf dem sein Name erhalten bleibt (Rut 4,10)
    "acker": '<path d="M.8 13.4L4 5.4h8l3.2 8z" fill="#A07A44" stroke="#3B3226" stroke-width=".8"/>'
             '<path d="M2.4 13.4L5 5.4M5.2 13.4L6.6 5.4M8 13.4V5.4M10.8 13.4L9.4 5.4M13.6 13.4L11 5.4" stroke="#6E4E2A" stroke-width=".6"/>'
             '<g stroke="#6E8B3D" stroke-width=".9" stroke-linecap="round"><path d="M4 11.6v-1.6M6.6 11.6V10M9.4 11.6V10M12 11.6V10M5 8.4v-1.2M8 8.4V7.2M11 8.4V7.2"/></g>'
             '<path d="M13 15.4V11q0-1.6 1.2-1.6t1.2 1.6v4.4z" fill="#B4AA9A" stroke="#3B3226" stroke-width=".6"/>',
    # Sklave: Tragkorb mit Last (Arbeitsgewand ohne Mantel, Tit 2,9)
    "tragkorb": '<path d="M2.4 6.4h11.2l-1.4 9.2H3.8z" fill="#B48A54" stroke="#3B3226" stroke-width=".8"/>'
                '<path d="M2.8 9h10.4M3.2 11.6h9.6M3.6 14h8.8" stroke="#8A6234" stroke-width=".6"/><path d="M5 6.4l.6 9.2M8 6.4v9.2M11 6.4l-.6 9.2" stroke="#8A6234" stroke-width=".5"/>'
                '<path d="M3.4 6.4Q3 2.6 6 3.2l1.4.4M12.6 6.4q.4-3.8-2.6-3.2" fill="none" stroke="#5B4630" stroke-width=".9"/>'
                '<g fill="#9A9488" stroke="#3B3226" stroke-width=".5"><ellipse cx="6" cy="5.6" rx="2" ry="1.4"/><ellipse cx="9.8" cy="5.4" rx="2.2" ry="1.5"/><ellipse cx="8" cy="4.2" rx="1.8" ry="1.2"/></g>',
    # Gast: Festbecher mit zwei Henkeln und Wein (Hochzeit)
    "festbecher": '<path d="M3.2 4.2h9.6Q12.6 9 8 9.8 3.4 9 3.2 4.2z" fill="#C2884A" stroke="#3B3226" stroke-width=".8"/><ellipse cx="8" cy="4.2" rx="4.8" ry="1.2" fill="#7A2340" stroke="#3B3226" stroke-width=".6"/>'
                  '<path d="M3.4 5.4Q.6 5.2 1.2 7.6t3 .6M12.6 5.4q2.8-.2 2.2 2.2t-3 .6" fill="none" stroke="#3B3226" stroke-width="1"/>'
                  '<path d="M7.2 9.6h1.6v3.2H7.2z" fill="#C2884A" stroke="#3B3226" stroke-width=".6"/><path d="M4.4 14.8Q8 12 11.6 14.8z" fill="#C2884A" stroke="#3B3226" stroke-width=".7"/>'
                  '<path d="M5 6q.4 1.8 2 2.6" fill="none" stroke="#E2B07A" stroke-width=".6"/>',
    # Königlicher Beamter: Siegel mit Krone an Bändern (im Dienst des Königs)
    "siegel": '<path d="M5.6 10.4L3.4 15.6l2.2-1 1.2 1.4 1-4.6M10.4 10.4l2.2 5.2-2.2-1-1.2 1.4-1-4.6" fill="#3E6E9E" stroke="#3B3226" stroke-width=".6"/>'
              '<path d="M8 1.2l1.3 1 1.6-.4.6 1.5 1.5.6-.4 1.6 1 1.3-1 1.3.4 1.6-1.5.6-.6 1.5-1.6-.4L8 12l-1.3-1-1.6.4-.6-1.5-1.5-.6.4-1.6-1-1.3 1-1.3-.4-1.6 1.5-.6.6-1.5 1.6.4z" fill="#A33A2E" stroke="#3B3226" stroke-width=".7"/>'
              '<path d="M5.4 8.6l-.4-3.2 1.7 1.5L8 4.4l1.3 2.5L11 5.4l-.4 3.2z" fill="#E0B24E" stroke="#6A1E16" stroke-width=".45"/>',
    # Freund: drei Brote bei Nacht (Lk 11,5)
    "drei-brote": '<path d="M12.4 .8a3.4 3.4 0 1 0 3 5.2 2.8 2.8 0 1 1-3-5.2z" fill="#F2D27A" stroke="#9C6F1C" stroke-width=".5"/>'
                  '<g fill="#D9A060" stroke="#3B3226" stroke-width=".7"><ellipse cx="4.6" cy="12.8" rx="3.6" ry="2.5"/><ellipse cx="11.4" cy="12.8" rx="3.6" ry="2.5"/><ellipse cx="8" cy="8.8" rx="3.6" ry="2.5"/></g>'
                  '<path d="M3 12.2q1.6-1 3.2 0M9.8 12.2q1.6-1 3.2 0M6.4 8.2q1.6-1 3.2 0" fill="none" stroke="#A8743A" stroke-width=".6"/>',
    # Tochter der Herodias: Handtrommel mit Schellen und Bändern (tanzt, Mk 6,22)
    "tamburin": '<circle cx="8" cy="7" r="5.6" fill="#F6EBD9" stroke="#8A5A2A" stroke-width="1.6"/>'
                '<g fill="#E0B24E" stroke="#9C6F1C" stroke-width=".4"><circle cx="8" cy="1.4" r="1"/><circle cx="13.6" cy="7" r="1"/><circle cx="2.4" cy="7" r="1"/><circle cx="12" cy="3" r="1"/><circle cx="4" cy="3" r="1"/></g>'
                '<path d="M5.4 12q-1.6 1.8-.8 3.6M8 12.6q-.4 1.8 1 3M10.6 12q1.4 1.6.8 3.6" fill="none" stroke="#D4537E" stroke-width="1.1" stroke-linecap="round"/>'
                '<path d="M14.2 11.2l1.4.8M14.6 9.6l1.4.2M1.8 11.2l-1.4.8" stroke="#3B3226" stroke-width=".6" stroke-linecap="round"/>',
    # Malchus: Ohr mit Verband und kurzes Schwert (Joh 18,10), Gewalt nur angedeutet
    "ohr-schwert": '<path d="M2.6 13.4Q.8 10.2 1.2 7 1.8 2 6.2 1.8q4.6.2 4.8 4.8.2 3-2.2 4.6-1.6 1-1.8 2.8-.4 2.6-2.8 2.8-1.2 0-1.6-1.6z" fill="#C89B72" stroke="#3B3226" stroke-width=".8"/>'
                   '<path d="M4.2 6.8q.4-2.6 2.4-2.4 2 .4 1.8 2.6-.2 1.6-1.4 2.2" fill="none" stroke="#3B3226" stroke-width=".7"/>'
                   '<path d="M2 3.4l7.4 3.4-.8 1.8L1.2 5.2z" fill="#FBF7EC" stroke="#A89C84" stroke-width=".5"/>'
                   '<path d="M15.4 1.2L10 12.4" stroke="#3B3226" stroke-width="1.8" stroke-linecap="round"/><path d="M15.4 1.2L10 12.4" stroke="#C9C2B4" stroke-width=".9" stroke-linecap="round"/>'
                   '<path d="M8.4 11.6l3.6 1.8" stroke="#9C6F1C" stroke-width="1.2" stroke-linecap="round"/><path d="M10 12.6l-1 2.4" stroke="#5B4630" stroke-width="1.3" stroke-linecap="round"/>',
    # Ältester: Stadttor (Älteste im Tor, Rut 4,1-2; in jeder Stadt, Tit 1,5)
    "stadttor": '<path d="M1 15.6V3.4h2.2v1.6h1.6V3.4H7v2.4h2V3.4h2.2v1.6h1.6V3.4H15v12.2z" fill="#C9B48E" stroke="#3B3226" stroke-width=".8"/>'
                '<path d="M5.2 15.6V10.4Q5.2 7.6 8 7.6t2.8 2.8v5.2z" fill="#3B3226"/><path d="M1 9h3M12 9h3M1 12.4h3M12 12.4h3M2.6 9v3.4M13.4 9v3.4" stroke="#A08A5A" stroke-width=".55"/>',
    # Heuchler: betende Hände, auffällig, mit Strahlen (betet, um gesehen zu werden, Mt 6,5)
    "betende-haende": '<path d="M8 1.4Q5.8 2.8 5.6 6.6L5 10.4l-1.4 2 1.6 3.2h5.6l1.6-3.2-1.4-2-.6-3.8Q10.2 2.8 8 1.4z" fill="#C89B72" stroke="#3B3226" stroke-width=".8"/>'
                      '<path d="M8 1.8v9.4" stroke="#3B3226" stroke-width=".6"/><path d="M4.4 13.2h7.2v2.4H4.4z" fill="#7A6A8E" stroke="#3B3226" stroke-width=".6"/>'
                      '<path d="M2.2 2.8l1.6 1.4M1.4 7h2M13.8 2.8l-1.6 1.4M14.6 7h-2" stroke="#D9A441" stroke-width="1.1" stroke-linecap="round"/>',
    # Syntyche: Handschlag (eines Sinnes sein, Phil 4,2)
    "handschlag": '<path d="M0 11.6L3.6 7.8l2.4 2.6-3.4 4z" fill="#6A8AA8" stroke="#3B3226" stroke-width=".7"/><path d="M16 11.6l-3.6-3.8-2.4 2.6 3.4 4z" fill="#A8687A" stroke="#3B3226" stroke-width=".7"/>'
                  '<path d="M3.4 8.2Q6 4.6 9.4 4.8l3.4 3.2-1.6 2.6q-2.6 2.6-5.6 2.4z" fill="#C89B72" stroke="#3B3226" stroke-width=".75"/>'
                  '<path d="M6.6 6.2l2.6 2.6M8 5.4l2.8 2.6M9.6 5l2.4 2.4M5 10.6q2-.2 3-2" fill="none" stroke="#3B3226" stroke-width=".55" stroke-linecap="round"/>',
    # Syrophönizierin: Hündchen frisst Brotkrumen unter dem Tisch (Mk 7,28)
    "hund-brot": '<path d="M.6 2.4h14.8v1.8H.6z" fill="#A07A44" stroke="#3B3226" stroke-width=".6"/><path d="M2.2 4.2v11.4M13.8 4.2v11.4" stroke="#7A5A34" stroke-width="1.2"/>'
                 '<g fill="#E8C98E" stroke="#A8743A" stroke-width=".3"><circle cx="6.4" cy="6" r=".6"/><circle cx="7.6" cy="7.6" r=".55"/><circle cx="5.6" cy="8.4" r=".5"/></g>'
                 '<path d="M8 12.6q0-2.6 2.8-2.8h1.6q1.8.2 1.8 2.4v2.8h-1v-2h-3.2v2h-1z" fill="#A8743A" stroke="#3B3226" stroke-width=".6"/>'
                 '<path d="M14.2 11q1.4-.6 1.2-2" fill="none" stroke="#3B3226" stroke-width=".7" stroke-linecap="round"/>'
                 '<circle cx="7" cy="10.4" r="2.1" fill="#A8743A" stroke="#3B3226" stroke-width=".6"/><path d="M5.4 10.6q-1.4.4-1.4 1.6l1.6-.2" fill="#A8743A" stroke="#3B3226" stroke-width=".5"/>'
                 '<path d="M7.4 8.6q1.4.2 1.4 2.2-1-.4-1.4-1.2z" fill="#6A4422"/><circle cx="6.4" cy="10" r=".4" fill="#3B3226"/><circle cx="4.1" cy="11.8" r=".35" fill="#3B3226"/>',
    # Schwiegermutter des Petrus: Schale mit Brot (sie diente ihnen, Mk 1,31)
    "schale": '<path d="M1.2 8.6h13.6q-.6 5.8-6.8 6.2-6.2-.4-6.8-6.2z" fill="#B4643A" stroke="#3B3226" stroke-width=".8"/><ellipse cx="8" cy="8.6" rx="6.8" ry="1.4" fill="#8A4A2A" stroke="#3B3226" stroke-width=".6"/>'
              '<path d="M3.8 8.4q1-3.8 4.2-3.8t4.2 3.8z" fill="#D9A060" stroke="#3B3226" stroke-width=".7"/><path d="M5.8 6.4l1 1.2M8.4 5.8l.8 1.4" stroke="#A8743A" stroke-width=".6"/>'
              '<path d="M3.2 11.6q4.8 1.6 9.6 0" fill="none" stroke="#D8946A" stroke-width=".7"/>',
    # Frau mit Blutfluss: Hand berührt die Quaste am Mantelsaum (Mk 5,27)
    "saum": '<path d="M3.4.6h12v8.6Q11.4 11.4 6.2 9.4z" fill="#A33A2E" stroke="#3B3226" stroke-width=".8"/><path d="M6.2 1v8M9.4 1v9.4M12.6 1v8.8" stroke="#7A2A22" stroke-width=".7"/>'
            '<path d="M6.2 9.4q5 2 9.2-.2" fill="none" stroke="#D9A441" stroke-width=".9"/>'
            '<path d="M10.6 10.2v4M11.8 10.2v4" stroke="#FFFDF6" stroke-width="1.3" stroke-linecap="round"/><path d="M11.2 9.8v4.6" stroke="#2E4A7A" stroke-width=".7"/>'
            '<path d="M.4 15.6L5.4 12.6" stroke="#3B3226" stroke-width="3.6" stroke-linecap="round"/><path d="M.4 15.6L5.4 12.6" stroke="#A88E6A" stroke-width="2.4" stroke-linecap="round"/>'
            '<path d="M5 12.4q1.4-1.6 3.6-1.6l1.4.2.2.8-1.8.2 2 .4-.2.8-2 .2q-1.4.8-2.6.6z" fill="#C89B72" stroke="#3B3226" stroke-width=".6"/>',
    # Lazarus: offenes Felsengrab, Stein weggerollt (Joh 11,38-44)
    "grab-offen": '<path d="M.6 15.6Q.4 6.2 6.2 3.4q5.8-2.6 9.2 2.6v9.6z" fill="#A89A84" stroke="#3B3226" stroke-width=".8"/>'
                  '<path d="M3.8 15.6V11q0-3.4 3.2-3.4t3.2 3.4v4.6z" fill="#2E2A24"/><path d="M5.4 15.6v-3.4q0-1.6 1.6-1.6t1.6 1.6v3.4z" fill="#F6EBD9" opacity=".85"/>'
                  '<circle cx="13" cy="12.6" r="3" fill="#8C8070" stroke="#3B3226" stroke-width=".7"/><path d="M11.4 11.2q1.6-1 3 0" fill="none" stroke="#6E6456" stroke-width=".5"/>',
    # Josef: Zimmermann (Mt 13,55): Hammer auf einem Brett
    "hammer": '<path d="M.8 12.6l12.8-3.4.8 3-12.8 3.4z" fill="#D2A86E" stroke="#3B3226" stroke-width=".7"/><path d="M3 13.2l9.6-2.6" stroke="#A8803E" stroke-width=".5"/>'
              '<path d="M3.6 13L11.4 3.2" stroke="#7A5A34" stroke-width="1.7" stroke-linecap="round"/>'
              '<g transform="rotate(38 11.6 3)"><rect x="7.8" y="1.4" width="7.6" height="3.2" rx=".6" fill="#8C8070" stroke="#3B3226" stroke-width=".7"/></g>',
    # Titus: Insel mit Städten im Meer (Kreta, Tit 1,5)
    "insel": '<path d="M.6 11h14.8v4.6H.6z" fill="#5A8AB0" stroke="#3B3226" stroke-width=".7"/><path d="M2 13.2q1-.8 2 0t2 0M8.6 14.2q1-.8 2 0t2 0" fill="none" stroke="#DCEBF6" stroke-width=".6"/>'
             '<path d="M1.6 11.4Q3.6 6.8 7.2 3.2q1.4 1.6 2.6 1.2 2.8 2.4 4.6 7z" fill="#8A9A5A" stroke="#3B3226" stroke-width=".8"/>'
             '<path d="M4.4 9h1.8v2H4.4zM8 8.2h2v2.8H8zM11 9.4h1.6v1.6H11z" fill="#F4F1EA" stroke="#3B3226" stroke-width=".4"/><path d="M4.2 9l1.1-1 1.1 1M7.8 8.2l1.2-1 1.2 1" fill="#A33A2E" stroke="#3B3226" stroke-width=".3"/>',
    # Noomi: Säugling Obed (Rut 4,16), Tuch in Ruts Olivgrün mit Gerstengelb (Runde 4: weisse Wickelbänder lasen sich als Christkind)
    "saeugling": '<path d="M2.4 13.8Q.8 11.4 3 9.6l6.8-5.2q2.6-1.4 3.8.8 1 2.2-1 3.8l-6.8 5.2q-2 1.4-3.4-.4z" fill="#8A9A5A" stroke="#3B3226" stroke-width=".8"/>'
                 '<path d="M5 9l2.4 3M7.8 6.8l2.4 3" stroke="#E8B84A" stroke-width="1"/>'
                 '<circle cx="12.2" cy="4.8" r="2.9" fill="#C89B72" stroke="#3B3226" stroke-width=".7"/><path d="M10.6 4.6q.6.6 1.2 0M12.8 4.2q.6.6 1.2 0" fill="none" stroke="#3B3226" stroke-width=".5"/>'
                 '<path d="M10.4 3.2q1.8-2 3.6-.4" fill="none" stroke="#3A2618" stroke-width="1"/>',
    # Elimelech: Stab mit grossem, verknotetem Reisebündel (Wegzug nach Moab, Rut 1,1)
    "buendel": '<path d="M1.4 15.8L10.6 3.6" stroke="#7A5A34" stroke-width="1.7" stroke-linecap="round"/>'
               '<path d="M10.8 4.4Q6 4.6 5.6 9.2q.2 4.8 5.2 5 5-.2 5.2-5-.4-4.6-5.2-4.8z" fill="#C9A27A" stroke="#3B3226" stroke-width=".8"/>'
               '<path d="M7 7.4q3.8 2 7.6 0M6.6 10.8q4 1.6 8.2 0" fill="none" stroke="#9A6A3A" stroke-width=".7"/>'
               '<path d="M9.6 4.8L8.6 1.8q1.6.2 2.2 2.4.8-2 2.4-2l-1.2 2.8" fill="#C9A27A" stroke="#3B3226" stroke-width=".7"/>',
    # Kapitän: Segelschiff (vorher Steuerruder, las sich als Löffel)
    "schiff": '<path d="M7.6 1v10.2" stroke="#5B4630" stroke-width="1.1"/><path d="M8.2 1.6q5 3.6 0 8.6z" fill="#F6EBD9" stroke="#3B3226" stroke-width=".7"/><path d="M7 2.4Q3 5.4 7 9.4z" fill="#E2CDA8" stroke="#3B3226" stroke-width=".6"/>'
              '<path d="M.8 10.6h14.4l-2.4 3.6H3.2z" fill="#8A5A30" stroke="#3B3226" stroke-width=".8"/><path d="M2 12.2h12" stroke="#5B3A20" stroke-width=".5"/>'
              '<path d="M.4 15.2q1.2-.9 2.4 0t2.4 0 2.4 0 2.4 0 2.4 0 2.4 0" fill="none" stroke="#5A8AB0" stroke-width=".9"/>',
    # Händler: Marktstand mit gestreiftem Sonnendach und Waren (kein Geldsack, siehe Lexikon-Regel)
    "marktstand": '<path d="M1.6 6.6v9M14.4 6.6v9" stroke="#7A5A34" stroke-width="1.2"/><path d="M.6 6.8L2.2 2h11.6l1.6 4.8z" fill="#F4F1EA" stroke="#3B3226" stroke-width=".7"/>'
                  '<path d="M3.6 2L2.8 6.8M6.4 2l-.4 4.8M9.6 2l.4 4.8M12.4 2l.8 4.8" stroke="#A33A2E" stroke-width="1.3"/><path d="M.6 6.8q1.2 1.2 2.4 0t2.4 0 2.6 0 2.6 0 2.4 0 2.4 0" fill="#F4F1EA" stroke="#3B3226" stroke-width=".6"/>'
                  '<path d="M1 11.6h14v1.8H1z" fill="#B07A3E" stroke="#3B3226" stroke-width=".6"/>'
                  '<path d="M3 11.6q-.6-2.4 1.4-2.6 2 .2 1.4 2.6z" fill="#C2884A" stroke="#3B3226" stroke-width=".5"/><circle cx="8.4" cy="10.4" r="1.3" fill="#D9A441" stroke="#3B3226" stroke-width=".4"/>'
                  '<circle cx="10.4" cy="10.6" r="1.1" fill="#6E8B3D" stroke="#3B3226" stroke-width=".4"/><path d="M11.6 11.6l.8-2.4h1.4l.6 2.4z" fill="#8E6A9A" stroke="#3B3226" stroke-width=".4"/>',
    "unkraut": '<g stroke="#3E4A2A" stroke-width="1" stroke-linecap="round" fill="none"><path d="M6 16Q6 8 3 2M8 16V1.4M10 16q0-8 3-14"/></g><g fill="#2E3420"><ellipse cx="3.4" cy="3" rx=".9" ry="1.5"/><ellipse cx="4.6" cy="5.4" rx=".9" ry="1.5"/><ellipse cx="8" cy="2.4" rx=".9" ry="1.5"/><ellipse cx="8" cy="5" rx=".9" ry="1.5"/><ellipse cx="12.6" cy="3" rx=".9" ry="1.5"/><ellipse cx="11.4" cy="5.4" rx=".9" ry="1.5"/></g>',
}


def _jakobsmuschel():
    """Jakobsmuschel: Fächer aus Rippen mit gewelltem Rand, zwei Ohren am Schloss, abwechselnd helle und dunkle Felder."""
    import math
    n, cx, cy, hx, hy = 9, 8, 8.4, 8, 14.2
    pts = [(cx + 7.2 * math.cos(math.radians(a)), cy + 7.4 * math.sin(math.radians(a))) for a in [190 + i * 160 / (n - 1) for i in range(n)]]
    out = ['<path d="M4.4 15.6L5.2 12.4h5.6l.8 3.2z" fill="#E6D4AE" stroke="#3B3226" stroke-width=".7"/>']
    for i in range(n - 1):
        (x1, y1), (x2, y2) = pts[i], pts[i + 1]
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        qx, qy = mx + (mx - cx) * .22, my + (my - cy) * .22
        col = "#F7EEDC" if i % 2 else "#E2CFA8"  # naturweiss statt orange (Runde 4: las sich als Fächer)
        out.append(f'<path d="M{hx} {hy}L{x1:.2f} {y1:.2f}Q{qx:.2f} {qy:.2f} {x2:.2f} {y2:.2f}z" fill="{col}"/>')
    edge = f"M{hx} {hy}L{pts[0][0]:.2f} {pts[0][1]:.2f}"
    for i in range(n - 1):
        (x1, y1), (x2, y2) = pts[i], pts[i + 1]
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        edge += f"Q{mx + (mx - cx) * .22:.2f} {my + (my - cy) * .22:.2f} {x2:.2f} {y2:.2f}"
    out.append(f'<path d="{edge}z" fill="none" stroke="#3B3226" stroke-width=".8" stroke-linejoin="round"/>')
    out.append("".join(f'<path d="M{hx} {hy}L{x:.2f} {y:.2f}" stroke="#9A8058" stroke-width=".5"/>' for x, y in pts[1:-1]))
    return "".join(out)


ATTR["jakobsmuschel"] = _jakobsmuschel()


# ---- Runde 4 (2026-10-23, Blindtest Runde 3): Zeichen, die als etwas anderes gelesen wurden, neu gezeichnet
def _saege():
    """Handsäge: Blatt mit deutlichen Zähnen und Holzgriff mit Griffloch (vorher flacher Streifen, las sich als Krone/Kamm)."""
    teeth = "".join("l.5 1.3.5-1.3" for _ in range(10))
    return ('<g transform="rotate(-30 8 8.4)">'
            '<path d="M.6 7.4L11.4 5.6v5.6H1.2z" fill="#D6D2C8" stroke="#3B3226" stroke-width=".7" stroke-linejoin="round"/>'
            f'<path d="M1.2 11.2{teeth}" fill="#D6D2C8" stroke="#3B3226" stroke-width=".55" stroke-linejoin="round"/>'
            '<path d="M2 8.6l8.8-1.4" stroke="#FFFDF6" stroke-width=".6"/>'
            '<path d="M10.8 4.2h3.4q1.8 0 1.8 1.8v5.8q0 1.8-1.8 1.8h-3.4z" fill="#A0703A" stroke="#3B3226" stroke-width=".75"/>'
            '<rect x="12.4" y="6.2" width="2" height="5" rx="1" fill="#FFFDF6" stroke="#3B3226" stroke-width=".5"/>'
            '<circle cx="11.6" cy="5.4" r=".45" fill="#D9A441"/><circle cx="11.6" cy="12.4" r=".45" fill="#D9A441"/></g>')


ATTR.update({
    "saege": _saege(),
    # Messer gesenkt, Spitze nach unten, mit Holzgriff (Tradition Bartholomäus); vorher schräg nach oben, las sich als Opfermesser (Abraham)
    "messer": '<g transform="rotate(24 8 8)"><path d="M6.4.6h3.2v6H6.4z" fill="#6A4A2A" stroke="#3B3226" stroke-width=".7"/>'
              '<circle cx="8" cy="2.2" r=".45" fill="#D9A441"/><circle cx="8" cy="4.8" r=".45" fill="#D9A441"/>'
              '<path d="M5.4 6.4h5.2v1.4H5.4z" fill="#8C8070" stroke="#3B3226" stroke-width=".5"/>'
              '<path d="M6.2 7.8h3.6q.8 4.2-1.6 7.8-.6.4-.8-.4.4-3.6-1.2-7.4z" fill="#D6D2C8" stroke="#3B3226" stroke-width=".7"/>'
              '<path d="M8.8 8.4q.4 3.2-.8 6" fill="none" stroke="#FFFDF6" stroke-width=".5"/></g>',
    # Kelch mit Schlange (Legende vom Giftbecher, Tradition Johannes); vorher Prunkkelch allein, las sich als Becher des Mundschenks
    "kelch": '<path d="M3.4 6.4h9.2q-.2 5-4.6 5.8-4.4-.8-4.6-5.8z" fill="#C9A04A" stroke="#8A6A2A" stroke-width=".8"/>'
             '<ellipse cx="8" cy="6.4" rx="4.6" ry="1.1" fill="#9C7A34" stroke="#8A6A2A" stroke-width=".5"/>'
             '<path d="M8 12.2v2M5 15.2h6" stroke="#8A6A2A" stroke-width="1.5" stroke-linecap="round"/>'
             '<path d="M8.8 6.6Q5.4 5.4 7.2 3.6 9.6 2 7.6 1.2" fill="none" stroke="#3B3226" stroke-width="2.3" stroke-linecap="round"/>'
             '<path d="M8.8 6.6Q5.4 5.4 7.2 3.6 9.6 2 7.6 1.2" fill="none" stroke="#5E9A3A" stroke-width="1.35" stroke-linecap="round"/>'
             '<ellipse cx="6.6" cy="1.3" rx="1.6" ry="1.05" fill="#5E9A3A" stroke="#3B3226" stroke-width=".5"/>'
             '<circle cx="6.2" cy="1" r=".3" fill="#1E1610"/><path d="M5.1 1.4l-1.1.4M5.1 1.4l-1-.5" stroke="#A33A2E" stroke-width=".4"/>',
    # Walkerstange: langer Stab mit flachem, geradem Brett (Tradition Jakobus, Sohn des Alphäus)
    "walkerstange": '<path d="M1.2 15.8L8.8 7.8" stroke="#3B3226" stroke-width="2.4" stroke-linecap="round"/><path d="M1.2 15.8L8.8 7.8" stroke="#8A6234" stroke-width="1.4" stroke-linecap="round"/>'
                    '<g transform="rotate(42 11.4 4.4)"><rect x="9.2" y="-.6" width="4.4" height="9" rx=".5" fill="#D2A86E" stroke="#3B3226" stroke-width=".8"/>'
                    '<path d="M10.6.2v7.4M12.2.2v7.4" stroke="#A8803E" stroke-width=".45"/></g>',
    # Keule: Holzknüppel, unten schmal, oben dick, Astknorren am Umriss (Tradition Thaddäus); vorher runder Kopf mit Punkten, las sich als Honigwabe
    "keule": '<path d="M1.8 15.2L3 13.6 11.2 2.6Q12.6.6 14.6 1.6 16 3 14.6 4.8L4.2 15.6Q2.6 16.6 1.8 15.2z" fill="#8A6A3A" stroke="#3B3226" stroke-width=".8"/>'
             '<path d="M9.6 5.4q-1.6-.4-1.4 1.2M13.2 6.8q.8 1.2 2 .4M6.6 10q-1.4-.2-1.2 1.2" fill="#8A6A3A" stroke="#3B3226" stroke-width=".7"/>'
             '<path d="M4.6 13.6L12.4 3.4M6.6 13.2l7-8.6" stroke="#6A4A2A" stroke-width=".45"/><path d="M2.6 13.4l1.6 1.4M3.6 12.2l1.6 1.4" stroke="#3B3226" stroke-width=".7"/>',
    # X-Kreuz aus zwei Holzbalken mit Maserung (Tradition Andreas); vorher zwei Striche, lasen sich als gekreuzte Bänder
    "x-kreuz": "".join(f'<g transform="rotate({a} 8 8)"><rect x="6.3" y=".4" width="3.4" height="15.2" rx=".4" fill="#A0703A" stroke="#3B3226" stroke-width=".8"/>'
                       '<path d="M7.4 1.2v13.6M8.7 1.2v13.6" stroke="#7A5230" stroke-width=".4"/></g>' for a in (45, -45)),
    # Stabkreuz: langer Holzstab mit kleinem Kreuz oben (Tradition Philippus); vorher kurzes Kreuz, las sich als Kreuzträger
    "stabkreuz": '<path d="M8 3.4v12.4" stroke="#3B3226" stroke-width="2.3" stroke-linecap="round"/><path d="M8 3.4v12.4" stroke="#8A6234" stroke-width="1.3" stroke-linecap="round"/>'
                 '<path d="M8 .9v7.2M4.4 3.8h7.2" stroke="#3B3226" stroke-width="2.6" stroke-linecap="round"/><path d="M8 .9v7.2M4.4 3.8h7.2" stroke="#E0B24E" stroke-width="1.5" stroke-linecap="round"/>'
                 '<g fill="#E0B24E" stroke="#3B3226" stroke-width=".5"><circle cx="8" cy=".9" r="1"/><circle cx="4.2" cy="3.8" r="1"/><circle cx="11.8" cy="3.8" r="1"/></g>'
                 '<circle cx="8" cy="15.4" r="1" fill="#8A6234" stroke="#3B3226" stroke-width=".5"/>',
    # Thomas: Hand mit Wundmal, ein Finger zeigt darauf (Joh 20,25-27); vorher Winkelmass, las sich als Baumeister
    "wundmal": '<path d="M3 15.6V9.2Q2.4 8 1.6 7.2.8 6.2 1.6 5.6q1-.4 2.2 1.2l.4.4V3q0-1 .8-1t.8 1v3.4V1.6q0-1 .8-1t.8 1v4.8V2.2q0-1 .8-1t.8 1v4.4V3.6q0-.9.8-.9t.8.9v6q0 2.4-1.4 3.6v2.4z" fill="#C89B72" stroke="#3B3226" stroke-width=".65"/>'
               '<circle cx="6.6" cy="10.2" r="1.1" fill="#A33A2E" stroke="#6A1E16" stroke-width=".4"/>'
               '<path d="M16 8.6h-3.4q-1.2 0-1.6 1l-2.6.1q-.9.1-.9.8t.9.8l2.8.1q.4 1.8 2 2h2.8z" fill="#B88A62" stroke="#3B3226" stroke-width=".7"/>'
               '<path d="M11.4 11.2h2M11.6 12.4h1.8" stroke="#3B3226" stroke-width=".4"/>',
    # Matthäus: Buch mit Feder und Münzen (Evangelist, Tradition; Zöllner, Mt 10,3); vorher Buch allein, las sich als Lehrer
    "buch-muenzen": '<path d="M.6 5Q3.6 3.6 7 5v9.4Q3.6 13 .6 14.4z" fill="#F4F1EA" stroke="#3B3226" stroke-width=".7"/><path d="M7 5q3.4-1.4 6.4 0v9.4Q10.4 13 7 14.4z" fill="#F4F1EA" stroke="#3B3226" stroke-width=".7"/>'
                    '<path d="M1.8 7q2.2-.8 4 0M1.8 9q2.2-.8 4 0M1.8 11q2.2-.8 4 0M8.2 7q2.2-.8 4 0M8.2 9q2.2-.8 4 0" fill="none" stroke="#A79A80" stroke-width=".5"/>'
                    '<path d="M8.6 10.6Q10.8 4 15.6.4q.4 4.6-4.6 8.4z" fill="#FFFDF6" stroke="#3B3226" stroke-width=".6"/><path d="M8.6 10.6l4-6.6" stroke="#3B3226" stroke-width=".4"/>'
                    '<circle cx="12.2" cy="13.4" r="2.3" fill="#E0B24E" stroke="#9C6F1C" stroke-width=".6"/><circle cx="14.4" cy="11.2" r="1.7" fill="#C9C2B4" stroke="#8C8070" stroke-width=".55"/>',
    # Judas Iskariot: Kasse mit Einwurfschlitz, eine Silbermünze fällt hinein (Joh 12,6: «er hatte die Kasse»); vorher Kästchen, las sich als Talent
    "kasse": '<path d="M1.4 8h10.4v7.6H1.4z" fill="#8A6A3A" stroke="#3B3226" stroke-width=".8"/><path d="M1.4 8l2.8-2.8h10.2L11.8 8z" fill="#A9844C" stroke="#3B3226" stroke-width=".7"/>'
             '<path d="M11.8 8l2.6-2.8v7.8l-2.6 2.6z" fill="#6E5230" stroke="#3B3226" stroke-width=".7"/><path d="M3.6 8v7.6M9.6 8v7.6" stroke="#5B4630" stroke-width=".9"/>'
             '<path d="M5.6 6.6h4.6" stroke="#1E1610" stroke-width="1" stroke-linecap="round"/>'
             '<path d="M5.4 10.4h2.4v2.6H5.4z" fill="#D9A441" stroke="#9C6F1C" stroke-width=".5"/><circle cx="6.6" cy="11.4" r=".4" fill="#1E1610"/>'
             '<ellipse cx="7.9" cy="2.6" rx="1.1" ry="2" fill="#C9C2B4" stroke="#6E6A60" stroke-width=".55"/><path d="M5.6 1.2v2M10.2 1.2v2" stroke="#8C8070" stroke-width=".5" stroke-linecap="round"/>',
    # Judas, nicht der Iskariot: Frage beim Mahl (Joh 14,22): Sprechblase mit Fragezeichen über Tischkante mit Brot und Becher
    "frage-mahl": '<path d="M8 .6C3.8.6 1 2.6 1 5.2c0 2 1.6 3.6 4 4.2L3.8 11.8 7.4 9.8H8c4.2 0 7-2 7-4.6S12.2.6 8 .6z" fill="#FFFDF6" stroke="#3B3226" stroke-width=".8"/>'
                  '<path d="M6.4 3.4q0-1.6 1.6-1.6t1.6 1.4q0 1-1.2 1.6-.5.3-.5 1.2" fill="none" stroke="#2E5478" stroke-width="1.15" stroke-linecap="round"/><circle cx="7.9" cy="7.2" r=".6" fill="#2E5478"/>'
                  '<ellipse cx="11.4" cy="13.8" rx="3.6" ry="1.9" fill="#D9A060" stroke="#3B3226" stroke-width=".6"/><path d="M9.6 13.2q1.8-1 3.6 0M10 14.6q1.4-.6 2.8 0" fill="none" stroke="#A8743A" stroke-width=".45"/>'
                  '<path d="M3.2 10.8h3.4l-.5 3.4H3.7z" fill="#C2884A" stroke="#3B3226" stroke-width=".55"/><path d="M4.9 14.2v1M3.6 15.6h2.6" stroke="#3B3226" stroke-width=".7" stroke-linecap="round"/>',
    # Der Jünger, den Jesus liebte (Joh 13,23): Herz
    "herz": '<path d="M8 15Q.8 10.4 1 5.4 1.4 1.4 4.8 1.4 7 1.4 8 3.8 9 1.4 11.2 1.4q3.4 0 3.8 4 .2 5-7 9.6z" fill="#C8414A" stroke="#3B3226" stroke-width=".8"/>'
            '<path d="M3.4 4.6q.6-1.6 2.2-1.4" fill="none" stroke="#F4B4B4" stroke-width=".9" stroke-linecap="round"/>',
    # Jünger-Rolle: Spur auf dem Weg, goldene Fussspuren voraus (Jesus), braune folgen (Mk 1,17-18); vorher zwei lose Spuren, zu schwach
    "fussspuren": None,
    # Sämann: offener Beutel mit Saatkörnern, Körner fliegen im Bogen heraus (Mk 4,3); vorher Beutel mit Schlaufe, las sich als Schleuder
    "saatbeutel": '<path d="M8.4 7.4Q11.4 1.4 15.8.2M9.4 8.6Q13 5.4 15.8 6" fill="none" stroke="#B4A070" stroke-width=".5" stroke-dasharray="1 .9"/>'
                  '<path d="M2 9.4Q.4 11.8 1.4 14 2.4 15.8 6.2 15.8t4.8-1.8q1-2.2-.6-4.6z" fill="#A08A5A" stroke="#3B3226" stroke-width=".8"/>'
                  '<ellipse cx="6.2" cy="9.4" rx="4.3" ry="1.6" fill="#6E5A36" stroke="#3B3226" stroke-width=".7"/><path d="M2.8 9.4q3.4-2.2 6.8 0" fill="#E8C98E" stroke="#8A6A3A" stroke-width=".4"/>'
                  '<path d="M3.4 12.4q2.8 1 5.6 0" fill="none" stroke="#7A6640" stroke-width=".5"/>'
                  '<g fill="#F2D896" stroke="#8A6A3A" stroke-width=".4">' + "".join(
                      f'<ellipse cx="{x}" cy="{y}" rx=".6" ry=".9" transform="rotate({r} {x} {y})"/>' for x, y, r in
                      ((9.6, 4.6, 30), (12.4, 2, 55), (15.2, 1, 75), (13, 5.8, 40), (15.4, 4.6, 60), (14.6, 8.4, 20))) + '</g>',
    # Löser: ausgezogener Schuh von der Seite, mit Sohle und Riemen (Rut 4,8); die Sandale von oben las sich als Brot, Riemen allein als Knoten
    "sandale": '<g transform="rotate(-12 8 9)"><path d="M1.6 11.4Q1.2 6.2 4.6 6l3.4.4q1.6 2.8 5 3.2 2.6.4 2.4 2.2z" fill="#A0703A" stroke="#3B3226" stroke-width=".8" stroke-linejoin="round"/>'
               '<ellipse cx="5.6" cy="6.6" rx="2.4" ry=".9" fill="#3B2616" stroke="#3B3226" stroke-width=".5"/>'
               '<path d="M7.4 6.6q.4 2.6-1.4 4.8" fill="none" stroke="#5B3A20" stroke-width="1"/>'
               '<path d="M1.2 11.4h14.4v1.4q0 1.2-1.4 1.2H2.4q-1.2 0-1.2-1.2z" fill="#5B3A20" stroke="#3B3226" stroke-width=".6"/>'
               '<path d="M3 9.4q1.4 1 3.2.6" fill="none" stroke="#7A4E2A" stroke-width=".5"/></g>',
    # Kranker: flache Strohmatte in Schrägsicht mit Geflecht und Fransen (Mk 2,4); gerollt las sie sich als Schriftrolle
    "matte-flach": '<path d="M.4 13.6L3.6 4.8h12l-3.2 8.8z" fill="#E0C68A" stroke="#3B3226" stroke-width=".8" stroke-linejoin="round"/>'
                   '<path d="M2 13.6l3.2-8.8M3.6 13.6l3.2-8.8M5.2 13.6l3.2-8.8M6.8 13.6L10 4.8M8.4 13.6l3.2-8.8M10 13.6l3.2-8.8M11.6 13.6l3.2-8.8" stroke="#B4944E" stroke-width=".5"/>'
                   '<path d="M1.4 10.8h12M2.8 7.2h12" stroke="#6A4A2A" stroke-width="1"/>'
                   '<path d="M.4 13.6l-.3 1.8M1.6 13.6l-.3 1.8M2.8 13.6l-.3 1.8M4 13.6l-.3 1.8M5.2 13.6l-.3 1.8M6.4 13.6l-.3 1.8M7.6 13.6l-.3 1.8M8.8 13.6l-.3 1.8M10 13.6l-.3 1.8M11.2 13.6l-.3 1.8M12.4 13.6l-.3 1.8" stroke="#B4944E" stroke-width=".6" stroke-linecap="round"/>',
    # Maria von Betanien: Fläschchen giesst Öl auf einen Fuss (Joh 12,3); vorher Fläschchen allein, wie das Salbgefäss der Maria aus Magdala
    "salbt-fuss": None,
    # Blinder: Zeichen «blind» über einer Bettelschale mit Münze (er sass da und bettelte, Joh 9,8)
    "blind-schale": '<path d="M2 5Q8-.8 14 5 8 10.8 2 5z" fill="#FFFDF6" stroke="#3B3226" stroke-width=".9"/><circle cx="8" cy="5" r="2" fill="#3B3226"/>'
                    '<path d="M3 9.4L13 .6" stroke="#A33A2E" stroke-width="1.7" stroke-linecap="round"/>'
                    '<path d="M1.4 11h13.2q-.6 4.6-6.6 4.8-6-.2-6.6-4.8z" fill="#B4643A" stroke="#3B3226" stroke-width=".8"/><ellipse cx="8" cy="11" rx="6.6" ry="1.2" fill="#8A4A2A" stroke="#3B3226" stroke-width=".6"/>'
                    '<circle cx="9.6" cy="10.8" r="1.2" fill="#C9C2B4" stroke="#6E6A60" stroke-width=".45"/>',
    # Geheilter Blindgeborener: offenes Auge (Zeichen «sehen») über derselben Bettelschale, ohne Durchstreichung (Joh 9,7: kam sehend
    # zurück); Prüfung 2026-10-26: Der Geheilte trug sonst weiter das Zeichen «blind»
    "sehend-schale": '<path d="M2 5Q8-.8 14 5 8 10.8 2 5z" fill="#FFFDF6" stroke="#3B3226" stroke-width=".9"/><circle cx="8" cy="5" r="2" fill="#3B3226"/>'
                     '<path d="M1.4 11h13.2q-.6 4.6-6.6 4.8-6-.2-6.6-4.8z" fill="#B4643A" stroke="#3B3226" stroke-width=".8"/><ellipse cx="8" cy="11" rx="6.6" ry="1.2" fill="#8A4A2A" stroke="#3B3226" stroke-width=".6"/>'
                     '<circle cx="9.6" cy="10.8" r="1.2" fill="#C9C2B4" stroke="#6E6A60" stroke-width=".45"/>',
    # Epaphroditus: Korb mit Gaben (Brot, Krug, Tuch mit Band), keine Münzen (Phil 4,18); der Gabenbeutel las sich als Geldbeutel (Judas)
    "gabenkorb": '<path d="M2.6 8.6Q8-.4 13.4 8.6" fill="none" stroke="#3B3226" stroke-width="1.8"/><path d="M2.6 8.6Q8-.4 13.4 8.6" fill="none" stroke="#B48A54" stroke-width=".9"/>'
                 '<ellipse cx="5.4" cy="8.2" rx="3" ry="1.8" fill="#D9A060" stroke="#3B3226" stroke-width=".6"/>'
                 '<path d="M9.6 9V5.6h1.2V4.6h2.4v1h1.2V9z" fill="#B4643A" stroke="#3B3226" stroke-width=".55"/>'
                 '<path d="M6.8 9.4q.6-3 2.6-3t2 3z" fill="#E2CDA8" stroke="#3B3226" stroke-width=".55"/><path d="M7.4 7.6l3.6 1M9.4 6.4v3" stroke="#A33A2E" stroke-width=".7"/>'
                 '<path d="M1.2 8.8h13.6l-1.6 6.8H2.8z" fill="#B48A54" stroke="#3B3226" stroke-width=".8"/>'
                 '<path d="M1.7 11h12.6M2.2 13.2h11.6M4.4 8.8l.4 6.8M8 8.8v6.8M11.6 8.8l-.4 6.8" stroke="#8A6234" stroke-width=".55"/>',
    # Die auserwählte Herrin: Brief und zwei grössere Kinder (2 Joh 1,1); vorher Kleinkind, las sich als Maria mit Kind
    "kinder-brief": '<path d="M.6 1h9.6l2.2 2.2V9H.6z" fill="#F4F1EA" stroke="#3B3226" stroke-width=".7"/><path d="M2 3.4h6.4M2 5.2h7.4" stroke="#A79A80" stroke-width=".6"/><circle cx="10.6" cy="7.2" r="1.3" fill="#A33A2E"/>'
                    '<circle cx="5.4" cy="7.6" r="2.3" fill="#C89B72" stroke="#3B3226" stroke-width=".6"/><path d="M3.1 7.4Q3 5 5.4 5t2.3 2.4Q6.8 6 5.4 6.1 4 6 3.1 7.4z" fill="#3A2618"/>'
                    '<path d="M2.4 16q-.2-5.2 3-6t3 6z" fill="#E8B84A" stroke="#3B3226" stroke-width=".6"/>'
                    '<circle cx="11.4" cy="9.4" r="2" fill="#C89B72" stroke="#3B3226" stroke-width=".6"/><path d="M9.4 9.2Q9.4 7.2 11.4 7.2t2 2Q12.6 8.1 11.4 8.2 10.2 8.1 9.4 9.2z" fill="#2E2017"/>'
                    '<path d="M8.8 16q-.2-4.2 2.6-4.8 2.8.6 2.6 4.8z" fill="#7FA05A" stroke="#3B3226" stroke-width=".6"/>',
    # Vater: Knabe steht neben ihm, ganze Figur mit Beinen (Mt 7,9); vorher Kind mit erhobenen Armen, las sich als Simeon mit Jesuskind
    "sohn-kind": '<circle cx="8" cy="3.4" r="2.7" fill="#C89B72" stroke="#3B3226" stroke-width=".6"/><path d="M5.3 3.2Q5.2.6 8 .6t2.7 2.6Q9.8 1.8 8 1.9 6.2 1.8 5.3 3.2z" fill="#2E2017"/>'
                 '<path d="M5.6 13V8.4Q5.6 6.2 8 6.1q2.4.1 2.4 2.3V13z" fill="#C8A25A" stroke="#3B3226" stroke-width=".6"/><path d="M5.6 10.4h4.8" stroke="#7A5A34" stroke-width=".9"/>'
                 '<path d="M5.2 7.4q-.8 2.4-.4 4.6M10.8 7.4q.8 2.4.4 4.6" fill="none" stroke="#3B3226" stroke-width="1.5" stroke-linecap="round"/>'
                 '<path d="M5.2 7.4q-.8 2.4-.4 4.6M10.8 7.4q.8 2.4.4 4.6" fill="none" stroke="#C8A25A" stroke-width=".8" stroke-linecap="round"/>'
                 '<path d="M6.8 13v2.4M9.2 13v2.4" stroke="#C89B72" stroke-width="1.3" stroke-linecap="round"/><path d="M6 15.6h1.6M8.6 15.6h1.6" stroke="#5B3A20" stroke-width=".9" stroke-linecap="round"/>',
    # Pilatus: Richterstuhl (Joh 19,13) als römischer Amtsstuhl mit gekreuzten Beinen und Purpurkissen auf einem Podest
    "richterstuhl": '<path d="M.6 13.6h14.8v2.2H.6z" fill="#D8CBB0" stroke="#3B3226" stroke-width=".6"/><path d="M2.2 11.8h11.6v1.8H2.2z" fill="#E7DCC4" stroke="#3B3226" stroke-width=".6"/>'
                    '<path d="M4 7.6q4 2.6 8 4.2M12 7.6q-4 2.6-8 4.2" fill="none" stroke="#3B3226" stroke-width="2.2" stroke-linecap="round"/>'
                    '<path d="M4 7.6q4 2.6 8 4.2M12 7.6q-4 2.6-8 4.2" fill="none" stroke="#D9A441" stroke-width="1.2" stroke-linecap="round"/>'
                    '<path d="M2.6 5.2h10.8v2.4H2.6z" rx="1" fill="#6A2E5E" stroke="#3B3226" stroke-width=".6"/><path d="M2.2 7.6h11.6" stroke="#9C6F1C" stroke-width="1"/>'
                    '<path d="M2.6 5.2l-.8-1.4M13.4 5.2l.8-1.4" stroke="#6A2E5E" stroke-width="1" stroke-linecap="round"/>',
    # Hauptmann: Rebstock-Stab des Zenturio (Tradition), knorrig, mit Knauf
    "rebstock": '<path d="M2.4 15.2L13 2.4" stroke="#3B3226" stroke-width="2.6" stroke-linecap="round"/><path d="M2.4 15.2L13 2.4" stroke="#7A4E2A" stroke-width="1.6" stroke-linecap="round"/>'
                '<path d="M5.4 12.2q-1.4-.4-1.6.8M8.4 8.2q1.4.4 1.8-.6M10.6 5.6q-1.2-.6-1.6.4" fill="#7A4E2A" stroke="#3B3226" stroke-width=".6"/>'
                '<path d="M4 13.8l8.4-10" stroke="#A8743A" stroke-width=".4" stroke-dasharray="1.2 .8"/>'
                '<circle cx="13.2" cy="2.2" r="1.5" fill="#D9A441" stroke="#3B3226" stroke-width=".6"/>',
    # Schriftgelehrter: offene Schriftrolle, darüber der lehrend erhobene Zeigefinger (Mk 1,22); Feder liess ihn als Schreiber lesen
    "rolle-lehre": '<path d="M2.8 8.6h10.4v6.6H2.8z" fill="#F4F1EA" stroke="#3B3226" stroke-width=".7"/><path d="M4.2 10.4h7.6M4.2 12h7.6M4.2 13.6h5" stroke="#A79A80" stroke-width=".6"/>'
                   '<rect x="1" y="7.8" width="2.6" height="8" rx="1.3" fill="#B07A3E" stroke="#3B3226" stroke-width=".6"/><rect x="12.4" y="7.8" width="2.6" height="8" rx="1.3" fill="#B07A3E" stroke="#3B3226" stroke-width=".6"/>'
                   '<path d="M7.2 7.4V4.2q0-.7.7-.7V.9q0-.8.8-.8t.8.8v4.2h1q1.2 0 1.2 1.2v1.1z" fill="#C89B72" stroke="#3B3226" stroke-width=".6"/>'
                   '<path d="M9.5 5.1h1.6v-.3q0-.7.7-.7t.6.7v1.4M7.2 5.4l-.7.2" fill="none" stroke="#3B3226" stroke-width=".45"/>'
                   '<path d="M5.4 1.6l1 .9M5 4.2h1.2M12 1.6l-1 .9" stroke="#D9A441" stroke-width=".8" stroke-linecap="round"/>',
})

_FOOT = ('<path d="M0 5.2q-1.9 0-2-2.1 0-1.5.7-2.9.5-1.3.2-2.6-.3-1.9 1.4-2.3 1.9-.2 2.1 1.9.1 1.7-.6 3.1-.4 1-.2 2.5.2 2.4-1.6 2.4z"/>'
         '<circle cx="-1.7" cy="-6.6" r=".95"/><circle cx="-.2" cy="-7.4" r=".78"/><circle cx="1.1" cy="-7.3" r=".68"/><circle cx="2.2" cy="-6.7" r=".58"/><circle cx="3" cy="-5.8" r=".5"/>')


def _fussspuren():
    """Zwei Fussspuren: die goldene voraus (Jesus), die braune folgt ihr (der Jünger), Mk 1,17-18."""
    return "".join(f'<g transform="translate({x} {y}) rotate({rot}) scale({sc})" fill="{col}" stroke="#2B211A" stroke-width=".55">{_FOOT}</g>'
                   for x, y, sc, rot, col in ((4.4, 11.4, .86, -8, "#5B4630"), (11.4, 7.4, .86, 8, "#C08A2A")))


def _salbt_fuss():
    """Maria von Betanien: schlankes Fläschchen, aus dem Öl auf einen nackten Fuss (von der Seite) tropft (Joh 12,3)."""
    return ('<path d="M10.2 7.4h5V5.8h-5z" fill="#6B8E7A" stroke="#3B3226" stroke-width=".5"/>'
            '<path d="M10.8 7.4h3.8v5.2Q15 15.6 12.4 15.6H2.4Q.6 15.6.8 13.8 1 12.4 2.8 12.2l5.6-.8q2.2-.6 2.4-2.4z" fill="#C89B72" stroke="#3B3226" stroke-width=".7"/>'
            '<g fill="#C89B72" stroke="#3B3226" stroke-width=".5"><circle cx="1.5" cy="13" r=".8"/><circle cx="2.8" cy="12.4" r=".7"/><circle cx="4" cy="12.1" r=".6"/></g>'
            '<path d="M11.6 14.6q1.2.2 2-.6" fill="none" stroke="#8A5A3A" stroke-width=".45" stroke-linecap="round"/>'
            '<g transform="rotate(-125 5.2 4.2)"><path d="M4 1.2h2.4v2.2l1.2 1.4v4.4H2.8V4.8L4 3.4z" fill="#E9D8B4" stroke="#3B3226" stroke-width=".65"/>'
            '<path d="M4 .4h2.4v1H4z" fill="#6B8E7A" stroke="#3B3226" stroke-width=".4"/></g>'
            '<g fill="#E8C060" stroke="#9C6F1C" stroke-width=".35"><path d="M8.2 6.4q.7 1 0 1.5-.7-.5 0-1.5z"/><path d="M8.6 8.8q.7 1 0 1.5-.7-.5 0-1.5z"/></g>')


ATTR["fussspuren"] = _fussspuren()
ATTR["salbt-fuss"] = _salbt_fuss()
ATTR_VB = "0 0 16 16"

# ------------------------------------------------------------------ Figuren
# robe, mantle, hair (Farbe), style (short|curls|long|bald|none), beard (None|short|full|long), beard_color,
# head (None | ("veil", Farbe) | ("turban", Farbe) | ("hood", Farbe) | ("crown",) | ("helmet",) | ("wreath",) | ("band", Farbe)),
# age (adult|young|old|child|baby), sex (m|f), belt, sash, apron, trim, attr (Attribut), wings, bound, chains, kneel
def F(robe, mantle=None, hair="#2E2017", style="short", beard=None, head=None, age="adult", sex="m", attr=None, **kw):
    return dict(robe=robe, mantle=mantle, hair=hair, style=style, beard=beard, head=head, age=age, sex=sex, attr=attr, **kw)


GREY, WHITE, DARK, BROWN, BLACK = "#8A8478", "#D8D2C4", "#2E2017", "#4A3020", "#1E1610"
APOSTLE = "#9C7A4C"
# Gemeinsames Jüngermerkmal (Runde 4, Blindtest Runde 3): Jüngergewand wie FIG-GRUPPE-ZWOELF, dunkler Gürtel und Wanderstab (Mk 6,8)
# an der linken Schulter; dazu je Jünger eigene Mantelfarbe und eigenes Zeichen auf der Brust
J = dict(belt="#5B4630", jstaff=True)
FIGS = {
    # Zwölf und Jünger (Jüngergewand, je eigene Mantelfarbe)
    "FIG-PETRUS": F(APOSTLE, "#C08A2A", GREY, "curls", "short", attr="schluessel", **J),
    "FIG-ANDREAS": F(APOSTLE, "#6E8B3D", "#5A4A3A", "long", "full", attr="x-kreuz", **J),
    "FIG-JAKOBUS-ZEBEDAEUS": F(APOSTLE, "#2F6F73", BROWN, "short", "full", attr="jakobsmuschel", **J),  # Muschel allein (am Stab las sie sich als Fächer)
    "FIG-JOHANNES-ZEBEDAEUS": F(APOSTLE, "#6A8FB3", "#6A4A2A", "short", None, age="young", attr="kelch", **J),
    "FIG-PHILIPPUS": F(APOSTLE, "#8F6BA8", DARK, "short", "short", attr="stabkreuz", **J),
    "FIG-BARTHOLOMAEUS": F(APOSTLE, "#7A4E3A", DARK, "curls", "full", attr="messer", **J),
    "FIG-NATANAEL": F(APOSTLE, "#5E7F3A", DARK, "curls", "full", attr="feigenbaum", **J),
    "FIG-MATTHAEUS": F(APOSTLE, "#3F5A7A", BROWN, "short", "full", attr="buch-muenzen", **J),
    "FIG-LEVI": F("#4A6B5A", "#4A6B5A", BROWN, "short", "short", attr="muenzen"),
    "FIG-THOMAS": F(APOSTLE, "#A0703A", DARK, "short", "short", attr="wundmal", **J),  # Wundmal (Joh 20,27) statt Winkelmass (las sich als Baumeister)
    "FIG-JAKOBUS-ALPHAEUS": F(APOSTLE, "#6B6B8A", BROWN, "short", "full", attr="walkerstange", **J),
    "FIG-THADDAEUS": F(APOSTLE, "#5F7A2A", DARK, "long", "full", attr="keule", **J),  # Mantel kräftiger moosgrün (Blindtest 2026-10-23)
    "FIG-JUDAS-NICHT-ISKARIOT": F(APOSTLE, "#5F8F8A", DARK, "curls", "short", attr="frage-mahl", **J),  # Frage beim Mahl; Locken zur Unterscheidung von Thomas
    "FIG-SIMON-KANANAEUS": F(APOSTLE, "#9A4E4E", "#3A2A1C", "curls", "full", attr="saege", **J),
    "FIG-JUDAS-ISKARIOT": F(APOSTLE, "#7A8A9A", DARK, "short", "short", attr="kasse", **J),
    "FIG-LIEBLINGSJUENGER": F(APOSTLE, "#E2CDA8", "#4A3020", "curls", None, age="young", attr="herz", **J),
    # Frauen
    "FIG-MARIA-MAGDALA": F("#E2CDA8", "#8E3B5E", "#4A2A1A", "long", sex="f", head=("veil", "#8E3B5E"), attr="alabaster", backdrop="grab"),  # offenes Grab hinter ihr (Joh 20,1)
    "FIG-MARIA-BETANIEN": F("#6B8E7A", None, "#3A2618", "long", sex="f", attr="salbt-fuss"),  # salbt die Füsse (Joh 12,3)
    "FIG-MARTA": F("#B4704A", None, "#3A2618", "short", sex="f", head=("veil", "#E9D8B4"), attr="kelle"),
    "FIG-MARIA-KLOPAS": F("#D8CBB0", None, DARK, "short", sex="f", head=("veil", "#7A6A8E")),
    "FIG-MARIA-MUTTER-JAKOBUS": F("#6E7F5A", None, DARK, "short", sex="f", head=("veil", "#D8CBB0"), attr="oelkrug"),
    "FIG-SALOME": F("#F2E6CC", None, GREY, "short", sex="f", age="old", head=("veil", "#B07A3E"), attr="oelkrug"),
    "FIG-HERODIAS": F("#7A3E6A", None, BLACK, "long", sex="f", trim="#D9A441", head=("veil", "#C9A0BE"), diadem=True, jewels=True, necklace=True),
    "FIG-TOCHTER-HERODIAS": F("#D4537E", None, BLACK, "long", sex="f", age="young", attr="tamburin"),
    "FIG-EUODIA": F("#A8687A", None, DARK, "short", sex="f", head=("veil", "#D8B4A0")),
    "FIG-SYNTYCHE": F("#6A8AA8", None, BROWN, "short", sex="f", head=("veil", "#F2E6CC"), attr="handschlag"),
    "FIG-AUSERWAEHLTE-HERRIN": F("#6A4A7A", None, DARK, "short", sex="f", head=("veil", "#F2E6CC"), attr="kinder-brief"),
    # Rut
    "FIG-RUT": F("#7A8B4A", None, BROWN, "short", sex="f", head=("veil", "#E8B84A"), attr="garbe"),
    "FIG-NOOMI": F("#C9BFAA", None, GREY, "short", sex="f", age="old", head=("veil", "#2E2E38")),  # Witwenkopftuch dunkel; kein Kind als Zeichen (wirkte im Bildtest vor Rut 4 wie ein eigenes Kind)
    "FIG-ORPA": F("#C08A8A", None, DARK, "short", sex="f", head=("veil", "#E2CDA8"), attr="buendel-tuch"),  # altrosa, Reisebündel (kehrt zurück, Rut 1,14-15)
    "FIG-BOAS": F("#E7DCC4", "#2F5F6F", "#5A4A3A", "short", "full", trim="#D9A441", attr="worfel"),  # helles Gewand mit Goldsaum (wohlhabend), Petrolmantel
    "FIG-ELIMELECH": F("#C9BFAA", "#6A5A4A", GREY, "short", "full", attr="buendel"),
    "FIG-MACHLON": F("#7A6A5A", None, DARK, "short", None, age="young", sash="#7A8B4A", attr="acker"),
    "FIG-KILJON": F("#7A6A5A", None, DARK, "curls", None, age="young", sash="#8E6A7A"),
    "FIG-LOESER": F("#8A7A6A", "#5B4630", DARK, "short", "full", attr="sandale"),  # Sandale von der Seite (von oben las sie sich als Brot)
    "FIG-OBED": F("#F2E6CC", None, DARK, "none", age="baby"),
    # Propheten, Könige
    "FIG-JONA": F("#6FB2E6", "#4A6E8A", DARK, "short", "full", backdrop="fisch"),  # Fisch hinter ihm statt auf der Brust (las sich als Fischer)
    "FIG-OBADJA": F("#E7DCC4", "#6A5A7A", GREY, "short", "long", attr="rolle", rough=True),
    "FIG-ELIJA": F("#8A6A3A", "#5B4630", GREY, "long", "long", fur=True, attr="feuerwagen"),
    "FIG-HERODES-ANTIPAS": F("#6A2E5E", "#3E1A36", BLACK, "short", "short", head=("band", "#D9A441"), trim="#D9A441"),
    # Johannes der Täufer und Evangelien-Personen
    "FIG-JOHANNES-TAEUFER": F("#8A6A3A", None, "#3A2618", "long", "full", belt="#5B4630", attr="kreuzstab", fur=True),
    "FIG-NIKODEMUS": F("#C9BFAA", "#3B4A6B", GREY, "short", "full", head=("turban", "#3B4A6B"), attr="lampe"),
    "FIG-LAZARUS": F("#E7DCC4", None, BROWN, "short", "short", belt="#8A7A60", attr="grab-offen"),
    "FIG-JAIRUS": F("#E7DCC4", "#4F6B7A", "#4A3020", "short", "full", head=("hood", "#E7DCC4"), tassels=True),
    "FIG-BARTIMAEUS": F("#C9BFAA", None, GREY, "short", "short", attr="blind", cloak_off="#8A7A60"),  # wirft den Mantel ab (Mk 10,50)  # blind (Mk 10,46); Stab allein las sich als Wanderer
    "FIG-GERASENER": F("#8A8070", None, DARK, "long", "full", attr="kette-gesprengt"),  # voller Bart (mit kurzem Bart als Frau gelesen)
    "FIG-JOSEF-ARIMATAEA": F("#7A8AA0", "#5A5A5A", GREY, "short", "full", linen=True),  # Leinentuch über der Schulter statt auf der Brust
    "FIG-SIMON-KYRENE": F("#8A7A50", None, DARK, "short", "short", belt="#5B4630", beam=True),  # Balken auf der Schulter (auf der Brust las er sich als «Balken im Auge»)
    "FIG-BARABBAS": F("#7A6A5A", None, BLACK, "short", "short", bound=True),
    "FIG-MALCHUS": F("#B8A98A", None, DARK, "short", None, sash="#4A5A7A", attr="ohr-schwert"),
    "FIG-PILATUS": F("#F2E6CC", None, "#9A948A", "short", None, trim="#6A2E5E", toga=True, attr="richterstuhl"),  # ergraut, Richterstuhl (Joh 19,13)
    "FIG-KAJAFAS": F("#4A5A7A", None, GREY, "short", "full", head=("turban", "#F6EBD9"), breast=True, plate=True),
    "FIG-HANNAS": F("#6A6A7A", "#8A8A8A", WHITE, "short", "long", head=("turban", "#F6EBD9"), attr="stab", breast=True),
    "FIG-SATAN": None,  # dunkler Schatten ohne Gestalt: Bauteil in bildsymbole.py
    # Mitarbeitende und Briefpersonen
    "FIG-TIMOTHEUS": F("#5A7A9A", None, BROWN, "short", None, age="young", attr="stab-brief"),
    "FIG-TITUS": F("#5A6A3A", None, DARK, "curls", "short", attr="insel"),  # Kreta statt Brief (Paulus trägt den Brief)
    "FIG-EPAPHRODITUS": F("#7A8A5A", "#E2CDA8", BROWN, "short", "short", attr="gabenkorb"),  # Gabenkorb statt Beutel (las sich als Geldbeutel)
    "FIG-DER-AELTESTE": F("#6A6A6A", "#E7DCC4", WHITE, "short", "long", age="old", attr="brief-feder"),
    "FIG-GAIUS": F("#8A6A4A", "#F6EBD9", DARK, "short", "short", attr="tuer-offen-licht"),
    "FIG-DIOTREPHES": F("#6A5A5A", "#C9BFAA", DARK, "short", "short", attr="tuer-zu"),
    "FIG-DEMETRIUS": F("#4A7A6A", "#E7DCC4", BROWN, "short", "short", attr="brief"),
    # Rollen
    "FIG-ROLLE-AELTESTER": F("#C9BFAA", "#6A5A4A", GREY, "short", "long", age="old", attr="stadttor"),  # Älteste im Tor (Rut 4,1-2)
    "FIG-ROLLE-BOTE": F("#E2CDA8", "#8A6A3A", DARK, "short", "short", attr="brief", staff=True),
    "FIG-ROLLE-ENGEL": F("#FFFFFF", None, "#D9A441", "short", None, wings=True),
    "FIG-ROLLE-FISCHER": F("#6A7F8A", None, DARK, "curls", "short", attr="netz"),
    "FIG-ROLLE-HIRTE": F("#8A7A50", "#F6EBD9", DARK, "short", "short", attr="hirte"),
    "FIG-ROLLE-HOHEPRIESTER": F("#4A5A7A", None, GREY, "short", "full", head=("turban", "#F6EBD9"), breast=True),
    "FIG-ROLLE-KAPITAEN": F("#8A6A3A", "#2F4F6F", DARK, "short", "full", head=("band", "#2F4F6F"), attr="schiff"),  # Schiff statt Ruder und Seil (las sich als Löffel, überladen)
    "FIG-ROLLE-KRANKER": F("#C9BFAA", None, DARK, "short", "short", attr="matte-flach", bandage=True),  # flache Matte (gerollt las sie sich als Schriftrolle), Verband
    "FIG-ROLLE-PHARISAEER": F("#5A6A7A", "#4F6D8A", DARK, "short", "full", tassels=True, tallit=True, tefillin=True),
    "FIG-ROLLE-PRIESTER": F("#F6EBD9", None, DARK, "short", "short", head=("turban", "#F6EBD9"), sash="#4A5A7A"),
    "FIG-ROLLE-SCHRIFTGELEHRTER": F("#6A5A4A", "#E7DCC4", DARK, "short", "full", attr="rolle-lehre"),  # lehrt (mit Feder als Schreiber gelesen)
    "FIG-ROLLE-TEMPELWACHE": F("#4A5A6A", None, DARK, "short", "short", belt="#C9BFAA", attr="laterne"),
    "FIG-ROLLE-WITWE": F("#C9BFAA", None, GREY, "short", sex="f", age="old", head=("veil", "#4A4A4A"), attr="zwei-muenzen"),
    # Gruppen
    "FIG-GRUPPE-SEELEUTE": F("#E2CDA8", None, DARK, "curls", "short", sash="#2F4F6F", head=("band", "#2F4F6F")),
    "FIG-GRUPPE-EDOM": F("#C9A27A", "#9A4E3A", DARK, "short", "full"),
    "FIG-GRUPPE-ZWOELF": F(APOSTLE, "#7A5A34", DARK, "curls", "full"),
}
GROUPS = {"FIG-GRUPPE-SEELEUTE", "FIG-GRUPPE-EDOM", "FIG-GRUPPE-ZWOELF"}


def slug(fid):
    return fid.replace("FIG-", "").replace("ROLLE-", "").replace("GRUPPE-", "g-").lower()


# ------------------------------------------------------------------ Stil «Symbol»: Ganzfigur ohne Gesicht
def _hair_sym(p):
    h, st = p["hair"], p["style"]
    if p["age"] == "baby":
        return ""
    if st == "curls":
        return "".join(f'<circle cx="{x}" cy="{y}" r="2" fill="{h}"/>' for x, y in ((10, 10), (12.4, 8), (15, 7.4), (17.6, 8), (20, 10)))
    if st == "long":
        return f'<path d="M8.4 14q-.6-8 6.6-8.4 7.2.4 6.6 8.4l1 7h-2.6l-.6-6q-1-4.6-4.4-5-3.4.4-4.4 5l-.6 6H7.4z" fill="{h}"/>'
    if st == "bald":
        return f'<path d="M8.6 15q-.4-3 1-4.6M21.4 15q.4-3-1-4.6" stroke="{h}" stroke-width="1.8" fill="none"/>'
    if st == "none":
        return ""
    return f'<path d="M8.6 12.5q1-7 6.4-7t6.4 7q-2-3-6.4-3t-6.4 3z" fill="{h}"/>'


def _beard_sym(p):
    b = p.get("beard")
    if not b:
        return ""
    c = p.get("beard_color") or p["hair"]
    d = {"short": "M9.5 16q5.5 6 11 0q-1 4-5.5 4.6-4.5-.6-5.5-4.6z",
         "full": "M9 16q6 9 12 0q-1 6-6 7q-5-1-6-7z",
         "long": "M9 16q6 12 12 0q-1 9-6 10q-5-1-6-10z"}[b]
    return f'<path d="{d}" fill="{c}"/>'


def _head_sym(p):
    hd = p.get("head")
    if not hd:
        return ""
    k = hd[0]
    if k == "veil":
        return f'<path d="M7 26q-1-14 2-17 3-4 6-4t6 4q3 3 2 17l-2-1q1-9-1.4-12-2-2.4-4.6-2.4t-4.6 2.4Q7.9 16 9 25z" fill="{hd[1]}" stroke="{INK}" stroke-width=".7"/>'
    if k == "hood":
        return f'<path d="M7.6 20q-1-12 7.4-13 8.4 1 7.4 13l-2 .4q.6-9-5.4-9.6-6 .6-5.4 9.6z" fill="{hd[1]}" stroke="{INK}" stroke-width=".7"/>'
    if k == "turban":
        return (f'<path d="M8.4 11q0-6 6.6-6.4 6.6.4 6.6 6.4z" fill="{hd[1]}" stroke="{INK}" stroke-width=".7"/>'
                f'<path d="M8.6 9q6.4-2 12.8 0" stroke="#C9BFAA" stroke-width=".8" fill="none"/>')
    if k == "band":
        return f'<path d="M8.6 10.6q6.4-2.4 12.8 0v1.8q-6.4-2.4-12.8 0z" fill="{hd[1]}"/>'
    if k == "crown":
        return '<path d="M8.5 10l1-7 3 4 2.5-5 2.5 5 3-4 1 7z" fill="#E0B24E" stroke="#9C6F1C" stroke-width=".8"/>'
    if k == "helmet":
        return f'<path d="M8 14q0-9 7-9t7 9z" fill="#8C8070" stroke="{INK}" stroke-width="1"/><path d="M9 5q6-5 12 0" fill="none" stroke="#8E1F2F" stroke-width="2.4"/>'
    if k == "wreath":
        return '<path d="M8.6 11q6.4-4 12.8 0" fill="none" stroke="#D9A441" stroke-width="1.8" stroke-dasharray="1.6 .8"/>'
    return ""


def symbol_person(fid):
    p = FIGS[fid]
    sid = "ill-p-" + slug(fid)
    o = []
    if p.get("wings"):
        o.append(f'<path d="M9 28Q-2 18 1 6q5 8 10 14zM21 28q11-10 8-22-5 8-10 14z" fill="#FFFDF6" stroke="#D9A441" stroke-width="1"/>')
    if p["age"] == "baby":
        o.append(f'<ellipse cx="15" cy="50" rx="11" ry="7" fill="{p["robe"]}" stroke="{INK}" stroke-width="1.1"/><circle cx="8.5" cy="46" r="4.4" fill="{SKIN}" stroke="{INK}" stroke-width="1"/>')
        return f'<symbol id="{sid}" viewBox="0 0 30 64">{"".join(o)}</symbol>'
    body = "M5 62L8 26q7-7 14 0l3 36z" if p["sex"] == "m" else "M4 62L8 27q7-7 14 0l4 35z"
    o.append(f'<path d="{body}" fill="{p["robe"]}" stroke="{INK}" stroke-width="1.2"/>')
    if p.get("fur"):
        o.append(f'<path d="M8 27q7-7 14 0l1 8q-8 3-16 0z" fill="#8A6A3A" stroke="{INK}" stroke-width=".7"/><path d="M9 30l1 3M12 29l.5 3M15 29v3M18 29l-.5 3M21 30l-1 3" stroke="#5B4630" stroke-width=".7"/>')
    if p.get("mantle"):
        o.append(f'<path d="M8 26q7-7 14 0l3 36H18L9 28z" fill="{p["mantle"]}" stroke="{INK}" stroke-width="1"/>')
    if p.get("toga"):
        o.append(f'<path d="M8 27q8 2 13 14l2 21h-3l-2-18Q14 32 8 30z" fill="#FFFFFF" stroke="{INK}" stroke-width=".7"/><path d="M20 41l2 21" stroke="{p["trim"]}" stroke-width="1.6"/>')
    elif p.get("trim"):
        o.append(f'<path d="M10.5 24.5L15 30l4.5-5.5" fill="none" stroke="{p["trim"]}" stroke-width="1.4"/>')
    if p.get("sash"):
        o.append(f'<path d="M9 25l13 22" stroke="{p["sash"]}" stroke-width="3.4"/>')
    if p.get("belt"):
        o.append(f'<path d="M7 40h16" stroke="{p["belt"]}" stroke-width="2"/>')
    if p.get("breast"):
        o.append('<path d="M11.5 30h7v7h-7z" fill="#D9A441" stroke="#9C6F1C" stroke-width=".6"/>'
                 + "".join(f'<circle cx="{13 + (i % 3) * 2}" cy="{31.6 + (i // 3) * 1.8}" r=".6" fill="{c}"/>'
                           for i, c in enumerate(["#A33A2E", "#3E6E9E", "#6E8B3D"] * 4)))
    if p.get("tassels"):
        o.append(f'<path d="M7 60v2M10 61v2M20 61v2M23 60v2" stroke="#F2E6CC" stroke-width="1.2"/>')
    if p.get("chains"):
        o.append(f'<g fill="none" stroke="#6A6A6A" stroke-width="1"><ellipse cx="6" cy="44" rx="2" ry="1.3"/><ellipse cx="3.5" cy="46" rx="2" ry="1.3"/><ellipse cx="24" cy="44" rx="2" ry="1.3"/><ellipse cx="26.5" cy="46" rx="2" ry="1.3"/></g>')
    if p.get("bound"):
        o.append(f'<path d="M10 38h10v5H10z" fill="{SKIN}" stroke="{INK}" stroke-width=".7"/><path d="M10 40.5h10" stroke="#8A6A3A" stroke-width="1.6"/>')
    hd = p.get("head")
    if hd and hd[0] == "veil":
        o.append(_head_sym(p))
    r = 6.0 if p["age"] in ("young", "child") else 6.5
    o.append(f'<circle cx="15" cy="14" r="{r}" fill="{SKIN}" stroke="{INK}" stroke-width="1.2"/>')
    if not (hd and hd[0] in ("veil", "hood", "turban", "helmet")):
        o.append(_hair_sym(p))
    o.append(_beard_sym(p))
    if hd and hd[0] != "veil":
        o.append(_head_sym(p))
    if p.get("plate"):
        o.append('<path d="M12 8.6h6v1.6h-6z" fill="#E0B24E"/>')
    if p.get("attr"):
        o.append(f'<svg x="-1" y="34" width="13" height="13" viewBox="{ATTR_VB}">{ATTR[p["attr"]]}</svg>')
    inner = "".join(o)
    if p["age"] == "child":  # Kind: kleiner, auf dem Boden stehend
        inner = f'<g transform="translate(4.5 19.2) scale(.7)">{inner}</g>'
    return f'<symbol id="{sid}" viewBox="0 0 30 64">{inner}</symbol>'


def symbol_group(fid):
    """Gruppe: drei gestaffelte Figuren desselben Aussehens, dahinter zwei blassere (Menge statt Dreiergruppe, Blindtest 2026-10-17)."""
    one = "ill-p-" + slug(fid) + "-1"
    return (symbol_person(fid).replace(f'id="ill-p-{slug(fid)}"', f'id="{one}"')
            + f'<symbol id="ill-p-{slug(fid)}" viewBox="0 0 30 64"><use href="#{one}" x="0" y="11" width="16" height="35" opacity=".5"/>'
              f'<use href="#{one}" x="14" y="11" width="16" height="35" opacity=".5"/><use href="#{one}" x="-4" y="17" width="22" height="47" opacity=".8"/>'
              f'<use href="#{one}" x="12" y="17" width="22" height="47" opacity=".8"/><use href="#{one}" x="3" y="10" width="25" height="54"/></symbol>')


def symbol_attrs():
    return "".join(f'<symbol id="ill-a-{k}" viewBox="{ATTR_VB}">{v}</symbol>' for k, v in ATTR.items())


def symbol_library():
    out = [symbol_attrs()]
    for fid, p in FIGS.items():
        if p is None:
            continue
        out.append(symbol_group(fid) if fid in GROUPS else symbol_person(fid))
    return "".join(out)


def symbol_render():
    return {fid: "ill-p-" + slug(fid) for fid, p in FIGS.items() if p is not None}


# ------------------------------------------------------------------ Stil «Anime»: Brustbild (Parameter für bilder_anime.CHAR)
FRONT = {
    "short": "M-10.6-.4Q-11-11.6 0-12Q11-11.6 10.6-.4Q8-6 0-6.6Q-8-6-10.6-.4z",
    "long": "M-10.6-1Q-10.5-11.6 0-12Q10.5-11.6 10.6-1Q7-6.4 .8-7.6L0-5.4-.8-7.6Q-7-6.4-10.6-1z",
    "bald": "M-10.9 2.4Q-11.4-2.6-10-5Q-8.4-3.4-8.2 1.6z M10.9 2.4Q11.4-2.6 10-5Q8.4-3.4 8.2 1.6z",  # Haarkranz tief an den Schläfen (vorher hohe Spitzen, wirkte «alienhaft»)
    "veil": "M-7.6-3.6Q0-8.4 7.6-3.6Q4-5.2 0-5Q-4-5.2-7.6-3.6z",
}
BACK_LONG = "M-10.6 -2Q-12.5 9-10 17L-5.6 16Q-8.4 7-7.6-1z M10.6 -2Q12.5 9 10 17L5.6 16Q8.4 7 7.6-1z"
BEARD = {"short": "M-8 6.4Q-7 12.4 0 13.4Q7 12.4 8 6.4Q6 10 0 10.6Q-6 10-8 6.4z",
         "full": "M-8.4 5Q-8 14 0 15.6Q8 14 8.4 5Q6.6 10.4 0 11Q-6.6 10.4-8.4 5z",
         "long": "M-8.6 4.6Q-9 15 0 19Q9 15 8.6 4.6Q6.6 10.6 0 11.2Q-6.6 10.6-8.6 4.6z"}


def anime_char(fid):
    p = FIGS[fid]
    c = {"hair": p["hair"], "robe": p["robe"]}
    if p.get("mantle"):
        c["mantle"] = p["mantle"]
    hd = p.get("head")
    st = p["style"]
    if hd and hd[0] in ("veil", "hood", "cowl"):
        c["veil"] = hd[1]
        c["front"] = FRONT["veil"]
        if hd[0] == "cowl":  # Männerkapuze eines Reisemantels (eigener Pfad in bilder_anime.head_inner)
            c["cowl"] = True
        if hd[0] == "hood":  # Gebetsmantel über dem Kopf (Männer): Streifen, damit er nicht als Frauenschleier gelesen wird (Blindtest 2026-10-23)
            c["hood"] = True
    elif st == "curls":
        c["curls"] = True
    elif st in FRONT:
        c["front"] = FRONT[st]
    if st == "long" and (not hd or hd[0] in ("crown", "band", "wreath")):  # langes Haar auch unter der Krone (Königin von Saba las sich als junger König)
        c["back"] = BACK_LONG
    if p.get("sex") == "f":  # Wimpern und Lippen im Stil Anime (bilder_anime.head_inner)
        c["female"] = True
    if p.get("beard"):
        c["beard"] = BEARD[p["beard"]]
    if hd and hd[0] == "crown":
        c["crown"] = True
    if hd and hd[0] == "helmet":
        c["helmet"] = True
    if hd and hd[0] == "turban":
        c["turban"] = hd[1]
    if hd and hd[0] == "band":
        c["band"] = hd[1]
    if hd and hd[0] == "wreath":
        c["wreath"] = True
    for k in ("belt", "sash", "trim", "wings", "chains", "bound", "fur", "breast", "plate", "toga", "tassels",
              "tallit", "tefillin", "bandage", "crossed", "rope", "patches", "sword", "staff", "rough",
              "jewels", "necklace", "diadem", "muffle", "shadow", "glow", "wrapped", "linen", "weeping", "backdrop", "attr_box",
              "jstaff", "beam", "cloak_off", "crest"):  # Schalter des Zeichners (bilder_anime.head_inner/body_inner)
        if p.get(k):
            c[k] = p[k]
    if p["age"] in ("young", "child"):
        c["young"] = True
    if p["age"] == "child":
        c["child"] = True
    if p["age"] == "old":
        c["old"] = True
    if p["age"] == "baby":
        c["baby"] = True
    if p.get("attr"):
        c["attr"] = "an-a-" + p["attr"]
    return c


def anime_chars():
    return {slug(fid): anime_char(fid) for fid, p in FIGS.items() if p is not None}


def anime_attrs():
    return "".join(f'<symbol id="an-a-{k}" viewBox="{ATTR_VB}">{v}</symbol>' for k, v in ATTR.items())


# ------------------------------------------------------------------ Weitere Figuren aus figuren_daten/*.json
# Aufbau: {"FIG-…": {"robe": "#…", "mantle": "#…"|null, "hair": "#…", "style": "short|curls|long|bald|none",
#          "beard": null|"short"|"full"|"long", "head": null|["veil", "#…"]|["turban", "#…"]|["hood", "#…"]|["band", "#…"]|["crown"]|["helmet"]|["wreath"],
#          "age": "adult|young|old|child|baby", "sex": "m|f", "attr": null|"<Attribut aus ATTR>", weitere Schalter: belt, sash, trim, wings, bound, chains, fur, breast, toga, tassels},
#  "_group": ["FIG-…"]  (Einträge, die als Gruppe von drei Figuren gezeichnet werden)}
def _load_extra():
    import json
    import pathlib
    d = pathlib.Path(__file__).resolve().parent / "figuren_daten"
    for f in sorted(d.glob("*.json")) if d.exists() else []:
        data = json.loads(f.read_text(encoding="utf-8"))
        for g in data.pop("_group", []):
            GROUPS.add(g)
        for fid, p in data.items():
            if fid in FIGS:
                raise SystemExit(f"{f.name}: Figur {fid} doppelt")
            if p.get("head"):
                p["head"] = tuple(p["head"])
            if p.get("attr") and p["attr"] not in ATTR:
                raise SystemExit(f"{f.name}: Attribut {p['attr']} unbekannt (vorhanden: {', '.join(sorted(ATTR))})")
            FIGS[fid] = F(**{k: v for k, v in p.items()})


_load_extra()
