from pydantic import BaseModel
from typing import List, Dict, Any
from uuid import UUID
from datetime import datetime

class QuestionnaireCreate(BaseModel):
    title: str
    type: str  # "evaluation" ou "perception"
    questions: List[Dict[str, Any]]

class QuestionnaireResponse(BaseModel):
    id: UUID
    title: str
    type: str
    questions: List[Dict[str, Any]]
    created_at: datetime

    class Config:
        from_attributes = True

class QuestionnaireAnswerCreate(BaseModel):
    user_id: UUID
    questionnaire_id: UUID
    answers: Dict[str, Any]

class QuestionnaireAnswerResponse(BaseModel):
    id: UUID
    user_id: UUID
    questionnaire_id: UUID
    answers: Dict[str, Any]
    created_at: datetime

    class Config:
        from_attributes = True
