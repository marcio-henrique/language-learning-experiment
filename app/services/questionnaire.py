from app.models.flashcard import Questionnaire, QuestionnaireUser
from sqlalchemy.orm import Session
from uuid import uuid4
from datetime import datetime
import pytz

def create_questionnaire(db: Session, data):
    questionnaire = Questionnaire(
        id=uuid4(),
        title=data.title,
        type=data.type,
        questions=data.questions,
        created_at=datetime.now(pytz.timezone('America/Sao_Paulo'))
    )
    db.add(questionnaire)
    db.commit()
    db.refresh(questionnaire)
    return questionnaire

def save_questionnaire_answer(db: Session, data):
    answer = QuestionnaireUser(
        id=uuid4(),
        user_id=data.user_id,
        questionnaire_id=data.questionnaire_id,
        answers=data.answers,
        created_at=datetime.now(pytz.timezone('America/Sao_Paulo'))
    )
    db.add(answer)
    db.commit()
    db.refresh(answer)
    return answer

def get_latest_questionnaire_by_type(db: Session, q_type: str):
    questionnaire = (
        db.query(Questionnaire)
        .filter(Questionnaire.type == q_type)
        .order_by(Questionnaire.created_at.desc())
        .first()
    )
    return questionnaire
    # if not questionnaire:
    #     raise HTTPException(status_code=404, detail="Questionnaire not found")
    # return QuestionnaireResponse.from_orm(questionnaire)