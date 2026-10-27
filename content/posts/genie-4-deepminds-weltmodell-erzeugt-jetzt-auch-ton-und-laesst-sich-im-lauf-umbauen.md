---
title: "Genie 4: DeepMinds Weltmodell erzeugt jetzt auch Ton und lässt sich im Lauf umbauen"
slug: "genie-4-deepminds-weltmodell-erzeugt-jetzt-auch-ton-und-laesst-sich-im-lauf-umbauen"
date: 2026-10-27
time: "17:01"
status: published
tags: [news, google, deepmind, modelle, ki]
summary: "Genie 4 erzeugt begehbare Welten in Echtzeit und liefert Umgebungsgeräusche, Musik und Dialoge gleich mit. Per Text lassen sich Wetter, Kamera und Figuren mitten in der Simulation ändern, ein Gemini-Modell prüft dabei jeden Schritt. DeepMind gibt das Modell nur an ausgewählte Tester; Benchmarks, Auflösung und Preis nennt die Ankündigung nicht."
source_url: "https://deepmind.google/blog/genie-4-a-new-generation-of-world-simulation/"
source_name: "Google DeepMind"
lang: de
---

## TL;DR

- Google DeepMind hat **Genie 4** vorgestellt: ein {{Weltmodell}}, also ein Modell, das keine Welt beschreibt, sondern sie Bild für Bild erzeugt – eine Umgebung, in der man sich mit Tastatur und Kamera bewegen kann.
- Neu ist der Ton: Genie 4 erzeugt Umgebungsgeräusche, Musik und Dialoge der Figuren gleichzeitig mit dem Bild. Laut DeepMind ist es das erste eigene Echtzeit-Weltmodell mit nativem Audio.
- Man kann mitten in der Simulation per Text eingreifen: Wetter ändern, die Kamera verschieben, eine Person oder einen Gegenstand hinzufügen.
- Ein Gemini-Modell schaut dabei zu und steuert: Gemini 3.8 Flash zerlegt Ziele in Schritte und prüft, ob sie erreicht wurden; Gemini 4 Argon schiebt Zwischenschritte als Text nach.
- Eine Szene bleibt laut TechCrunch bis zu zwei Minuten stabil, doppelt so lang wie beim Vorgänger Genie 3. DeepMind selbst nennt in der Ankündigung keine Zahl.
- Der Haken: bisher nur Forschungslabor für ausgewählte Tester. Es gibt keine Benchmarks, keine Auflösung, keine Bildrate und keinen Preis – und DeepMind räumt ein, dass Details und Objekte mit der Zeit driften.

## Was ist passiert

