from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID
from datetime import datetime

class FlashcardCreate(BaseModel):
    # id: str
    title: str
    description: str
    example_sentence: str
    example_translation: str
    question: str
    options: List[str]
    correct_answer: str
    grammar_structure_type: str
    grammar_structure_value: str
    # created_at: str
    type: str

    class Config:
        from_attributes = True


class FlashcardResponse(BaseModel):
    id: UUID
    title: str
    description: str
    example_sentence: str
    example_translation: str
    question: str
    options: List[str]
    correct_answer: str
    grammar_structure_type: Optional[str]
    grammar_structure_value: Optional[str]
    created_at: datetime
    type: str

    class Config:
        from_attributes = True


class FlashcardListResponse(BaseModel):
    flashcards: List[FlashcardResponse]