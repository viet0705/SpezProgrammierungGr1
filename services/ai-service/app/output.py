# OutputGenerator: Interpretationsergebnis als JSON-Antwort zusammenstellen


class OutputGenerator:
    def build(self, stats: list[dict], interpretation: str) -> dict:
        return {"interpretation": interpretation, "stats": stats}