from fastapi import APIRouter, UploadFile, File, Request, Depends, Query
from sqlalchemy.orm import Session
from app.schemas.flashcard import FlashcardCreate, FlashcardResponse, FlashcardListResponse
from app.services.flashcard import create_flashcard, get_flashcards, get_unique_flashcards
from fastapi.responses import JSONResponse
from app.generator import process_text
from typing import Optional, List
from app.models.flashcard import FlashcardType
from app.db import SessionLocal
import logging

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter()

@router.post("/flashcards/", response_model=FlashcardResponse)
async def create_flashcard_endpoint(flashcard: FlashcardCreate, db: Session = Depends(get_db)):
    return create_flashcard(db, flashcard)

@router.get("/flashcards/", response_model=FlashcardListResponse)
async def get_flashcards_endpoint(db: Session = Depends(get_db)):
    flashcards = get_flashcards(db)
    flashcards_response = [FlashcardResponse.from_orm(fc) for fc in flashcards]
    return FlashcardListResponse(flashcards=flashcards_response)

@router.get("/flashcards/custom/", response_model=FlashcardListResponse)
def get_custom_flashcards(
    auto_flashcards: int = Query(0, ge=0),
    auto_flashcards_rand: bool = Query(False),
    manual_flashcards: int = Query(0, ge=0),
    manual_flashcards_rand: bool = Query(False),
    db: Session = Depends(get_db)
):
    manual = get_unique_flashcards(db, FlashcardType.MANUAL, manual_flashcards, manual_flashcards_rand)
    auto = get_unique_flashcards(db, FlashcardType.AUTOMATIC, auto_flashcards, auto_flashcards_rand)
    
    total = manual + auto
    return FlashcardListResponse(
        flashcards=[FlashcardResponse.from_orm(f) for f in total]
    )

@router.post("/generate-flashcards/")
async def generate_flashcards(
    request: Request,
    file: Optional[UploadFile] = File(None)
):
    if file is not None:
        content = await file.read()
        text = content.decode('utf-8')
    else:
        try:
            body = await request.json()
            text = body.get("text", None)
            if text is None:
                return JSONResponse(
                    status_code=400,
                    content={"error": "JSON inválido. Esperado campo 'text'."}
                )
        except Exception:
            return JSONResponse(
                status_code=400,
                content={"error": "Corpo inválido. Envie um arquivo .txt ou JSON com campo 'text'."}
            )


    flashcards = process_text(text)
    return {"flashcards": flashcards}