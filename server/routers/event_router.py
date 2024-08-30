from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.event import EventCreate, EventUpdate, Event as EventSchema
from services import event_service
from utils.database import get_db
from typing import List

event_router = APIRouter()

@event_router.get('/events', response_model=List[EventSchema])
def get_all_events(db: Session = Depends(get_db)):
    events = event_service.get_events(db=db)
    if not events:
        raise HTTPException(status_code=404, detail="No events found in DB")
    return events

@event_router.post("/events/", response_model=EventSchema)
def create_event(event_data: EventCreate, db: Session = Depends(get_db)):
    """Create a new event"""
    event = event_service.create_event(db, event_data)
    return event

@event_router.get("/events/{event_id}", response_model=EventSchema)
def get_event(event_id: int, db: Session = Depends(get_db)):
    """Get an event by its ID"""
    event = event_service.get_event_by_id(db, event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event

@event_router.get("/events/type/{event_type}", response_model=list[EventSchema])
def get_events_by_type(event_type: int, db: Session = Depends(get_db)):
    """Get all events of a specific type"""
    events = event_service.get_events_by_type(db, event_type)
    if not events:
        raise HTTPException(status_code=404, detail="No events found for this type")
    return events

@event_router.put("/events/{event_id}", response_model=EventSchema)
def update_event(event_id: int, event_update: EventUpdate, db: Session = Depends(get_db)):
    """Update an existing event"""
    updated_event = event_service.update_event(db, event_id, event_update)
    if not updated_event:
        raise HTTPException(status_code=404, detail="Event not found")
    return updated_event

@event_router.delete("/events/{event_id}", response_model=None)
def delete_event(event_id: int, db: Session = Depends(get_db)):
    """Delete an event by its ID"""
    event_service.delete_event(db, event_id)
    return {"detail": "Event deleted successfully"}
