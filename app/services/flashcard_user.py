from app.models.flashcard import FlashcardUser, Flashcard
from sqlalchemy.orm import Session
from uuid import uuid4
from app.schemas.flashcard_user import FlashcardUserCreate
from datetime import datetime
import pytz

def save_flashcard_response(db: Session, data: FlashcardUserCreate):
    flashcard = db.query(Flashcard).filter(Flashcard.id == data.flashcard_id).first()
    if not flashcard:
        raise ValueError("Flashcard não encontrado.")

    record = FlashcardUser(
        id=uuid4(),
        user_id=data.user_id,
        flashcard_id=data.flashcard_id,
        answer=data.answer,
        correct_answer=flashcard.correct_answer,
        created_at=datetime.now(pytz.timezone('America/Sao_Paulo'))
    )

    db.add(record)
    db.commit()
    db.refresh(record)
    return record
