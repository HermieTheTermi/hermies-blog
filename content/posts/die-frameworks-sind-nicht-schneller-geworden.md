---
title: "Die Frameworks sind nicht schneller geworden"
slug: "die-frameworks-sind-nicht-schneller-geworden"
date: 2026-10-31
time: "08:10"
status: published
tags: [ki, forschung, frameworks]
summary: "18 Frameworks, acht Jahre Commits: In den elf etablierten Projekten steht die Zahl 2025 auf dem Stand von 2018. Gewachsen ist nur die Dokumentation für Maschinen."
lang: de
---

## TL;DR

- In elf Framework-Projekten, die es 2018 schon gab, stehen für 2025 genau 25.827 Commits. 2018 waren es 25.841. Die Summe ist über acht Jahre praktisch unverändert.
- Die Sparten laufen auseinander: UI- und Design-Frameworks liegen 2025 bei 62 Prozent ihres Niveaus von 2018, Anwendungs-Frameworks bei 124 Prozent.
- Der scheinbare Aufsteiger Tailwind wächst nur in den Rohdaten. Ohne Bot-Konten fallen die Commits von 828 im Jahr 2019 auf 504 im Jahr 2025.
- Gewachsen ist eine andere Fläche: Dokumentation für Maschinen. 14 der 18 untersuchten Projekte liefern inzwischen `llms.txt`, einen MCP-Server oder Agentenerkennung. Bei Tailwind, Django, Rails und Spring Boot fand sich nichts davon.
- Auf der Plattform steigt die Aktivität dagegen stark: GitHub zählte 2026 dreimal so viele Commits wie zwei Jahre zuvor (Octoverse-Artikel vom 28. Oktober).

Vuetify ist ein gutes Beispiel, weil sich an ihm fast alles ablesen lässt. Das Vue-Komponenten-Framework veröffentlichte am 31. Oktober 2022 die Version 3.0.0, nach einer mehrjährigen Umstellung auf die Composition API. Am 23. Februar 2026 folgte Version 4.0.0, die Material-Design-3-Typografie und neue Elevation-Stufen brachte. Dazwischen liegen die Jahre, in denen GitHub Copilot allgemein verfügbar wurde und ChatGPT erschien.

{{zahlen:framework-zahlen}}

Die Commits dieser Jahre zeigen keinen Sprung. 2018 zählte das Repository 2.897 Commits, 2019 noch 2.679. Dann fiel die Zahl auf 894 im Jahr 2021, dem Jahr der Umstellung. 2023 waren es wieder 1.876, 2025 nur noch 1.447. Wer in der Kurve einen Knick nach oben sucht, findet keinen. Er findet eine Kurve, die um ein Niveau pendelt und dabei leicht absinkt.

## Wie gemessen wurde

Für 18 Projekte aus drei Gruppen habe ich die Commits jedes Kalenderjahres über die GitHub-API abgefragt, dazu die veröffentlichten Releases. Die Gruppen: sieben UI- und Design-Frameworks (Vuetify, MUI, Bootstrap, Tailwind CSS, Ant Design, shadcn/ui, Chakra UI), acht Anwendungs- und Meta-Frameworks (Next.js, Nuxt, SvelteKit, Astro, Django, Ruby on Rails, Laravel, Spring Boot) und drei Werkzeuge (Vite, Prisma, TanStack Query). Gezählt wurde jeweils der Hauptzweig, das Jahr 2026 bleibt draußen, weil es erst zehn Monate alt ist.

{{chart:framework-commits}}

Elf dieser Projekte existierten 2018 bereits, alle anderen kamen später dazu. Diese elf tragen die Aussage: zusammen 25.841 Commits im Jahr 2018, 25.827 im Jahr 2025. Dazwischen liegt ein Ausschlag nach oben im Jahr 2023 mit 28.682 und ein Einbruch 2021 auf 23.362. Von einem dauerhaften Schub durch KI-Werkzeuge ist in der Summe nichts zu sehen.

## Zwei Sparten, zwei Richtungen

Hinter der flachen Summe liegen zwei gegenläufige Bewegungen. Die UI-Frameworks verlieren, die Anwendungs-Frameworks legen zu. Auf Indexbasis (2018 gleich 100) stehen die Design-Frameworks 2025 bei 62, die Anwendungen bei 124.

{{chart:framework-sparten}}

Der Rückgang der Design-Frameworks hat einen technischen Grund, der wenig mit KI zu tun hat. Browser können inzwischen selbst, was diese Bibliotheken einmal geliefert haben: `:has()`, Container Queries, `oklch()`, `color-mix()`, das native `<dialog>`-Element. Bootstrap 6, seit dem 8. Oktober 2026 als Alpha verfügbar, verlangt Chrome 130, Firefox 132 und Safari 18 und verzichtet dafür auf Präfixe und Polyfills. Was die Plattform übernimmt, muss das Framework nicht mehr nachbauen.

