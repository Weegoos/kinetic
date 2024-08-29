from fastapi import APIRouter, Depends, HTTPException, Response, Request
from sqlalchemy.orm import Session
from models.models import Event
from utils.database import get_db
from services import event_service
from schemas.event import EventCreate, Event as EventSchema, EventUpdate
import jwt

event_router = APIRouter()

# Эндпоинт для создания события
@event_router.post("/events/", response_model=EventSchema)
def create_event(event_data: EventCreate, req: Request, db: Session = Depends(get_db)):
    """Creates event"""
    
    access_token = req.cookies.get('access_token')
    if not access_token:
        raise HTTPException(status_code=404, detail="No access token found")
    
    decoded_token = jwt.decode(access_token, options={"verify_signature": False})
    
    user_login = decoded_token.get("preferred_username")
    user_fullname = decoded_token.get("name")
    
    
    event = Event(
        name=event_data.name,
        event_type=event_data.event_type,
        start_date=event_data.start_date,
        end_date=event_data.end_date,
        location=event_data.location,
        manager_login=user_login,
        manager_fullname=user_fullname
    )
    
    created_event = event_service.create_event(db, event)
    return created_event

# Эндпоинт для получения всех событий по типу
@event_router.get("/events/{event_type}", response_model=list[EventSchema])
def get_events_by_type(event_type: int, db: Session = Depends(get_db)):
    events = event_service.get_events_by_type(db, event_type)
    if not events:
        raise HTTPException(status_code=404, detail="Events not found")
    return events

# Эндпоинт для обновления события
@event_router.put("/events/{event_id}", response_model=EventSchema)
def update_event(event_id: int, event_data: EventUpdate, db: Session = Depends(get_db)):
    event = event_service.get_event_by_id(db, event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    
    for key, value in event_data.model_dump(exclude_unset=True).items():
        setattr(event, key, value)
    
    db.commit()
    db.refresh(event)
    return event
