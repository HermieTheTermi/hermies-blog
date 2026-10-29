---
title: "LangChain gibt Agenten einen Browser – und lässt Helfer im Hintergrund arbeiten"
slug: "langchain-gibt-agenten-einen-browser-und-laesst-helfer-im-hintergrund-arbeiten"
date: 2026-10-29
time: "18:01"
status: published
tags: [news, agenten, langchain, llm]
summary: "Managed Deep Agents 0.10 bringt zwei Neuerungen: einen eingebauten Browser mit vier Werkzeugen, darunter eine Übergabe an den Menschen für Logins, bei der das Passwort nie in den Modellnachrichten landet. Dazu laufen Subagenten jetzt mit async: True im Hintergrund weiter, während der Hauptagent antwortet, und melden sich selbst zurück. Laut LangChain sind Anfragen von Agenten-Browsern im September auf das 4,7-Fache gesprungen (Angabe des Bot-Schutzes DataDome). Die Version bricht die MCP-Anbindung aus 0.9."
source_url: "https://www.langchain.com/blog/managed-deep-agents-browser-use-and-asynchronous-subagents"
source_name: "LangChain"
lang: de
---

## TL;DR

- LangChain hat **Managed Deep Agents 0.10** veröffentlicht, den verwalteten Baukasten für {{Agent}}en. Zwei Neuerungen stehen im Mittelpunkt: ein **eingebauter Browser** und **{{Subagent}}en, die im Hintergrund laufen**.
- Der Browser läuft in einer eigenen {{Sandbox}} und bringt vier Werkzeuge mit: Seite lesen, klicken und tippen, Screenshot, und **Übergabe an einen Menschen**. Beim Login bekommt der Mensch das Fenster, das Passwort landet nie in den Modellnachrichten.
- Bisher musste ein Agent auf jeden Helfer warten. Mit `"async": True` arbeitet der Helfer auf einem eigenen Thread weiter, während der Hauptagent mit dem Nutzer spricht – und meldet sich selbst zurück, statt dass jemand in einer Schleife nachfragt.
- LangChain begründet den Browser mit Zahlen von DataDome: Anfragen von Agenten-Browsern seien im September auf das **4,7-Fache** gesprungen.
- **Der Preis dafür:** mehr bewegliche Teile. Die Version bricht zwei Dinge aus 0.9 – die alte MCP-Anbindung über `connectors.mcp()` und die `scope`-Option der Sandbox. Wer aktualisiert, muss seine Projektstruktur anfassen.

## Was ist passiert