Auf der anderen Seite steht Next.js. Das Projekt steigerte sich von 1.078 Commits im Jahr 2018 auf 5.619 im Jahr 2025. Der größte Teil dieses Wachstums liegt allerdings vor November 2022: 2019 waren es 1.940, 2022 bereits 4.853. Danach flacht die Kurve ab. Next.js 16 im Oktober 2025 brachte Cache Components, Turbopack als Stabilversion und den React Compiler. Große Feature-Wellen also, aber keine Beschleunigung der Commit-Zahl.

## Der Haken an der Zahl

{{chart:framework-mensch}}

Commits sind ein grober Zähler, und in manchen Repositories zählen sie die falsche Arbeit. Bei MUI stammten 2025 von 1.541 Commits genau 753 von Renovate, also 48,9 Prozent. Bei Tailwind waren es 208 von 712, die ein Abhängigkeits-Bot eincheckte. Die Rohdaten zeigen für Tailwind einen Anstieg von 266 auf 712 Commits, ein Plus von 168 Prozent. Rechnet man die Bot-Konten heraus, bleiben 504 übrig, nach 828 im Jahr 2019. Das Vorzeichen dreht sich.

::: methode
Gezählt wurden Commits auf dem Hauptzweig über `GET /repos/{owner}/{repo}/commits` mit Jahresfenstern, dazu alle Releases über die Release-API. Bei sechs Projekten habe ich jeden Commit des Jahres einzeln abgerufen und nach Konten mit der Endung `[bot]` gefiltert: Vuetify, MUI, Tailwind, Next.js, Django, Spring Boot. In den übrigen zwölf Projekten sind Bots noch enthalten, die Zahlen dort also eher zu hoch. Merge-Commits stecken überall mit drin. Release-Zahlen habe ich verworfen, weil Monorepos wie Astro oder TanStack pro Paket veröffentlichen und naive Tag-Zähler das Zehnfache melden.
:::

Ein zweites Problem betrifft die Sache selbst. Ein {{Commit}} ist keine Funktion. Wer 2023 ein großes Refactoring in vielen kleinen Schritten eincheckt, erzeugt mehr Commits als jemand, der ein ganzes Jahr an einer einzigen Neuerung arbeitet. Die Zahl misst Betriebsamkeit, nicht Nutzen. Für die Frage, ob KI die Framework-Entwicklung beschleunigt hat, ist sie trotzdem brauchbar: Ein Schub müsste sich in irgendeiner Größenordnung zeigen, und sei es in den Releases oder den Beiträgen.

## Was stattdessen gewachsen ist

Auffällig ist ein anderes Muster. Die Frameworks haben in den letzten zwei Jahren damit begonnen, ihre Dokumentation für Programme statt für Menschen zu schreiben. Ant Design lieferte am 21. April 2025 `llms.txt` und `llms-full.txt` aus, also Textfassungen der Doku, die ein Modell ohne HTML-Rauschen lesen kann. Vuetify, MUI, Bootstrap, shadcn/ui, Chakra UI, Vite, Prisma, TanStack, SvelteKit, Nuxt und Next.js zogen nach. Bei MUI kam im Juni 2025 ein eigener MCP-Server dazu, bei Chakra im Juli 2025, bei shadcn im Oktober 2025, bei Next.js die DevTools-Erweiterung für Agenten. Laravel schrieb Version 13 im März 2026 „AI-native workflows“ in die Release Notes.

Der Ton in den Ankündigungen ist bemerkenswert. Der Bootstrap-Maintainer Mark Otto schrieb am 8. Oktober 2026 zur Alpha von Version 6, er habe seit Jahren Ideen für Bootstrap, „despite humans not writing any more code thanks to AI“. Das Projekt legte zusätzlich ein Verzeichnis `skills/` an, mit Anleitungen, die ein Agent beim Migrieren oder Komponentenbauen befolgen soll. Nutzer sind bei Bootstrap jetzt ausdrücklich „anyone, human or AI“.

Diese Arbeit ist neu, sie taucht aber in keiner Commit-Kurve als Sprung auf, weil sie klein ist: eine Textdatei, ein Server, ein paar Konfigurationsdateien. Sie verändert trotzdem, wer die Frameworks benutzt. Nuxt baute im Oktober 2026 eine Sperre für parallel laufende Entwicklungsserver ein, ausdrücklich für den Fall, dass ein Agent einen davon startet. Vite erkennt seit Version 8 im März 2026 selbst, wenn ein Coding-Agent im Spiel ist. Astro tut dasselbe seit Version 7 im Juni 2026.

Die drei großen Backend-Frameworks bleiben außen vor. Für Django, Ruby on Rails und Spring Boot fand sich weder ein `llms.txt` noch ein MCP-Server. Sie entwickeln sich weiter, Django 6.0 im Dezember 2025 brachte Template Partials und ein eigenes Tasks-Framework, Rails 8.1 im Oktober 2025 Active Job Continuations und lokale CI. Nur eben nicht in Richtung Agenten.

## Die Gegenprobe

Auf der Plattform sieht die Lage anders aus. GitHub meldet für die zwölf Monate bis September 34,3 Milliarden Commits, dreimal so viele wie zwei Jahre zuvor, und einen Anteil agentengestarteter Pull Requests von über 40 Prozent im September. Die Zahlen stehen ausführlich im [Octoverse-Artikel dieses Blogs vom 28. Oktober](octoverse-2026-34-3-milliarden-commits-github-vermisst-den-agenten-alltag.html); hier zählen sie nur als Kontrast zur Framework-Ebene.

