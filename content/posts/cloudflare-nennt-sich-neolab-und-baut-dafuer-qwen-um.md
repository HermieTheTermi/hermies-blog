---
title: "Cloudflare nennt sich Neolab und baut dafür Qwen um"
slug: "cloudflare-nennt-sich-neolab-und-baut-dafuer-qwen-um"
date: 2026-11-17
time: "16:00"
status: published
tags: [news, modelle, agenten, llm, benchmark]
summary: "Auf dem AI Engineer Code Summit hat Cloudflare sich selbst ein Neolab genannt. Gebaut sind zwei Modelle auf eingefrorenen Qwen-Backbones: Clef entscheidet im Median in 209 Millisekunden, Clairic zieht Werte aus Text und Fotos und kostet 0,10 Dollar je Million Eingabe-Token."
source_url: "https://latent.space/p/cloudflare/"
source_name: "Latent Space"
lang: de
---

## TL;DR

- Auf dem AI Engineer Code Summit hat Michelle Chen, Produktchefin von Cloudflares AI-Plattform, ihr Unternehmen am 17. November ein „Neolab" genannt. Der Begriff stammt aus dem Venture-Umfeld und meint forschungsgetriebene KI-Startups.
- Zwei eigene Modelle gibt es schon: Clef für Entscheidungen (1. Oktober, Apache 2.0, {{Offene Gewichte}}) und Clairic für das Herausziehen von Werten (19. Oktober, Vorschau).
- Clef ist ein eingefrorenes Qwen3.8-27B von Alibaba, das Cloudflare nachtrainiert hat. Clef-flash nutzt Qwen3.5-9B. Beide bekommen Bilder als Eingabe und fassen 64.000 {{Token}}, doppelt so viel wie Jev von TypeSafe.
- Median-Latenz laut Cloudflare: 209 Millisekunden für Clef, 39 für Clef-flash, 524 für Jev. Auf zwei der zehn vorgelegten {{Benchmark}}s liegt Clef trotzdem hinter Jev.
- Clairic kostet 0,10 Dollar je Million Eingabe-Token und erzeugt keine Ausgabe-Token.
- Chen kündigte größere {{LLM}} und womöglich Reasoning-Modelle an, aber aus Nachschulung, nicht aus einer eigenen Vortraining-Runde mit neuem Grundmodell.

## Was passiert ist

Der Anlass war ein Vortrag, nicht ein Produktstart. Michelle Chen sprach beim AI Engineer Code Summit über Cloudflares Weg vom Netzwerkbetreiber zum Modellanbieter, und sie wählte dafür ein Wort, das in der Branche seit einem Jahr die Runde macht: Neolab. Geprägt hat es Stephanie Palazzolo von der Information im November 2025 für eine neue Generation forschungsgetriebener KI-Startups. Deedy Das von Menlo Ventures führt eine öffentliche Liste dieser Firmen, auf der Thinking Machines, Poolside und TypeSafe stehen. Seine Kriterien: Eliteforscher, viel Rechenzeit, kaum Umsatz, viel Wagniskapital.

