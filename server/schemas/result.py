from pydantic import BaseModel, Field
from typing import Optional
from datetime import date, datetime

class TestResultBase(BaseModel):
    user_id: str  # ID пользователя из Keycloak
    event_id: int
    score: int

class TestResultCreate(TestResultBase):
    pass

class TestResult(TestResultBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True