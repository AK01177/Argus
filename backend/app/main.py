from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.auth import router as auth_router
from app.config import settings

app=FastAPI(
    title=settings.PROJECT_NAME,
    description="Repo Companion",
    version="0.0.1"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix="/api/auth", tags=["Auth"])

@app.get("/health")
def health_check():
    return{
        "kesa_hai": "badhiya",
        "project": settings.PROJECT_NAME,
        "environment": settings.ENVIRONMENT
    }