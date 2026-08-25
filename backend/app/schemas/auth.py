from pydantic import BaseModel

class TokenRequest(BaseModel):
    github_pat: str