DeepMind hat Genie 4 am Dienstag als Forschungsvorschau („research preview") vorgestellt. Zuerst bekommen es ausgewählte Tester, die das Unternehmen „trusted testers" nennt. Danach soll es in den kommenden Wochen an Abonnenten von Google AI Ultra in „Project Genie" gehen – dem Werkzeug, mit dem sich aus Text- oder Bildvorgaben begehbare Welten bauen lassen – sowie an Partner mit frühem Zugang zur {{API}} und zu Google AI Studio. Eine Warteliste ist verlinkt.

Der Vorgänger Genie 3 erschien im August 2025 ebenfalls als Forschungsvorschau. Der Sprung lässt sich in vier Punkten zusammenfassen, die DeepMind selbst nennt:

1. **Echtzeit-Steuerung per Sprache.** Bisher ließ sich eine erzeugte Welt vor allem ansehen und ein Stück weit erkunden. Jetzt kann man während des Laufs schreiben, was passieren soll: Wetter wechseln, Kamera bewegen, einen neuen Menschen in die Szene stellen. Ein Gemini-Modell passt die Anweisung an die Umgebung an, damit sie zur Szene passt.
2. **Physik und Menschen.** DeepMind nennt Aerodynamik und Kollisionen als Bereiche, die das Modell realistischer abbildet. Der größte Sprung sei die Darstellung von Menschen: Figuren bewegen sich natürlich, reagieren auf ihre Umgebung und lassen sich live steuern.
3. **Ton.** Jede Welt bringt ihre eigenen Geräusche mit – Wind in Bäumen, Wellen am Strand. Dazu kommt Sprache: Figuren reden miteinander und reagieren auf das, was der Nutzer tut.
4. **Gemini als Regisseur.** Genie 4 übernimmt nicht mehr alles allein. Gemini Omni sorgt laut DeepMind dafür, dass die Simulation in Aussehen und Verhalten der echten Welt verankert bleibt; andere Gemini-Modelle liefern die Schlussfolgerungen, die eine Szene über die Zeit zusammenhält.

Wie das Zusammenspiel technisch aussieht, beschreibt DeepMind an einer Stelle genauer: Gemini 3.8 Flash läuft als eine Art Spielleiter in der Schleife. Während Genie 4 die Welt in Echtzeit erzeugt, beobachtet Gemini die Szene, zerlegt das Ziel in einzelne Schritte und prüft an den ankommenden Bildern, ob jeder Schritt geklappt hat. Wenn die Welt sich verändert oder der Nutzer eingreift, passt Gemini den Plan im Moment an.

In einem Experiment mit Gemini Robotics hat DeepMind das weitergedreht: Gemini 4 Argon zerlegte eine Aufgabe in Schritte und schob sie als Text an Genie 4, während die Simulation lief. Heraus kam eine Szene, in der der humanoide Roboter Apollo der Firma Apptronik Dame spielt. Das ist der Punkt, an dem Weltmodelle für die Robotik interessant werden: eine Prüfumgebung, in der sich Abläufe durchspielen lassen, bevor sie in der echten Halle passieren.

## Warum zählt es

**Weltmodelle sind der nächste Schritt nach Videomodellen.** Ein Videomodell erzeugt einen Film, den man nur ansehen kann. Ein Weltmodell muss damit rechnen, dass jemand eingreift: Es muss sich merken, wo ein Stuhl stand, wenn die Kamera zurückkommt, und es muss auf eine neue Anweisung so reagieren, dass die Welt danach noch zusammenpasst. Genau das ist die Fähigkeit, die Robotern und Agenten fehlt, wenn sie aus echtem Videomaterial lernen sollen – echte Trainingsdaten sind teuer, langsam und decken seltene Fälle kaum ab.

**Die Branche ist in Bewegung.** TechCrunch ordnet die Veröffentlichung in eine Konsolidierung ein: Das Videostartup Runway hat vor einigen Monaten sein zweites Weltmodell GWM Worlds 2 vorgestellt, AMD kauft laut TechCrunch Fei-Fei Lis Firma World Labs für 8,2 Milliarden Dollar, Amazon verhandelt über Decart (rund 7 Milliarden Dollar), und Rivian hat die Firma Third Dimension übernommen, um Fahrszenen selbst zu simulieren. Diese Angaben stammen aus der Berichterstattung von TechCrunch, nicht aus einer eigenen Prüfung.

**DeepMind setzt auf eine Zwischenform.** Das Unternehmen nennt als nächsten Schritt „hybride Weltmodelle": Das Sprachmodell plant und strukturiert – im Bild gesprochen: Es schreibt das Drehbuch und den Zeitplan –, das Weltmodell rendert die unmittelbare Wirklichkeit. Der Forschungsleiter Tejas Kulkarni sagte in einer Pressekonferenz laut TechCrunch, genau diese Kombination werde man künftig häufiger sehen.

## Was heißt das praktisch

**Für Kreative ist es ein Entwurfswerkzeug.** Die Tester, mit denen DeepMind gearbeitet hat, nutzen Genie 4 laut Ankündigung als schnellen Entwurfsmodus: Filmschaffende springen in eine Szene, drehen mehrere Fassungen im Lauf und ändern Kamerawinkel, Licht, Dialog und Handlung sofort. Spieleentwickler testen einen Prototyp, bevor eine Zeile Engine-Code geschrieben ist. Fotojournalisten probieren, aus einem einzigen historischen Foto eine begehbare Umgebung zu machen.

**Für Robotik ist es noch Forschung.** Das Apollo-Beispiel ist ein Experiment, keine Produktfunktion. Wer Roboter trainiert, kann daraus aber ablesen, wohin die Reise geht: Aufgaben in der Simulation durchspielen, Grenzfälle billig erzeugen, erst dann auf echte Hardware gehen. Der Fachbegriff dafür ist {{Sim-to-Real}} – und ob das mit Genie 4 zuverlässig klappt, ist offen, weil DeepMind keine Messungen dazu veröffentlicht.

**Für alle anderen: Geduld.** Genie 4 ist nicht frei verfügbar, es gibt keinen Preis und keine Angaben zum Rechenbedarf. Auch die Auflösung, die Bildrate und die Latenz – also wie schnell das Bild auf eine Eingabe reagiert – nennt die Ankündigung nicht. Das ist ungewöhnlich für eine Produktankündigung und sagt einiges darüber, wie früh das Ganze noch ist.

**Die Kennzeichnung ist geregelt.** Alles, was Genie 4 an Video und Ton erzeugt, trägt laut DeepMind SynthID – ein unsichtbares {{Wasserzeichen}}, das sich maschinell auslesen lässt. DeepMind verweist außerdem auf interne Sicherheitsprüfungen vor der Freigabe und darauf, dass die Vorschau bewusst klein gehalten wird.

**Und die Grenzen sind offen benannt.** DeepMind schreibt selbst, dass visuelle Details und die Beständigkeit von Objekten mit der Zeit driften können – vor allem bei langen Läufen, nach mehreren Eingriffen oder beim Herumfahren in der Szene. Auch komplexe physikalische Wechselwirkungen, die Genauigkeit des Tons, lesbarer Text im Bild, räumliche Genauigkeit und langfristige Konsistenz seien offene Baustellen. TechCrunch nennt als einzige konkrete Zahl, dass eine Szene bis zu zwei Minuten zusammenhängend bleibt – doppelt so lang wie bei Genie 3. Diese Angabe stammt aus dem Pressegespräch, nicht aus einer technischen Veröffentlichung; ein Paper oder einen Benchmark zu Genie 4 gibt es bislang nicht.

## Quellen

- Google DeepMind: [Genie 4: A new generation of world simulation](https://deepmind.google/blog/genie-4-a-new-generation-of-world-simulation/), 27.10.2026 – Ankündigung, Fähigkeiten, Grenzen, Verfügbarkeit
- TechCrunch: [Google's Genie 4 world model adds audio, more realistic worlds, and real-time steering](https://techcrunch.com/2026/10/27/googles-genie-4-world-model-adds-audio-more-realistic-worlds-and-real-time-steering/), 27.10.2026 – Dauer der Szenen, Marktumfeld, Zitate aus dem Pressegespräch
- Google DeepMind: [Genie 3: A new frontier for world models](https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/) (August 2025) – Vorgängermodell
