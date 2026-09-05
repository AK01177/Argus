from sqlalchemy.orm import Session
from app.models.repo import Repo
from app.models.repo_file import RepoFile
from app.models.file_summary import FileSummary

class RepoRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_repo_by_id(self, repo_id: int) -> Repo | None:
        return self.db.query(Repo).filter(Repo.id == repo_id).first()

    def get_repo_files(self, repo_id: int) -> list[RepoFile]:
        return self.db.query(RepoFile).filter(RepoFile.repo_id == repo_id).all()

    def get_file_summary(self, repo_file_id: int, content_hash: str) -> FileSummary | None:
        return self.db.query(FileSummary).filter(
            FileSummary.repo_file_id == repo_file_id,
            FileSummary.content_hash == content_hash
        ).first()
