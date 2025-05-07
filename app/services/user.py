from app.models.flashcard import User, UserGroup
from app.schemas.user import UserCreate
from sqlalchemy.orm import Session
from uuid import uuid4
from sqlalchemy import func
from datetime import datetime
import pytz

def create_user(db: Session, user_data: UserCreate):
    # Verifica se usuário já existe
    existing = db.query(User).filter(User.email == user_data.email).first()
    if existing:
        return existing

    # Conta usuários em cada grupo
    count_a = db.query(func.count()).filter(User.group == UserGroup.A).scalar()
    count_b = db.query(func.count()).filter(User.group == UserGroup.B).scalar()

    # Decide grupo com base no menor número
    chosen_group = UserGroup.A if count_a <= count_b else UserGroup.B

    user = User(
        id=uuid4(),
        email=user_data.email,
        name=user_data.name,
        group=chosen_group,
        # sex=user_data.sex,
        # german_level=user_data.german_level,
        # university_student=user_data.university_student,
        # university=user_data.university,
        # university_course=user_data.university_course,
        # university_period=user_data.university_period,
        # accepted_terms=user_data.accepted_terms or datetime.now(pytz.timezone('America/Sao_Paulo')),
    )

    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_users(db: Session):
    users = db.query(User).all()

    return users