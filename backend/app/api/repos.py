from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db import get_db
from app.repositories.repo_repositories import RepoRepository

router = APIRouter()

@router.get("/{repo_id}/tree")
def get_repo_tree(repo_id : int, db: Session= Depends(get_db)):
    repo_repo= RepoRepository(db)

    repo=repo_repo.get_repo_by_id(repo_id)
    if not repo:
        raise HTTPException(status_code="404", detail="Repo Not Found")

    files= repo_repo.get_repo_files(repo_id)

    response_data=[]
    for f in files:
        summary=repo_repo.get_file_summary(f.id, f.content_hash)

        response_data.append({
            "path": f.path,
            "summary": summary.summary if summary else None
        }
        )

    return {"repo id": repo_id, "files": response_data} 