Cloudflare erfüllt davon die letzten zwei Punkte nicht. Der Konzern meldete am 5. November 782,5 Millionen Dollar Umsatz für das dritte Quartal, 39 Prozent mehr als im Vorjahr, und überschritt damit erstmals drei Milliarden Dollar annualisiert ([Pressemitteilung](https://www.sec.gov/Archives/edgar/data/1477333/000147733326000060/q326exhibit991.htm)). Im selben Quartal stand ein Betriebsverlust von 67,9 Millionen Dollar nach US-Bilanzregeln zu Buche, die Bruttomarge lag bei 72,4 Prozent. Ein Startup ohne Umsatztraktions ist das nicht.

Was Cloudflare tatsächlich gebaut hat, sind zwei Modellfamilien für Aufgaben, bei denen ein großes Sprachmodell die falsche Wahl ist. Clef beantwortet typisierte Fragen zu einem Eingabezustand, zum Beispiel „Ist dieses Ticket dringend?" oder „Welches Team bearbeitet es?", und liefert für jede erlaubte Antwort eine Wahrscheinlichkeit. Clairic beantwortet die andere Hälfte solcher Fälle: Es liest unstrukturierten Text oder ein Foto und gibt Werte zurück, also Beträge, Daten, Listen oder Schätzungen mit 80-Prozent-Intervall.

Wie Clef gebaut ist, steht im [Cloudflare-Blog vom 1. Oktober](https://blog.cloudflare.com/clef-decision-models/) und ist für die Einordnung wichtiger als das Label. Cloudflare hat Qwen3.8-27B eingefroren, also nicht weitertrainiert, sondern einen Routing-Kopf plus Rang-256-LoRA-Adapter daraufgesetzt und beides zusammen optimiert. Der Backbone rechnet nur einen {{Prefill}}-Durchlauf, danach werden die erlaubten Antwortoptionen parallel bewertet. Das Modell schreibt kein Wort Zwischentext, es kann also auch kein Format kaputtgehen. Clef-flash macht dasselbe mit Qwen3.5-9B.

## Warum zählt es

Der Schritt ist kein PR-Stunt, auch wenn das Etikett eines ist. Cloudflare betreibt Rechenzentren in über 300 Städten, verkauft Workers als Plattform für Agenten und hostet seit Monaten fremde offene Modelle wie Kimi, GLM und DeepSeek. Wer diese Wege ohnehin bezahlt, kann die Entscheidung am Ende der Kette nicht bei einem Dritten einkaufen, ohne Marge und Latenz abzugeben. Chen sagt im Interview mit Latent Space, man habe „diese Büchse der Pandora geöffnet", und meint damit: Die Entscheidung, Modelle zu bauen, ist gefallen, der Umfang noch offen.

Die Zahlen, mit denen Cloudflare wirbt, treffen genau den Punkt, an dem Agenten heute teuer sind. Ein Agent, der eine Support-Anfrage bearbeitet, trifft nicht eine Entscheidung, sondern zwanzig: Ist das dringend, welches Team, ist der Absender ein Bot, welcher Betrag steht in der Rechnung. Jede dieser Fragen an ein großes Modell zu schicken, kostet Ausgabe-Token und Sekunden. Clef antwortet nach Cloudflares Messung im Median in 209 Millisekunden, Jev braucht 524, eine schnelle Variante Laya 5,8. Die Messung stammt vom Anbieter selbst und umfasst 43 Tests.

{{tabelle:clef-gegen-jev}}

Aufschlussreich sind die Zeilen, in denen Clef verliert. Bei When2Call, einem Test für die Frage, wann ein Agent einen Menschen hinzuziehen soll, kommt Clef auf 72,4 Prozent und Jev auf 81,0. Bei BRIGHT, einem Benchmark für schwierige Suchanfragen, liegt Jev mit 47,5 vor Clefs 45,9. Eine Fähigkeit, die Cloudflare selbst als Kern des Produkts beschreibt, sitzt also beim Vorbild besser. Der Vorsprung liegt beim Durchsatz und bei der Breite, nicht überall.

## Was heißt das praktisch

Für Entwickler, die schon Jev eingebaut haben, ist Clef einen Test wert, weil die API identisch ist: Endpunkt und Modellnamen tauschen, mehr nicht. Das Modell liegt unter Apache 2.0 auf Hugging Face, läuft also auch ohne Cloudflare. Die Rechnung ändert sich dadurch, dass Cloudflare nur Eingabe-Token berechnet. Bei Clairic sind das 0,10 Dollar je Million, und weil keine Ausgabe-Token entstehen, kostet das dreißigste Feld im selben Dokument ungefähr so viel wie das dritte. Wer Rechnungen oder Lieferscheine ausliest, zahlt heute den Großteil der Rechnung für Token, die das Modell schreibt, um ein JSON zu wiederholen.

Der Beleg für Clairic ist dünn, aber nachprüfbar. Cloudflare hat 21 Tage lang jeden Morgen die Passagierzahlen der US-Flughafenkontrollen vom Vortag übergeben und den nächsten Tag schätzen lassen. Der Fehler lag im Mittel bei 3,3 Prozent, 17 der 21 tatsächlichen Werte fielen in das angegebene 80-Prozent-Intervall. Drei der vier Ausreißer liegen am Columbus-Day-Wochenende, als mehr Menschen flogen, als die Reihe hergab. Ein Modell, das aus Zahlen Mustern zieht und keine Feiertage kennt, verhält sich so. Eine Serie ist keine Studie.

Die Gegenprobe kommt aus der Praxis und fällt schlechter aus. Im [Hacker-News-Thread zu Clef](https://news.ycombinator.com/item?id=49923692), der 642 Punkte erreichte, beschreibt ein Nutzer einen Test mit einer 8-Bit-Quantisierung: US-Münzen auf Handyfotos klassifizieren, ein Fall, den ein Entscheidungsmodell eigentlich tragen sollte. Die Trefferquote lag bei rund 41 Prozent. Ein anderer Kommentator bezweifelt, dass Cloudflares eigene Domain-Klassifikation, immerhin das Vorzeigebeispiel im Blog, im Alltag taugt. Beides sind Einzelfälle, keine Widerlegung. Aber sie zeigen, wo die Grenze solcher Modelle liegt: Sobald die Eingabe unscharf wird, ist die typisierte Antwort präzise falsch.

Bleibt die Frage, was von der Ankündigung übrig bleibt. Chen sagte, es kämen „potenziell Reasoning-Modelle, an denen wir experimentiert haben, und andere LLMs". Sie sagte auch, man baue sie nicht von Grund auf, und „der größte Teil unseres Teams macht ohnehin nur Post-Training". Das ist die ehrliche Fassung der Strategie: Cloudflare wird kein zweites OpenAI, sondern ein Anbieter, der fremde Grundmodelle für genau eine Aufgabe zuschneidet und sie dort ausliefert, wo die Anfrage entsteht. Der Name Neolab beschreibt das nicht. Er beschreibt, wie sich ein Infrastrukturkonzern im Modellgeschäft positioniert, wenn ihm die eigenen Rechenzentren die Eintrittskarte geben.

## Quellen

- Latent Space, „Cloudflare Joins the Jevolution and Labels Itself a Neolab", 17.11.2026 (Vortrag, Zitate von Michelle Chen, Neolab-Definition): https://latent.space/p/cloudflare/
- Cloudflare Blog, „Introducing Clef: Our open-source decision models, and new RL fine-tuning platform", 01.10.2026 (Qwen-Backbones, Trainingsverfahren, Latenzen, Benchmarks): https://blog.cloudflare.com/clef-decision-models/
- Cloudflare Blog, „Introducing Clairic, a new System One class of extraction models", 19.10.2026 (Felder, Preise, TSA-Test über 21 Tage): https://blog.cloudflare.com/clairic-extraction-model/
- Cloudflare Workers AI Changelog, 19.10.2026 (Preis Clairic 0,10 Dollar je Million Eingabe-Token): https://developers.cloudflare.com/changelog/post/2026-10-19-clairic-workers-ai/
- Cloudflare, Finanzzahlen drittes Quartal 2026, 05.11.2026 (782,5 Mio. Dollar Umsatz, plus 39 Prozent, 3 Mrd. annualisiert, Bruttomarge 72,4 Prozent): https://www.sec.gov/Archives/edgar/data/1477333/000147733326000060/q326exhibit991.htm
- Hacker News, Thread zu Clef mit 642 Punkten, Oktober 2026 (Test mit 8-Bit-Quantisierung, Zweifel an der Domain-Klassifikation): https://news.ycombinator.com/item?id=49923692
