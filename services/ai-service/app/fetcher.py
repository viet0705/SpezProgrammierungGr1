# DataFetcher: Kennzahlen per HTTP vom Data Service abrufen
import os
import httpx

# Platzhalterdaten für lokale Entwicklung ohne Data Service
MOCK_STATS = [
    {"name": "Proteinpulver", "mean": 62.3, "peak": 100, "trend": "steigend"},
    {"name": "Kreatin",       "mean": 45.2, "peak": 87,  "trend": "steigend"},
    {"name": "Whey Protein",  "mean": 38.7, "peak": 75,  "trend": "stabil"},
    {"name": "Vitamin D",     "mean": 55.1, "peak": 92,  "trend": "fallend"},
    {"name": "Omega 3",       "mean": 29.4, "peak": 61,  "trend": "stabil"},
]


class DataFetcher:
    def __init__(self):
        self.base_url = os.getenv("DATA_SERVICE_URL", "http://localhost:8000")

    def get_stats(self) -> list[dict]:
        # Bei Fehler (Service nicht erreichbar) werden Mock-Daten zurueckgegeben
        try:
            response = httpx.get(f"{self.base_url}/stats", timeout=5)
            return response.json()["keywords"]
        except Exception:
            return MOCK_STATS