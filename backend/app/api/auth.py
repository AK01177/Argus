from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.schemas.auth import TokenRequest
from app.db import get_db
from app.models.user import User

router=APIRouter()

@router.post("/pat")
def save_github_token(request: TokenRequest, db: Session=Depends(get_db)):
    if not request.github_pat.startswith("ghp_") and not request.github_pat.startswith("github_pat_"):
        raise HTTPException(status_code=400, detail="Invalid Github PAT format")

    existing_user=db.query(User).filter(User.username==request.username).first()

    if existing_user:
        existing_user.github_token=request.github_pat
        db.commit()
        return{"status": "Success", "message": "Updating existing user's Token"}
    else:
        new_user=User(username=request.username, github_token=request.github_pat)
        db.add(new_user)
        db.commit()
        return{"status": "Success", "message": "Created new user and saved token"}