# data/

Strukturierte Zeitreihen, die aus den veroeffentlichten Briefings zurueckgewonnen werden.

## depot.jsonl

Eine Zeile pro Briefing-Ausgabe, erzeugt von `tools/extract_depot.py`:

```json
{
  "datum": "2026-09-15",
  "quelle": "e/2026-09-15.html",
  "tag_pct": -0.34,
  "seit_einstand_pct": 8.54,
  "positionen": [{"ticker": "ASML", "name": "ASML Holding", "gv_pct": 17.16, "tag_pct": 0.02}],
  "allokation_pct": {"ASML": 19.3, "Uebrige": 15.2}
}
```

Alle Werte sind Prozentzahlen — Betraege stehen wie bisher nur in der Mail, nie im Repo.

Neu erzeugen nach jeder Ausgabe:

```
python3 tools/extract_depot.py          # schreibt data/depot.jsonl
python3 tools/extract_depot.py --check  # nur pruefen
```

Das Skript liest ausschliesslich das Archiv unter `e/` und ist damit jederzeit
reproduzierbar. Die acht aeltesten Ausgaben (bis 2026-08-04) nutzen ein
frueheres Template ohne Allokations-Panel; dort bleibt `allokation_pct` leer.
