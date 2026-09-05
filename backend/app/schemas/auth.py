from pydantic import BaseModel


class TokenRequest(BaseModel):
    username: str
    github_pat: str
