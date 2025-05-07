from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.schemas.questionnaire import (
    QuestionnaireCreate, QuestionnaireResponse,
    QuestionnaireAnswerCreate, QuestionnaireAnswerResponse
)
from app.services.questionnaire import create_questionnaire, save_questionnaire_answer, get_latest_questionnaire_by_type

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/questionnaires/", response_model=QuestionnaireResponse)
def create_questionnaire_endpoint(data: QuestionnaireCreate, db: Session = Depends(get_db)):
    return create_questionnaire(db, data)

@router.post("/questionnaires/answer/", response_model=QuestionnaireAnswerResponse)
def answer_questionnaire_endpoint(data: QuestionnaireAnswerCreate, db: Session = Depends(get_db)):
    return save_questionnaire_answer(db, data)

@router.get("/questionnaires/latest", response_model=QuestionnaireResponse)
def get_latest_questionnaire(type: str, db: Session = Depends(get_db)):
    last_questionnaire = get_latest_questionnaire_by_type(db, type)
    return last_questionnaire