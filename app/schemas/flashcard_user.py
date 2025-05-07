from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class FlashcardUserCreate(BaseModel):
    user_id: UUID
    flashcard_id: UUID
    answer: str

class FlashcardUserResponse(BaseModel):
    id: UUID
    user_id: UUID
    flashcard_id: UUID
    answer: str
    correct_answer: str
    created_at: datetime

    class Config:
        from_attributes = True
