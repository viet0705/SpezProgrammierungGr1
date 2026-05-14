import os
from pathlib import Path
from fastapi import FastAPI

# .env aus dem Root-Verzeichnis laden (nur für lokale Entwicklung ohne Docker)
env_path = Path(__file__).parent.parent.parent.parent / ".env"
if env_path.exists():
    for line in env_path.read_text().splitlines():
        if "=" in line and not line.startswith("#"):
            key, val = line.split("=", 1)
            os.environ.setdefault(key.strip(), val.strip())

from app.routes import router

app = FastAPI(title="AI Analysis Service")
app.include_router(router)