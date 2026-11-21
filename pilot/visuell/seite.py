#!/usr/bin/env python3
"""Seite «Visuelle Sprache der Bibel» (Analyse und Vorschlag, 2026-11-21) aus den Beispielen in beispiele.py.

  python3 pilot/visuell/seite.py <ausgabe.html> <ordner-mit-vignetten> [<jona-bild.png>]
"""
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import beispiele as B  # noqa: E402

ROOT = B.ROOT
AQ = ROOT / "data/illustrations/aquarell"


def fig(inhalt, titel, text, regel=None, beleg=None, id_=None, breit=True):
    meta = ""
    if regel or beleg:
        meta = '<dl class="meta">' + (f"<dt>Regel</dt><dd>{regel}</dd>" if regel else "") + (f"<dt>Belege</dt><dd>{beleg}</dd>" if beleg else "") + "</dl>"
    return (f'<figure class="bsp{" breit" if breit else ""}"{f" id={chr(34)}{id_}{chr(34)}" if id_ else ""}><div class="papier">{inhalt}</div>'
            f'<figcaption><strong>{titel}</strong> {text}{meta}</figcaption></figure>')


def pz(x):
    return f"{x:.1f}".replace(".", ",")


def img(url, alt, cls=""):
    return f'<img src="{url}" alt="{B.esc(alt)}" class="{cls}">'


