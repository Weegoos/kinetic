from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from models.event_result import EventResult
from models.user import User
from schemas.event_result import EventResultCreate, EventResultUpdate
from typing import List


def get_event_results(db: Session) -> List[EventResult]:
    """
    Get all user event results from DB
    """
    event_results = db.query(EventResult).all()
    if not event_results:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Event results not found in DB"
        )
    return event_results

def create_event_result(db: Session, event_result_data: EventResultCreate) -> EventResult:
    """
    Create a new event result and save it to the database.
    """
    new_event_result = EventResult(**event_result_data.dict())
    db.add(new_event_result)
    db.commit()
    db.refresh(new_event_result)
    return new_event_result


def get_event_result_by_id(db: Session, event_result_id: int) -> EventResult:
    """
    Retrieve an event result by its ID.
    """
    event_result = db.query(EventResult).filter(EventResult.id == event_result_id).first()
    if event_result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Event result with ID {event_result_id} not found",
        )
    return event_result


def get_event_results_by_user_login(db: Session, user_login: str) -> list[EventResult]:
    """
    Retrieve all event results for a specific user login.
    """
    event_results = db.query(EventResult).filter(EventResult.user_login == user_login).all()
    if not event_results:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No event results found for user with login {user_login}",
        )
    return event_results


def get_event_results_by_user_iin(db: Session, iin: str) -> list[EventResult]:
    """
    Retrieve all event results for a specific user IIN.
    """
    event_results = db.query(EventResult).join(EventResult.user).filter(User.iin == iin).all()
    if not event_results:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No event results found for user with IIN {iin}",
        )
    return event_results


def update_event_result(db: Session, event_result_id: int, event_result_update: EventResultUpdate) -> EventResult:
    """
    Update an existing event result.
    """
    event_result = get_event_result_by_id(db, event_result_id)
    if not event_result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Event result with ID {event_result_id} not found",
        )

    # Update fields using the dictionary method, exclude_unset=True to ignore fields not provided
    update_data = event_result_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(event_result, key, value)

    db.commit()
    db.refresh(event_result)
    return event_result


def delete_event_result(db: Session, event_result_id: int) -> None:
    """
    Delete an event result by its ID.
    """
    event_result = get_event_result_by_id(db, event_result_id)
    if not event_result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Event result with ID {event_result_id} not found",
        )
    
    db.delete(event_result)
    db.commit()
