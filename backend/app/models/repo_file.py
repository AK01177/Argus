from sqlalchemy import Column, ForeignKey, Integer, String

from app.db import Base


class RepoFile(Base):
    __tablename__="repo_files"
    id=Column(Integer, primary_key=True, index=True)
    repo_id=Column(Integer, ForeignKey("repos.id"))
    path=Column(String, index=True)
    content_hash=Column(String)
