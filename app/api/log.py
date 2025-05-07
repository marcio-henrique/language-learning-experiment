from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.schemas.log import LogCreate, LogResponse
from app.services.log import save_log

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/logs/", response_model=LogResponse)
def create_log(data: LogCreate, db: Session = Depends(get_db)):
    return save_log(db, data)
