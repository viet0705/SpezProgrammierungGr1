from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="AI Analysis Service")
app.include_router(router)
