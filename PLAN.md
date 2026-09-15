# Plan — Vom Briefing zum Beweisapparat

Stand 2026-09-15 · geschrieben von Fable 5.1 · fuer Vuk und jedes Modell, das danach kommt.

Dieses Dokument ist die Uebergabe zwischen Modellgenerationen. Wer es liest,
soll ohne den Gespraechsverlauf weiterarbeiten koennen. Aendere es, wenn sich
die Lage aendert — aber halte fest, *warum*.

## Ziel

Mit Agenten Geld verdienen — zwei Beteiligte, Vuk und das jeweils aktuelle
Modell. Kein Fremdkapital, keine Kunden im Trading-Teil. Das System soll ueber
Modellgenerationen hinweg wachsen, nicht mit jeder neuen Generation von vorn
beginnen.

## Was ueber Modellgenerationen kumuliert

Nicht das Modell. Nicht ein Algorithmus. Zwei Dinge:

1. **Der Datensatz.** Jeder Entscheid mit Inputs, These, Groesse, Horizont,
   Invalidierung, Modellversion und spaeter dem Ergebnis. Nach einem Jahr
   hunderte beschriftete Faelle in unserer Nische. Hat sonst niemand.
2. **Das Replay.** Ein neues Modell wird an der gesamten Historie gemessen,
   bevor es einen einzigen neuen Entscheid faellt. Jede Generation holt mehr
   aus denselben Daten.

Das Modell ist der Motor, der Datensatz der Treibstoff. Jeder mit demselben
Abo hat denselben Motor — der Motor kann darum nie der Vorteil sein.

## Wo der Vorteil herkommt — und wo nicht

Vorteil entsteht aus: schneller sein / mehr wissen / laenger halten koennen /
Maerkte bearbeiten, die zu klein fuer Profis sind / Muehsames tun.

Ein Agent kann nicht schneller sein als colocated Server. Er kann aber
**unendlich breit lesen, ohne muede zu werden, fuer Rappen.** Darum:

- Agenten laufen 24/7 — sie *lesen* 24/7, sie handeln nicht 24/7.
- Entschieden wird selten, bewusst, mit Haltedauer Wochen bis Monate.
- Daytrading ist der Ort mit dem groebsten strukturellen Nachteil. Nicht tun.

Nischen mit echtem strukturellem Vorteil fuer kleines Kapital:

- **CH/EU Small Caps** (50–500 Mio. MCap, kaum Analysten, Meldungen in
  DE/FR/IT). Fonds koennen dort keine Position aufbauen; wir schon.
  Ingestion fuer "Dinge lesen, die niemand liest" steht bereits (Briefing).
- **Sondersituationen**: Uebernahmen, Spin-offs, Indexaufnahmen,
  Bezugsrechte. Mechanische Ereignisse, in Filings auffindbar.
- **Prognosemaerkte**: LLM-nativ, duenn gehandelt. Rechtslage CH pruefen.

## Rangliste nach Gewinnwahrscheinlichkeit

1. **Bauen und verkaufen** — kein Gegner, skalierbar. Das Briefing ist ein
   Produkt. Dieselbe Infrastruktur speist beide Wege.
2. **Nischen-Informationsvorteil** — echt, kapazitaetsbegrenzt.
3. **Langfristig systematisch investieren** — Marktrendite, sicheres Fundament.
4. **Daytrading 24/7** — niedrig. Gegner haben Speed, Gebuehren fressen.

## Phasen

**Phase 0 — Beweisapparat (bis ca. 2026-12)**
- [x] Depot-Zeitreihe aus dem Archiv (`tools/extract_depot.py`, `data/depot.jsonl`)
- [ ] Entscheidungslog als JSONL (Zeit, Modell, Inputs, These, Groesse, Horizont, Invalidierung)
- [ ] Taegliches Scoring gegen realisierte Kurse und gegen VUSA
- [ ] Replay-Harness: beliebigen Tag durch ein neues Modell laufen lassen

**Phase 1 — Nische finden (bis ca. 2027-09)**
- [ ] Ingestion auf SIX-Ad-hoc, Handelsregister, Small-Cap-Presse richten
- [ ] Sondersituationen auf Papier, unbegrenztes Notional, 100+ Entscheide
- [ ] Ehrliche Messung: Signal ja/nein. Messlatte: VUSA nach Kosten, nicht 40 %.

**Phase 2 — Einsatz oder Kurswechsel (ab 2027-09)**
- Signal → echtes Geld, niedrige Frequenz, Groesse langsam hoch
- kein Signal → Infrastruktur verkaufen (Weg 1)

**Parallel, unabhaengig, ab sofort:** CHF 400/Monat in VUSA, ab 2027-01 in
die Saeule 3a bis zum Maximum. Wartet auf nichts.

## Harte Grenzen

- **Steuern (Kreisschreiben 36):** Haltedauer >= 6 Monate, Umsatz <= 5x Depot
  p.a., kein Fremdkapital, Derivate nur zur Absicherung. Wird pro
  Steuerpflichtigem beurteilt, nicht pro Konto — ein aktives Nebenkonto kann
  das Hauptdepot mitreissen. Mit Steuerberater abklaeren.
- **Kein Echtgeld vor Evidenz.** Ein CHF-500-Konto misst Courtage, nicht
  Koennen (48–346 % Gebuehrenlast p.a. je nach Frequenz). Wenn ueberhaupt,
  dann als Klempner-Test fuer Anbindung und Psyche — nie als Beweis.
- **Modellwechsel = neues Segment.** Modellversion bei jedem Entscheid
  loggen. Kein heimlicher Wechsel mitten in einer Messreihe.
- **Nur Prozentwerte im Repo.** Betraege bleiben in der Mail.

## Zahlen, die den Plan geformt haben (aus 50 Tagen Depot-Historie)

- Vola annualisiert ~17.7 %, Tagesstreuung 1.11 %, 26/50 Tage positiv
- 40 % p.a. bei dieser Vola verlangen Sharpe ~2.2 (Medallion: ~2.0)
- Koennen von Glueck trennen: Jahre > (2/Sharpe)^2 — bei Sharpe 1.0 vier Jahre
- 3a-Steuerabzug auf CHF 4'800/Jahr bei 25 %: CHF 1'200 garantiert.
  CHF 500 Agentendepot bei erhofften 40 %: CHF 200, unsicher.
