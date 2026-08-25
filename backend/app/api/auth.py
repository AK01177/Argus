from fastapi import APIRouter, HTTPException
from app.schemas.auth import TokenRequest

router=APIRouter()

@router.post("/pat")
def save_github_token(request: TokenRequest):
    if not request.github_pat.startswith("ghp_") and not request.github_pat.startswith("github_pat_"):
        raise HTTPException(status_code=400, detail="Invalid Github PAT format")

    return{"status":"success", "message":"Token Saved Successfully"}