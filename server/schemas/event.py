from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime

class EventBase(BaseModel):
    name: str
    event_type: int  # 1 - physical test, 2 - shooting test, etc.
    start_date: date
    end_date: date
    location: str
    manager_login: str  # ID менеджера из Keycloak
    manager_fullname: str
    exercise_category: str  # e.g., "Strength", "Endurance", "Speed"
    exercise_name: str      # e.g., "Push-ups", "3km run", "100m sprint"

class EventCreate(EventBase):
    pass

class EventUpdate(BaseModel):
    name: Optional[str] = None
    event_type: Optional[int] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    location: Optional[str] = None
    exercise_category: Optional[str] = None
    exercise_name: Optional[str] = None

class Event(EventBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True
