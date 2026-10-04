---
title: "Jev: Ein Modell, das keine Texte schreibt - und die Agenten-Werkzeuge erobert"
slug: "jev-ein-modell-das-keine-texte-schreibt-und-die-agenten-werkzeuge-erobert"
date: 2026-10-04
status: published
tags: [modelle, agenten, langchain, ollama, benchmark, news]
summary: "TypeSafe AI veröffentlicht mit Jev ein Modell, das keine Texte generiert, sondern typisierte Entscheidungen mit Wahrscheinlichkeiten liefert – in Millisekunden und für 0,042 Dollar pro Million Eingabe-Token. Vercel, Ollama und LangChain haben es binnen Wochen eingebaut. Der Haken: Fast alles sind Herstellerangaben, und die eigene Dokumentation listet neun bekannte Schwächezonen."
source_url: "https://typesafe.ai/blog/introducing-system-one-models-and-jev"
source_name: "TypeSafe AI"
lang: de
---

## TL;DR

- TypeSafe AI hat mit **Jev** ein Modell veröffentlicht, das **keine Texte schreibt**. Es nimmt einen Zustand (Text oder JSON) plus eine Liste typisierter Fragen entgegen und antwortet mit Wahrscheinlichkeiten statt mit Sätzen. Die Ankündigung stammt vom [15. September 2026](https://typesafe.ai/blog/introducing-system-one-models-and-jev), der eigentliche Anlass ist die Welle danach.
- Drei Fragetypen gibt es: **Choice** (eine Option aus einer festen Liste), **Score** (Einstufung auf einer Skala) und **Noul** (Ja/Nein mit Wahrscheinlichkeit).
- Preis laut Anbieter: **0,042 US-Dollar pro Million Eingabe-Token** — 42 Dollar pro Milliarde. Ausgabe-Token kosten nichts. Das Kontextfenster fasst 32.000 Token für den Zustand plus die längste Frage, die Antwort liegt laut TypeSafe bei **70 bis 500 Millisekunden**.
- Der breite Rollout ist der eigentliche Punkt: Vercel meldet die **schnellste Ersttags-Verbreitung eines Modells** in seinem AI Gateway, **Ollama 0.35** führt seit dem 29. September lokale Entscheidungsmodelle über einen neuen Endpunkt aus, und **LangChain** setzt Jev als Bewerter („Judge") in LangSmith ein.
- Der Haken: Fast alle Zahlen sind **Herstellerangaben**, unabhängig nachgeprüft ist fast nichts. TypeSafe dokumentiert außerdem selbst, wo das Modell patzt — Rechnen, Zählen, Datumsvergleiche, große Zustände und manipulierte Eingaben.

## Ein Modell, das nichts schreiben will

Wer heute mit einem Sprachmodell arbeitet, bekommt Text. Auch wenn am Ende nur „billing" oder „urgent" herauskommen soll, schreibt das Modell erst einen Satz oder ein JSON-Objekt, und der Code muss danach prüfen, ob die Antwort überhaupt dem erwarteten Format entspricht. TypeSafe AI aus San Francisco hält das für den falschen Ansatz. Die Firma nennt ihr Modell Jev ein **System-One-Modell** — angelehnt an Daniel Kahnemans Unterscheidung zwischen schnellem, intuitivem Denken („System 1") und langsamem, abwägendem Denken („System 2") aus dem Buch *Thinking, Fast and Slow*.

Statt Text zu erzeugen, definiert der Aufrufer die möglichen Antworten vorab. Er schickt einen **Zustand** (zum Beispiel eine Support-Anfrage als Text) und eine Reihe **typisierter Fragen**. Jev bewertet alle Fragen in einem einzigen Durchlauf und gibt für jede eine Antwort mit Wahrscheinlichkeit und einem Vertrauenswert zurück. Laut Anbieter erzeugt das Modell dabei nicht Token für Token nacheinander, sondern alle Ausgaben **parallel** in einer Abfrage — das ist die technische Begründung für die Geschwindigkeit. (Ein **Token** ist die kleinste Texteinheit, mit der solche Modelle rechnen; grob ein Wortteil.)

Drei Frageformen sind erlaubt:

- **Choice:** „Welches Team soll das Ticket bearbeiten?" Antwort: eine von vorgegebenen Optionen, mit Wahrscheinlichkeit für jede Option.
- **Score:** „Wie dringend ist das Ticket?" Antwort: eine Einstufung zwischen vorgegebenen Stufen, etwa „Routine", „Bald", „Dringend".
- **Noul:** „Fordert der Kunde ausdrücklich eine Rückerstattung?" Antwort: eine Wahrscheinlichkeit zwischen 0 und 1 für Ja.

Im Beispiel aus der Ollama-Dokumentation entscheidet das Modell in einem Aufruf gleichzeitig über Team, Rückerstattung und Dringlichkeit — mit Werten wie 0,985 für „billing" und 0,012 für „technical". Das ist der Unterschied zu einem Chat-Modell, das diese drei Urteile nacheinander in einem Fließtext unterbringen müsste.

## Was der Hersteller verspricht

TypeSafe nennt für Jev 1.13 (die Modell-ID `jev-1.13.0`):

- **0,042 US-Dollar pro Million Eingabe-Token**, Ausgabe-Token kostenlos. Auf der eigenen Startseite rechnet die Firma das als **238-mal billigeren Eingabepreis als Claude Fable 5.1**.
- **70 bis 500 Millisekunden** Ende-zu-Ende-Laufzeit. Für dieselbe Art von Aufgaben sei das **40- bis 200-mal schneller** als Frontier-Modelle.
- Ein Kontextfenster von **32.000 Token** für den Zustand plus die längste Frage (maximal 64.000 Token pro Anfrage insgesamt), Rate-Limits von 100.000 Token und 80 Anfragen pro Sekunde.
- Sogenannte **kalibrierte** Wahrscheinlichkeiten: Hohe angegebene Sicherheit soll häufiger auch tatsächlich richtig bedeuten. Das Modell gibt also nicht nur eine Antwort, sondern auch eine Einschätzung, wie sicher es sich ist.

Die spektakulärere Zahl von **193,6-mal schneller und 444,6-mal billiger** stammt aus einer eigenen Testreihe über vier „Workflows" — also fest vorgegebenen Code-Abläufen, in denen Jev einzelne Verzweigungen übernimmt. TypeSafe sagt selbst dazu, dass der Vergleichsmaßstab der Durchschnitt der beiden größten verfügbaren Modelle war, was die Bewertung in Richtung OpenAI und Anthropic verschiebt, und dass die Workflows von eigenen Mitarbeitern gebaut wurden. Es sind also Firmenangaben über eine selbst gebaute Prüfung. Unabhängige Nachprüfung fehlt.

Der stärkste Satz in der Ankündigung ist zugleich der, der am meisten Prüfung braucht: Jev **könne nicht halluzinieren**. Gemeint ist: Weil die möglichen Antworten vorab festgeschrieben sind, kann das Modell nichts erfinden, was nicht in der Antwortliste steht — es gibt schlicht keine freie Textausgabe. TypeSafe schreibt, Typfehler seien „mathematisch unmöglich" und mit einem einzigen Gegenbeispiel widerlegbar. Das ist eine Aussage über die *Form* der Antwort, nicht über ihren *Inhalt*: Eine Antwort kann weiterhin schlicht falsch sein. Die Dokumentation räumt das auch ein — Kalibrierung gelte über Gruppen von Vorhersagen und garantiere nicht, dass eine einzelne Antwort korrekt ist.

## Warum das zählt

Der Engpass in heutigen Agenten — also Programmen, die ein Modell selbstständig Werkzeuge aufrufen lassen — ist selten die Intelligenz, sondern die Zahl der Modellaufrufe. Jede Verzweigung, jede Einordnung, jede Risikobewertung ist ein eigener Aufruf, und jeder kostet Zeit und Geld. Wenn Entscheidungen in Millisekunden statt Sekunden fallen, ändert das, was praktisch machbar ist: Prüfen bei *jedem* verarbeiteten Datensatz statt bei einer Stichprobe, Sicherheitsfilter für jede eingehende Nachricht statt für jede tausendste.

Genau dort hat das Modell innerhalb weniger Wochen Anschluss gefunden:

- **Vercel** meldet im „AI Gateway Production Index" vom 18. September, Jev sei das **schnellste je adoptierte Modell** der Plattform gewesen: In den ersten 24 Stunden nutzten es knapp **13 Prozent der zahlenden Teams** — doppelt so viele wie die GPT-5.6-Familie und mehr als sechsmal so viele wie Fable 5.1. Die Zahl ist mit Vorsicht zu lesen: Vercel gab das Modell bis zum 25. September kostenlos ab, der erste Tag war also gratis. Wie viele Teams im Oktober noch darauf zugreifen, sagt mehr aus.
- **Ollama** unterstützt seit Version 0.35 (29. September) Entscheidungsmodelle über den neuen Endpunkt `/v1/systemone`. Damit läuft diese Bauart erstmals lokal auf dem eigenen Rechner. Mitgeliefert werden drei Modelle: `nimble` (9 Milliarden Parameter, von Bespoke Labs), `tev1` (4 Mrd.) und `tev1:0.8b` (Together AI). Ollama nennt ein Beispiel: Nimble 9B brauchte auf einem MacBook Pro mit M5-Max-Chip im Schnitt **91 Millisekunden pro Entscheidung** — schnell genug, um live ein Pac-Man-Spiel zu steuern.
- **LangChain** nutzt Jev als Bewerter für Agenten-Tests in LangSmith (21. September). Der Vergleich mit klassischen Sprachmodell-Bewertern fiel deutlich aus: Jev traf laut LangChain bei jeder getesteten Entscheidung dieselbe Wahl wie ein menschlicher Prüfer, mit **92- bis 913-mal geringerer Streuung**, brauchte **0,44 Sekunden** pro Aufruf statt 2,16 bis 2,83 Sekunden und kostete für den kompletten Durchlauf **0,34 Dollar** statt 0,39 (GPT-5.6 Luna), 2,90 (GPT-5.6 Terra) oder 28,17 Dollar (Claude Sonnet 4.6).

## Was heißt das praktisch

Wer einen Agenten baut, bekommt hier ein zusätzliches Werkzeug, aber keinen Ersatz. Sprachmodelle schreiben weiterhin Texte, planen mehrstufige Aufgaben und erklären ihre Entscheidungen — all das kann Jev nicht, und die Dokumentation sagt ausdrücklich, für Textgenerierung sei es das falsche Werkzeug. Der sinnvolle Einsatz ist die enge, klar umrissene Frage mit vorgegebenem Antwortraum: Ticket einsortieren, Nachrichten moderieren, Risiko einstufen, Modell-Routing, Inhalte filtern.

Ehrlich dazugehört, wie viele Kanten die Dokumentation selbst auflistet. In der Seite „Jev 1.13 jaggedness" (zuletzt geprüft am 2. Oktober) stehen neun bekannte Schwächen:

- **Rechnen und zählen geht nicht.** TypeSafe schreibt es deutlich: „Jev ist kein Taschenrechner." Wer eine Häufigkeit braucht, soll sie im Code zählen und das Modell pro Einzelentscheidung fragen.
- **Datumsangaben** liest das Modell als Text, nicht als Größen. „Welches Datum liegt früher?" ist unzuverlässig. Empfehlung: Datumsteile einzeln auslesen, die Reihenfolge im Code bestimmen.
- **Wörtliches Verständnis.** Das Modell beantwortet die Frage, die dasteht — nicht die, die gemeint war. Zweideutigkeiten und doppelte Verneinungen kosten Genauigkeit.
- **Großer Zustand schadet.** Je mehr irrelevanter Text mitgeschickt wird, desto schlechter die Trefferquote („context rot"). Vorher filtern.
- **Reihenfolge der Optionen** kann das Ergebnis beeinflussen; das Modell neigt zur zuerst genannten.
- **Manipulierte Eingaben** können die Antwort verschieben. Wer fremde Texte einspeist, muss das testen.
- **Andere Sprachen als Englisch** funktionieren, aber schwächer — TypeSafe empfiehlt eigene Tests.
- Wer Schwellenwerte an eine Version angepasst hat, soll die feste Kennung wie `jev-1.13.0` verwenden statt des Alias `jev-latest`, weil sich dahinter das Modell ohne eigenes Zutun ändern kann.

Dazu kommt ein Punkt, der in der Ankündigung fehlt: TypeSafe gibt auf der Modellseite an, dass die Rate-Limits **dynamisch angepasst** werden und sich ohne Ankündigung ändern können, weil die Nachfrage gerade sehr hoch sei. Für Produktivsysteme ist das ein Risiko, das man einplanen muss.

Bemerkenswert ist schließlich, was das Modell über die Branche sagt. Die erste große Neuheit der Saison im Agenten-Bauwerkzeugkasten ist kein größeres Chat-Modell, sondern ein kleineres, das auf eine einzige Aufgabe zugeschnitten ist — und das in wenigen Tagen in die Werkzeuge eingebaut wurde, mit denen Agenten gebaut werden. Wenn Entscheidungen billig werden, verschwindet der Grund, sie zu sparen.

## Quellen

- TypeSafe AI, „Introducing System One Models & Jev", 15. September 2026: https://typesafe.ai/blog/introducing-system-one-models-and-jev
- TypeSafe AI, Dokumentation „System One": https://docs.typesafe.ai/concepts/system-one
- TypeSafe AI, Dokumentation „Models" (Preis, Kontextfenster, Rate-Limits, Aliase): https://docs.typesafe.ai/models
- TypeSafe AI, „Jev 1.13 jaggedness" (bekannte Schwächen, zuletzt geprüft 2. Oktober 2026): https://docs.typesafe.ai/model-jaggedness/jev-1.13
- Ollama, „Ollama now supports Jev-style decision models", 29. September 2026: https://ollama.com/blog/ollama-now-supports-jev-style-decision-models
- LangChain, „Jev is now available in LangSmith Evals", 21. September 2026: https://www.langchain.com/blog/jev-is-now-available-in-langsmith-evals
- LangChain, „What Is Jev? A Guide to TypeSafe AI's System One Model", 17. September 2026: https://www.langchain.com/blog/building-a-harness-with-jev
- Vercel, „AI Gateway Production Index, September 2026", 18. September 2026: https://vercel.com/blog/ai-gateway-production-index-september-2026
