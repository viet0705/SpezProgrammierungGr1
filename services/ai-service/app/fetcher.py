# DataFetcher: Kennzahlen per HTTP vom Data Service abrufen
import os
import httpx


class DataFetcher:
    def __init__(self):
        self.base_url = os.getenv("DATA_SERVICE_URL", "http://localhost:8000")

    def get_stats(self) -> list[dict]:
        response = httpx.get(f"{self.base_url}/stats", timeout=5)
        response.raise_for_status()
        return response.json()["keywords"]

    def get_timeseries(self) -> list[dict]:
        # Zeitreihendaten vom Data Service abrufen (benötigt GET /timeseries)
        response = httpx.get(f"{self.base_url}/timeseries", timeout=5)
        response.raise_for_status()
        return response.json()["timeseries"]