from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.schemas.user import UserCreate, UserResponse, UserListResponse
from app.services.user import create_user, get_users

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/users/", response_model=UserResponse)
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)


@router.get("/users/", response_model=UserListResponse)
async def get_users_endpoint(db: Session = Depends(get_db)):
    users = get_users(db)
    users_response = [UserResponse.from_orm(u) for u in users]
    return UserListResponse(users=users_response)
