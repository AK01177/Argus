from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.sql import func

from app.db import Base


class Job(Base):
    __tablename__ = "jobs"
    id=Column(Integer, primary_key=True, index=True)
    repo_id=Column(Integer, ForeignKey("repos.id"))
    status=Column(String, default="pending")
    created_at=Column(DateTime(timezone=True), server_default=func.now())
    finished_at=Column(DateTime(timezone=True), nullable=True)