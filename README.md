# Google Trends Analyse – Supplements

## Projektteam

| Name | Rolle |
|------|-------|
| Dongwoo Kim | AI Service, Visualisierung, Dokumentation, Pitch |
| Quoc Viet Nguyen | Data Service, Docker, Kubernetes |

## 1. Executive Summary

In diesem Projekt haben wir das Google Trends Suchinteresse für fünf Supplement-Begriffe in Deutschland untersucht. 
Analysiert wurden Vitamin D, Omega 3, Kreatin, Proteinpulver und Whey Protein im Zeitraum vom 09.04. bis 08.05.2026. 
Da alle fünf Begriffe gleichzeitig exportiert wurden, normalisiert Google Trends die Werte relativ zum höchsten Datenpunkt im gesamten Vergleich. 
Vitamin D erreichte dabei am 15. April den höchsten Wert von 100 und bildet damit den Referenzpunkt für alle anderen Begriffe. 
Mit einem Mittelwert von 78,6 dominiert Vitamin D das Suchinteresse deutlich, zeigt aber wie Omega 3 einen fallenden Trend nach dem Peak. 
Kreatin und Proteinpulver verhalten sich über den Zeitraum stabil, während Whey Protein mit einem Mittelwert von 24,5 das geringste Interesse aller fünf Begriffe aufweist. 
Insgesamt lässt sich sagen, dass klassische Gesundheitssupplemente wie Vitamin D und Omega 3 zwar nach wie vor stark nachgefragt werden, das Interesse im Verlauf des Aprils jedoch spürbar nachgelassen hat.

---

## 2. Ziele des Projekts

Google Trends stellt zwar öffentlich zugängliche Suchdaten bereit, aber ohne weitere Verarbeitung lassen sich daraus kaum konkrete Aussagen ableiten. 
Genau dieses Problem adressiert unser Projekt: Wie lassen sich Rohdaten automatisiert so aufbereiten, dass sie verständliche Erkenntnisse liefern? 
Die zentrale Fragestellung lautet, welche Supplement-Begriffe in Deutschland am meisten gesucht werden, wann Peaks auftreten und wie sich das Interesse im Zeitverlauf entwickelt. 
Ziel war es, eine Anwendung zu entwickeln, die diesen gesamten Prozess vom CSV-Import über die statistische Auswertung bis zur KI-gestützten Interpretation vollständig automatisiert. 
Die KI-Komponente soll dabei keine vorgefertigten Texte ausgeben, sondern Schlussfolgerungen direkt aus den berechneten Kennzahlen ableiten.
Das Projekt zeigt damit, wie sich öffentlich verfügbare Daten mit wenig Aufwand in verwertbare Insights überführen lassen, etwa für Marktanalysten oder Produktmanager im Gesundheitsbereich.

---

## 3. Anwendung und Nutzung

Zum Starten der Anwendung wird zunächst eine `.env-Datei` im Root-Verzeichnis mit dem OpenAI API Key angelegt.
Im zweiten Schritt werden beide Services mit `docker compose up --build` gestartet.
Der Data Service ist danach auf Port 8000 erreichbar und gibt berechnete Kennzahlen sowie Zeitreihendaten als JSON zurück, der AI Service auf Port 8001 liefert eine KI-generierte Interpretation sowie drei Diagramme als PNG-Bilder.
Wer die Anwendung in Kubernetes deployen möchte, wendet anschließend die Manifeste aus dem k8s/-Ordner mit `kubectl apply` an.
Die Anwendung richtet sich an alle, die ohne eigene Datenanalyse-Kenntnisse strukturierte Aussagen über Suchtrends benötigen, etwa Marktanalysten oder Produktmanager im Gesundheits- und Fitnessbereich.
Da die Ergebnisse als JSON und PNG ausgegeben werden, lassen sie sich außerdem leicht in bestehende Dashboards integrieren.

---

## 4. Datenanalyse und Ergebnisse

