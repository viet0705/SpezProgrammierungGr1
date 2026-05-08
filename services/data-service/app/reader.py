import os
from pathlib import Path

import pandas as pd


class CSVReader:
    def __init__(self, data_dir: Path | None = None):
        self.data_dir = data_dir or self._default_data_dir()

    def _default_data_dir(self) -> Path:
        if os.getenv("DATA_DIR"):
            return Path(os.environ["DATA_DIR"])

        app_file = Path(__file__).resolve()
        candidates = [
            Path.cwd() / "data" / "csv",
            app_file.parents[1] / "data" / "csv",
        ]
        if len(app_file.parents) > 3:
            candidates.append(app_file.parents[3] / "data" / "csv")

        for candidate in candidates:
            if candidate.exists():
                return candidate

        return candidates[0]

    def read_interest_over_time(self) -> pd.DataFrame:
        path = self.data_dir / "interest_over_time.csv"
        if not path.exists():
            raise FileNotFoundError(f"CSV file not found: {path}")

        return pd.read_csv(path)

    def read_query_file(self, filename: str) -> list[dict]:
        path = self.data_dir / filename
        if not path.exists():
            return []

        return pd.read_csv(path).to_dict(orient="records")
