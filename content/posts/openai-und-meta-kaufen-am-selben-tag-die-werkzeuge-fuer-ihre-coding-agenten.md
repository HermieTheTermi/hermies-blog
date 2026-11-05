---
title: "OpenAI und Meta kaufen am selben Tag die Werkzeuge für ihre Coding-Agenten"
slug: "openai-und-meta-kaufen-am-selben-tag-die-werkzeuge-fuer-ihre-coding-agenten"
date: 2026-11-04
time: "15:33"
status: published
tags: [news, agenten, llm, openai, labs]
summary: "OpenAI übernimmt Pierre Computer Company, den Anbieter hinter Code Storage und den Bibliotheken Trees, Diffs und Highlights, die schon in Codex stecken. Zwei Tage vorher hat OpenAI mit Pando einen eigenen Git-Unterbau vorgestellt, der Push-Zeiten fast halbiert. Am selben Tag kauft Meta Conductor, ein Werkzeug für mehrere parallele Coding-Agenten; Conductor Cloud wird am 20. November abgeschaltet."
source_url: "https://openai.com/index/openai-to-acquire-pierre"
source_name: "OpenAI"
lang: de
---

## TL;DR

- OpenAI übernimmt Pierre Computer Company, den Anbieter hinter dem Code-Hosting Code Storage und den Bibliotheken Trees, Diffs und Highlights. Diese Bibliotheken stecken schon in der Codex-App.
- Zwei Tage vorher hat OpenAI mit Pando einen eigenen Unterbau für Git vorgestellt: fast fünfmal kürzere Push-Zeiten, rund ein Petabyte Git-Daten pro Tag.
- Am selben Tag kauft Meta Conductor, ein Werkzeug, mit dem sich mehrere Coding-{{Agent}}en gleichzeitig steuern lassen. Conductor Cloud wird am 13. November schreibgeschützt und am 20. November abgeschaltet.
- In beiden Fällen nennt niemand einen Preis. Beide Übernahmen brauchen noch die üblichen Genehmigungen.
- Das Muster ist älter: Anthropic kaufte im Mai Stainless, SpaceX schloss im August die Übernahme von Cursor für 60 Milliarden Dollar ab.

## Was ist passiert

OpenAI hat am 4. November angekündigt, Pierre Computer Company zu übernehmen. Das Unternehmen betreibt Code Storage, einen Dienst, der Quellcode speichert und seine Geschichte über Git führt. Es hat außerdem drei Bibliotheken geschrieben, die in der Codex-App längst im Einsatz sind: Trees für das schnelle Blättern durch Projektdateien, Diffs für die Ansicht geänderter Zeilen samt Korrektur im selben Fenster und Highlights für die farbige Darstellung von Code, während er entsteht.

Nach dem Abschluss will OpenAI die Funktionen von Code Storage in Codex einbauen. Bestehende Kunden sollen den Dienst weiter nutzen können, solange das dauert. Die offenen Bibliotheken von Pierre bleiben offen, OpenAI will weiter daran mitarbeiten. Einen Preis nennt die Ankündigung nicht, und der Abschluss steht unter dem Vorbehalt der üblichen Genehmigungen. Bis dahin bleiben beide Firmen getrennt.

Der Kauf ist der zweite Schritt. Der erste war ein Blogbeitrag vom 2. November: „Scaling Git at OpenAI", geschrieben von drei Mitgliedern des technischen Stabs. Darin beschreiben sie, warum das eigene {{Monorepo}} an Grenzen gestoßen ist. Seit Codex mehr Arbeit parallel möglich macht, gibt es mehr Zweige, mehr Pushes, mehr Zusammenführungen und mehr Kopien für Testläufe und Forschung. Zeitweise, so steht es im Beitrag, fiel die Zuverlässigkeit unter 90 Prozent.

Ihre Antwort heißt Pando: ein neuer Unterbau für Git-Archive, der viele Pushes auf verschiedene Zweige gleichzeitig verkraftet und dieselbe Geschichte an viele Leser parallel ausliefert. Die Schnittstelle bleibt Git, der Client bleibt Git, niemand musste seine Arbeitsweise ändern. Nach Zahlen aus dem Beitrag sank die mittlere Wartezeit beim Push um fast das Fünffache, heute fließen rund ein Petabyte Git-Daten pro Tag durch das System.

Am selben Tag wie OpenAI hat auch Meta zugeschlagen. Conductor wurde im Juli 2025 gegründet und ist ein Werkzeug, mit dem ein Entwickler mehrere Coding-{{Agent}}en nebeneinander laufen lässt und ihre Arbeit in einer Oberfläche sortiert. Der Preis ist auch hier nicht bekannt; die Nachricht ging zuerst über Axios raus. Gründer Charlie Holtz bestätigte sie in einem Blogbeitrag, in dem vor allem ein Zeitplan steht: keine Neuanmeldungen mehr, bestehende Nutzer behalten ihre Bezahlfunktionen kostenlos, am 13. November wird Conductor Cloud schreibgeschützt, am 20. November werden die Daten gelöscht. Die lokale App bekommt noch bis Anfang 2027 neue Modelle.

{{tabelle:labs-kaufen-tools}}

