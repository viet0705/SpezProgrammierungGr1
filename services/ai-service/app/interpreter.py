# Interpreter: Kennzahlen per LLM interpretieren
import os
from openai import OpenAI


class Interpreter:
    def __init__(self):
        self.client = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY"),
            base_url=os.getenv("OPENAI_BASE_URL"),
        )

    def interpret(self, stats: list[dict]) -> str:
        lines = [
            f"- {k['name']}: Mean={k['mean']}, Peak={k['peak']} (am {k['peak_date']}), Trend={k['trend']}"
            for k in stats
        ]
        prompt = (
            "Du bist ein Datenanalyst. Interpretiere folgende Google Trends Kennzahlen "
            "für Supplements in Deutschland (letzter Monat). Gib konkrete Aussagen zu "
            "Trends, Peaks und Unterschieden. Antworte auf Deutsch in 3–5 Sätzen.\n\n"
            + "\n".join(lines)
        )
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
        )
        return response.choices[0].message.content