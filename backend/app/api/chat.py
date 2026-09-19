
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel

from app.db import get_db
from app.models.code_chunk import CodeChunk
from app.models.repo_file import RepoFile
from app.providers.llm import GeminiProvider

router = APIRouter()

class ChatRequest(BaseModel):
    repo_id: int
    question: str

@router.post("/")
def chat_with_repo(request: ChatRequest, db: Session = Depends(get_db)):
    llm = GeminiProvider()

    question_embedding = llm.embed_text(request.question)


    closest_chunks = (
        db.query(CodeChunk)
        .join(RepoFile, CodeChunk.repo_file_id == RepoFile.id)
        .filter(RepoFile.repo_id == request.repo_id)
        .order_by(CodeChunk.embedding.cosine_distance(question_embedding))
        .limit(5)
        .all()
    )

    if not closest_chunks:
        return {"answer": "I couldn't find any code in this repository to answer that."}

    context_texts = [chunk.code_content for chunk in closest_chunks]

    answer= llm.answer_question(request.question, context_texts)

    return {"answer": answer}

