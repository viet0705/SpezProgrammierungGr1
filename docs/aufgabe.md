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

## Bewertung (100 Punkte)

- Konzept und README – 40 Punkte  
- AI-Komponente – 25 Punkte  
- Docker – 20 Punkte  
- Kubernetes (mindestens zwei Services) – 10 Punkte  
- Pitch – 5 Punkte  

---

## Notenskala

- **1.0 (sehr gut):** 95 – 100 Punkte  
- **1.7:** 85 – 89 Punkte  
- **2.0 (gut):** 80 – 84 Punkte  
- **2.3:** 75 – 79 Punkte  
- **3.0 (befriedigend):** 65 – 69 Punkte  
- **4.0 (ausreichend):** 50 – 54 Punkte  
- **5.0 (nicht bestanden):** < 50 Punkte  

---

## Abgabefrist

**23.05.2026, 23:59:59 Uhr**

Per E-Mail an:
- alkurdiz@htw-berlin.de  
- richtero@htw-berlin.de  

inklusive GitHub Repository Link.