def main():
    out, vig = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
    jona = pathlib.Path(sys.argv[3]) if len(sys.argv) > 3 and pathlib.Path(sys.argv[3]).is_file() else None
    d = json.loads((B.P / "inhaltsarten.json").read_text(encoding="utf-8"))
    v = lambda n, **kw: B.bild(vig / f"{n}.png", **kw)  # noqa: E731

    stationen = [("G1-schoepfung", "Schöpfung", "Gen 1"), ("G2-abraham", "Verheissung an Abraham", "Gen 15"), ("G3-exodus", "Auszug aus Ägypten", "Ex 14"),
                 ("G4-david", "David, der König", "1 Sam 16"), ("G5-exil", "Exil", "2 Kön 25"), ("G6-grab", "Kreuz und leeres Grab", "Mk 16"),
                 ("G7-gemeinde", "Die Gemeinde", "Apg 2"), ("G8-neuschoepfung", "Neue Schöpfung", "Offb 22")]
    crop = {"G8-neuschoepfung": (0.50, 0.12, 0.88, 0.72)}
    band = "".join(f'<div class="st"><img src="{v(n, breite=420, crop=crop.get(n, (0.12, 0.08, 0.88, 0.92)))}" alt="{B.esc(name)}">'
                   f'<span class="st-n">{i}</span><b>{name}</b><small>{ref}</small></div>' for i, (n, name, ref) in enumerate(stationen, 1))
    gross = f'<div class="stationen">{band}</div>'

    portraits = ["FIG-JESUS", "FIG-MARIA-MUTTER-JESU", "FIG-PAULUS", "FIG-TITUS", "FIG-ROLLE-VATER", "FIG-ROLLE-SOHN", "FIG-ROLLE-SPEISEMEISTER",
                 "FIG-ROLLE-AELTESTER", "FIG-ZENAS", "FIG-APOLLOS", "FIG-OBJ-KRUG-WASSER", "FIG-OBJ-SCHRIFTROLLE"]
    lex = json.loads((ROOT / "scripts/authoring/bilder_aquarell_daten/figuren.json").read_text(encoding="utf-8"))
    namen = {"FIG-JESUS": "Jesus", "FIG-MARIA-MUTTER-JESU": "Maria", "FIG-PAULUS": "Paulus", "FIG-TITUS": "Titus", "FIG-ROLLE-VATER": "Vater (Lk 15)",
             "FIG-ROLLE-SOHN": "jüngerer Sohn", "FIG-ROLLE-SPEISEMEISTER": "Speisemeister", "FIG-ROLLE-AELTESTER": "Ältester", "FIG-ZENAS": "Zenas",
             "FIG-APOLLOS": "Apollos", "FIG-OBJ-KRUG-WASSER": "Steinkrug", "FIG-OBJ-SCHRIFTROLLE": "Schriftrolle"}
    lexikon = '<div class="lex">' + "".join(f'<div><img src="{B.bild(AQ / "figuren" / (p + ".webp"), breite=240)}" alt="{namen[p]}"><span>{namen[p]}</span></div>'
                                             for p in portraits) + "</div>"

    pilot = ROOT / "pilot/struktur/ergebnis"
    bild_tit_buch = B.bild(pathlib.Path(sys.argv[4]) if len(sys.argv) > 4 else AQ / "img/TIT-001-E1.webp", breite=1100)
    lk15 = B.bild(pathlib.Path(sys.argv[5]), breite=1100) if len(sys.argv) > 5 else ""
    e1 = B.bild(AQ / "img/TIT-001-E1.webp", breite=360)
    r2 = B.bild(AQ / "img/TIT-003-R2.webp", breite=360)
    c2 = B.bild(AQ / "img/TIT-003-C2.webp", breite=420)
    l2 = B.bild(AQ / "img/LUK-015-L2.webp", breite=520)
    p1 = v("P1-baum", breite=520, crop=(0.50, 0.04, 0.80, 0.92))
    p2 = v("P2-spreu", breite=520, crop=(0.25, 0.10, 0.75, 0.90))
    roh_p1 = v("P1-baum", breite=420, crop=(0.15, 0.03, 0.85, 0.92))
    roh_g8 = v("G8-neuschoepfung", breite=420, crop=(0.15, 0.10, 0.88, 0.85))

    anteil = d["anteil"]
    erz = str(anteil["erz"]).replace(".", ",")

    jona_html = (img(B.bild(jona, breite=1100), "Jona in vier gemalten Stationen: Sturm, Fisch, Ninive, Rizinus") if jona else
                 '<p class="platzhalter">Die vier gemalten Stationen von Jona folgen.</p>')

    seite = f"""<title>Visuelle Sprache der Bibel</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Source+Serif+4:opsz,wght@8..60,400;8..60,600&display=swap">
<style>
/* Layout: eine Lesespalte für den Text, Beispiele dürfen breiter werden; Papierflächen für Bilder bleiben in beiden Modi hell. */
:root {{
  --bg: #F6F5F1; --fg: #22231F; --muted: #686A62; --rule: #DAD7CE; --soft: #ECEAE3; --accent: #A4532A; --accent-soft: #F1E2D6;
  --paper: #FBF8F2; --paper-rule: #E2DBCC;
  --f-display: "Source Serif 4", Georgia, "Times New Roman", serif;
  --f-text: Inter, "Helvetica Neue", Arial, sans-serif;
}}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{
  --bg: #1B1C19; --fg: #E9E7E0; --muted: #A5A39A; --rule: #3A3B35; --soft: #26271F; --accent: #E0915F; --accent-soft: #3A2A20; color-scheme: dark }} }}
:root[data-theme="dark"] {{ --bg: #1B1C19; --fg: #E9E7E0; --muted: #A5A39A; --rule: #3A3B35; --soft: #26271F; --accent: #E0915F; --accent-soft: #3A2A20; color-scheme: dark }}
body {{ background: var(--bg); color: var(--fg); font-family: var(--f-text); font-size: 16px; line-height: 1.6;
  padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px)); padding-block: 0 64px }}
.wrap {{ max-width: 1060px; margin: 0 auto }}
.text {{ max-width: 720px }}
header {{ padding-block: 48px 24px; border-bottom: 1px solid var(--rule); margin-bottom: 32px }}
.eyebrow {{ font-size: 12px; letter-spacing: .08em; text-transform: uppercase; color: var(--muted); margin: 0 0 10px }}
h1 {{ font-family: var(--f-display); font-weight: 600; font-size: clamp(34px, 6vw, 54px); line-height: 1.05; margin: 0 0 16px; text-wrap: balance }}
h2 {{ font-family: var(--f-display); font-weight: 600; font-size: 28px; line-height: 1.2; margin: 56px 0 12px; text-wrap: balance }}
h3 {{ font-size: 17px; margin: 28px 0 6px }}
.lead {{ font-size: 19px; color: var(--fg); max-width: 720px; margin: 0 }}
.stand {{ color: var(--muted); font-size: 14px; margin-top: 14px }}
p, li {{ max-width: 720px }}
a {{ color: var(--accent) }}
nav.toc {{ display: flex; flex-wrap: wrap; gap: 6px 14px; font-size: 14px; margin: 22px 0 0 }}
nav.toc a {{ color: var(--muted); text-decoration: none; border-bottom: 1px solid var(--rule) }}
nav.toc a:hover, nav.toc a:focus-visible {{ color: var(--accent) }}
.kurz {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 14px; margin: 18px 0 }}
.kurz div {{ background: var(--soft); border-radius: 8px; padding: 14px 16px; min-width: 0 }}
.kurz b {{ display: block; font-family: var(--f-display); font-size: 19px; margin-bottom: 4px }}
.kurz p {{ margin: 0; font-size: 15px }}
figure.bsp {{ margin: 26px 0 34px }}
.papier {{ background: var(--paper); border: 1px solid var(--paper-rule); border-radius: 6px; padding: 10px; overflow-x: auto }}
.papier svg {{ display: block; width: 100%; min-width: 640px; height: auto; --f-text: var(--f-text); --f-display: var(--f-display) }}
.papier img {{ display: block; width: 100%; height: auto }}
figcaption {{ font-size: 14.5px; color: var(--muted); margin-top: 10px; max-width: 760px }}
figcaption strong {{ color: var(--fg) }}
dl.meta {{ display: grid; grid-template-columns: max-content 1fr; gap: 2px 12px; margin: 8px 0 0; font-size: 13.5px }}
dl.meta dt {{ font-weight: 600; color: var(--fg) }} dl.meta dd {{ margin: 0 }}
.tbl {{ overflow-x: auto; margin: 16px 0 }}
table {{ border-collapse: collapse; width: 100%; min-width: 760px; font-size: 14.5px }}
th, td {{ text-align: left; vertical-align: top; padding: 9px 10px; border-bottom: 1px solid var(--rule) }}
th {{ font-size: 12px; letter-spacing: .05em; text-transform: uppercase; color: var(--muted); font-weight: 600 }}
td.pct {{ font-variant-numeric: tabular-nums; white-space: nowrap }}
.chip {{ display: inline-block; width: 10px; height: 10px; border-radius: 2px; margin-right: 6px; vertical-align: 0 }}
.bars {{ display: grid; gap: 6px; margin: 14px 0; max-width: 760px }}
.bar {{ display: grid; grid-template-columns: minmax(130px, 260px) 1fr 54px; gap: 10px; align-items: center; font-size: 14px }}
.bar-t {{ background: var(--soft); height: 14px; border-radius: 3px; overflow: hidden }} .bar-f {{ display: block; height: 100% }}
.bar-v {{ font-variant-numeric: tabular-nums; text-align: right }}
.leg {{ display: flex; flex-wrap: wrap; gap: 6px 16px; font-size: 13.5px; margin: 10px 0 }}
.leg i {{ display: inline-block; width: 12px; height: 12px; border-radius: 2px; margin-right: 6px; vertical-align: -1px }}
.stationen {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px }}
.st {{ position: relative; display: flex; flex-direction: column; gap: 2px; font-size: 13.5px; color: #3E413B; min-width: 0 }}
.st img {{ aspect-ratio: 4 / 3; object-fit: cover; border-radius: 4px }}
.st-n {{ position: absolute; top: 6px; left: 6px; width: 22px; height: 22px; border-radius: 50%; background: #FBF8F2; border: 1px solid #CDBFA6;
  font-size: 12px; display: grid; place-items: center; color: #3E413B }}
.st small {{ color: #7A7C73 }}
.lex {{ display: grid; grid-template-columns: repeat(6, 1fr); gap: 8px }}
.lex div {{ display: flex; flex-direction: column; align-items: center; font-size: 12.5px; color: #3E413B; min-width: 0 }}
.lex img {{ aspect-ratio: 1; object-fit: cover; border-radius: 4px }}
.zwei {{ display: grid; grid-template-columns: 1fr 1fr; gap: 14px }}
.zwei > * {{ min-width: 0 }}
.ebenen {{ display: grid; gap: 0; margin: 16px 0; border-left: 2px solid var(--rule) }}
.ebene {{ display: grid; grid-template-columns: 150px 1fr; gap: 14px; padding: 12px 0 12px 18px; position: relative }}
.ebene::before {{ content: ""; position: absolute; left: -7px; top: 18px; width: 12px; height: 12px; border-radius: 50%; background: var(--bg); border: 2px solid var(--accent) }}
.ebene h4 {{ margin: 0; font-family: var(--f-display); font-size: 19px }}
.ebene p {{ margin: 0 0 4px; font-size: 15px }}
.ebene .form {{ font-size: 13.5px; color: var(--muted) }}
.merk {{ max-width: 760px }}
.merk-v {{ display: grid; grid-template-columns: 260px 1fr; gap: 18px; align-items: center; color: #3E413B }}
.merk-v img {{ border-radius: 4px }}
.merk-ref {{ font-size: 13px; letter-spacing: .06em; text-transform: uppercase; color: #7A7C73; margin: 0 }}
.merk-z {{ font-family: var(--f-display); font-size: 21px; line-height: 1.4; margin: 6px 0 10px }}
.luecke {{ border-bottom: 2px solid #BD8067; color: transparent; background: #F1E6D6; border-radius: 2px; padding: 0 4px; cursor: pointer }}
.luecke.offen {{ color: #8A4B33; background: transparent }}
.merk-h {{ font-size: 13.5px; color: #7A7C73; margin: 0 }}
.regeln {{ counter-reset: r; list-style: none; padding: 0; display: grid; gap: 10px }}
.regeln li {{ counter-increment: r; display: grid; grid-template-columns: 34px 1fr; gap: 6px; max-width: 820px }}
.regeln li::before {{ content: counter(r); font-family: var(--f-display); font-weight: 600; color: var(--accent); font-size: 20px; line-height: 1.3 }}
.ev {{ font-size: 12px; color: var(--muted); white-space: nowrap }}
.platzhalter {{ padding: 40px; text-align: center; color: #7A7C73 }}
.hinweis {{ background: var(--accent-soft); border-radius: 8px; padding: 14px 16px; max-width: 760px }}
.phasen {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 12px; margin: 14px 0 }}
.phasen div {{ border: 1px solid var(--rule); border-radius: 8px; padding: 14px; min-width: 0 }}
.phasen b {{ font-family: var(--f-display); font-size: 18px }}
.phasen p {{ margin: 6px 0 0; font-size: 14.5px }}
.quellen li {{ font-size: 14px; margin-bottom: 4px }}
@media (max-width: 720px) {{
  .stationen {{ grid-template-columns: repeat(2, 1fr) }} .lex {{ grid-template-columns: repeat(3, 1fr) }} .zwei {{ grid-template-columns: 1fr }}
  .ebene {{ grid-template-columns: 1fr }} .merk-v {{ grid-template-columns: 1fr }} .bar {{ grid-template-columns: 120px 1fr 48px }}
}}
@media (prefers-reduced-motion: reduce) {{ * {{ transition: none !important }} }}
</style>

<div class="wrap">
<header>
  <p class="eyebrow">Atmo Bible · Analyse und Vorschlag</p>
  <h1>Visuelle Sprache der Bibel</h1>
  <p class="lead">Wie wir die ganze Bibel auf allen Ebenen so ins Bild bringen, dass sie zugänglich wird, im Gedächtnis bleibt und zum Vertiefen anregt: welche Teile in welcher Form, nach festen Regeln statt nach Geschmack.</p>
  <p class="stand">Stand 21. November 2026 · Entwurf, fachlich nicht geprüft · Grundlage: unsere Tests seit Oktober, der Strukturkatalog, 673 Kernanalysen, eine Literaturrecherche und neue Beispielbilder</p>
  <nav class="toc" aria-label="Inhalt"><a href="#kurz">Kurzfassung</a><a href="#gelernt">Was die Tests zeigen</a><a href="#forschung">Was die Forschung sagt</a>
  <a href="#bestand">Woraus die Bibel besteht</a><a href="#formen">Form je Inhalt</a><a href="#ebenen">Die Ebenen</a><a href="#beispiele">Beispiele</a>
  <a href="#gedaechtnis">Gedächtnis</a><a href="#zugang">Zugänglich für alle</a><a href="#prozess">Prozess</a><a href="#umfang">Umfang und Reihenfolge</a><a href="#offen">Zu entscheiden</a></nav>
</header>

<section id="kurz">
<h2>Kurzfassung</h2>
<div class="kurz">
  <div><b>{erz} % erzählen</b><p>Diese Teile der Bibel tragen gemalte Szenen im Aquarellstil. Die anderen {100 - anteil['erz']:.0f} % sind unter anderem Prophetenworte, Lieder, Briefe, Weisheit, Gesetze, Listen und Visionen. Sie brauchen gezeichnete Strukturbilder, Karten, Zeitleisten und Modelle.</p></div>
  <div><b>Form je Feld, gemischt</b><p>Die Darstellung wird für jedes Bildfeld aus dem Inhalt gewählt, auch innerhalb eines Buchs. In den zwölf bisher analysierten Büchern passt die Szene für 47 % der Abschnitte. Für den Rest passt eine Strukturform.</p></div>
  <div><b>Daten zeichnen, das Bildmodell malt</b><p>Anordnung, Zahlen, Masse und Worte kommen aus Daten und sind genau. Figuren, Gegenstände und Landschaft malt das Bildmodell als Szene oder Vignette. Nie stehen Text oder Masse im gemalten Bild.</p></div>
  <div><b>Feste Anker auf allen Ebenen</b><p>Jedes Buch hat einen festen Platz, jede Figur ein festes Aussehen, jede Geschichte einen Ort auf der Karte und eine Zeit. Höhere Ebenen zeigen dieselben Bilder wie die Ebenen darunter.</p></div>
  <div><b>Jedes Bild hat eine Aufgabe</b><p>Schmückende Bilder schaden dem Lernen nachweislich. Gemalt wird, was der Text erzählt oder selbst als Bild gebraucht; alles Weitere ist als Ausgestaltung (R) oder Deutung (I) gekennzeichnet.</p></div>
  <div><b>Einprägen heisst abrufen</b><p>Bilder werden nicht nur gezeigt, sondern abgefragt: Szenen ordnen, Merkvers ergänzen, nach einem Tag und nach einer Woche wiederholen, später in grösseren Abständen. Dazu kommt Audio zu jeder Szene.</p></div>
</div>
</section>

<section id="gelernt">
<h2>Was die Tests seit Oktober zeigen</h2>
<div class="tbl"><table>
<thead><tr><th>Test</th><th>Ergebnis</th><th>Folgerung</th></tr></thead>
<tbody>
<tr><td>Gezeichnete Bilder ohne Bildmodell (Symbol- und Animestil, rund 1200 Bilder)</td><td>Inhaltlich geprüft, aber optisch nicht gut genug; sie wirken technisch und laden nicht zum Verweilen ein.</td><td>Durch gemalte Szenen oder Hybridbilder ersetzen.</td></tr>
<tr><td>Aquarellszenen mit automatischer Prüfung (Joh 2, Mk 4, Lk 15, Titus; 31 Felder)</td><td>Bei Geschichten stark und berührend. Nach Schärfung der Regeln haben alle Felder bestanden, ohne Handarbeit.</td><td>Standard für alles Erzählte.</td></tr>
<tr><td>Titus vollständig als Szenen</td><td>Bei Anweisungen und Listen entstehen erfundene Alltagsszenen; sie sind wenig aussagekräftig und schwer eindeutig zu prüfen.</td><td>Form je Feld aus dem Inhalt (Entscheid 28.10.).</td></tr>
<tr><td>Stilprobe mit stärkerer Reduktion</td><td>Figuren werden kleiner, Gesichter und Gesten schlechter lesbar.</td><td>Detailgrad wie die Stilvorlage.</td></tr>
<tr><td>Hybridpiloten: Seligpreisungen, Stiftshütte, Karte Joh 2</td><td>Gezeichnete Anordnung mit gemalten Vignetten oder Aquarelltextur wirkt ruhig, schön und genau.</td><td>Standard für Strukturbilder.</td></tr>
<tr><td>Bildlexikon mit 45 gemalten Einträgen</td><td>Figuren und Gegenstände sind über Bücher hinweg wiedererkennbar.</td><td>Grundlage für alle Ebenen; laufend ergänzen.</td></tr>
</tbody></table></div>
</section>

<section id="forschung">
<h2>Was die Forschung sagt</h2>
<p class="text">Kontrollierte Studien zur Wirkung von Bildern auf Bibelkenntnis gibt es praktisch keine. Gut belegt ist die allgemeine Lern- und Gedächtnisforschung; die Regeln unten übertragen sie. Die Stärke der Belege steht jeweils dabei.</p>
<ol class="regeln">
<li><div><b>Bilder bleiben besser haften als Worte</b>, vor allem wenn Bild und Wort zusammen kommen (Bildüberlegenheit, doppelte Codierung). Der Effekt verschwindet, wenn die Bilder einander zu ähnlich sind. <span class="ev">stark</span></div></li>
<li><div><b>Schmückende Details schaden.</b> Interessante, aber für das Lernziel unnötige Bilder senken das Behalten. Am stärksten schaden sie neben Diagrammen und als Dauerhintergrund. <span class="ev">stark, Metaanalyse über 58 Studien</span></div></li>
<li><div><b>Erzähltes wird viel besser erinnert</b> als Sachtext (Erinnerung g = 0,72). Argumentierende Texte wie Briefe und Gesetze brauchen am Bildschirm deshalb mehr Strukturhilfe. <span class="ev">stark</span></div></li>
<li><div><b>Beschriftung direkt am Bildteil</b>, Wesentliches hervorheben, in kleine Einheiten teilen, Namen vorab einführen. <span class="ev">stark (Mayer)</span></div></li>
<li><div><b>Rund vier Einheiten</b> fasst das Arbeitsgedächtnis. Je Ebene sollten 3 bis 5 Hauptgruppen sichtbar sein, nicht mehr. <span class="ev">stark</span></div></li>
<li><div><b>Abrufen festigt</b> mehr als nochmals lesen (g = 0,51 gegenüber Nochmal-Lesen). Am stärksten wirkt es, wenn nach einem Tag bis knapp einer Woche erneut geprüft wird. <span class="ev">stark</span></div></li>
<li><div><b>Orte als Gedächtnishilfe</b> (Gedächtnispalast) helfen bei Reihenfolgen deutlich, die Studien sind aber methodisch schwach. <span class="ev">grosser Effekt, schwache Evidenz</span></div></li>
<li><div><b>Bilder sind keine Weltsprache.</b> Bildzeichen wie Bewegungslinien oder Sterne werden je nach Kultur missverstanden. Wie Zeit angeordnet wird, folgt der Schreibrichtung. <span class="ev">mittel</span></div></li>
</ol>
<p class="text">Bestehende Ansätze passen dazu. BibleProject zeigt die Gesamtstruktur jedes Buchs und erreicht sehr viele Menschen; eine unabhängige Wirkungsprüfung fehlt. Comic- und Kinderbibeln sind stark bei Geschichten, lassen aber Gesetz, Prophetie und Apokalyptik meist weg, Briefe kommen kaum vor, und manches Bild fügt hinzu, was nicht im Text steht. Datengezeichnete Übersichten (Stammbäume, Zeitleisten) sind genau, wirken aber nach unserer Einschätzung oft spröde. Unser Weg verbindet beides: gemalt, wo erzählt wird, gezeichnet, wo geordnet wird, und alles aus derselben geprüften Analyse.</p>
</section>

<section id="bestand">
<h2>Woraus die Bibel besteht</h2>
<p class="text">Jedes Kapitel der Bibel ist nach seiner vorherrschenden Inhaltsart eingeordnet, gemessen in Versen. Das ist eine Schätzung je Kapitel: Ein Lied mitten in einer Erzählung zählt hier zur Erzählung. Für die Planung reicht diese Genauigkeit.</p>
{B.anteile()}
{fig(B.bibliothek(), "Die Bibel als Bibliothek.", "Jedes Buch ist ein Block, seine Breite entspricht der Zahl der Verse. Die Farben zeigen, woraus das Buch besteht. Diese Ansicht taugt auch als Einstieg in der App: Jedes Buch hat seinen festen Platz, und man sieht auf einen Blick, wo erzählt, gesungen, gemahnt oder geordnet wird.", "Bibelebene: Übersicht mit festen Plätzen (Gedächtnis: Ort).", "Verszahlen aus dem Navigationsgerüst; Inhaltsarten je Kapitel geschätzt (pilot/visuell/inhaltsarten.py).", "bibliothek")}
{B.legende()}
</section>

<section id="formen">
<h2>Welche Form für welchen Inhalt</h2>
<p class="text">Der Strukturkatalog kennt 33 Baumuster und 20 Darstellungen. Für die Planung bündeln wir sie hier in sechs eigene Gruppen (der Katalog selbst ordnet die Baumuster in neun Familien). Die Tabelle zeigt die Hauptform, die Ergänzungen und das Beispiel weiter unten auf dieser Seite.</p>
<div class="tbl"><table>
<thead><tr><th>Inhalt</th><th>Anteil</th><th>Hauptform</th><th>Ergänzt durch</th><th>Beispiel</th><th>Achtung</th></tr></thead>
<tbody>
<tr><td><span class="chip" style="background:{B.FAM['erz'][0]}"></span>Erzählung</td><td class="pct">{erz} %</td><td>Gemalte Szenen, ein Feld je tragendem Moment</td><td>Karte bei Wegen, Zeitleiste bei Daten, Stammbaum</td><td><a href="#b-jona">Jona</a>, <a href="#b-szene">Lk 15</a></td><td>Nur malen, was erzählt wird; Ankündigung bleibt Ankündigung.</td></tr>
<tr><td><span class="chip" style="background:{B.FAM['rede'][0]}"></span>Rede und Lehre, Gleichnis</td><td class="pct">{str(anteil['rede']).replace('.', ',')} %</td><td>Gleichnis als Szene; Reihen als Raster mit Vignetten</td><td>Redner klein am Rand</td><td><a href="#b-selig">Seligpreisungen</a></td><td>Gleichnisfiguren sind keine geschichtlichen Personen.</td></tr>
<tr><td><span class="chip" style="background:{B.FAM['ordnung'][0]}"></span>Gesetz, Listen, Bau</td><td class="pct">{pz(anteil['gesetz'] + anteil['liste'] + anteil['bau'])} %</td><td>Raster, Stammbaum, Modell und Grundriss</td><td>Weiche (wenn – dann), Karte für Gebiete</td><td><a href="#b-mt1">Mt 1</a>, <a href="#b-stifts">Stiftshütte</a></td><td>Zahlen nie glätten; Rekonstruktion als R kennzeichnen.</td></tr>
<tr><td><span class="chip" style="background:{B.FAM['lied'][0]}"></span>Lied, Gebet, Weisheit</td><td class="pct">{pz(anteil['poesie'] + anteil['weisheit'])} %</td><td>Strophen- und Parallelismusbild, Gegenüberstellung</td><td>Vignette für die Bildworte des Textes</td><td><a href="#b-ps1">Psalm 1</a></td><td>Bilder nur, wo der Text selbst ein Bild gebraucht.</td></tr>
<tr><td><span class="chip" style="background:{B.FAM['proph'][0]}"></span>Prophetie und Vision</td><td class="pct">{pz(anteil['prophetie'] + anteil['vision'])} %</td><td>Gegenläufige Bewegung, Karte der Völker, Reihenbild</td><td>Zeichenhandlung als Szene, beschriftete Skizze</td><td><a href="#b-obadja">Obadja</a>, <a href="#b-offb">Offb</a></td><td>Gericht und Heil vollständig; Deutungen nicht als Fahrplan zeichnen.</td></tr>
<tr><td><span class="chip" style="background:{B.FAM['brief'][0]}"></span>Brief und Argument</td><td class="pct">{str(anteil['brief']).replace('.', ',')} %</td><td>Spalten («nicht … sondern», «einst – jetzt»), Pfeilkette, Kurve</td><td>Szene nur, wo der Brief eine erzählt</td><td><a href="#b-titus">Titus</a>, <a href="#b-phil">Phil 2</a></td><td>Begründungen («denn») nie weglassen.</td></tr>
</tbody></table></div>
<p class="text">Aus den 673 vorhandenen Kernanalysen (zwölf Bücher, vor allem Evangelien) ergibt sich für die äussere Form der Abschnitte: Szenen 47 %, Dialog 13 %, Pfeilkette 9 %, Spalten 8 %, Raster 6 %, Gliederungsbild 5 %, zwei Ebenen 5 %, Rest unter 2 %. Für die ganze Bibel mit ihrem kleineren Erzählanteil dürfte der Anteil der Szenen eher bei einem Drittel liegen.</p>
</section>

<section id="ebenen">
<h2>Die Ebenen</h2>
<p class="text">Jede Ebene beantwortet eine eigene Frage. Gemeinsam ist allen: Was oben steht, kommt aus der Ebene darunter. So begegnet man demselben Bild beim Lesen eines Abschnitts, im Kapitel und im Buchüberblick wieder, und gerade diese Wiederholung prägt ein.</p>
<div class="ebenen">
  <div class="ebene"><h4>Bibel</h4><div><p>Wie hängt alles zusammen? Die Bibliothek der 66 Bücher und die grosse Geschichte in acht Stationen.</p><span class="form">Übersicht mit festen Plätzen · 8 gemalte Stationen · <a href="#b-gross">Beispiel</a></span></div></div>
  <div class="ebene"><h4>Testament, Buchgruppe</h4><div><p>Wann und wo? Eine Zeitleiste mit den Büchern nach Handlungszeit und eine Karte des Raums.</p><span class="form">Zeitleiste und Karte, Unsicheres sichtbar · <a href="#b-zeit">Beispiel</a></span></div></div>
  <div class="ebene"><h4>Buch</h4><div><p>Wovon handelt das Buch, wie ist es gebaut? Vier bis sechs Stationen und ein Bild des Aufbaus.</p><span class="form">Stationen (Szene oder Struktur je Station) und Buchband · <a href="#b-jona">Jona</a>, <a href="#b-titus">Titus</a></span></div></div>
  <div class="ebene"><h4>Kapitel</h4><div><p>Was geschieht der Reihe nach? Die Bildfolge der Abschnitte mit kurzem Band.</p><span class="form">Felder aus den Abschnitten, keine neuen Bilder</span></div></div>
  <div class="ebene"><h4>Abschnitt</h4><div><p>Was steht hier genau, wer handelt, wie ist der Text gebaut? Ein Feld je tragendem Moment.</p><span class="form">Form je Feld: Szene, Spalten, Raster, Kurve, Karte … · <a href="#b-szene">Szene</a>, <a href="#b-t3">Struktur</a></span></div></div>
  <div class="ebene"><h4>Vers</h4><div><p>Was will ich behalten? Merkverse mit ihrem Bild, als Lückentext zum Abrufen.</p><span class="form">Merkkarte mit Wiederholung · <a href="#b-merk">Beispiel</a></span></div></div>
</div>
{fig(img(bild_tit_buch, "Titus auf Buchebene: vier Stationen aus den Abschnittsbildern"), "Dieselben Bilder auf mehreren Ebenen.", "Die Buchebene von Titus braucht keine neuen Bilder: Ihre vier Stationen sind Felder aus den Abschnitten. Wer den Abschnitt gelesen hat, erkennt sie im Überblick wieder.", "Von unten nach oben (VERDICHTUNG.md); Wiederkehr prägt ein.", None, "b-ebenen")}
</section>

<section id="beispiele">
<h2>Beispiele</h2>
<p class="text">Alle Beispiele sind nach den Regeln dieses Vorschlags entstanden, nicht von Hand gestaltet. Gezeichnetes stammt aus Daten und aus dem Wortlaut unserer Arbeitsübersetzung; gemalte Teile stammen aus dem Bildlexikon, aus geprüften Szenen oder aus einem Pilotlauf.</p>

<h3>Bibel: die grosse Geschichte</h3>
{fig(gross, "Acht Stationen von der Schöpfung bis zur neuen Schöpfung.", "Als Band auf der Startseite und als Anker für die Bibliothek: Jedes Buch lässt sich einer oder mehreren Stationen zuordnen. Die Auswahl der Stationen ist eine redaktionelle Entscheidung und als solche zu kennzeichnen; Gott wird nicht gemalt.", "Bibelebene: 4–8 Stationen, je eine Vignette.", "Gemalt im Pilotlauf vom 21.11.2026 ohne automatische Prüfung.", "b-gross")}

<h3>Testament: Zeit</h3>
{fig(B.zeitleiste(), "Zeitleiste nach Handlungszeit.", "Frühe Epochen ohne Jahreszahl, gestrichelt; danach gängige Schätzungen. In Sprachen, die von rechts nach links geschrieben werden, läuft die Achse gespiegelt.", "Unsicherheit sichtbar machen statt Punkte vorzutäuschen.", "Jahreszahlen: übliche Schätzungen (R).", "b-zeit")}

<h3>Buch, Erzählung: Jona</h3>
{fig(jona_html, "Jona in vier Stationen.", "Ein erzählendes Buch: alle vier Stationen als gemalte Szene, im regulären Prozess gemalt und automatisch geprüft. Gott wird nicht gemalt; seine Schlussfrage steht im Band, und das Ende bleibt offen wie im Text.", "Erzählung → Szene; offener Schluss bleibt offen.", "Szenenplan szenen-jon.json mit Belegen B/R/I je Feld.", "b-jona")}
{fig(B.jona_struktur(), "Der Aufbau daneben.", "Dasselbe Buch braucht zusätzlich ein Strukturbild: Die Kapitel 1 und 3 laufen parallel, ebenso 2 und 4. Das Leitwort «hinab» zeichnet den Abstieg bis zu den Wurzeln der Berge. Szene und Struktur ergänzen sich.", "Gemischt erlaubt: Struktur als eigenes Feld neben den Szenen.", "Alle Zitate aus der Arbeitsübersetzung Jona 1–4.", "b-jona-s")}

<h3>Buch, Brief: Titus</h3>
{fig(B.titus_buchband(e1, r2), "Titus als Buchband mit Form je Feld.", "Gemalt werden nur die beiden Stellen, an denen der Brief selbst eine Szene hat: Titus setzt in Kreta Älteste ein, Zenas und Apollos werden ausgerüstet. Die übrigen Felder sind Strukturbilder. Die zwei Bögen zeigen den Bau des Briefs: zweimal folgen auf Weisungen ein «denn» und die Begründung aus der Gnade.", "Brief → Spalten, Raster, Pfeil; Szene nur, wo erzählt wird.", "Strukturkatalog: Titus «zweimal Pflichten → denn Gnade».", "b-titus")}
<div>
{fig(B.titus_nicht_sondern(), "Tit 1,7–8: nicht … sondern.", "Die linke Spalte ist durchgestrichen, wie es der Text mit «nicht» sagt. Fünf Glieder stehen gegen sechs, so wie im Text.", None, None, "b-t1")}
{fig(B.titus_einst(c2), "Tit 3,3–7: einst und als aber.", "Die Wende steht in der Mitte. Rechts folgen die Glieder der Rettung der Reihe nach. Die kleine Vignette ist aus dem Abschnittsbild übernommen.", None, None, "b-t3")}
</div>

<h3>Brief, Hymnus: Philipper 2</h3>
{fig(B.phil2(), "Der Weg hinab und hinauf.", "Der Christushymnus als V: Bis zum Kreuz handelt er selbst, ab «Darum» handelt Gott. Die Form selbst ist die Merkhilfe.", "Kurve für Abstieg und Erhöhung; Wende markiert.", "Wortlaut Phil 2,6–11, Arbeitsübersetzung.", "b-phil")}

<h3>Prophetie: Obadja</h3>
{fig(B.obadja(), "Hoch und tief, mit Karte.", "Edom wohnt hoch und wird hinabgestürzt, der Berg Zion steigt auf; in der Mitte steht der Spiegelsatz. Die kleine Karte verankert das Wort an seinem Ort.", "Umkehrung als gegenläufige Linien; Ort als Anker.", "Zitate Obd 3, 4, 15, 21; Lage ungefähr (R).", "b-obadja")}

<h3>Liste: Matthäus 1</h3>
{fig(B.matthaeus1(), "Drei Reihen von Generationen.", "Der Text nennt die Ordnung selbst («vierzehn Generationen»). Das Bild zeigt alle Namen und die vier Frauen, die der Text nennt, und glättet die Zählung der dritten Reihe nicht.", "Zahl und Glieder vollständig; Musterbruch sichtbar.", "Namen aus Mt 1,2–16, Arbeitsübersetzung.", "b-mt1")}

<h3>Lied: Psalm 1</h3>
{fig(B.psalm1(p1, p2), "Zwei Wege.", "Ein Lied, das selbst in Bildern spricht. Gemalt werden genau diese Bildworte, Baum und Spreu, als kleine Vignetten; die Ordnung zeigt die Gegenüberstellung.", "Poesie → Gegenüberstellung; Vignette nur für Bildworte des Textes.", "Vignetten aus dem Pilotlauf, ausgeschnitten (siehe unten).", "b-ps1")}

<h3>Vision: Offenbarung</h3>
{fig(B.offb(), "Drei Siebenerreihen.", "Im Text klar ist: dreimal sieben; bei Siegeln und Posaunen steht ein Einschub vor dem siebten Glied; auf das siebte Siegel folgen die Posaunen. Wie die Reihen zusammenhängen, ist Deutung; das Bild sagt es und legt sich nicht fest.", "Vision → Reihenbild; Deutungen offenlegen.", "Offb 6,1 – 8,1; 8,2 – 11,19; 16,1–21.", "b-offb")}

<h3>Bereits gemalt: Szene, Reihe, Modell, Karte</h3>
{fig(img(lk15, "Lukas 15,11–32 in drei gemalten Feldern"), "Szene: Lukas 15,11–32.", "Drei Felder nach den tragenden Momenten, mit wörtlicher Rede und Stichwortband. Automatisch geprüft und in der App.", "Erzählung → Szene.", None, "b-szene") if lk15 else ""}
{fig(img(B.bild(pilot / "seligpreisungen_B.png", breite=1000), "Seligpreisungen als Raster mit Vignetten"), "Reihe mit Vignetten: Seligpreisungen.", "Acht Glieder vollständig, Rahmen durch die gleiche Verheissung am Anfang und Ende, Zukunft farbig unterschieden. Die Vignetten sind als gedeutet (I) gekennzeichnet.", "Reihe → Raster; Vignette pro Glied.", None, "b-selig")}
{fig(img(B.bild(pilot / "stiftshuette_B.png", breite=1100), "Stiftshütte als Modell mit Massen"), "Modell: die Stiftshütte.", "Masse aus dem Text, gezeichnet; die Aquarelltextur macht daraus ein Bild, das man gern ansieht. Was rekonstruiert ist, steht als R dabei.", "Bau → Modell; B und R je Mass.", None, "b-stifts")}
{fig(img(B.bild(pilot / "karte_C.png", breite=700), "Karte Kana, Kafarnaum, Jerusalem"), "Karte: Johannes 2.", "Wege aus dem Text, gestrichelt, wo der Verlauf nicht überliefert ist; dazu das Höhenprofil zu «hinab» und «hinauf».", "Weg → Karte; Unsicheres gestrichelt.", None, "b-karte", False)}

<h3>Figuren über die ganze Bibel</h3>
{fig(lexikon, "Bildlexikon.", "Jede Person, Rolle und jedes wichtige Ding hat ein festes Aussehen, gemalt und geprüft. So erkennt man Titus im Abschnitt, im Kapitel und im Buch wieder, und Figuren verwechseln sich nicht.", "Unterscheidbare Figuren; Menschen des antiken Vorderen Orients.", None, "b-lex")}

<h3>Vers: Merkkarte</h3>
{fig(B.merkkarte(l2), "Lukas 15,24 zum Einprägen.", "Das Bild aus dem Abschnitt trägt den Vers. Die Lücken werden beim Antippen sichtbar; die App fragt den Vers nach einem Tag und nach einer Woche wieder ab, danach in grösseren Abständen.", "Abruf statt nur Zeigen; Bild aus der Ebene darunter.", None, "b-merk")}

<h3>Was die Prüfung abfangen muss</h3>
<div class="zwei">
{fig(img(roh_p1, "Rohbild Psalm 1 mit einer nicht verlangten Figur"), "Rohbild Psalm 1.", "Verlangt war nur ein Baum am Wasser. Das Bildmodell hat einen Mann im terrakottaroten Mantel dazugemalt, der wie Jesus aussieht.", None, None, None, False)}
{fig(img(roh_g8, "Rohbild neue Schöpfung mit einer nicht verlangten Figur"), "Rohbild neue Schöpfung.", "Dasselbe hier. Die Figur kommt aus der Stilvorlage. Für die Vignetten oben wurde sie weggeschnitten; im Regelbetrieb fängt die automatische Prüfung so etwas ab und lässt neu malen.", None, None, None, False)}
</div>
</section>

<section id="gedaechtnis">
<h2>Wie Bilder beim Einprägen helfen</h2>
<p class="text">Gedächtnis braucht Anker. Wir setzen fünf, die sich über die ganze Bibel durchziehen und auf jeder Ebene gleich bleiben:</p>
<div class="tbl"><table>
<thead><tr><th>Anker</th><th>Was er festhält</th><th>Umsetzung</th></tr></thead>
<tbody>
<tr><td>Ort</td><td>wo ein Buch steht, wo etwas geschah</td><td>Feste Plätze in der Bibliothek; Karte mit denselben Orten in allen Büchern</td></tr>
<tr><td>Zeit</td><td>wann es spielt, was gleichzeitig ist</td><td>Eine Zeitleiste für alle; jedes Buch und jede Geschichte hat ihre Marke</td></tr>
<tr><td>Figur</td><td>wer handelt</td><td>Bildlexikon: festes Aussehen, Farbe und Zeichen je Person</td></tr>
<tr><td>Gestalt</td><td>wie der Text gebaut ist</td><td>Wiederkehrende Formen: V-Kurve, Spiegel, Raster, Treppe, Spalten</td></tr>
<tr><td>Bildwort</td><td>der Satz, der bleibt</td><td>Merkvers mit Bild und Stichwortband in der eigenen Sprache</td></tr>
</tbody></table></div>
<p class="text">Dazu kommt das Abrufen. Die App zeigt Bilder nicht nur, sie fragt sie ab: Stationen eines Buchs in die richtige Reihenfolge bringen, ein Bild seinem Kapitel zuordnen, Lücken im Merkvers füllen. Abgefragt wird nach einem Tag und nach einer Woche, danach in grösseren Abständen. Der Lernmodus mit Merkversen, den es schon gibt, wird dafür um Bildfragen erweitert.</p>
</section>

<section id="zugang">
<h2>Zugänglich für Menschen weltweit</h2>
<ul class="text">
<li><b>Audio zu jeder Szene.</b> Viele Menschen lernen vor allem über das Hören. Eine gesprochene Erzählung zum Bild hilft allen und ist für sie unverzichtbar.</li>
<li><b>Gott wird nie als Figur gemalt</b>, sondern nur so, wie der Text ihn zeigt: als Stimme, Wolke, Feuer, Licht. Für Traditionen, die auch Jesus und Propheten nicht abbilden, ein wählbarer Modus «ohne Personenbilder» (Szene von hinten, nur die Reaktion der anderen, oder Strukturbild).</li>
<li><b>Menschen des antiken Vorderen Orients</b>, keine europäischen Figuren. Das prüft die Bildprüfung schon heute mit.</li>
<li><b>Leserichtung:</b> Zeitleisten und Bildfolgen laufen in Sprachen, die von rechts nach links geschrieben werden, gespiegelt. Szenen sind so gebaut, dass sie einzeln verständlich bleiben.</li>
<li><b>Farbe nie allein</b>: Jede Farbbedeutung hat auch eine Beschriftung oder Form; Kontrast mindestens 4,5 : 1. Jedes Strukturbild gibt es zusätzlich als lesbare Textstruktur für Bildschirmleser.</li>
<li><b>Keine Comic-Kürzel</b> wie Bewegungslinien, Sterne oder Schweisstropfen als Bedeutungsträger. Sprechblasen nur mit wörtlichem Text in der eigenen Sprache.</li>
</ul>
</section>

<section id="prozess">
<h2>Was das für den Prozess heisst</h2>
<p class="text">Vorgeschlagen ist eine neue Fassung des Bildprozesses, die alle Formen umfasst. Die Schritte bleiben regelbasiert und laufen ohne Handarbeit:</p>
<ol class="regeln">
<li><div><b>Kernanalyse und Struktur</b> wie bisher: Momente, Baumuster, Glieder, Belege.</div></li>
<li><div><b>Form je Feld wählen</b> nach einer festen Tabelle aus Baumuster und Inhalt, mit Begründung im Datensatz. Gemalt wird nur, was erzählt wird oder als Bildwort im Text steht.</div></li>
<li><div><b>Anordnung aus Daten zeichnen</b>: Spalten, Raster, Kurven, Karten, Zeitleisten, Modelle. Feste Prüfungen sichern alle Glieder, die Zahl, die Reihenfolge, den Wortlaut und die Lesbarkeit auf dem Handy.</div></li>
<li><div><b>Malen</b>: Szenen und Vignetten durch das Bildmodell, mit den bestehenden Regeln und der Prüfung durch zwei Instanzen.</div></li>
<li><div><b>Zusammensetzen und schlussprüfen</b>: gemalte Teile in die gezeichnete Anordnung, Blindtest der fertigen Tafel, Belege B/R/I sichtbar.</div></li>
<li><div><b>Ebenen von unten nach oben</b>: Kapitel, Buch und Bibel aus den fertigen Feldern, ohne neue Bilder, wo es geht.</div></li>
</ol>
</section>

<section id="umfang">
<h2>Umfang, Kosten, Reihenfolge</h2>
<p class="text">Hochgerechnet aus den analysierten Büchern hat die Bibel rund 4000 Abschnitte mit zusammen etwa 9500 Bildfeldern. Etwa ein Drittel davon, rund 3200, sind Szenen. Gemalt haben bisher rund 0,40 Dollar je Szene gekostet, einschliesslich Wiederholungen und Prüfung; das ergibt rund 1300 Dollar. Dazu kommen Vignetten für Strukturbilder (vielleicht 2000 Stück), Neuprüfungen bei Regeländerungen und schwierige Fälle. Die ganze Bibel liegt damit grob bei 1500 bis 2500 Dollar für Bilder, verteilt über die Zeit.</p>
<div class="phasen">
  <div><b>1 · Gerüst</b><p>Bibliothek, grosse Geschichte, Zeitleiste, Karte und für alle 66 Bücher die Buchebene mit 4–6 Stationen. Rund 350 Felder. Gibt sofort Orientierung über die ganze Bibel.</p></div>
  <div><b>2 · Erzählungen</b><p>Abschnitte der erzählenden Bücher: Genesis bis Ester, Evangelien, Apostelgeschichte, dazu Jona und Daniel 1–6.</p></div>
  <div><b>3 · Struktur</b><p>Briefe, Psalmen, Weisheit, Propheten, Gesetz als Strukturbilder mit Vignetten. Braucht zuerst den Zeichner für die 20 Darstellungen.</p></div>
  <div><b>4 · Einprägen</b><p>Merkverse mit Bild, Bildfragen im Lernmodus, Audio, Wiederholungsplan. Danach Test mit Leserinnen und Lesern verschiedener Herkunft.</p></div>
</div>
</section>

<section id="offen">
<h2>Zu entscheiden</h2>
<ol class="text">
<li>Gilt die Zuordnung «Form je Inhalt» oben als Regel für den nächsten Prozess?</li>
<li>Beginnen wir mit Phase 1, dem Gerüst über alle 66 Bücher?</li>
<li>Soll die Bibliothek der Einstieg in der App werden?</li>
<li>Soll es einen wählbaren Modus «ohne Personenbilder» geben?</li>
<li>Audio: eigene Sprachaufnahmen, synthetische Stimme oder später?</li>
</ol>
</section>

<section>
<h2>Quellen</h2>
<ul class="quellen text">
<li>Eigene Grundlagen: <code>docs/STRUKTURKATALOG.md</code>, <code>docs/BILDSTIL.md</code>, <code>docs/VERDICHTUNG.md</code>, Kernanalysen in <code>data/core-analyses</code>, Piloten in <code>pilot/</code>.</li>
<li>Mayer, Research-based principles for designing multimedia instruction: <a href="https://www.unh.edu/teaching-learning-resource-hub/sites/default/files/media/2023-06/itow-research-based-principles-for-designing-multimedia-instruction-mayer.pdf">PDF</a></li>
<li>Sundararajan und Adesope 2020, Seductive details (Metaanalyse): <a href="https://rex.libraries.wsu.edu/esploro/outputs/journalArticle/Keep-it-Coherent-A-Meta-Analysis-of/99900601155501842">WSU</a></li>
<li>Mar et al. 2021, Narrative und Sachtexte: <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC8219577">PMC</a></li>
<li>Adesope, Trevisan und Sundararajan 2017, Übungstests: <a href="https://education.wsu.edu/documents/2018/01/rethinking-use-tests.pdf/">PDF</a></li>
<li>Ondřej 2025, Methode der Orte (Metaanalyse): <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC12514325/">PMC</a></li>
<li>Cowan 2001, Kapazität des Arbeitsgedächtnisses: <a href="https://pubmed.ncbi.nlm.nih.gov/11515286/">PubMed</a></li>
<li>Fuhrman und Boroditsky 2010, Zeit und Schreibrichtung: <a href="https://escholarship.org/content/qt68k986hb/qt68k986hb.pdf">PDF</a></li>
<li>Dowse et al. 2023, Bildzeichen bei geringer Lesefähigkeit: <a href="https://hsag.co.za/index.php/hsag/article/view/2192/3921">HSAG</a></li>
<li>Roberts et al. 2020, Gottesbilder und Hautfarbe: <a href="https://news.stanford.edu/stories/2020/01/consequences-perceiving-god-white-man">Stanford</a></li>
<li>Shaw, How Story Bibles Work (Themelios): <a href="https://www.thegospelcoalition.org/themelios/article/telling-the-story-from-the-bible-how-story-bibles-work/">TGC</a></li>
<li>BibleProject: <a href="https://bibleproject.com/other-resources/posters/">Poster je Buch</a> · Chris Harrison, BibleViz: <a href="https://www.chrisharrison.net/projects/bibleviz/">Projekt</a></li>
<li>Die vollständige Recherche mit Evidenzstufen liegt im Projekt unter <code>pilot/visuell/recherche.md</code>.</li>
</ul>
</section>
</div>
<script>
document.querySelectorAll('.luecke').forEach(function (el) {{
  el.setAttribute('role', 'button'); el.setAttribute('tabindex', '0'); el.setAttribute('aria-label', 'Lücke aufdecken');
  function auf() {{ el.classList.add('offen'); el.removeAttribute('aria-label'); }}
  el.addEventListener('click', auf); el.addEventListener('keydown', function (e) {{ if (e.key === 'Enter' || e.key === ' ') {{ e.preventDefault(); auf(); }} }});
}});
</script>
"""
    out.write_text(seite, encoding="utf-8")
    print(out, round(len(seite) / 1e6, 2), "MB")


if __name__ == "__main__":
    main()
