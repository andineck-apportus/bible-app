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
    "x-kreuz": '<path d="M2 2l12 12M14 2L2 14" stroke="#7A5A34" stroke-width="2.6" stroke-linecap="round"/>',
    "messer": '<path d="M3 13l8-8 2 1-8 8z" fill="#C9C2B4" stroke="#3B3226" stroke-width=".7"/><path d="M11 5l2.6-2.6" stroke="#5B4630" stroke-width="2.2" stroke-linecap="round"/>',
    "saege": '<path d="M1 10h13v3H1z" fill="#C9C2B4" stroke="#3B3226" stroke-width=".7"/><path d="M1 10l1.5-2 1.5 2 1.5-2 1.5 2 1.5-2 1.5 2 1.5-2 1.5 2" fill="none" stroke="#3B3226" stroke-width=".7"/><path d="M14 9h2v5h-2z" fill="#7A5A34"/>',
    "keule": '<path d="M4 14L11 4" stroke="#7A5A34" stroke-width="2" stroke-linecap="round"/><ellipse cx="11.6" cy="3.6" rx="3" ry="2.4" fill="#7A5A34" stroke="#3B3226" stroke-width=".7"/>',
    "winkelmass": '<path d="M3 2v11h11" fill="none" stroke="#8C8070" stroke-width="2.4" stroke-linejoin="round"/>',
    "kreuzstab": '<path d="M8 1v15M4.5 4.5h7" stroke="#7A5A34" stroke-width="1.8" stroke-linecap="round"/>',
    "kasse": '<path d="M2 6h12v8H2z" fill="#8A6A3A" stroke="#3B3226" stroke-width=".8"/><path d="M2 6l2-3h8l2 3" fill="#A07A44" stroke="#3B3226" stroke-width=".8"/><circle cx="8" cy="10" r="1.3" fill="#D9A441"/>',
    "muschel": '<path d="M8 14L2 5q6-5 12 0z" fill="#F2E6CC" stroke="#3B3226" stroke-width=".8"/><path d="M8 14L5 4M8 14V3M8 14l3-10" stroke="#B4A98F" stroke-width=".7"/>',
    "walkerstange": '<path d="M3 15L13 2" stroke="#7A5A34" stroke-width="1.8" stroke-linecap="round"/><path d="M11 2h5v3h-5z" fill="#8A6A3A"/>',
    "buch": '<path d="M2 3h6v11H2zM8 3h6v11H8z" fill="#F4F1EA" stroke="#3B3226" stroke-width=".8"/><path d="M13 1l2 6" stroke="#3B3226" stroke-width="1"/>',
    "kelch": '<path d="M4 2h8q0 6-4 7-4-1-4-7z" fill="#D9A441" stroke="#9C6F1C" stroke-width=".8"/><path d="M8 9v4M5 14h6" stroke="#9C6F1C" stroke-width="1.4" stroke-linecap="round"/>',
    "stabkreuz": '<path d="M8 1v15M5 4h6" stroke="#8F6BA8" stroke-width="1.6" stroke-linecap="round"/>',
    "feigenblatt": '<path d="M8 15V8M8 8Q2 9 2 4q3 1 4-2 2 2 2 2 0 0 2-2 1 3 4 2 0 5-6 4z" fill="#5E7F3A" stroke="#3B3226" stroke-width=".7"/>',
    "aehren": '<g stroke="#B08A2A" stroke-width="1.1" stroke-linecap="round"><path d="M5 15L7 3M8 15V2M11 15L9 3"/></g><g fill="#E8B84A" stroke="#B08A2A" stroke-width=".5"><ellipse cx="7" cy="4" rx="1.4" ry="2.4"/><ellipse cx="8" cy="3" rx="1.4" ry="2.4"/><ellipse cx="9.2" cy="4" rx="1.4" ry="2.4"/></g>',
    "worfel": '<path d="M3 15L11 5" stroke="#7A5A34" stroke-width="1.6" stroke-linecap="round"/><path d="M9.5 6.5l3-4 3 3-4 3z" fill="#A07A44" stroke="#3B3226" stroke-width=".7"/>',
    "schuh": '<path d="M2 11q0-4 3-4l3 1q2 1 6 1 1 0 1 2v2H2z" fill="#8A6A3A" stroke="#3B3226" stroke-width=".8"/><path d="M5 7v-3" stroke="#5B4630" stroke-width="1"/>',
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
    "saeugling": '<ellipse cx="8" cy="10" rx="6" ry="4" fill="#F2E6CC" stroke="#3B3226" stroke-width=".8"/><circle cx="4.5" cy="8.5" r="2.4" fill="#C89B72" stroke="#3B3226" stroke-width=".6"/>',
    # Ergänzt nach dem Blindtest 2026-10-23 (reports/figuren-blindtest-2026-10-23.json): je Figur ein eigenes, im Text oder in der Tradition begründetes Zeichen
    "fisch": '<path d="M1.2 9.6Q5 3.2 11 6.6l3.6-3v9.4L11 10.4Q5 14.6 1.2 9.6z" fill="#5A8AB0" stroke="#3B3226" stroke-width=".8"/><path d="M8 7.2q1 1.8 0 4M5.6 10.6q1.6.8 3.4.2" fill="none" stroke="#2E5478" stroke-width=".6"/><circle cx="3.8" cy="8.4" r=".8" fill="#3B3226"/>',
    "brief-feder": '<path d="M1.5 4h8.5l2 2v9.5H1.5z" fill="#F4F1EA" stroke="#3B3226" stroke-width=".8"/><path d="M3.2 7.4h6M3.2 9.6h7M3.2 11.8h5" stroke="#A79A80" stroke-width=".8"/><path d="M8.6 13.6Q10 6 15.4.6q.6 5.4-5 9.6" fill="#FFFDF6" stroke="#3B3226" stroke-width=".7"/><path d="M8.6 13.6l3.4-7.4" stroke="#3B3226" stroke-width=".5"/>',
    "blind": '<path d="M.8 8.4Q8 1.4 15.2 8.4 8 15.4.8 8.4z" fill="#FFFDF6" stroke="#3B3226" stroke-width="1"/><circle cx="8" cy="8.4" r="2.4" fill="#3B3226"/><path d="M2.2 14.6L13.8 2.2" stroke="#A33A2E" stroke-width="2" stroke-linecap="round"/>',
    "rolle-feder": '<path d="M2.6 5h8v8.6h-8z" fill="#F4F1EA" stroke="#3B3226" stroke-width=".7"/><path d="M4 7.6h5M4 9.6h5M4 11.6h3.4" stroke="#A79A80" stroke-width=".7"/><rect x="1" y="4" width="2.6" height="10.6" rx="1.3" fill="#B07A3E" stroke="#3B3226" stroke-width=".6"/><rect x="9.6" y="4" width="2.6" height="10.6" rx="1.3" fill="#B07A3E" stroke="#3B3226" stroke-width=".6"/><path d="M11 13L15.4 1" stroke="#3B3226" stroke-width="1.6" stroke-linecap="round"/><path d="M11 13L15.4 1" stroke="#C9A86A" stroke-width=".8" stroke-linecap="round"/>',
    "matte-rolle": '<g transform="rotate(-28 8 8) translate(8 8) scale(.84) translate(-8 -8)"><path d="M.4 5.6h15.2v5.6H.4z" fill="#C9B48E" stroke="#3B3226" stroke-width=".8"/><path d="M2.6 5.6v5.6M5.2 5.6v5.6M7.8 5.6v5.6M10.4 5.6v5.6M13 5.6v5.6" stroke="#A08A5A" stroke-width=".6"/><ellipse cx="15.6" cy="8.4" rx="1.4" ry="2.8" fill="#D8C49C" stroke="#3B3226" stroke-width=".7"/><path d="M15.6 7.2a.8 1.2 0 1 1 0 2.4" fill="none" stroke="#8A7A50" stroke-width=".5"/><path d="M4 5v7M12 5v7" stroke="#6A4A2A" stroke-width="1.2"/></g>',
    "alabaster": '<path d="M4.8 15.4Q1.8 12 3.2 8.4 4 6.6 6 6.4h4q2 .2 2.8 2 1.4 3.6-1.6 7z" fill="#F2EADA" stroke="#3B3226" stroke-width=".8"/><path d="M6.2 6.4V4.4h3.6v2" fill="#E2D6BE" stroke="#3B3226" stroke-width=".7"/><path d="M5 2.6h6v1.8H5z" fill="#8E3B5E" stroke="#3B3226" stroke-width=".6"/><circle cx="8" cy="1.8" r="1" fill="#8E3B5E" stroke="#3B3226" stroke-width=".5"/><path d="M4.4 10.6q3.6 1 7.2 0" fill="none" stroke="#C9B48E" stroke-width=".7"/>',
    "oelkrug": '<path d="M5 15q-3.6-1.4-3.2-5.2Q2.2 6.6 6 6.2h4q3.8.4 4.2 3.6.4 3.8-3.2 5.2z" fill="#B07A3E" stroke="#3B3226" stroke-width=".8"/><path d="M6 6.2l.4-2.6h3.2l.4 2.6" fill="#B07A3E" stroke="#3B3226" stroke-width=".7"/><path d="M5.6 2.6h4.8v1.2H5.6z" fill="#6E7F5A"/><path d="M3 10.4h10" stroke="#E8C98E" stroke-width=".9"/>',
    "wasserkrug": '<path d="M4.6 15.4Q2 11.4 3 7.6 3.8 5.4 5.8 5h4.4q2 .4 2.8 2.6 1 3.8-1.6 7.8z" fill="#B4643A" stroke="#3B3226" stroke-width=".8"/><path d="M6 5V2.6h4V5" fill="#B4643A" stroke="#3B3226" stroke-width=".7"/><path d="M5.6 6.4Q2 5.4 2.4 9M10.4 6.4q3.6-1 3.2 2.6" fill="none" stroke="#3B3226" stroke-width="1"/><path d="M3.4 10h9.2" stroke="#E8C98E" stroke-width=".8"/><path d="M6.6 1.4q1.4 1 2.8 0" fill="none" stroke="#6FA8D8" stroke-width="1"/>',
    "traube": '<path d="M8 4.6V1.4" stroke="#5B4630" stroke-width="1.2" stroke-linecap="round"/><path d="M8 3Q11 .4 14.4 2.4 12.6 5.6 8.6 4.4z" fill="#6E8B3D" stroke="#3B3226" stroke-width=".6"/><g fill="#6A3A6E" stroke="#3B3226" stroke-width=".5"><circle cx="5.6" cy="6.2" r="1.7"/><circle cx="8.8" cy="6.2" r="1.7"/><circle cx="4.4" cy="9" r="1.7"/><circle cx="7.2" cy="8.8" r="1.7"/><circle cx="10.2" cy="8.8" r="1.7"/><circle cx="5.8" cy="11.6" r="1.7"/><circle cx="8.8" cy="11.6" r="1.7"/><circle cx="7.4" cy="14.2" r="1.7"/></g>',
    "daemon": '<path d="M9 13Q3.4 12.6 3 7.6q-.2-3.2 2.2-5.4Q5 5 6.8 5.6 6.4 2.6 9 1q-.2 2.8 1.8 4 2.6 2 2.2 4.8Q12.6 13.2 9 13zM6 13.4q-1.4 1.4-3.4 1.2M10.4 13.4q.8 1.6 2.6 2" fill="#4A4050" stroke="#2A2430" stroke-width=".6" opacity=".9"/>',
    "muschelstab": '<path d="M12 1v15" stroke="#7A5A34" stroke-width="1.8" stroke-linecap="round"/><path d="M6 13.4L1.4 6.6Q2 2 6 1.6q4 .4 4.6 5z" fill="#F2C78E" stroke="#3B3226" stroke-width=".8"/><path d="M6 13.4L3 4.4M6 13.4l-1-10M6 13.4l1-10M6 13.4l3-9" stroke="#B07A3E" stroke-width=".7"/><path d="M4.6 12.4h2.8v1.8H4.6z" fill="#F2C78E" stroke="#3B3226" stroke-width=".6"/><path d="M7.2 9.4l4.8-3" stroke="#5B4630" stroke-width=".8"/>',
    "geldbeutel": '<path d="M5 6q-3.4 3-3.4 6.2 0 3 6.4 3t6.4-3Q14.4 9 11 6z" fill="#7A3E2A" stroke="#3B3226" stroke-width=".8"/><path d="M5 6q3-1.6 6 0M6 5.6L4.6 2.6M10 5.6l1.4-3" stroke="#D9A441" stroke-width="1.1" stroke-linecap="round" fill="none"/><circle cx="8" cy="11" r="2.4" fill="#E0B24E" stroke="#9C6F1C" stroke-width=".6"/><circle cx="12.6" cy="2.6" r="1.6" fill="#E0B24E" stroke="#9C6F1C" stroke-width=".5"/>',
    "saatbeutel": '<path d="M4 4.6q-3 3-3 6t5.6 3 5.6-3-3-6z" fill="#A08A5A" stroke="#3B3226" stroke-width=".8"/><path d="M4 4.6h4.4" stroke="#5B4630" stroke-width="1.4"/><path d="M4.6 4.4Q8 .2 14 1.6" fill="none" stroke="#5B4630" stroke-width="1"/><g fill="#E8C98E" stroke="#8A6A3A" stroke-width=".35"><ellipse cx="12.4" cy="6.4" rx=".8" ry="1.1"/><ellipse cx="14" cy="9.4" rx=".8" ry="1.1"/><ellipse cx="11.6" cy="11" rx=".8" ry="1.1"/><ellipse cx="13.8" cy="13.6" rx=".8" ry="1.1"/></g>',
    "tuer-offen-licht": '<path d="M1 7.6L8 1.6l7 6z" fill="#A0603A" stroke="#3B3226" stroke-width=".8"/><path d="M2 7.4h12v8.2H2z" fill="#D8C49C" stroke="#3B3226" stroke-width=".8"/><path d="M5.6 15.6V10q0-2.2 2.4-2.2t2.4 2.2v5.6z" fill="#F2C76E" stroke="#3B3226" stroke-width=".7"/><path d="M5.6 10.2L3.6 9v7.4l2-.8z" fill="#7A5A34" stroke="#3B3226" stroke-width=".6"/>',
    "gebetsriemen": '<path d="M2 12Q8 8 14 12" fill="none" stroke="#2E2017" stroke-width="1.6"/><path d="M5.2 3.2h5.6v5.6H5.2z" fill="#1E1610" stroke="#5B4630" stroke-width=".6"/><path d="M5.2 3.2l1-1.6h5.6l-1 1.6zM10.8 3.2l1-1.6v5.6l-1 1.6z" fill="#3B3226"/><path d="M8 8.8V11M3 11.4q-1 2 0 4.4M13 11.4q1 2 0 4.4" fill="none" stroke="#2E2017" stroke-width="1.2"/>',
    "feuerrad": '<path d="M3.6 9Q2 4.6 5 2q-.2 2.4 1.4 3Q6.6 1.4 9.8.6 8.8 3 10.6 4q1.6-1.6 1.2-3.4 3.2 3.2 1 8z" fill="#E8783A" stroke="#A3461E" stroke-width=".6"/><circle cx="8" cy="10.4" r="4.6" fill="none" stroke="#7A5A34" stroke-width="1.4"/><path d="M8 5.8v9.2M3.4 10.4h9.2M4.8 7.2l6.4 6.4M11.2 7.2l-6.4 6.4" stroke="#7A5A34" stroke-width=".8"/><circle cx="8" cy="10.4" r="1.2" fill="#5B4630"/>',
    "leinen": '<path d="M2 2.4h12l-.6 4.6 1 8.6-2.6-1.4-2.4 1.4-2.4-1.4-2.4 1.4-2.4-1.4L1.6 7z" fill="#F6EBD9" stroke="#3B3226" stroke-width=".8"/><path d="M2 2.4q6 3 12 0" fill="#E2D6BE" stroke="#3B3226" stroke-width=".6"/><path d="M5 5.4l-.4 8.6M8 5.8v8.6M11 5.4l.4 8.6" stroke="#D8CBB0" stroke-width=".7"/>',
    "stab-brief": '<path d="M3.4 1v15" stroke="#7A5A34" stroke-width="1.8" stroke-linecap="round"/><path d="M5.4 4.4h7.4l2 2v8.8H5.4z" fill="#F4F1EA" stroke="#3B3226" stroke-width=".8"/><path d="M7 8h5.6M7 10.4h6" stroke="#A79A80" stroke-width=".8"/><circle cx="12.4" cy="12.8" r="1.4" fill="#A33A2E"/>',
    "blatt-muenzen": '<path d="M1.6 1.6h9.6v10H1.6z" fill="#F4F1EA" stroke="#3B3226" stroke-width=".8"/><path d="M3.2 4.2h6.4M3.2 6.4h6.4M3.2 8.6h4" stroke="#A79A80" stroke-width=".8"/><circle cx="10.4" cy="12.4" r="2.6" fill="#E0B24E" stroke="#9C6F1C" stroke-width=".6"/><circle cx="13.4" cy="10" r="2.2" fill="#C9C2B4" stroke="#8C8070" stroke-width=".6"/>',
    "tafel-griffel": '<path d="M1.6 2.4h10v12.4h-10z" fill="#A07A44" stroke="#3B3226" stroke-width=".8"/><path d="M3 3.8h7.2v9.6H3z" fill="#3B3226"/><path d="M4.2 6h4.6M4.2 8.2h4.6M4.2 10.4h3" stroke="#C9B48E" stroke-width=".6"/><path d="M10.4 13.6L15.2 1.8" stroke="#8C8070" stroke-width="1.3" stroke-linecap="round"/>',
    "hirte": '<path d="M13.6 16V5q0-4-2.6-4T8.6 3.4" fill="none" stroke="#7A5A34" stroke-width="1.6" stroke-linecap="round"/><g fill="#FFFDF6" stroke="#3B3226" stroke-width=".6"><circle cx="4.4" cy="9" r="2"/><circle cx="7" cy="8.2" r="2"/><circle cx="9.6" cy="9" r="2"/><circle cx="5.6" cy="11.4" r="2"/><circle cx="8.6" cy="11.4" r="2"/></g><ellipse cx="2.4" cy="8.4" rx="1.6" ry="2" fill="#3B3226"/><path d="M5 13v2.6M9 13v2.6" stroke="#3B3226" stroke-width=".9"/>',
    "buendel": '<path d="M2.6 16L13 1.4" stroke="#7A5A34" stroke-width="1.6" stroke-linecap="round"/><path d="M11.2 4.6q-4 .4-4.4 4.4.2 4 4.4 4.2 4.2-.2 4.4-4.2-.4-4-4.4-4.4z" fill="#C9A27A" stroke="#3B3226" stroke-width=".8"/><path d="M8.6 7.2q2.6 1.6 5.2 0M9 10.6q2.2 1 4.4 0" fill="none" stroke="#9A6A3A" stroke-width=".6"/><path d="M10.2 4.8l1-2 1 2" fill="#C9A27A" stroke="#3B3226" stroke-width=".6"/>',
    "frage": '<path d="M1.6 2.4h12.8v9H7l-3.4 3.4v-3.4h-2z" fill="#FFFDF6" stroke="#3B3226" stroke-width=".8"/><path d="M6 5.4q0-1.8 2-1.8t2 1.6q0 1.2-1.4 1.8-.6.4-.6 1.4" fill="none" stroke="#2E5478" stroke-width="1.2" stroke-linecap="round"/><circle cx="8" cy="9.8" r=".7" fill="#2E5478"/>',
    "balken": '<path d="M.6 6.4L14 .8l1.4 3.4L2 9.8z" fill="#9A6A3A" stroke="#3B3226" stroke-width=".8"/><path d="M3 6.6l9.6-4M4.4 7.6l6-2.6" stroke="#6A4A2A" stroke-width=".5"/>',
    "ruder": '<path d="M2.4 15.6L11.6 4.4" stroke="#7A5A34" stroke-width="1.5" stroke-linecap="round"/><path d="M9.8 6.6Q10.4 2.4 13.6.8q2 .4 1.4 2.6-1 3.2-5.2 3.2z" fill="#A07A44" stroke="#3B3226" stroke-width=".7"/><path d="M1.2 12.6l3 2.6" stroke="#7A5A34" stroke-width="1.5" stroke-linecap="round"/>',
    "sack": '<path d="M4 6.4Q1 9 1.6 12.4 2.4 15.6 8 15.6t6.4-3.2Q15 9 12 6.4z" fill="#5E5A52" stroke="#2E2A24" stroke-width=".8"/><path d="M4 6.4q4-1.6 8 0" fill="none" stroke="#2E2A24" stroke-width="1"/><path d="M6 5.8Q6.2 2 8 1.6q1.8.4 2 4.2" fill="#5E5A52" stroke="#2E2A24" stroke-width=".7"/><path d="M5.4 4.8h5.2" stroke="#8A6A3A" stroke-width="1.2"/>',
    "unkraut": '<g stroke="#3E4A2A" stroke-width="1" stroke-linecap="round" fill="none"><path d="M6 16Q6 8 3 2M8 16V1.4M10 16q0-8 3-14"/></g><g fill="#2E3420"><ellipse cx="3.4" cy="3" rx=".9" ry="1.5"/><ellipse cx="4.6" cy="5.4" rx=".9" ry="1.5"/><ellipse cx="8" cy="2.4" rx=".9" ry="1.5"/><ellipse cx="8" cy="5" rx=".9" ry="1.5"/><ellipse cx="12.6" cy="3" rx=".9" ry="1.5"/><ellipse cx="11.4" cy="5.4" rx=".9" ry="1.5"/></g>',
}
ATTR_VB = "0 0 16 16"

