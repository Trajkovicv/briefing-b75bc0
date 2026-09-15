# Kontext fuer jede Sitzung — zuerst lesen

Dieses Repo ist Vuks Arbeitsraum mit Claude. Es enthaelt das veroeffentlichte
Morgen-Briefing (`e/`, `index.html`, `style.css`) und seit 2026-09-15 die
Arbeitsdokumente fuer das gemeinsame Vorhaben. Wer hier arbeitet, soll ohne
Gespraechsverlauf weitermachen koennen. Lies `PLAN.md` fuer die Herleitung.

## Wie Vuk arbeiten will

- Nicht Fragen beantworten und leicht anpassen — **seine Lage durchdenken**
  und Richtung vorschlagen. Er will vom Modell gefuehrt werden, nicht bedient.
- Er denkt gross und will, dass das Modell mitzieht. Bremsen nur mit Zahlen,
  nie mit Vorsicht.
- Deutsch, direkt, keine Schonung. Er hat ausdruecklich um Klarheit gebeten.
- Kontinuitaet ueber Modellgenerationen ist ihm wichtig: Jedes Modell soll
  dort weitermachen, wo das letzte aufgehoert hat. Darum diese Datei.

## Was feststeht (Stand 2026-09-15)

- **Trading mit Agenten ist nicht der Weg zum Geld.** Speed-Nachteil,
  Gebuehren, adversarial. Herleitung mit seinen Depotdaten in `PLAN.md`.
  Depot und Briefing bleiben sein eigenes Labor, nicht die Einnahmequelle.
- **Der Weg ist: Modelle bei Menschen einbauen, die es selbst nie tun.**
  KMU in Aargau/Zuerich, Vertrauensmarkt, Schweizerdeutsch, lokal.
  Staerkere Modelle machen den Einbauer wertvoller, nicht wertloser —
  solange er die Beziehung hat. Das ist der Ort, an dem der Modellfortschritt
  fuer ihn arbeitet.
- **Der Beweis existiert schon:** das Briefing laeuft seit 2026-07-28
  taeglich. Das ist das Ding, das er zeigt.
- **CHF 400/Monat investieren wartet auf nichts.** VUSA, ab 2027-01 Saeule 3a
  (frankly). Entkoppelt von jedem Projekt.

## Was ich ueber die Lage weiss

- Wohnort Nussbaumen AG (Obersiggenthal), Pendeltag nach Kloten — Arbeitsort
  steht im Briefing, Taetigkeit ist mir nicht bekannt.
- Swissquote-Depot mit 13 Positionen, konzentriert (ASML, TSM, TSLA, PLTR
  ~62 %). Historie in `data/depot.jsonl`, nur Prozentwerte.
- Angeschlossen: Hue-Licht und Spotify ueber MCP — er automatisiert auch
  sein Zuhause. Die Briefing-Pipeline laeuft ausserhalb dieses Repos.
- Sprachen der Quellen im Briefing: Deutsch, Englisch, Serbisch/Bosnisch,
  Russisch.

## Leads (Details in `KUNDEN.md`)

- **Gaertner**, allein, viel Admin → erster Kunde, hier entsteht der Kern
- **Sara Transporte AG**, Doettingen, ~120 LKW → grosser Fisch, Discovery zuerst
- **Bruder**, Reinigung, 3 Personen, nutzt Claude schon → Referenz/Partner, kein Kunde

Verfuegbare Zeit: ~25 h/Woche (Wochenende + Abende). Stand 2026-09-15.

## Offen — beim naechsten Mal klaeren, falls noch nicht geschehen

- Was er beruflich tut und welche Faehigkeiten er ausser diesem Setup hat
- Wo die Briefing-Pipeline laeuft (fuer alles, was in die Ausgabe eingreift)
- Inventar der relevanten Ordner auf seinem Laptop — er fuehrt das lokal
  mit Claude Code durch und committet das Ergebnis als `INVENTAR.md`

## Repo-Regeln

- Nur Prozentwerte, nie Betraege. Betraege bleiben in der Mail.
- `tools/extract_depot.py` nach jeder neuen Ausgabe laufen lassen.
- `PLAN.md` und diese Datei fortschreiben, wenn sich Entscheidungen aendern —
  mit Datum und Grund, damit das naechste Modell die Wendungen versteht.
