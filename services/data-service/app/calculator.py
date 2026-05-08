import pandas as pd


class StatsCalculator:
    def calculate(self, data: pd.DataFrame) -> list[dict]:
        return [self._keyword_stats(data, column) for column in data.columns if column != "date"]

    def _keyword_stats(self, data: pd.DataFrame, keyword: str) -> dict:
        values = data[keyword]
        peak_index = values.idxmax()

        return {
            "name": keyword,
            "mean": round(float(values.mean()), 2),
            "peak": int(values.max()),
            "peak_date": data.loc[peak_index, "date"].date().isoformat(),
            "trend": self._trend(values),
        }

    def _trend(self, values: pd.Series) -> str:
        if len(values) < 2:
            return "stabil"

        midpoint = len(values) // 2
        first_half_mean = values.iloc[:midpoint].mean()
        second_half_mean = values.iloc[midpoint:].mean()
        difference = second_half_mean - first_half_mean

        if difference > 5:
            return "steigend"
        if difference < -5:
            return "fallend"
        return "stabil"
