#!/usr/bin/env python3
"""Zieht die Depot-Daten aus den archivierten Briefing-Seiten in eine JSONL-Zeitreihe.

Die Briefings sind die einzige Quelle, in der die Depot-Historie ueberhaupt
festgehalten ist - allerdings als HTML-Prosa. Dieses Skript macht daraus
auswertbare Daten: eine Zeile pro Tag, eine Zeitreihe pro Position.

    python3 tools/extract_depot.py            # schreibt data/depot.jsonl
    python3 tools/extract_depot.py --check    # nur pruefen, nichts schreiben
"""
import argparse
import json
import pathlib
import re
import sys

REPO = pathlib.Path(__file__).resolve().parent.parent
ARCHIV = REPO / "e"
OUT = REPO / "data" / "depot.jsonl"

# "−0.34 %" / "+17.16 %" - die Seiten nutzen das typografische Minus (U+2212).
NUM = r"[+−-]?\d+[.,]?\d*"


def pct(text):
    """'+17.16 %' -> 17.16 ; '−0.34 %' -> -0.34 ; sonst None."""
    if text is None:
        return None
    t = text.replace("−", "-").replace(",", ".").replace("%", "").strip()
    try:
        return round(float(t), 4)
    except ValueError:
        return None


def strip_tags(s):
    return re.sub(r"<[^>]*>", "", s).strip()


def parse(path):
    html = path.read_text(encoding="utf-8", errors="replace")
    day = {"datum": path.stem, "quelle": f"e/{path.name}"}

    # Kopfzahlen: Tagesveraenderung steht als erste KPI im Hero. Die aeltesten
    # Ausgaben nutzen ein anderes Template - dort steht der Wert nur in der
    # Ueberblickszeile "Depot X % zum Vortag", die es in beiden Formaten gibt.
    kpis = re.findall(r'kpi-num">\s*([^<]+)', html)
    tag = pct(kpis[0]) if kpis else None
    if tag is None:
        m = re.search(r"Depot\s*(" + NUM + r")\s*%\s*zum Vortag", html)
        tag = pct(m.group(1)) if m else None
    day["tag_pct"] = tag

    # "Seit Einstand" steht im Depot-Panel als eigene Kennzahl.
    m = re.search(r"Seit Einstand.*?(" + NUM + r")\s*%", html, re.S)
    day["seit_einstand_pct"] = pct(m.group(1)) if m else None

    # Positionstabelle: <td><strong>TICKER</strong> <span class="dim">Name</span></td>
    #                   <td class="r ...">G/V</td><td class="r ...">heute</td>
    row = re.compile(
        r"<td><strong>([^<]+)</strong>\s*<span class=\"dim\">([^<]*)</span></td>\s*"
        r"<td class=\"r [^\"]*\">([^<]*)</td>\s*"
        r"<td class=\"r [^\"]*\">([^<]*)</td>",
        re.S,
    )
    positionen = []
    for ticker, name, gv, heute in row.findall(html):
        positionen.append(
            {
                "ticker": strip_tags(ticker),
                "name": strip_tags(name),
                "gv_pct": pct(gv),
                "tag_pct": pct(heute),
            }
        )
    day["positionen"] = positionen

    # Allokation: die Balkenbreiten im "fuel"-Element sind die Prozentwerte,
    # die Labels stehen als eigene Liste darunter.
    alloc = re.search(r'panelhead">Allokation.*?<div class="alegende">(.*?)</div>\s*</div>\s*</div>', html, re.S)
    gewichte = {}
    if alloc:
        block = alloc.group(1)
        labels = re.findall(r'<span class="name">([^<]+)</span>', block)
        werte = re.findall(r'<span class="pct">\s*(' + NUM + r")\s*%", block)
        for lab, val in zip(labels, werte):
            gewichte[strip_tags(lab)] = pct(val)
    day["allokation_pct"] = gewichte

    return day


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="nur pruefen, nichts schreiben")
    args = ap.parse_args()

    tage = []
    for path in sorted(ARCHIV.glob("2026-*.html")):
        day = parse(path)
        if not day["positionen"]:
            print(f"  uebersprungen (kein Depot-Block): {path.name}", file=sys.stderr)
            continue
        tage.append(day)

    if not tage:
        print("Keine Daten gefunden.", file=sys.stderr)
        return 1

    print(f"{len(tage)} Tage extrahiert: {tage[0]['datum']} bis {tage[-1]['datum']}")
    alle = {p["ticker"] for d in tage for p in d["positionen"]}
    print(f"{len(alle)} Ticker: {' '.join(sorted(alle))}")

    if args.check:
        return 0

    OUT.parent.mkdir(exist_ok=True)
    with OUT.open("w", encoding="utf-8") as fh:
        for d in tage:
            fh.write(json.dumps(d, ensure_ascii=False) + "\n")
    print(f"geschrieben: {OUT.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
