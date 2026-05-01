# Temporaeres Testskript – nicht fuer Produktion
import os
from pathlib import Path

# .env aus dem Root-Verzeichnis laden
env_path = Path(__file__).parent.parent.parent / ".env"
if env_path.exists():
    for line in env_path.read_text().splitlines():
        if "=" in line and not line.startswith("#"):
            key, val = line.split("=", 1)
            os.environ.setdefault(key.strip(), val.strip())

from app.fetcher import DataFetcher
from app.interpreter import Interpreter

print("=== DataFetcher ===")
stats = DataFetcher().get_stats()
for s in stats:
    print(s)

print("\n=== Interpreter ===")
result = Interpreter().interpret(stats)
print(result)