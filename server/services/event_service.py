from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from models.event import Event
from typing import List
from schemas.event import EventCreate, EventUpdate

def get_events(db: Session) -> List[Event]:
    """
    Get all events, which located in DB
    """
    events = db.query(Event).all()
    if not events:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No events found in DB",
        )
    return events

def create_event(db: Session, event_data: EventCreate) -> Event:
    """
    Create a new event and save it to the database.
    """
    new_event = Event(**event_data.dict())
    db.add(new_event)
    db.commit()
    db.refresh(new_event)
    return new_event

def get_event_by_id(db: Session, event_id: int) -> Event:
    """
    Retrieve an event by its ID.
    """
    event = db.query(Event).filter(Event.id == event_id).first()
    if event is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Event with ID {event_id} not found",
        )
    return event

def get_events_by_type(db: Session, event_type: int) -> list[Event]:
    """
    Retrieve all events of a specific type.
    """
    events = db.query(Event).filter(Event.event_type == event_type).all()
    if not events:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No events found for event type {event_type}",
        )
    return events

def update_event(db: Session, event_id: int, event_update: EventUpdate) -> Event:
    """
    Update an existing event.
    """
    event = get_event_by_id(db, event_id)
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Event with ID {event_id} not found",
        )

    update_data = event_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(event, key, value)

    db.commit()
    db.refresh(event)
    return event

def delete_event(db: Session, event_id: int) -> None:
    """
    Delete an event by its ID.
    """
    event = get_event_by_id(db, event_id)
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Event with ID {event_id} not found",
        )
    
    db.delete(event)
    db.commit()
