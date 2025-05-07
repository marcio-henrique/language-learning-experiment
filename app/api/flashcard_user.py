from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.schemas.flashcard_user import FlashcardUserCreate, FlashcardUserResponse
from app.services.flashcard_user import save_flashcard_response

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/flashcards/answer/", response_model=FlashcardUserResponse)
def answer_flashcard(data: FlashcardUserCreate, db: Session = Depends(get_db)):
    try:
        return save_flashcard_response(db, data)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
