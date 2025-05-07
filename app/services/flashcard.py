from sqlalchemy.orm import Session
from sqlalchemy import desc
import random
from app.models.flashcard import Flashcard, FlashcardType
from app.schemas.flashcard import FlashcardCreate
from uuid import uuid4
from datetime import datetime

def create_flashcard(db: Session,flashcard: FlashcardCreate):
    db_flashcard = Flashcard(
        id=uuid4(),
        title=flashcard.title,
        description=flashcard.description,
        example_sentence=flashcard.example_sentence,
        example_translation=flashcard.example_translation,
        question=flashcard.question,
        options=flashcard.options,
        correct_answer=flashcard.correct_answer,
        grammar_structure_type=flashcard.grammar_structure_type,
        grammar_structure_value=flashcard.grammar_structure_value,
        type=flashcard.type,
        created_at=datetime.now()
    )
    
    db.add(db_flashcard)
    db.commit()
    db.refresh(db_flashcard)

    return db_flashcard

def get_flashcards(db: Session):
    flashcards = db.query(Flashcard).all()

    return flashcards

def get_unique_flashcards(db: Session, flashcard_type: FlashcardType, quantity: int, randomize: bool):
    query = db.query(Flashcard).filter(Flashcard.type == flashcard_type)
    
    if not randomize:
        query = query.order_by(desc(Flashcard.created_at))
    
    results = query.all()

    # Remover flashcards com grammar_structure_value duplicado
    unique = {}
    for flashcard in results:
        key = flashcard.grammar_structure_value
        if key and key not in unique:
            unique[key] = flashcard

    flashcards = list(unique.values())

    if randomize:
        random.shuffle(flashcards)

    return flashcards[:quantity]