Im Analysezeitraum vom 09.04. bis 08.05.2026 zeigen die fünf Supplement-Begriffe deutlich unterschiedliche Suchmuster.
Vitamin D sticht dabei klar heraus: Mit einem Mittelwert von 78,6 und einem Peak von 100 am 15. April liegt es weit vor allen anderen Begriffen.
Auffällig ist außerdem, dass Vitamin D am 21. April nochmals auf etwa 93 anstieg, bevor es in der zweiten Monatshälfte spürbar abfiel.
Omega 3 folgt mit einem Mittelwert von 66,6 und einem Peak von 81 am 14. April, wobei die zeitliche Nähe beider Peaks auf einen gemeinsamen externen Auslöser hindeuten könnte.
Kreatin bleibt mit einem Mittelwert von 47,8 über den gesamten Zeitraum stabil, ebenso wie Proteinpulver mit 31,6, was auf ein gleichbleibendes Interesse in der Fitness-Community hindeutet.
Whey Protein zeigt mit einem Mittelwert von 24,5 nicht nur das geringste Suchinteresse, sondern auch den stärksten Rückgang gegen Ende des Zeitraums.

---

## 5. Visualisierung

Die Anwendung erstellt drei Diagramme, die jeweils unterschiedliche Aspekte der Daten sichtbar machen.
Das Ranking-Diagramm ist ein horizontales Balkendiagramm, das die fünf Begriffe nach ihrem Durchschnittswert sortiert und damit auf einen Blick zeigt, welches Supplement im Beobachtungszeitraum am meisten gesucht wurde.
Das Peak-vs-Durchschnitt-Diagramm stellt für jeden Begriff den Höchstwert und den Mittelwert nebeneinander dar, was verdeutlicht, wie stark das Interesse kurzfristig geschwankt ist.
Das Zeitverlauf-Diagramm zeigt die tägliche Entwicklung aller fünf Begriffe als Liniendiagramm und macht saisonale Muster sowie den allgemeinen Rückgang im Monatsverlauf sichtbar.
Die drei Visualisierungen ergänzen sich dabei gut: Das Ranking gibt einen schnellen Überblick, während die anderen beiden Diagramme tiefergehende Einblicke in Schwankungen und zeitliche Entwicklungen ermöglichen.
Da die Anwendung kein Frontend besitzt, werden alle Diagramme serverseitig mit matplotlib generiert und direkt als PNG-Bilder zurückgegeben.

---

## 6. Herausforderungen und Learnings

Eine der ersten Hürden war die Service-Kommunikation zwischen den beiden Containern.
Lokal funktioniert localhost problemlos, aber in Docker Compose und Kubernetes muss der Service-Name als Hostname verwendet werden.
Das haben wir über die Umgebungsvariable DATA_SERVICE_URL gelöst, die je nach Umgebung unterschiedlich gesetzt wird.
Für die Diagrammerstellung musste außerdem das Agg-Backend von matplotlib explizit gesetzt werden, da Docker-Container keine grafische Oberfläche haben und sonst ein Fehler geworfen wird.
Das wichtigste Learning war für uns, dass eine saubere Trennung der beiden Services zwar anfangs mehr Aufwand bedeutet, die unabhängige Entwicklung und spätere Wartung aber deutlich vereinfacht.
Insgesamt hat das Projekt gezeigt, wie viel Aufwand allein in der richtigen Konfiguration von Containerumgebungen steckt.
Rückblickend war der größte Lerneffekt nicht die KI-Integration selbst, sondern zu verstehen, wie viel Konfigurationsarbeit nötig ist, bevor die eigentliche Analyse überhaupt beginnen kann.

---

## 7. Zukunftsvision

Die naheliegendste Erweiterung wäre die Integration der pytrends-Bibliothek, um Google Trends-Daten automatisch abzurufen, anstatt CSV-Dateien manuell zu exportieren.
Da die aktuelle Analyse nur einen Monat abdeckt, wäre eine Erweiterung auf einen Jahreszeitraum besonders interessant, um saisonale Muster zu erkennen, etwa ob Vitamin D im Winter deutlich mehr gesucht wird als im Sommer.
Ein Web-Frontend mit Streamlit würde die Diagramme und die KI-Interpretation übersichtlich darstellen und die Anwendung auch für nicht-technische Nutzer zugänglich machen.
Langfristig wäre es spannend, die Google Trends-Daten mit echten Verkaufsdaten von Plattformen wie Amazon oder Temu zu verknüpfen und zu untersuchen, ob ein hohes Suchinteresse tatsächlich mit steigenden Verkaufszahlen korreliert.
Das würde den Mehrwert der Anwendung deutlich erhöhen, da Suchdaten allein keine Kaufabsicht belegen.
Für Langzeitanalysen wäre außerdem eine Datenbankanbindung sinnvoll, die historische Snapshots speichert und Vergleiche über mehrere Monate hinweg ermöglicht.