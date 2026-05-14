# Development Guide

## Voraussetzungen

- Docker Desktop (mit aktiviertem Kubernetes)
- Git
- OpenAI API Key

---

## Lokaler Start mit Docker Compose

### 1. Repository klonen

```bash
git clone https://github.com/viet0705/SpezProgrammierungGr1.git
cd SpezProgrammierungGr1
```

### 2. Umgebungsvariablen setzen

```bash
cp .env.example .env
# .env öffnen und OPENAI_API_KEY eintragen
```

### 3. Services starten

```bash
docker compose up --build
```

### 4. Endpunkte testen

**Data Service** (`http://localhost:8000`)

| Endpunkt | Beschreibung |
|----------|--------------|
| `GET /health` | Statusprüfung |
| `GET /stats` | Kennzahlen als JSON (Mean, Peak, Trend) |
| `GET /timeseries` | Tageswerte als JSON |

**AI Service** (`http://localhost:8001`)

| Endpunkt | Beschreibung |
|----------|--------------|
| `GET /health` | Statusprüfung |
| `GET /analysis` | KI-Interpretation als JSON |
| `GET /charts/ranking` | Ranking-Diagramm (PNG) |
| `GET /charts/peak` | Peak vs. Durchschnitt (PNG) |
| `GET /charts/timeseries` | Zeitverlauf (PNG) |

### 5. Services stoppen

```bash
docker compose down
```

---

## Kubernetes Deployment (lokal)

### Voraussetzung

Docker Desktop → Settings → Kubernetes → Enable Kubernetes aktivieren.

### 1. Images lokal bauen

```bash
docker compose build
```

### 2. Manifeste anwenden

```bash
kubectl apply -f k8s/data-service/
kubectl apply -f k8s/ai-service/
```

### 3. API Key als Secret hinterlegen (optional, für /analysis)

```bash
kubectl create secret generic ai-api-secret \
  --from-literal=OPENAI_API_KEY=sk-...
```

### 4. Deployment prüfen

```bash
kubectl get deployments
kubectl get services
kubectl get pods
```

### 5. Endpunkte erreichbar machen

```bash
kubectl port-forward service/data-service 8000:8000
kubectl port-forward service/ai-service 8001:8000
```

### 6. Manifeste entfernen

```bash
kubectl delete -f k8s/data-service/
kubectl delete -f k8s/ai-service/
```

---

## Projektstruktur

```
SpezProgrammierungGr1/
├── services/
│   ├── data-service/
│   │   ├── app/
│   │   │   ├── main.py         FastAPI Einstiegspunkt
│   │   │   ├── routes.py       API-Endpunkte
│   │   │   ├── reader.py       CSVReader – Dateien einlesen
│   │   │   ├── cleaner.py      DataCleaner – Daten bereinigen
│   │   │   └── calculator.py   StatsCalculator – Kennzahlen berechnen
│   │   └── Dockerfile
│   └── ai-service/
│       ├── app/
│       │   ├── main.py         FastAPI Einstiegspunkt
│       │   ├── routes.py       API-Endpunkte
│       │   ├── fetcher.py      DataFetcher – Daten vom Data Service holen
│       │   ├── interpreter.py  Interpreter – KI-Interpretation (GPT-4o-mini)
│       │   ├── output.py       OutputGenerator – JSON-Antwort zusammenstellen
│       │   └── visualizer.py   Visualizer – Diagramme erstellen
│       └── Dockerfile
├── k8s/
│   ├── data-service/
│   │   ├── deployment.yaml
│   │   └── service.yaml
│   └── ai-service/
│       ├── deployment.yaml
│       └── service.yaml
├── data/csv/                   Google Trends CSV-Dateien
├── docker-compose.yml
├── .env.example
├── README.md
└── DEVELOPMENT.md
```

---

## Abhängigkeiten

**Data Service**
- `fastapi` — Web-Framework
- `uvicorn` — ASGI-Server
- `pandas` — CSV-Verarbeitung und Statistikberechnung

**AI Service**
- `fastapi` — Web-Framework
- `uvicorn` — ASGI-Server
- `httpx` — HTTP-Client für Data Service Anfragen
- `openai` — GPT-4o-mini API
- `matplotlib` — Diagrammerstellung