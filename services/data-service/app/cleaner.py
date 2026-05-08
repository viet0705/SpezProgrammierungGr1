import pandas as pd


class DataCleaner:
    def clean_interest_over_time(self, data: pd.DataFrame) -> pd.DataFrame:
        cleaned = data.copy()
        cleaned = cleaned.rename(columns={cleaned.columns[0]: "date"})
        cleaned["date"] = pd.to_datetime(cleaned["date"], errors="coerce")

        for column in cleaned.columns:
            if column == "date":
                continue

            cleaned[column] = (
                cleaned[column]
                .astype(str)
                .str.replace("<1", "0", regex=False)
                .str.replace(",", ".", regex=False)
            )
            cleaned[column] = pd.to_numeric(cleaned[column], errors="coerce").fillna(0)

        cleaned = cleaned.dropna(subset=["date"]).sort_values("date")
        return cleaned
