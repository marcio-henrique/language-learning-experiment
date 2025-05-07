from app.models.flashcard import LogUser
from sqlalchemy.orm import Session
from uuid import uuid4
from datetime import datetime
import pytz

def save_log(db: Session, data):
    log = LogUser(
        id=uuid4(),
        user_id=data.user_id,
        timestamp_begin=data.timestamp_begin,
        timestamp_end=data.timestamp_end,
        event_type=data.event_type,
        screen=data.screen,
        html_element_id=data.html_element_id,
        context=data.context,
        created_at=datetime.now(pytz.timezone('America/Sao_Paulo'))
    )
    db.add(log)
    db.commit()
    db.refresh(log)
    return log
