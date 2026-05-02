# API-Endpunkte des AI Service
from fastapi import APIRouter
from fastapi.responses import Response, JSONResponse
from app.fetcher import DataFetcher
from app.interpreter import Interpreter
from app.output import OutputGenerator
from app.visualizer import Visualizer

router = APIRouter()
fetcher = DataFetcher()
interpreter = Interpreter()
output = OutputGenerator()
visualizer = Visualizer()


@router.get("/health")
def health():
    return {"status": "ok"}


@router.get("/analysis")
def get_analysis():
    stats = fetcher.get_stats()
    interpretation = interpreter.interpret(stats)
    return JSONResponse(output.build(stats, interpretation))


@router.get("/charts/ranking", response_class=Response)
def get_ranking_chart():
    stats = fetcher.get_stats()
    return Response(content=visualizer.ranking_chart(stats), media_type="image/png")


@router.get("/charts/peak", response_class=Response)
def get_peak_chart():
    stats = fetcher.get_stats()
    return Response(content=visualizer.peak_chart(stats), media_type="image/png")


@router.get("/charts/timeseries", response_class=Response)
def get_timeseries_chart():
    # Zeitverlauf-Diagramm – benoetigt laufenden Data Service mit GET /timeseries
    timeseries = fetcher.get_timeseries()
    return Response(content=visualizer.timeseries_chart(timeseries), media_type="image/png")