from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Text, Enum, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from datetime import datetime
import enum
import uuid
import pytz

from app.models.base import Base

# from sqlalchemy.ext.declarative import declarative_base
# Base = declarative_base()


class UserGroup(enum.Enum):
    A = "A"
    B = "B"

class FlashcardType(str, enum.Enum):
    MANUAL = "Manual"
    AUTOMATIC = "Automatic"

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String)
    name = Column(String)
    sex = Column(String)
    german_level = Column(String)
    university_student = Column(String)
    university = Column(String)
    university_course = Column(String)
    university_period = Column(String)
    group = Column(Enum(UserGroup), nullable=False)
    accepted_terms = Column(DateTime)
    created_at = Column(DateTime, default=datetime.now(pytz.timezone('America/Sao_Paulo')))

    flashcards_user = relationship("FlashcardUser", back_populates="user")
    questionnaires_user = relationship("QuestionnaireUser", back_populates="user")
    logs = relationship("LogUser", back_populates="user")

class Flashcard(Base):
    __tablename__ = "flashcards"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String)
    description = Column(Text)
    example_sentence = Column(Text)
    example_translation = Column(Text)
    question = Column(Text)
    options = Column(JSON)
    correct_answer = Column(String)

    grammar_structure_type = Column(String)
    grammar_structure_value = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

    type = Column(Enum(FlashcardType), nullable=False, default=FlashcardType.AUTOMATIC)

    flashcards_user = relationship("FlashcardUser", back_populates="flashcard")

class FlashcardUser(Base):
    __tablename__ = "flashcards_user"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    flashcard_id = Column(UUID(as_uuid=True), ForeignKey("flashcards.id"))
    answer = Column(String)
    correct_answer = Column(String)
    created_at = Column(DateTime, default=datetime.now(pytz.timezone('America/Sao_Paulo')))

    user = relationship("User", back_populates="flashcards_user")
    flashcard = relationship("Flashcard", back_populates="flashcards_user")

class Questionnaire(Base):
    __tablename__ = "questionnaires"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String)
    type = Column(String)  # ex: "validacao", "percepcao"
    questions = Column(JSON)
    created_at = Column(DateTime, default=datetime.now(pytz.timezone('America/Sao_Paulo')))

    questionnaires_user = relationship("QuestionnaireUser", back_populates="questionnaire")

class QuestionnaireUser(Base):
    __tablename__ = "questionnaires_user"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    questionnaire_id = Column(UUID(as_uuid=True), ForeignKey("questionnaires.id"))
    answers = Column(JSON)
    created_at = Column(DateTime, default=datetime.now(pytz.timezone('America/Sao_Paulo')))

    user = relationship("User", back_populates="questionnaires_user")
    questionnaire = relationship("Questionnaire", back_populates="questionnaires_user")

class EducationalText(Base):
    __tablename__ = "educational_texts"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String)
    content = Column(Text)
    created_at = Column(DateTime, default=datetime.now(pytz.timezone('America/Sao_Paulo')))

class EducationalTextUser(Base):
    __tablename__ = "educational_texts_user"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    educational_text_id = Column(UUID(as_uuid=True), ForeignKey("educational_texts.id"))
    created_at = Column(DateTime, default=datetime.now(pytz.timezone('America/Sao_Paulo')))

class LogUser(Base):
    __tablename__ = "logs_user"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    timestamp_begin = Column(DateTime, nullable=False)
    timestamp_end = Column(DateTime)
    event_type = Column(String, nullable=False)
    screen = Column(String)
    html_element_id = Column(String)
    context = Column(JSON)
    created_at = Column(DateTime, default=datetime.now(pytz.timezone('America/Sao_Paulo')))

    user = relationship("User", back_populates="logs")
