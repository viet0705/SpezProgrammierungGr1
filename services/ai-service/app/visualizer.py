# Visualizer: Diagramme erstellen (Ranking, Peak vs. Durchschnitt, Zeitverlauf)
import io
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


class Visualizer:
    def ranking_chart(self, stats: list[dict]) -> bytes:
        # Horizontales Balkendiagramm – Ranking nach durchschnittlichem Interesse
        names = [k["name"] for k in stats]
        means = [k["mean"] for k in stats]

        fig, ax = plt.subplots(figsize=(8, 5))
        bars = ax.barh(names, means, color="steelblue")
        ax.bar_label(bars, fmt="%.1f", padding=4)
        ax.set_xlabel("Durchschnittliches Interesse (0–100)")
        ax.set_title("Supplements – Ranking nach Interesse")
        ax.invert_yaxis()
        plt.tight_layout()

        return self._to_png(fig)

    def peak_chart(self, stats: list[dict]) -> bytes:
        # Liniendiagramm – Peak vs. Durchschnitt je Keyword
        names = [k["name"] for k in stats]
        peaks = [k["peak"] for k in stats]
        means = [k["mean"] for k in stats]

        x = range(len(names))
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.plot(x, peaks, marker="o", label="Peak", color="tomato")
        ax.plot(x, means, marker="s", label="Durchschnitt", color="steelblue")
        ax.set_xticks(x)
        ax.set_xticklabels(names, rotation=15)
        ax.set_ylabel("Interesse (0–100)")
        ax.set_title("Supplements – Peak vs. Durchschnitt")
        ax.legend()
        plt.tight_layout()

        return self._to_png(fig)

    def timeseries_chart(self, timeseries: list[dict]) -> bytes:
        # Zeitverlauf – Interesse je Keyword ueber Zeit (erwartet Daten von GET /timeseries)
        # Format: [{"date": "2024-04-01", "Proteinpulver": 45, "Kreatin": 23, ...}, ...]
        if not timeseries:
            raise ValueError("Keine Zeitreihendaten vorhanden")

        dates = [d["date"] for d in timeseries]
        keywords = [k for k in timeseries[0] if k != "date"]

        fig, ax = plt.subplots(figsize=(10, 5))
        for keyword in keywords:
            values = [d[keyword] for d in timeseries]
            ax.plot(dates, values, marker="o", label=keyword)

        ax.set_xlabel("Datum")
        ax.set_ylabel("Interesse (0–100)")
        ax.set_title("Supplements – Zeitverlauf")
        ax.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()

        return self._to_png(fig)

    def _to_png(self, fig) -> bytes:
        # Diagramm als PNG-Bytes speichern und Figure schliessen
        buf = io.BytesIO()
        fig.savefig(buf, format="png")
        plt.close(fig)
        return buf.getvalue()