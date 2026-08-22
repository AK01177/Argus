from fastapi import FastAPI
from app.config import settings

app=FastAPI(
    title=settings.PROJECT_NAME,
    description="Repo Companion",
    version="0.0.1"
)

@app.get("/health")
def health_check():
    return{
        "kesa_hai": "badhiya",
        "project": settings.PROJECT_NAME,
        "environment": settings.ENVIRONMENT
    }