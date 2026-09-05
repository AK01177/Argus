import os
import shutil
import hashlib
from sqlalchemy.orm import Session

from app.domain.ingestion import clone_repo_to_temp
from app.domain.tree_walker import get_files_to_parse
from app.providers.llm import GeminiProvider
from app.repositories.repo_repositories import RepoRepository

from app.models.repo_file import RepoFile
from app.models.file_summary import FileSummary

class IngestionService:
    def __init__(self, db:Session):
        self.db=db
        self.repo_repo=RepoRepository(db)
        self.llm=GeminiProvider()

    def process_repo(self, repo_id: int):
        repo=self.repo_repo.get_repo_by_id(repo_id)
        if not repo:
            print("Repo not found") 
            return

        temp_dir=None
        try:
            temp_dir=clone_repo_to_temp(repo.url)
            valid_files=get_files_to_parse(temp_dir)

            for file_path in valid_files:
                rel_path = os.path.relpath(file_path, temp_dir)
                with open(file_path, "r", encoding="utf-8",errors="ignore") as f:
                    content=f.read()

                content_hash=hashlib.sha256(content.encode("utf-8")).hexdigest()

                existing_file=self.db.query(RepoFile).filter(
                    RepoFile.repo_id == repo.id,
                    RepoFile.path == rel_path
                ).first()

                if existing_file:
                    print(f"Skipping {rel_path}, already exists!")
                    continue

                repo_file=RepoFile(repo_id=repo.id, path=rel_path, content_hash=content_hash)
                self.db.add(repo_file)
                self.db.flush()

                summary_text=self.llm.summarize_file(rel_path, content)

                file_summary=FileSummary(
                    repo_file_id=repo_file.id,
                    content_hash=content_hash,
                    summary=summary_text
                )
                self.db.add(file_summary)
                self.db.commit()
                import time
                time.sleep(15)
            print("Ingestion Complete")

        except Exception as e:
            self.db.rollback()
            print(f"Failed to process the Repo : {e}")
        finally:
            if temp_dir and os.path.exists(temp_dir):
                shutil.rmtree(temp_dir)