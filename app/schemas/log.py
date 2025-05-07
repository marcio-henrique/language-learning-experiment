from pydantic import BaseModel
from typing import Optional, Dict, Any
from uuid import UUID
from datetime import datetime

class LogCreate(BaseModel):
    user_id: UUID
    timestamp_begin: datetime
    timestamp_end: Optional[datetime]
    event_type: str
    screen: Optional[str]
    html_element_id: Optional[str]
    context: Optional[Dict[str, Any]]

class LogResponse(BaseModel):
    id: UUID
    user_id: UUID
    timestamp_begin: datetime
    timestamp_end: Optional[datetime]
    event_type: str
    screen: Optional[str]
    html_element_id: Optional[str]
    context: Optional[Dict[str, Any]]
    created_at: datetime

    class Config:
        from_attributes = True
