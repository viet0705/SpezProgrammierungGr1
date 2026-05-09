from fastapi import APIRouter

from app.calculator import StatsCalculator
from app.cleaner import DataCleaner
from app.reader import CSVReader

router = APIRouter()
reader = CSVReader()
cleaner = DataCleaner()
calculator = StatsCalculator()


def _load_timeseries():
    raw_data = reader.read_interest_over_time()
    return cleaner.clean_interest_over_time(raw_data)


@router.get("/health")
def health():
    return {"status": "ok"}


@router.get("/live")
def live():
    return {"status": "alive"}


@router.get("/ready")
def ready():
    _load_timeseries()
    return {"status": "ready"}


@router.get("/stats")
def get_stats():
    timeseries = _load_timeseries()
    keywords = calculator.calculate(timeseries)

    return {
        "category": "Supplements",
        "region": "DE",
        "period": "last_month",
        "keywords": keywords,
    }


@router.get("/timeseries")
def get_timeseries():
    timeseries = _load_timeseries()
    output = timeseries.copy()
    output["date"] = output["date"].dt.date.astype(str)

    return {"timeseries": output.to_dict(orient="records")}
