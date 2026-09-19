from sqlalchemy import Column, ForeignKey, Integer, String
from pgvector.sqlalchemy import Vector
from app.db import Base

class CodeChunk(Base):
    __tablename__ = "code_chunks"

    id= Column(Integer, primary_key=True, index=True)
    repo_file_id= Column(Integer, ForeignKey("repo_files.id"), nullable=False)

    code_content=Column(String, nullable=False)

    embedding= Column(Vector(768))