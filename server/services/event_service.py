from sqlalchemy.orm import Session
from models.models import Event
from schemas.event import EventCreate, EventUpdate

def create_event(db: Session, event: Event) -> Event:
    """
    Create a new event and save it to the database.
    """
    db.add(event)
    db.commit()
    db.refresh(event)
    return event

def get_event_by_id(db: Session, event_id: int) -> Event:
    """
    Retrieve an event by its ID.
    """
    return db.query(Event).filter(Event.id == event_id).first()

def get_events_by_type(db: Session, event_type: int):
    """
    Retrieve all events of a specific type.
    """
    return db.query(Event).filter(Event.event_type == event_type).all()

def update_event(db: Session, event_id: int, event_update: EventUpdate) -> Event:
    """
    Update an existing event.
    """
    event = get_event_by_id(db, event_id)
    if not event:
        return None  # Or raise an exception depending on your use case

    # Update fields
    for key, value in event_update.dict(exclude_unset=True).items():
        setattr(event, key, value)

    db.commit()
    db.refresh(event)
    return event
