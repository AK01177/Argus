from fastapi import FastAPI
from app.config import settings
from app.api.auth import router as auth_router

app=FastAPI(
    title=settings.PROJECT_NAME,
    description="Repo Companion",
    version="0.0.1"
)

app.include_router(auth_router, prefix="/api/auth", tags=["Auth"])

@app.get("/health")
def health_check():
    return{
        "kesa_hai": "badhiya",
        "project": settings.PROJECT_NAME,
        "environment": settings.ENVIRONMENT
    }