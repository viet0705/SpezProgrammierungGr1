import os
import httpx
from fastapi import APIRouter
from fastapi.responses import Response, JSONResponse
from app.analysis import interpret
from app.charts import ranking_chart, peak_chart

router = APIRouter()

DATA_SERVICE_URL = os.getenv("DATA_SERVICE_URL", "http://localhost:8000")

# Beispieldaten fuer lokale Entwicklung (solange Data Service nicht verfuegbar)
MOCK_STATS = [
    {"name": "Proteinpulver", "mean": 62.3, "peak": 100, "trend": "steigend"},
    {"name": "Kreatin",       "mean": 45.2, "peak": 87,  "trend": "steigend"},
    {"name": "Whey Protein",  "mean": 38.7, "peak": 75,  "trend": "stabil"},
    {"name": "Vitamin D",     "mean": 55.1, "peak": 92,  "trend": "fallend"},
    {"name": "Omega 3",       "mean": 29.4, "peak": 61,  "trend": "stabil"},
]


def fetch_stats() -> list[dict]:
    try:
        response = httpx.get(f"{DATA_SERVICE_URL}/stats", timeout=5)
        return response.json()["keywords"]
    except Exception:
        return MOCK_STATS


@router.get("/analysis")
def get_analysis():
    stats = fetch_stats()
    interpretation = interpret(stats)
    return JSONResponse({"interpretation": interpretation, "stats": stats})


@router.get("/charts/ranking", response_class=Response)
def get_ranking_chart():
    stats = fetch_stats()
    return Response(content=ranking_chart(stats), media_type="image/png")


@router.get("/charts/peak", response_class=Response)
def get_peak_chart():
    stats = fetch_stats()
    return Response(content=peak_chart(stats), media_type="image/png")