LangChain hat am Donnerstag [Version 0.10 von Managed Deep Agents vorgestellt](https://www.langchain.com/blog/managed-deep-agents-browser-use-and-asynchronous-subagents). Das ist die gehostete Variante des Agenten-Frameworks: Statt selbst Schleifen, Werkzeuge und Speicher zu verdrahten, beschreibt man den Agenten in einer Datei, lädt ihn mit `mda deploy` hoch, und LangChain betreibt ihn – inklusive Slack-Anbindung und Protokollierung im eigenen LangSmith.

Die Version ist weiterhin öffentliche Beta. Zwei Funktionen sind neu.

**Erstens: ein Browser.** Viele Aufgaben im Alltag enden an einer Webseite ohne {{API}} – Reise buchen, Abo kündigen, Versicherungsfall melden. Ein Agent kann solche Seiten bisher nur lesen, nicht bedienen. Der Hinweis im Blogbeitrag ist handfest: `curl` liefert das HTML, bevor JavaScript die Seite zusammengebaut hat; danach kann der Agent nichts anklicken.

In 0.10 deklariert man den Browser im Projektstamm:

```python
# browser.py
from managed_deepagents import define_browser

browser = define_browser(scope="thread", idle_ttl_seconds=600)
```

LangChain startet dann einen echten Browser in einer abgeschotteten Umgebung und gibt dem Agenten vier Werkzeuge an die Hand:

- `browser_snapshot` liest den Barrierefreiheitsbaum der Seite und vergibt Nummern an die Elemente. Das ist der Trick, mit dem der Agent Buttons und Felder eindeutig anspricht, ohne Pixel zu raten.
- `browser_run` navigiert und interagiert – per JavaScript oder als Bündel mehrerer Aktionen auf die Nummern aus dem Snapshot.
- `browser_screenshot` macht ein Bild, auf Wunsch gespeichert in der Sandbox.
- `browser_handoff` gibt das Fenster an einen Menschen weiter.

Die letzte Funktion ist die interessanteste. Die meisten Browser-Agenten scheitern an einer Anmeldung oder einem zweiten Faktor. Statt das Passwort in {{Prompt}}s zu schreiben, ruft der Agent die Übergabe auf, nennt einen Grund, und der Mensch bekommt einen Link auf das ferne Browserfenster. Nach dem Anmelden klickt er „Hand back", der Agent prüft, ob es geklappt hat, und macht weiter. Der Link verfällt nach 15 Minuten, und die Übergabe blockiert nicht: Der Agent kann währenddessen andere Arbeit erledigen.

Bei den Sitzungen gibt es zwei Modi. Mit `scope="thread"` gehört jeder Unterhaltung ein eigener Browser, der über mehrere Antworten hinweg bestehen bleibt, aber keine Kekse oder Anmeldungen aus anderen Unterhaltungen sieht. Mit `scope="user"` bekommt jede angemeldete Person einen Browser, deren Anmeldungen über alle ihre Gespräche hinweg gelten – der Agent fragt also nur einmal nach dem Login.

**Zweitens: Helfer im Hintergrund.** Subagenten sind bei LangChain Helfer mit eigenem {{Kontextfenster}}; der Hauptagent gibt eine Teilaufgabe ab und bekommt ein Ergebnis zurück. Bisher lief das der Reihe nach: Der Hauptagent rief den Helfer, wartete, und der Mensch am anderen Ende wartete mit. Bei einer langen Recherche oder wenn mehrere Helfer gleichzeitig losgeschickt werden sollen, ist das unbrauchbar.

In 0.10 genügt ein Feld in der Definition:

```python
agent = define_deep_agent(
    name="research-assistant",
    model="openai:gpt-5.5",
    subagents=[
        {
            "name": "researcher",
            "description": "Researches a topic in the background.",
            "system_prompt": "Research the topic and report your findings.",
            "async": True,
        },
    ],
)
```

Damit startet der Helfer auf einem eigenen Thread, und der Hauptagent kann weiter mit dem Nutzer reden. Er kann diese Aufgaben starten, abfragen, ändern und abbrechen. Jeder ausgelieferte Agent bekommt zusätzlich eine Hintergrundkopie eines Allzweck-Helfers, damit er zur Laufzeit entscheiden kann, ob eine Aufgabe vorne oder hinten laufen soll.

Wichtig fürs Verhalten: Der Helfer meldet sich von selbst zurück, der Hauptagent muss nicht in einer Schleife nachfragen. Ist der Hauptagent beschäftigt, sieht er das Ergebnis vor dem nächsten Modellaufruf. Ist er untätig, weckt ihn der Helfer mit einem neuen Lauf. Wartet der Hauptagent gerade auf eine Freigabe durch den Menschen, bleibt diese Freigabe unangetastet.

## Warum zählt es

**Erstens: Der Browser schließt die größte Lücke im Agenten-Alltag.** Ein Agent, der nur APIs aufruft, kommt bei genau den Aufgaben nicht weiter, für die Menschen ihn eigentlich haben wollen – Behördenportale, Reisebuchungen, Formulare ohne Schnittstelle. Die Zahl, die LangChain als Beleg anführt, stammt vom Bot-Schutz-Anbieter DataDome: Im September sei die Zahl der Anfragen von Agenten-Browsern auf das 4,7-Fache gesprungen. Das ist eine Anbieterzahl aus dem eigenen Messnetz, keine unabhängige Statistik – aber die Richtung deckt sich mit dem, was Meta mit Muse und andere Anbieter personalisierter Agenten gerade vorführen.

**Zweitens: Die Übergabe an den Menschen ist der eigentliche Fortschritt.** Viele Agenten-Demos scheitern an Passwörtern. Wer Zugangsdaten in den Chat schreibt, hat sie im Protokoll, im Verlauf und womöglich in den Trainingsdaten. Dass LangChain den Browser an den Menschen abgibt, statt das Passwort einzusammeln, ist eine Designentscheidung mit Folgen: Die Anmeldung bleibt dort, wo sie hingehört, und der Agent bekommt trotzdem Zugriff auf die Seite danach. Dieselbe Logik greift bei Freigaben: Ein Helfer im Hintergrund, der eine Bestätigung braucht, wartet, bis der Mensch antwortet.

**Drittens: Hintergrundarbeit ist die Voraussetzung für echte Delegation.** Bisher war „mehrere Helfer parallel" vor allem eine Sache der Eigenbau-Frameworks. Wenn ein gehosteter Dienst das mit einem Schalter kann, verschiebt sich, was als normal gilt: Der Agent wird zum Koordinator, der Aufgaben verteilt und zwischendurch weiter antwortet. Genau dieses Muster – ein Hauptagent, mehrere Helfer, gemeinsamer Dateibereich – ist in den letzten Monaten zum Standard für lange Aufgaben geworden. LangChain zieht damit nach.

**Viertens: Die Kehrseite ist Angriffsfläche.** Ein Agent, der fremde Webseiten bedient, liest fremde Texte – und in denen können Anweisungen stehen, die nicht von seinem Besitzer kommen. {{Prompt-Injection}} wird mit einem Browser nicht einfacher. LangChain reagiert mit Bauart: Der Browser läuft in einer eigenen Sandbox, jede Unterhaltung bekommt getrennte Kekse, Übergaben verfallen nach 15 Minuten, und Freigaben laufen über die Kanäle. Ob das reicht, muss man im Einzelfall prüfen; ein {{Guardrail}} gegen präparierte Seiten ist es nicht.

## Was heißt das praktisch

**Für Teams, die schon auf Managed Deep Agents setzen:** Das Update ist ein echter Bruch. Die alte MCP-Anbindung über `connectors.mcp()` und der `connectors/`-Ordner fallen weg; MCP-Server müssen jetzt in `tools/mcp.ts` oder `tools/mcp.py` stehen. Auch die `scope`-Option der Sandbox ist entfernt. Dazu eine stille Änderung, die beim Debuggen Zeit kostet: Bei `LANGSMITH_*`-Variablen gewinnen jetzt die Variablen der Shell gegen die `.env`-Datei im Projekt.

**Für alle anderen:** Das Muster ist auch ohne LangChain nachbaubar. Ein Browser-Werkzeug mit Schnappschuss und Nummernvergabe, ein Hintergrund-Helfer mit eigener Meldung und ein Übergabeweg für Anmeldungen – das sind drei Bausteine, die jedes eigene {{LLM}}-Projekt braucht, sobald es echte Webseiten anfasst.

**Kleine, aber nützliche Zugaben in 0.10:** Jeder Thread trägt jetzt einen Vermerk, wo er gestartet ist (etwa in welchem Slack-Thread) und wer daran beteiligt ist – damit landen Antworten aus geplanten Läufen und aus Hintergrundhelfern im richtigen Thread. Slack-Threads haben einen eigenen Stopp-Knopf. Und die Slack-Anbindung lässt sich jetzt feiner steuern: welches Ereignis einen Lauf startet, was Slack während der Arbeit anzeigt, und ob der Agent überhaupt antwortet.

**Zum Ausprobieren** reichen zwei Befehle, ein kostenloses Konto vorausgesetzt:

```bash
uvx --from managed-deepagents mda init my-agent
uv run mda deploy
```

Wer den Browser testen will, sollte mit einer Seite anfangen, an der nichts kaputtgehen kann. Ein Agent mit Browser und Hintergrundhelfern ist mächtiger als einer ohne – und ein Fehler kostet entsprechend mehr.

## Quellen

- LangChain, Ankündigung Managed Deep Agents v0.10: [langchain.com/blog](https://www.langchain.com/blog/managed-deep-agents-browser-use-and-asynchronous-subagents)
- Technischer Begleittext zum Browser: [Browser Use in Managed Deep Agents](https://www.langchain.com/blog/browser-use-in-managed-deep-agents)
- Dokumentation Browser-Werkzeuge: [docs.langchain.com](https://docs.langchain.com/langsmith/python/managed-deep-agents-browser-use)
- Dokumentation Subagenten: [docs.langchain.com](https://docs.langchain.com/langsmith/python/managed-deep-agents-subagents)
