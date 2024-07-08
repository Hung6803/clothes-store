from typing import Optional
from sqlalchemy.orm import Session
from app.account import model

def verify_email_exist(email: str, db_session: Session) -> Optional[model.Account]:
    return db_session.query(model.Account).get(email)