# ------------------------------------------------------------------ Figuren
# robe, mantle, hair (Farbe), style (short|curls|long|bald|none), beard (None|short|full|long), beard_color,
# head (None | ("veil", Farbe) | ("turban", Farbe) | ("hood", Farbe) | ("crown",) | ("helmet",) | ("wreath",) | ("band", Farbe)),
# age (adult|young|old|child|baby), sex (m|f), belt, sash, apron, trim, attr (Attribut), wings, bound, chains, kneel
def F(robe, mantle=None, hair="#2E2017", style="short", beard=None, head=None, age="adult", sex="m", attr=None, **kw):
    return dict(robe=robe, mantle=mantle, hair=hair, style=style, beard=beard, head=head, age=age, sex=sex, attr=attr, **kw)


GREY, WHITE, DARK, BROWN, BLACK = "#8A8478", "#D8D2C4", "#2E2017", "#4A3020", "#1E1610"
APOSTLE = "#9C7A4C"
FIGS = {
    # Zwölf und Jünger (Jüngergewand, je eigene Mantelfarbe)
    "FIG-PETRUS": F(APOSTLE, "#C08A2A", GREY, "curls", "short", attr="schluessel"),
    "FIG-ANDREAS": F(APOSTLE, "#6E8B3D", "#5A4A3A", "long", "full", attr="x-kreuz"),
    "FIG-JAKOBUS-ZEBEDAEUS": F(APOSTLE, "#2F6F73", BROWN, "short", "full", attr="muschelstab"),
    "FIG-JOHANNES-ZEBEDAEUS": F(APOSTLE, "#6A8FB3", "#6A4A2A", "short", None, age="young", attr="kelch"),
    "FIG-PHILIPPUS": F(APOSTLE, "#8F6BA8", DARK, "short", "short", attr="stabkreuz"),
    "FIG-BARTHOLOMAEUS": F(APOSTLE, "#7A4E3A", DARK, "curls", "full", attr="messer"),
    "FIG-NATANAEL": F(APOSTLE, "#5E7F3A", DARK, "curls", "full", attr="feigenblatt"),
    "FIG-MATTHAEUS": F(APOSTLE, "#3F5A7A", BROWN, "short", "full", attr="buch"),
    "FIG-LEVI": F("#4A6B5A", "#4A6B5A", BROWN, "short", "short", attr="muenzen"),
    "FIG-THOMAS": F(APOSTLE, "#A0703A", DARK, "short", "short", attr="winkelmass"),
    "FIG-JAKOBUS-ALPHAEUS": F(APOSTLE, "#6B6B8A", BROWN, "short", "full", attr="walkerstange"),
    "FIG-THADDAEUS": F(APOSTLE, "#8A8F4A", DARK, "long", "full", attr="keule"),
    "FIG-JUDAS-NICHT-ISKARIOT": F(APOSTLE, "#5F8F8A", DARK, "short", "short", attr="frage"),
    "FIG-SIMON-KANANAEUS": F(APOSTLE, "#9A4E4E", "#3A2A1C", "curls", "full", attr="saege"),
    "FIG-JUDAS-ISKARIOT": F(APOSTLE, "#7A8A9A", DARK, "short", "short", attr="kasse"),
    "FIG-LIEBLINGSJUENGER": F(APOSTLE, "#E2CDA8", "#4A3020", "curls", None, age="young"),
    # Frauen
    "FIG-MARIA-MAGDALA": F("#E2CDA8", "#8E3B5E", "#4A2A1A", "long", sex="f", head=("veil", "#8E3B5E"), attr="alabaster"),
    "FIG-MARIA-BETANIEN": F("#6B8E7A", None, "#3A2618", "long", sex="f", attr="flaeschchen"),
    "FIG-MARTA": F("#B4704A", None, "#3A2618", "short", sex="f", head=("veil", "#E9D8B4"), attr="kelle"),
    "FIG-MARIA-KLOPAS": F("#D8CBB0", None, DARK, "short", sex="f", head=("veil", "#7A6A8E")),
    "FIG-MARIA-MUTTER-JAKOBUS": F("#6E7F5A", None, DARK, "short", sex="f", head=("veil", "#D8CBB0"), attr="oelkrug"),
    "FIG-SALOME": F("#F2E6CC", None, GREY, "short", sex="f", age="old", head=("veil", "#B07A3E"), attr="oelkrug"),
    "FIG-HERODIAS": F("#7A3E6A", None, BLACK, "long", sex="f", trim="#D9A441", head=("veil", "#C9A0BE")),
    "FIG-TOCHTER-HERODIAS": F("#D4537E", None, BLACK, "long", sex="f", age="young"),
    "FIG-EUODIA": F("#A8687A", None, DARK, "short", sex="f", head=("veil", "#D8B4A0")),
    "FIG-SYNTYCHE": F("#6A8AA8", None, BROWN, "short", sex="f", head=("veil", "#F2E6CC")),
    "FIG-AUSERWAEHLTE-HERRIN": F("#6A4A7A", None, DARK, "short", sex="f", head=("veil", "#F2E6CC"), attr="kind"),
    # Rut
    "FIG-RUT": F("#7A8B4A", None, BROWN, "short", sex="f", head=("veil", "#E8B84A"), attr="garbe"),
    "FIG-NOOMI": F("#C9BFAA", None, GREY, "short", sex="f", age="old", head=("veil", "#4A4A5A")),
    "FIG-ORPA": F("#8E6A7A", None, DARK, "short", sex="f", head=("veil", "#E2CDA8")),
    "FIG-BOAS": F("#E8B84A", "#2F5F6F", "#5A4A3A", "short", "full", attr="worfel"),
    "FIG-ELIMELECH": F("#C9BFAA", "#6A5A4A", GREY, "short", "full", attr="buendel"),
    "FIG-MACHLON": F("#7A6A5A", None, DARK, "short", None, age="young", sash="#7A8B4A"),
    "FIG-KILJON": F("#7A6A5A", None, DARK, "curls", None, age="young", sash="#8E6A7A"),
    "FIG-LOESER": F("#8A7A6A", "#5B4630", DARK, "short", "full", attr="schuh"),
    "FIG-OBED": F("#F2E6CC", None, DARK, "none", age="baby"),
    # Propheten, Könige
    "FIG-JONA": F("#6FB2E6", "#4A6E8A", DARK, "short", "full", attr="fisch"),
    "FIG-OBADJA": F("#E7DCC4", "#6A5A7A", GREY, "short", "long", attr="rolle", rough=True),
    "FIG-ELIJA": F("#8A6A3A", "#5B4630", GREY, "long", "long", fur=True, attr="feuerrad"),
    "FIG-HERODES-ANTIPAS": F("#6A2E5E", "#3E1A36", BLACK, "short", "short", head=("band", "#D9A441"), trim="#D9A441"),
    # Johannes der Täufer und Evangelien-Personen
    "FIG-JOHANNES-TAEUFER": F("#8A6A3A", None, "#3A2618", "long", "full", belt="#5B4630", attr="kreuzstab", fur=True),
    "FIG-NIKODEMUS": F("#C9BFAA", "#3B4A6B", GREY, "short", "full", head=("turban", "#3B4A6B"), attr="lampe"),
    "FIG-LAZARUS": F("#E7DCC4", None, BROWN, "short", "short", belt="#8A7A60"),
    "FIG-JAIRUS": F("#E7DCC4", "#4F6B7A", "#4A3020", "short", "full", head=("hood", "#E7DCC4"), tassels=True),
    "FIG-BARTIMAEUS": F("#C9BFAA", "#8A7A60", GREY, "short", "short", attr="stab"),
    "FIG-GERASENER": F("#8A8070", None, DARK, "long", "short", chains=True),
    "FIG-JOSEF-ARIMATAEA": F("#F6EBD9", "#5A5A5A", GREY, "short", "full", attr="leinen"),
    "FIG-SIMON-KYRENE": F("#8A7A50", None, DARK, "short", "short", belt="#5B4630", attr="balken"),
    "FIG-BARABBAS": F("#7A6A5A", None, BLACK, "short", "short", bound=True),
    "FIG-MALCHUS": F("#B8A98A", None, DARK, "short", None, sash="#4A5A7A"),
    "FIG-PILATUS": F("#F2E6CC", None, "#5A4A3A", "short", None, trim="#6A2E5E", toga=True),
    "FIG-KAJAFAS": F("#4A5A7A", None, GREY, "short", "full", head=("turban", "#F6EBD9"), breast=True, plate=True),
    "FIG-HANNAS": F("#6A6A7A", "#8A8A8A", WHITE, "short", "long", head=("turban", "#F6EBD9"), attr="stab", breast=True),
    "FIG-SATAN": None,  # dunkler Schatten ohne Gestalt: Bauteil in bildsymbole.py
    # Mitarbeitende und Briefpersonen
    "FIG-TIMOTHEUS": F("#5A7A9A", None, BROWN, "short", None, age="young", attr="stab-brief"),
    "FIG-TITUS": F("#5A6A3A", None, DARK, "curls", "short", attr="brief"),
    "FIG-EPAPHRODITUS": F("#7A8A5A", "#E2CDA8", BROWN, "short", "short", attr="beutel"),
    "FIG-DER-AELTESTE": F("#6A6A6A", "#E7DCC4", WHITE, "short", "long", age="old", attr="brief-feder"),
    "FIG-GAIUS": F("#8A6A4A", "#F6EBD9", DARK, "short", "short", attr="tuer-offen-licht"),
    "FIG-DIOTREPHES": F("#6A5A5A", "#C9BFAA", DARK, "short", "short", attr="tuer"),
    "FIG-DEMETRIUS": F("#4A7A6A", "#E7DCC4", BROWN, "short", "short", attr="brief"),
    # Rollen
    "FIG-ROLLE-AELTESTER": F("#C9BFAA", "#6A5A4A", GREY, "short", "long", age="old", attr="stab"),
    "FIG-ROLLE-BOTE": F("#E2CDA8", "#8A6A3A", DARK, "short", "short", attr="brief", staff=True),
    "FIG-ROLLE-ENGEL": F("#FFFFFF", None, "#D9A441", "short", None, wings=True),
    "FIG-ROLLE-FISCHER": F("#6A7F8A", None, DARK, "curls", "short", attr="netz"),
    "FIG-ROLLE-HIRTE": F("#8A7A50", "#F6EBD9", DARK, "short", "short", attr="hirte"),
    "FIG-ROLLE-HOHEPRIESTER": F("#4A5A7A", None, GREY, "short", "full", head=("turban", "#F6EBD9"), breast=True),
    "FIG-ROLLE-KAPITAEN": F("#8A6A3A", "#2F4F6F", DARK, "short", "full", head=("band", "#2F4F6F"), attr="ruder", rope=True),
    "FIG-ROLLE-KRANKER": F("#C9BFAA", None, DARK, "short", "short", attr="matte-rolle"),
    "FIG-ROLLE-PHARISAEER": F("#5A6A7A", "#4F6D8A", DARK, "short", "full", tassels=True, tallit=True, tefillin=True),
    "FIG-ROLLE-PRIESTER": F("#F6EBD9", None, DARK, "short", "short", head=("turban", "#F6EBD9"), sash="#4A5A7A"),
    "FIG-ROLLE-SCHRIFTGELEHRTER": F("#6A5A4A", "#E7DCC4", DARK, "short", "full", attr="rolle-feder"),
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
    if st == "long" and not hd:
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
              "tallit", "tefillin", "bandage", "crossed", "rope", "patches", "sword", "staff", "rough"):  # Schalter des Zeichners (bilder_anime.head_inner/body_inner)
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
