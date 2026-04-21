# Aufgabe

Diese Aufgabe besteht aus zwei Teilen:

1. Inhaltliche Abgabe (Template mit 7 Fragen)  
2. Technische Umsetzung (AI + Docker + Kubernetes mit zwei Services + Github + Pitch)  

Gruppengrösse ist 1 bis 2 Personen pro Gruppe.
Gruppen sind per Email an alkurdiz@htw-berlin.de ODER per Moodle einzutragen https://moodle.htw-berlin.de/mod/wiki/view.php?id=2035127.

Die Abgabe der Prüfungsleistung hat bis spätestens am 23.05.2026 23:59:59 Uhr per E-Mail an alkurdiz@htw-berlin.de und richtero@htw-berlin.de zu erfolgen mit dem GitHub Repository.
---

## Technologie-Stack
- Docker
- Docker Compose
- Kubernetes
- Github
- Google Trends
- AI

### Hinweis zu Daten  
Für alle werden Daten von Google Trends verwendet [Google Trends](https://trends.google.com/). 

---

## Zielstellung
Ziel ist es, reale Suchdaten aus Google Trends zu analysieren und daraus mithilfe einer containerisierten Anwendung datenbasierte Erkenntnisse und AI-gestützte Interpretationen zu gewinnen.

Dabei soll eine Anwendung entwickelt werden, die Daten verarbeitet, visualisiert und automatisch interpretiert.

---

## Datengrundlage
Verwende Google Trends mit folgenden Einstellungen:

- **Region:** Deutschland  
- **Zeitraum:** letzter Monat  
- **Suchtyp:** Web Search  

Analysiere **eine der folgenden Kategorien**:

### Schuhe
- Tennisschuhe  
- Fußballschuhe  
- Basketballschuhe  
- Designer Sneaker  
- High Top Sneaker  
- bequeme Sneaker  
- Retro Sneaker  
- Casual Sneaker  

### Matcha
- Matcha Tee  
- Matcha Pulver  
- Ceremonial Matcha  
- Premium Matcha  
- Uji Matcha  
- Bio Matcha  
- Matcha Latte  
- Matcha kaufen  
- Matcha Wirkung  

### Cold Drinks
- Cold Brew Kaffee
- Softdrinks
- Eiskaffee  
- Eistee  
- Matcha Latte kalt  
- Energy Drink  
- Iced Latte  

### Supplements
- Proteinpulver  
- Kreatin  
- Whey Protein  
- Vitamin D  
- Omega 3  
- Magnesium  

Verwende maximal **5 Begriffe gleichzeitig** in Google Trends.
Alle verwendeten Begriffe müssen:
- thematisch vergleichbar sein
- zur gleichen Kategorie gehören

Exportiere die Daten als CSV:
- **Interest over time**
- **Top queries**
- **Rising queries**

---

## Systemanforderungen

Die Anwendung muss aus **mindestens zwei Services** bestehen:

### 1. Data Service
Der Data Service muss eine API bereitstellen, die die berechneten Daten als JSON zurückgibt.

**Verantwortlich für:**
- Einlesen der CSV-Dateien  
- Datenbereinigung  
- Berechnung von Kennzahlen  

**Mindestfunktionen:**
- Durchschnitt (Mean)  
- Maximum (Peak)  
- Trendrichtung (steigend / fallend / stabil)  

---

### 2. AI / Analysis Service
Die AI-Analyse muss auf den berechneten Kennzahlen (z. B. Mean, Peak, Trend) basieren.

**Verantwortlich für:**
- Abruf der Daten vom Data Service  
- Durchführung der Analyse  
- Generierung einer Interpretation  

Die Services müssen über **HTTP miteinander kommunizieren**.
Direkter Zugriff auf Dateien zwischen Services ist nicht erlaubt.
---

## Visualisierung

Die Anwendung muss mindestens **zwei Visualisierungen** enthalten, z. B.:

- Zeitverlauf (Line Chart)  
- Vergleich mehrerer Begriffe  
- Ranking nach Interesse  

---

## AI-Anforderungen

Die Anwendung muss eine **automatische Interpretation** erzeugen.

Diese muss:
- auf den berechneten Daten basieren  
- konkrete Aussagen enthalten  

**Beispiele:**
- Welcher Begriff zeigt den stärksten Trend  
- Wo treten Peaks auf  
- Welche Unterschiede gibt es  

Reine Textgenerierung ohne Datenbasis ist **nicht ausreichend**.

Die AI-Komponente ist **kein Chatbot**.  
Sie dient ausschließlich der automatischen Analyse und Interpretation der Daten.

Die AI muss strukturierte Daten (z. B. Mean, Peak, Trend) verarbeiten und daraus nachvollziehbare Aussagen ableiten.

Interaktive Chat-Funktionalität ist nicht erforderlich und wird nicht bewertet.

---

## Wo greift die AI ein?

Ganz konkret im Datenfluss:
```text
Data Service → liefert Zahlen
↓
AI Service → übersetzt Zahlen in Aussagen
```

- Der **Data Service** berechnet Kennzahlen (z. B. Mean, Peak, Trend).  
- Der **AI Service** interpretiert diese Kennzahlen und erzeugt verständliche Aussagen.  

Die AI fungiert als **Interpretationsschicht zwischen Daten und Nutzer:innen**.
---

## Docker

- Jeder Service muss containerisiert sein  
- Die Anwendung muss lokal mit Docker gestartet werden können und zusätzlich erfolgreich in Kubernetes deployt werden.

---

## Kubernetes

Die Anwendung muss in Kubernetes deployt werden mit:

- mindestens **2 Deployments**  
- mindestens **2 Services**  

---

## GitHub

Das Projekt muss als **GitHub Repository** abgegeben werden.

**Anforderungen:**
- Vollständiger Code im Repository  
- README.md im Root-Verzeichnis  

**Das Repository muss enthalten:**
- Quellcode aller Services  
- Dockerfile(s)  
- Kubernetes YAML-Dateien  
- verwendete CSV-Dateien  

---

## Ziel

Am Ende soll eine lauffähige Anwendung entstehen, die:

- Daten verarbeitet  
- Trends visualisiert  
- automatisch interpretiert  
- als containerisierte Anwendung in Kubernetes läuft  


---

# Teil 1: Abgabe-Template - Inhaltliche Abgabe 

Bitte beantworten Sie die folgenden Abschnitte in vollständigen Sätzen.  
Jede Antwort soll ca. 7–10 Zeilen umfassen.  
Antworten mit weniger als 7 Zeilen gelten als unzureichend und führen zu Punktabzug.  
Stichpunkte sind nicht zulässig.
Die README.md soll am Ende maximal 220 Zeilen umfassen.

1. Executive Summary – Geben Sie eine kurze Zusammenfassung Ihres Projekts.  
Welche Kategorie wurde analysiert und welche zentralen Erkenntnisse wurden gewonnen?  
2. Ziele des Projekts – Welches Ziel verfolgt Ihr Projekt?  
Welches Problem oder welche Fragestellung im Kontext von Google Trends wird untersucht?  
3. Anwendung und Nutzung – Wie wird die Anwendung gestartet (How to start, Step by step)?  
Wie wird Ihre Anwendung genutzt? 
Wer sind die potenziellen Nutzer:innen?  
4. Datenanalyse und Ergebnisse – Welche Muster oder Trends konnten Sie erkennen?  
Gab es auffällige Peaks, Unterschiede oder Entwicklungen?  
Welche Begriffe haben sich besonders hervorgehoben? 
5. Visualisierung – Welche Visualisierungen wurden erstellt und warum?  
Wie helfen diese, die Daten besser zu verstehen? 
6. Herausforderungen und Learnings – Welche technischen oder fachlichen Probleme sind aufgetreten?  
Wie wurden diese gelöst?  
Was haben Sie aus dem Projekt gelernt?  
7. Zukunftsvision – Wie könnte Ihr System weiterentwickelt werden?  
Welche zusätzlichen Daten, Features oder AI-Methoden könnten integriert werden? 

---

# Teil 2: Technische Umsetzung 

## 1. AI-Komponente

- Es muss mindestens **eine AI-Funktion** implementiert werden (z. B. Analyse, Zusammenfassung oder Empfehlung).
- Nutzung einer API (z. B. Deepseek, OpenAI) ist erlaubt. (API-Keys werden vom Dozenten bereitgestellt)
- Die AI muss auf den berechneten Daten basieren (z. B. Mean, Peak, Trend).
- Die AI darf nicht ausschließlich auf Rohtexten ohne Datenanalyse basieren.

---

## 2. Docker

- Die Anwendung muss containerisiert werden (Dockerfile).
- Alle Services müssen enthalten sein.
- Die Anwendung muss lokal startbar sein mit:

```bash
docker compose up -d
```

## 3. Kubernetes (lokal, z. B. kind oder Docker Desktop)

- Mindestens **2 Services** (Data Service und AI Service)  
- Mindestens **1 Deployment pro Service**  
- Services müssen über **HTTP kommunizieren**  

---

## 4. Pitch (Audio bevorzugt, alternativ Video)

- Dauer: **1–3 Minuten**

**Inhalt:**
- Problemstellung  
- wichtigste Erkenntnisse  

---

## Abgabeformat

### Code (GitHub Repository) mit:
- Quellcode aller Services  
- Dockerfile(s)  
- Kubernetes-Manifeste (Ordner `k8s/`)  
- verwendete CSV-Dateien  

### README.md
- Antworten auf die Fragen aus Teil 1  
- maximal **220 Zeilen**  

### Pitch
- Audio bevorzugt, alternativ Video  
- Dauer: **1–3 Minuten**

---

## Bewertung (100 Punkte)

- Konzept und README – 40 Punkte  
- AI-Komponente – 25 Punkte  
- Docker – 20 Punkte  
- Kubernetes (mindestens zwei Services) – 10 Punkte  
- Pitch – 5 Punkte  

---

## Notenskala

- **1.0 (sehr gut):** 95 – 100 Punkte  
- **1.3:** 90 – 94 Punkte  
- **1.7:** 85 – 89 Punkte  
- **2.0 (gut):** 80 – 84 Punkte  
- **2.3:** 75 – 79 Punkte  
- **2.7:** 70 – 74 Punkte  
- **3.0 (befriedigend):** 65 – 69 Punkte  
- **3.3:** 60 – 64 Punkte  
- **3.7:** 55 – 59 Punkte  
- **4.0 (ausreichend):** 50 – 54 Punkte  
- **5.0 (nicht bestanden):** < 50 Punkte  

---

## Hinweise

- Nachweise bitte **textbasiert im README**, keine Screenshots  
- Google Trends Daten sind **relativ (0–100)** und müssen korrekt interpretiert werden  
- Pitch: Audio bevorzugt, Video optional  

---

## To-do-Liste

1. Thema wählen (eine Kategorie auswählen)  
2. Google Trends Daten exportieren (CSV)  
3. Data Service implementieren  
4. AI Service implementieren  
5. Anwendung in Docker containerisieren  
6. Anwendung lokal starten (`docker compose up -d`)  
7. Kubernetes Deployment erstellen (`k8s/` Ordner)  
8. Services in Kubernetes deployen  
9. Pitch aufnehmen (1–3 Minuten)  
10. Finale Kontrolle:
   - README vollständig (max. 220 Zeilen)  
   - Code vollständig  
   - Docker + Kubernetes funktional  
   - GitHub Repository vollständig  

---

## Abgabefrist

Die Abgabe erfolgt bis spätestens:

**23.05.2026, 23:59:59 Uhr**

Per E-Mail an:

- alkurdiz@htw-berlin.de  
- richtero@htw-berlin.de  

inklusive GitHub Repository Link.