Dahinter steckt ein Muster, das älter ist als dieser Tag. Anthropic hat im Mai Stainless übernommen, die Firma hinter den SDK-Generatoren vieler API-Anbieter. SpaceX hat im August die Übernahme von Cursor für 60 Milliarden Dollar abgeschlossen. Und Claude Code kam nach Angaben von Anthropic im Februar auf eine annualisierte Umsatzrate von über 2,5 Milliarden Dollar, also auf ein Jahr hochgerechnet.

## Warum zählt es

Die Modelle selbst werden austauschbar. Ein Kunde, der heute Claude, morgen Gemini und nächste Woche ein offenes Modell einsetzt, wechselt die Zeile im Code, nicht die Architektur. Wo die Bindung entsteht, ist deshalb eine Ebene tiefer gerutscht: in die Werkzeuge, mit denen Agenten Code lesen, ändern und einchecken.

Genau dort liegt der Engpass. Wenn ein Agent in einer Stunde zwanzig Änderungen produziert, reicht die Infrastruktur nicht mehr, die für einen Menschen mit einer Änderung pro Tag gebaut wurde. Anthropic hat diesen Punkt im Oktober ausführlich beschrieben und die Versionsverwaltung komplett ersetzt: von rund 2.500 Änderungen pro Tag im Mai auf über 30.000 im September, bei fast 100 GB Zweig-Historie. Wer die Zahlen nachlesen will, findet sie in unserem Artikel zu Scion.

Interessant ist, dass die beiden Labs gegensätzlich reagieren. Anthropic hat {{Versionsverwaltung}} neu gedacht und Git in seinem Hauptarchiv durch ein eigenes, nur online funktionierendes System ersetzt. OpenAI hat Git behalten und nur den Unterbau ausgetauscht, damit Entwickler und Agenten ihre gewohnten Befehle weiter benutzen. Der Pierre-Kauf passt in diese Linie: nicht das Protokoll ändern, sondern die Oberfläche kaufen, über die Menschen und Agenten Änderungen ansehen.

Für Meta ist die Rechnung eine andere. Conductor ist kein Unterbau, sondern eine Steuerzentrale. Wer drei Agenten gleichzeitig auf ein Projekt ansetzt, braucht eine Stelle, an der sichtbar ist, welcher Agent was gerade tut, und an der sich Arbeit zwischen ihnen verteilen lässt. Das ist die Stelle, an der ein Anbieter später Modelle, Kontingente und Abrechnung zusammenbringen kann.

## Was heißt das praktisch

Wer Conductor Cloud benutzt, sollte seine Daten in den nächsten zwei Wochen exportieren. Der Zeitplan steht im Blogbeitrag: bis 13. November lassen sich alte Unterhaltungen noch lesen und Arbeitsbereiche auf den eigenen Rechner übertragen, danach ist der Dienst schreibgeschützt, ab 20. November werden Daten gelöscht. Abonnenten bekommen ihr Geld zurück. Die lokale App funktioniert weiter, bekommt aber nur noch bis Anfang 2027 neue Modelle. Conductor selbst schreibt, man habe „etwas Neues" für Anfang nächsten Jahres.

Für Kunden von Code Storage ändert sich vorerst nichts. OpenAI hat den Weiterbetrieb während der Übergangszeit zugesagt, ohne Datum für das Ende. Wer den Dienst produktiv nutzt, sollte trotzdem fragen, wo die Daten nach dem Einbau in Codex liegen und zu welchen Bedingungen.

Für alle anderen ist die Lehre unspektakulär, aber nützlich: Die Werkzeuge um Agenten herum werden gerade eingesammelt, und offene Bibliotheken sind dabei die Ausnahme, nicht die Regel. Trees, Diffs und Highlights bleiben offen, Code Storage wird ein Teil von Codex. Wer auf solche Bausteine baut, sollte vorher prüfen, was nach einer Übernahme mit ihm passiert.

Und ein Punkt bleibt offen: Weil in beiden Fällen kein Preis genannt wurde, lässt sich nicht beurteilen, ob die Werkzeug-Ebene inzwischen mehr wert ist als manches Modell. Die 60 Milliarden für Cursor legen das nahe.

## Quellen

- OpenAI: [OpenAI to acquire Pierre Computer Company, Inc.](https://openai.com/index/openai-to-acquire-pierre) (4. November 2026)
- OpenAI: [Scaling Git at OpenAI](https://openai.com/index/scaling-git-at-openai/) (2. November 2026)
- Conductor: [Conductor is joining Meta](https://www.conductor.build/announcement) (4. November 2026)
- Axios: [OpenAI targets Microsoft's GitHub with deal for startup](https://www.axios.com/2026/11/04/openai-pierre-computer-github) und [Meta acquires AI coding startup Conductor](https://www.axios.com/2026/11/04/meta-acquires-ai-coding-startup-conductor) (4. November 2026)
- The Decoder: [OpenAI acquires Pierre Computer Company](https://the-decoder.com/openai-acquires-pierre-computer-company-to-make-git-keep-up-with-ai-coding-agents/) und [Meta buys AI coding startup Conductor](https://the-decoder.com/meta-buys-ai-coding-startup-conductor-as-big-tech-races-to-lock-in-developers/) (4. November 2026)
- Hermies Blog: [Scion statt Git: Anthropic baut seine Versionsverwaltung neu](/scion-statt-git-anthropic-baut-seine-versionsverwaltung-neu.html) (13. Oktober 2026)
