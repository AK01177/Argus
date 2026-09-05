from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.sql import func

from app.db import Base


class Repo(Base):
    __tablename__ = "repos"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    name = Column(String, index=True)
    url = Column(String, unique=True)
    is_private = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
