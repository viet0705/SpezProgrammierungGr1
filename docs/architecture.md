# Projektarchitektur

## Übersicht

Dieses Projekt analysiert Google Trends Daten der Kategorie **Supplements** (Region: Deutschland)
und besteht aus zwei unabhängigen Microservices, die über HTTP miteinander kommunizieren.

```
[ Google Trends CSV ]
        ↓
[ Data Service :8000 ]  →  liefert Mean, Peak, Trend als JSON
        ↓
[ AI Service :8001   ]  →  interpretiert Daten, generiert Visualisierungen
```

---

## Ordnerstruktur

```
SpezProgrammierungGr1/
├── services/
│   ├── data-service/              ← Viet
│   │   ├── app/
│   │   │   ├── __init__.py
│   │   │   ├── main.py            ← FastAPI App-Einstiegspunkt
│   │   │   ├── routes.py          ← API-Endpunkte (GET /health, GET /stats)
│   │   │   ├── reader.py          ← CSVReader: CSV-Dateien einlesen
│   │   │   ├── cleaner.py         ← DataCleaner: Datenbereinigung
│   │   │   └── calculator.py      ← StatsCalculator: Mean, Peak, Trendrichtung
│   │   ├── tests/
│   │   ├── Dockerfile
│   │   └── requirements.txt
│   └── ai-service/                ← Dongwoo
│       ├── app/
│       │   ├── __init__.py
│       │   ├── main.py            ← FastAPI App-Einstiegspunkt
│       │   ├── routes.py          ← API-Endpunkte (GET /health, GET /analysis, GET /charts/*)
│       │   ├── fetcher.py         ← DataFetcher: Kennzahlen per HTTP vom Data Service abrufen
│       │   ├── interpreter.py     ← Interpreter: Kennzahlen per LLM interpretieren
│       │   ├── output.py          ← OutputGenerator: JSON-Antwort zusammenstellen
│       │   └── visualizer.py      ← Visualizer: Diagramme erstellen (matplotlib)
│       ├── tests/
│       ├── Dockerfile
│       └── requirements.txt
├── k8s/
│   ├── data-service/
│   │   ├── deployment.yaml        ← Kubernetes Deployment-Konfiguration
│   │   └── service.yaml           ← Kubernetes Service-Konfiguration
│   └── ai-service/
│       ├── deployment.yaml
│       └── service.yaml
├── data/
│   └── csv/                       ← Google Trends CSV-Dateien (von Viet exportiert)
├── docs/                          ← Projektdokumentation (nicht Teil der Abgabe)
├── docker-compose.yml             ← Lokaler Start beider Services
├── .env.example                   ← Benötigte Umgebungsvariablen (Vorlage)
└── README.md                      ← Abgabedokument (7 Fragen)
```

---

## Services

### Data Service (Port 8000)
- Liest CSV-Dateien aus `data/csv/` (`CSVReader`)
- Bereinigt die Rohdaten (`DataCleaner`)
- Berechnet Kennzahlen: **Mean**, **Peak**, **Trendrichtung** (`StatsCalculator`)
- Stellt Ergebnisse als JSON über `GET /stats` bereit
- Technologie: Python, FastAPI, pandas

### AI Service (Port 8001)
- Ruft Kennzahlen vom Data Service per HTTP ab (`DataFetcher`)
- Interpretiert die Kennzahlen mit einem LLM (`Interpreter`)
- Stellt die Interpretation als JSON über `GET /analysis` bereit (`OutputGenerator`)
- Erstellt mindestens 2 Visualisierungen als PNG (`Visualizer`): Ranking-Diagramm + Zeitverlauf
- Technologie: Python, FastAPI, OpenAI SDK, matplotlib

---

## Lokale Entwicklung

```bash
# Beide Services starten
docker compose up -d

# Data Service direkt erreichbar unter
http://localhost:8000/docs

# AI Service direkt erreichbar unter
http://localhost:8001/docs
```

### Entwicklung ohne Docker

Zum Testen einzelner Klassen ohne laufende Services:

```bash
cd services/ai-service
source .venv/Scripts/activate
python test_run.py
```

> `test_run.py` ist ein temporaeres Skript fuer die lokale Entwicklung und nicht fuer den Produktionsbetrieb vorgesehen.

## Umgebungsvariablen

Datei `.env` im Root-Verzeichnis erstellen (Vorlage: `.env.example`):

```
OPENAI_API_KEY=...
OPENAI_BASE_URL=...
DATA_SERVICE_URL=http://data-service:8000
```

> Die `.env` Datei wird nicht ins Repository eingecheckt (gitignore).