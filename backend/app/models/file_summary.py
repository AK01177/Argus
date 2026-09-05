from sqlalchemy import Column, Integer, String, ForeignKey, Text
from app.db import Base

class FileSummary(Base):
    __tablename__ = "file_summaries"

    id=Column(Integer, primary_key=True, index=True)
    repo_file_id=Column(Integer, ForeignKey("repo_files.id"))
    content_hash=Column(String, index=True)
    summary=Column(Text) 