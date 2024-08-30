from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime

class EventResultBase(BaseModel):
    user_login: str
    user_fullname: str
    user_iin: Optional[str]
    event_id: int
    score: int
    evaluator_login: str
    evaluator_fullname: str
    evaluated_at: Optional[datetime]

class EventResultCreate(EventResultBase):
    pass

class EventResultUpdate(BaseModel):
    user_login: Optional[str]
    user_iin: Optional[str]
    event_id: Optional[int]
    score: Optional[int]
    evaluator_login: Optional[str]
    evaluator_fullname: Optional[str]
    evaluated_at: Optional[datetime]