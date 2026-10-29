#!/usr/bin/env python3
"""Bildlauf automatisch in main übernehmen (Prozess PROC-FREIGABE 2.0, Entscheid Andi Neck 2026-10-28).

Aufruf auf einem Stand von main, nachdem der Lauf auf Branch «bilder-auto/<Lauf>» gesichert ist:
  python3 scripts/authoring/bilder_merge.py bilder-auto/<Lauf>

- Szenen, die der Lauf geändert hat, kommen aus dem Lauf (auswahl.json, Bilder), alles andere bleibt wie auf main.
- Ebenso Einzelporträts des Bildlexikons (Schritt «figuren»): Einträge, deren «image»/«check» im Stil-Datensatz der Lauf
  geändert hat, kommen samt Bild (data/illustrations/aquarell/figuren/) aus dem Lauf.
- Abgeleitete Dateien (Bilddatensätze, SVG) werden danach neu geschrieben.
- Abbruch ohne Commit, wenn danach Konfliktmarken bleiben oder der Validator Fehler meldet.
Ob ein Bild in der App «geprüft» heisst, entscheidet weiterhin seine Prüfstufe; übernommen werden auch Felder in Prüfung,
damit der Stand sichtbar ist (sie tragen Stufe «entwurf»).
"""
import json
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
F = "scripts/authoring/bilder_aquarell_daten/auswahl.json"
STIL = "data/illustrations/styles/ILLSTYLE-AQUARELL.json"


def git(*a, check=True):
    return subprocess.run(["git", *a], cwd=ROOT, check=check, capture_output=True, text=True)


def main():
    b = sys.argv[1]
    git("fetch", "-q", "origin", f"{b}:refs/remotes/origin/{b}")
    git("merge", "-q", "--no-commit", "--no-ff", f"origin/{b}", check=False)
    base = json.loads(git("show", f"origin/{b}~1:{F}").stdout)
    theirs = json.loads(git("show", f"origin/{b}:{F}").stdout)
    ours = json.loads(git("show", f"HEAD:{F}").stdout)

    def zeige(rev, pfad):
        r = git("show", f"{rev}:{pfad}", check=False)
        return json.loads(r.stdout) if r.returncode == 0 else {}
    portr = {k: {x: v[x] for x in ("image", "check") if x in v} for k, v in zeige(f"origin/{b}", STIL).get("renderings", {}).items()}
    portr_basis = {k: {x: v[x] for x in ("image", "check") if x in v} for k, v in zeige(f"origin/{b}~1", STIL).get("renderings", {}).items()}
    portr_neu = [k for k, v in portr.items() if v and portr_basis.get(k) != v]
    neu = [k for k, v in theirs.items() if base.get(k) != v]
    # Hat main eine Szene seit dem Start des Laufs selbst geändert (z. B. neu gemalt), bleibt main: sonst überschreibt eine
    # Neuprüfung auf altem Stand das neue Bild (Lauf 41 überschrieb Joh 2 J2 aus Lauf 40).
    veraltet = [k for k in neu if ours.get(k) != base.get(k)]
    if veraltet:
        print("::warning::Lauf auf älterem Stand, main behalten für: " + ", ".join(veraltet))
    neu = [k for k in neu if k not in veraltet]
    for k in neu:
        ours[k] = theirs[k]
    (ROOT / F).write_text(json.dumps(ours, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for f in git("diff", "--name-only", "--diff-filter=U").stdout.split():
        if f.startswith(("data/illustrations/aquarell/img/", "data/illustrations/aquarell/figuren/")):
            git("checkout", "--theirs", "--", f)
        elif f.startswith("data/illustrations/aquarell/") or f in (F, STIL):
            git("checkout", "--ours", "--", f)
            if f == F:
                (ROOT / F).write_text(json.dumps(ours, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if portr_neu:  # Porträts aus dem Lauf in den Stil-Datensatz von main; der Generator behält sie bei
        st = json.loads((ROOT / STIL).read_text(encoding="utf-8"))
        for k in portr_neu:
            st.setdefault("renderings", {}).setdefault(k, {}).update(portr[k])
        (ROOT / STIL).write_text(json.dumps(st, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    subprocess.run([sys.executable, "scripts/authoring/bilder_aquarell.py"], cwd=ROOT, check=True)
    marken = git("grep", "-l", "-E", "^(<<<<<<<|>>>>>>>)", "--", "data", "scripts", check=False).stdout.strip()
    if marken:
        sys.exit(f"Konfliktmarken bleiben: {marken}")
    v = subprocess.run([sys.executable, "scripts/validate.py"], cwd=ROOT, capture_output=True, text=True)
    if v.returncode:
        sys.exit("Validator meldet Fehler:\n" + "\n".join(l for l in v.stdout.splitlines() if l.startswith(("ERROR", "FAIL")))[:3000])
    git("add", "-A", "data", "scripts")
    git("commit", "-qm", f"Bildlauf {b.split('/')[-1]} automatisch übernommen ({', '.join(neu + portr_neu) or 'keine Szenen geändert'})\n\nProzess PROC-FREIGABE@2.0")
    print("übernommen:", neu, portr_neu)


if __name__ == "__main__":
    main()
