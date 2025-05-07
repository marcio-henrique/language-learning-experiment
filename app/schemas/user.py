from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime
from uuid import UUID

class UserCreate(BaseModel):
    email: EmailStr
    name: Optional[str]
    # sex: Optional[str]
    # german_level: Optional[str]
    # university_student: Optional[str]
    # university: Optional[str]
    # university_course: Optional[str]
    # university_period: Optional[str]
    # accepted_terms: Optional[datetime]

    class Config:
        from_attributes = True

class UserResponse(BaseModel):
    id: UUID
    email: EmailStr
    group: str

    class Config:
        from_attributes = True

class UserListResponse(BaseModel):
    users: List[UserResponse]