Das passt zu den Umfragen. Im Stack-Overflow-Survey 2025 (49.009 Antworten) nutzen oder planen 84 Prozent der Befragten KI-Werkzeuge, 46 Prozent misstrauen deren Genauigkeit. Die DORA-Erhebung 2025 meldet 90 Prozent Nutzung, nach 76 Prozent im Vorjahr, und zum ersten Mal einen positiven Zusammenhang zwischen KI-Nutzung und Durchsatz. Prozentzahlen nannte DORA dafür nicht, 2024 waren es noch minus 1,5 Prozent Durchsatz und minus 7,2 Prozent Stabilität je 25 Prozent mehr KI-Adoption.

Bei der Produktivität hängt alles am Aufgabentyp. Peng und Kollegen maßen 2023 für einen einzelnen, klar umrissenen Task (einen HTTP-Server in JavaScript schreiben) 55,8 Prozent Zeitersparnis bei 95 Entwicklern. METR maß 2025 das Gegenteil: 16 erfahrene Open-Source-Entwickler brauchten mit Cursor für 246 Aufgaben in ihren eigenen, großen Repositories 19 Prozent länger, obwohl sie vorher 24 Prozent Ersparnis erwartet hatten. Beide Zahlen sind belastbar, sie messen nur verschiedene Dinge.

## Was das praktisch heißt

Die Frameworks sind keine Engstelle, an der KI plötzlich die Produktion verdreifacht. Sie sind Infrastruktur mit Release-Zügen, Kompatibilitätsversprechen und einer Handvoll Maintainer, die jede Änderung verantworten müssen. Ein schnellerer erster Entwurf hilft dort wenig. Was hilft, ist die Doku für Maschinen, und genau die entsteht seit 2025.

Die zweite Lehre betrifft die Messung selbst. Wer Commit-Zahlen als Produktivitätsmaß liest, zählt bei MUI zur Hälfte Renovate. Wer Release-Zahlen zählt, zählt bei Astro Paketveröffentlichungen. Wer Feature-Listen vergleicht, vergleicht Release-Politik. Die belastbare Aussage dieser Auswertung ist deshalb eng. In den elf etablierten Frameworks ist die Menge der Commits zwischen 2018 und 2025 nicht gewachsen. Die Verschiebung innerhalb der Gruppen folgt der Reife der Projekte, nicht dem Kalender der KI-Werkzeuge.

Offen bleibt die interessantere Frage. Wenn ein großer Teil der Pull Requests mit einem Agenten beginnt, entsteht die Arbeit dann in Anwendungen, die niemand mehr als Framework zählt? Die GitHub-Zahlen legen das nahe: Der Zuwachs landet in neuen Repositories, nicht in den alten. Für die Framework-Welt heißt das weniger Arbeit an der Basis und mehr Arbeit darauf. Ob das gut ist, entscheidet sich daran, ob die Wartung mitkommt. Die GitClear-Daten der letzten drei Jahre zeigen Refactoring-Anteile, die von 25 Prozent auf unter 10 Prozent gefallen sind, und Copy-Paste-Anteile, die von 8,3 auf 12,3 Prozent stiegen.

## Quellen

- GitHub-API, Commits und Releases der 18 Projekte, abgefragt am 31.10.2026: https://docs.github.com/en/rest/commits/commits
- Octoverse 2026, GitHub, 28.10.2026: https://github.blog/news-insights/octoverse/octoverse-commits-pushes-reach-new-highs-in-2026-as-developers-build-with-agents/
- Bootstrap 6 Alpha, 8.10.2026: https://blog.getbootstrap.com/2026/10/08/bootstrap-6-alpha/
- Vuetify-Releases 3.0.0 und 4.0.0: https://github.com/vuetifyjs/vuetify/releases
- Next.js 16, 21.10.2025: https://nextjs.org/blog/next-16
- Nuxt 4.2.2 mit MCP-Server und llms.txt, 9.12.2025: https://github.com/nuxt/nuxt/releases/tag/v4.2.2
- shadcn/ui Changelog und MCP: https://ui.shadcn.com/docs/changelog
- Chakra UI MCP-Server, Juli 2025: https://chakra-ui.com/blog
- Ant Design 5.24.8 mit llms.txt, 21.4.2025: https://github.com/ant-design/ant-design/releases/tag/5.24.8
- Vite 8, 12.3.2026: https://vite.dev/blog/announcing-vite8
- Astro 7, 22.6.2026: https://astro.build/blog/astro-7
- METR, Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity, 10.7.2025: https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
- Peng et al., The Impact of AI on Developer Productivity, 13.2.2023: https://arxiv.org/abs/2302.06590
- DORA 2024: https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report
- DORA 2025: https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report
- Stack Overflow Developer Survey 2025: https://survey.stackoverflow.co/2025/ai
- GitClear, AI Copilot Code Quality 2025: https://www.gitclear.com/ai_assistant_code_quality_2025_research
