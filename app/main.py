from fastapi import FastAPI
from app.models.base import Base
from app.db import engine
from app.api import flashcards, users, flashcard_user, questionnaires, log
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(flashcards.router)
app.include_router(flashcard_user.router)
app.include_router(users.router)
app.include_router(questionnaires.router)
app.include_router(log.router
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)