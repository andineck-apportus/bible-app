#!/usr/bin/env python3
"""Bildzeichen aus Twemoji (docs/SYMBOLPROZESS.md, «Runde 12: Emoji zuerst», Entscheid Andi Neck 2026-10-25).

Von Hand gezeichnete Piktogramme, besonders Körperteile, wurden mit mehr Detail unverständlicher. Wo es geht, besteht ein
Zeichen deshalb aus Twemoji (Twitter, Inc. und Mitwirkende, https://github.com/jdecked/twemoji, CC BY 4.0): ein Emoji,
höchstens zwei, nach einer festen Anordnung. Hände und Gesichter in einem Hautton, der zu den Figuren passt.

Zuordnung: scripts/authoring/emoji_zuordnung.json
    {"FIG-…": {"emoji": ["palm-up-hand", "coin"], "anordnung": "paar", "grund_de": "…"}, …}
Anordnungen:
    einzeln   ein Emoji
    paar      zwei Emoji nebeneinander, leicht überlappend (das erste ist das Hauptmotiv)
    abzeichen zweites Emoji klein unten rechts auf dem ersten (Zusatz: Ort, Gegenstand)
    verbot    erstes Emoji mit rotem Verbotskreis darüber («nicht tun»)
    nein      erstes Emoji mit rotem X unten rechts («falsch, nein»)

    python3 scripts/authoring/emoji_zeichen.py            # Auszug und Ersetzungen schreiben
    python3 scripts/authoring/emoji_zeichen.py --namen D  # Liste aller Emoji-Namen nach D (für die Zuordnung)
    python3 scripts/authoring/emoji_zeichen.py --entwuerfe E.json Z.json   # Zuordnungsvorschläge Z als Entwürfe für zeichen_test.py

Schreibt vendor/twemoji/twemoji-auszug.json (nur benutzte Emoji, mit Herkunft und Lizenz) und
scripts/authoring/bildsymbole_daten/ueberarbeitet/zzz-emoji.json (wird von bilder_anime.library() übernommen).
Das vollständige Paket @iconify-json/twemoji wird bei Bedarf mit npm in ~/.cache/atmo-emoji geholt (nicht im Repository).
"""
import json
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
CACHE = pathlib.Path.home() / ".cache/atmo-emoji"
PKG = "@iconify-json/twemoji@1.2.5"
ZUORDNUNG = ROOT / "scripts/authoring/emoji_zuordnung.json"
AUSZUG = ROOT / "vendor/twemoji/twemoji-auszug.json"
OUT = ROOT / "scripts/authoring/bildsymbole_daten/ueberarbeitet/zzz-emoji.json"
TON = "medium-light-skin-tone"  # passt zu den Figuren (Haut #E2AE80)
HERKUNFT = {"quelle": "Twemoji (Twitter, Inc. und Mitwirkende), https://github.com/jdecked/twemoji, über " + PKG,
            "lizenz": "CC BY 4.0", "lizenz_url": "https://creativecommons.org/licenses/by/4.0/",
            "aenderungen_de": "Auszug; Hautton gewählt; teils zu zweit angeordnet oder mit Verbots- bzw. Nein-Zeichen ergänzt"}


def paket():
    f = CACHE / "package/icons.json"
    if not f.exists():
        CACHE.mkdir(parents=True, exist_ok=True)
        tgz = subprocess.run(["npm", "pack", PKG, "--silent"], cwd=CACHE, capture_output=True, text=True, check=True).stdout.strip().splitlines()[-1]
        subprocess.run(["tar", "xzf", tgz], cwd=CACHE, check=True)
    return json.loads(f.read_text(encoding="utf-8"))


def body(icons, name):
    """Inhalt eines Emoji (36×36); Hände und Gesichter mit Hautton, wenn es ihn gibt."""
    ic = icons["icons"]
    for n in (f"{name}-{TON}", name):
        if n in ic:
            return n, ic[n]["body"]
        al = icons.get("aliases", {}).get(n)
        if al and al.get("parent") in ic:
            return al["parent"], ic[al["parent"]]["body"]
    raise SystemExit(f"FEHLER: Emoji «{name}» gibt es in Twemoji nicht (Liste: --namen)")


VERBOT = ('<circle cx="18" cy="18" r="15.5" fill="none" stroke="#D32F2F" stroke-width="3.4"/>'
          '<path d="M7.2 7.2L28.8 28.8" stroke="#D32F2F" stroke-width="3.4" stroke-linecap="round"/>')
NEIN = ('<g transform="translate(25 25)"><circle r="9" fill="#FFFFFF" stroke="#D32F2F" stroke-width="2"/>'
        '<path d="M-4.2 -4.2L4.2 4.2M4.2 -4.2L-4.2 4.2" stroke="#D32F2F" stroke-width="2.8" stroke-linecap="round"/></g>')


def zeichen(icons, e):
    """(viewBox, svg) eines Zeichens aus der Zuordnung."""
    names, an = e["emoji"], e.get("anordnung", "einzeln")
    bs = [body(icons, n)[1] for n in names]
    if an == "einzeln" or len(bs) == 1 and an not in ("verbot", "nein"):
        return "0 0 36 36", bs[0]
    if an == "paar":  # Hauptmotiv gross, zweites etwas kleiner und tiefer, leicht überlappend
        return "0 0 62 36", f'<g>{bs[0]}</g><g transform="translate(34 8) scale(.78)">{bs[1]}</g>'
    if an == "abzeichen":
        return "0 0 40 40", f'<g>{bs[0]}</g><g transform="translate(20 20) scale(.55)">{bs[1]}</g>'
    if an == "verbot":
        return "0 0 36 36", f'<g transform="translate(5 5) scale(.72)">{bs[0]}</g>{VERBOT}'
    if an == "nein":
        return "0 0 36 36", f'{bs[0]}{NEIN}'
    raise SystemExit(f"FEHLER: unbekannte Anordnung {an}")


def main():
    args = sys.argv[1:]
    icons = paket()
    if args[:1] == ["--namen"]:
        names = sorted(n for n in icons["icons"] if "skin-tone" not in n)
        pathlib.Path(args[1]).write_text("\n".join(names) + "\n", encoding="utf-8")
        print(f"PASS: {len(names)} Namen nach {args[1]}")
        return
    if args[:1] == ["--entwuerfe"]:
        z = json.loads(pathlib.Path(args[2]).read_text(encoding="utf-8"))
        out = {}
        for k, e in z.items():
            vb, svg = zeichen(icons, e)
            out[k] = {"vb": vb, "svg": svg, "bedeutung": e.get("bedeutung", ""), "gezeichnet": " + ".join(e["emoji"]) + f" ({e.get('anordnung', 'einzeln')})"}
        pathlib.Path(args[1]).write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"PASS: {len(out)} Entwürfe nach {args[1]}")
        return
    z = json.loads(ZUORDNUNG.read_text(encoding="utf-8"))
    out, used = {}, {}
    for fid, e in z.items():
        if not e.get("emoji"):
            continue
        for n in e["emoji"]:
            rn, b = body(icons, n)
            used[rn] = b
        vb, svg = zeichen(icons, e)
        out[fid] = {"vb": vb, "svg": svg}
    AUSZUG.parent.mkdir(parents=True, exist_ok=True)
    AUSZUG.write_text(json.dumps({**HERKUNFT, "emoji": dict(sorted(used.items()))}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"PASS: {len(out)} Zeichen aus {len(used)} Emoji; {AUSZUG.relative_to(ROOT)}, {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
