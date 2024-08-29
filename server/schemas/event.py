from pydantic import BaseModel, Field
from typing import Optional
from datetime import date, datetime

class EventBase(BaseModel):
    name: str
    event_type: int  # 1 - physical test, 2 - shooting test, 3... - other test
    start_date: date
    end_date: date
    location: str
    manager_id: str  # ID менеджера из Keycloak

class EventCreate(EventBase):
    pass

class EventUpdate(BaseModel):
    name: Optional[str] = None
    event_type: Optional[int] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    location: Optional[str] = None

class Event(EventBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True


