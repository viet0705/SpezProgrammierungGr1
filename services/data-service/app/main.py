from fastapi import FastAPI

from app.routes import router

app = FastAPI(title="Google Trends Data Service")
app.include_router(router)
