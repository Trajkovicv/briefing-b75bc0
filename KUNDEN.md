# Kunden — Leads, Stand und naechster Schritt

Stand 2026-09-15. Arbeitsdokument, wird nach jedem Kontakt fortgeschrieben.
Namen von Privatpersonen bleiben draussen; oeffentliche Firmen duerfen rein.

Verfuegbare Zeit: ~20 h am Wochenende + ~1 h pro Abend = ~25 h/Woche.

## Reihenfolge

1. **Gaertner** — erster Kunde. Fuehlt den Schmerz, ist allein, ist ein Kollege.
   Hier wird der wiederverwendbare Kern gebaut (Offerte + Rechnung per Sprache).
2. **Sara Transporte AG** — der grosse Fisch. Discovery zuerst, nichts bauen,
   bevor wir ihren Ablauf kennen. Einstieg ueber den Sohn.
3. **Bruder** — kein Kunde, sondern Referenz und moeglicher Partner
   (Storengeraet). Nicht verkaufen an jemanden, der keinen Schmerz fuehlt.

## 1 · Gaertner (Einzelunternehmer, allein, viel Admin)

**Was wir wissen:** allein, viel Admin, Kollege von Vuk.

**Was wir bauen:** Sprachmemo → Offerte / Rechnung als PDF, schweizkonform.
- Nach der Besichtigung spricht er ins Handy: Kunde, Ort, Positionen.
  → Offerte mit seiner Preisliste, seinem Logo, Schweizer Format. Ein Tipp: senden.
- Nach dem Auftrag: "fertig, 4 h, 2 Saecke Gruengut extra" → Rechnung mit
  **QR-Rechnung** (Pflicht in CH seit 2022 — das ist das technische Stueck,
  das sitzen muss).
- Mahnung automatisch nach 30 Tagen.
- Belege: Foto vom Landi-Kassenzettel → kategorisiert → Monatsordner fuer
  den Treuhaender.
- Sprache als Oberflaeche, weil er dreckige Haende hat und im Bus sitzt.
  Die Oberflaeche ist das Produkt.

**Vor dem Bauen klaeren:** Nutzt er bexio oder ein anderes Buchhaltungstool?
(Dann fuettern wir das per API statt PDFs zu erzeugen.) MWST-pflichtig
(> CHF 100k Umsatz)? Wie sieht seine heutige Offerte aus — eine als Vorlage.
Wie viele Offerten und Rechnungen pro Monat?

**Preis-Idee:** Setup CHF 1'500 + CHF 150/Monat, oder nur Monatsbetrag.
Erster Kunde darf guenstiger sein — gegen eine Referenz.

**Warum das der Kern ist:** einmal gebaut, gilt es fuer jeden Handwerker.
Gaertner → Maler → Plattenleger → Sanitaer. Gleiches Produkt, andere Preisliste.

## 2 · Sara Transporte AG, Doettingen AG

**Was wir wissen (oeffentlich):** gegruendet 2014, Familienbetrieb, Fuehrung
Hamzi und Sadik Alijovi. Rund 120 LKW, Standorte Doettingen, Moehlin,
Waldshut-Tiengen (DE), Unterkirnach (DE), Durham (GB, seit 2021).
Europaweite Transporte in allen Fahrzeugtypen inkl. ADR, Zollabwicklung
CH↔EU, Lager und Kommissionierung. Buero-Team ~10 Personen laut einer Quelle.

**Was das heisst:** Das ist ein mittelgrosser Spediteur, kein KMU im Sinne
des Gaertners. 120 LKW laufen nicht ueber WhatsApp — sie haben ein TMS
(Transport-Management-System). Wir ersetzen nichts, wir haengen uns davor.

**Wo bei einem Spediteur dieser Groesse das Geld liegt:**
- **Frachtanfragen per Mail** in DE/EN/FR/IT, dutzende pro Tag. Ein
  Disponent liest, tippt ab, kalkuliert, antwortet — Stunden pro Tag.
  Agent: Mail lesen → Von/Nach/Termin/Gewicht/Paletten/Fahrzeugtyp/ADR
  extrahieren → gegen ihre Preislogik pruefen → Antwortentwurf.
  Das ist der Einstieg: hoher Wert, geringes Risiko, ihr eigener Posteingang.
- **Lieferschein → Rechnung**: Fahrer fotografiert den unterschriebenen
  Lieferschein, das Buero ordnet ihn dem Auftrag zu und fakturiert.
  Dokument-Erkennung + Zuordnung. Zweiter Schritt.
- **Zoll**: GB-Standort seit 2021 = taeglich Post-Brexit-Zoll. Hochgradig
  strukturiert und repetitiv — aber Compliance-Risiko. Nicht als Erstes.

**Wie man an so eine Firma verkauft:** nicht mit Folien. Mit ihren Daten.
"Gebt mir zwei Wochen euren Anfragen-Posteingang, ich zeige euch, was ein
Agent damit macht. Kein Vertrag, keine Kosten." Dann entscheiden sie auf
Basis dessen, was sie gesehen haben.

**Naechster Schritt:** Sohn fragen, ob er ein Gespraech mit dem Vater
vermittelt. Discovery-Fragen: Welches TMS? Wie kommen Anfragen rein und
wer bearbeitet sie? Wie lange dauert eine Offerte? Wie werden Lieferscheine
verarbeitet? Was nervt das Buero am meisten?

**Warum es sich lohnt:** Ein Retainer von CHF 3'000–5'000/Monat ist bei
dieser Groesse realistisch, wenn der Pilot sitzt. Und die Referenz
"Sara Transporte, 120 LKW" oeffnet jeden anderen Spediteur im Aargau.

## 3 · Bruder (Reinigung, 3 Personen, Einzelunternehmen)

**Was wir wissen:** nutzt Claude bereits (Website, Storengeraet-Entwicklung),
sagt "kein Bedarf, kein Admin".

**Was er uebersieht — ehrlich gesagt vermutlich wenig, das er fuehlt.**
"Kein Admin" in einem Dreimannbetrieb heisst: Der Admin passiert am
Sonntagabend und wird nicht gezaehlt. Die Frage ist nicht "brauchst du KI",
sondern "was hast du letzten Sonntagabend fuer die Firma gemacht?"

Was in einer Reinigungsfirma typisch liegen bleibt:
- Offerten-Nachfassen: unbeantwortete Offerten sind verlorenes Geld.
- Google-Bewertungen: Reinigung ist ein Bewertungsgeschaeft. Nach jedem
  Auftrag automatisch eine Bitte um Bewertung.
- Foto → Offerte in Minuten statt Besichtigung + Abend.

**Der eigentliche Hebel ist das Storengeraet.** Wenn er ein Produkt
entwickelt, liegt das Geld nicht in seinem Admin, sondern im Verkauf des
Geraets: Landingpage → Anfragen → automatische Offerte → Bestellung.
Dort ist Vuk Partner, nicht Dienstleister.

**Rolle:** Referenz ("mein Bruder, Reinigungsfirma") und Sparringspartner.
Nicht als Kunde bearbeiten.

## Quellen zu Sara Transporte

- https://saratransporte.ch/
- https://www.sara-transporte.ch/ueber-uns/
- https://business-monitor.ch/de/companies/513893-sara-transporte-ag
- https://www.moneyhouse.ch/en/company/sara-transporte-ag-11449857441
- https://ch.kompass.com/c/sara-transporte-ag/ch886958/
- https://rocketreach.co/sara-transporte-ag-profile_b7d1c265c0e48b16
