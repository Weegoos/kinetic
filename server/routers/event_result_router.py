from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from schemas.event_result import EventResultCreate, EventResultUpdate, EventResultBase
from services import event_result_service
from utils.database import get_db

event_result_router = APIRouter()

# Endpoint to get all event results
@event_result_router.get('/event_results', response_model=list[EventResultBase])
def get_all_event_results(db: Session = Depends(get_db)):
    """Get all event results from DB"""
    event_results = event_result_service.get_event_results(db)
    return event_results

# Endpoint to create a new event result
@event_result_router.post("/event_results", response_model=EventResultBase)
def create_event_result(event_result_data: EventResultCreate, db: Session = Depends(get_db)):
    """Create a new event result"""
    event_result = event_result_service.create_event_result(db, event_result_data)
    return event_result 

# Endpoint to retrieve an event result by its ID
@event_result_router.get("/event_results/{event_result_id}", response_model=EventResultBase)
def get_event_result_by_id(event_result_id: int, db: Session = Depends(get_db)):
    """Get an event result by its ID"""
    event_result = event_result_service.get_event_result_by_id(db, event_result_id)
    if not event_result:
        raise HTTPException(status_code=404, detail="EventResult not found")
    return event_result

# Endpoint to retrieve all event results for a specific user by their IIN
@event_result_router.get("/event_results/user/{user_iin}", response_model=list[EventResultBase])
def get_event_results_by_user_iin(user_iin: str, db: Session = Depends(get_db)):
    """Get all event results for a specific user by their IIN"""
    event_results = event_result_service.get_event_results_by_user_iin(db, user_iin)
    if not event_results:
        raise HTTPException(status_code=404, detail="No event results found for this user")
    return event_results

# Endpoint to update an existing event result
@event_result_router.put("/event_results/{event_result_id}", response_model=EventResultBase)
def update_event_result(event_result_id: int, event_result_update: EventResultUpdate, db: Session = Depends(get_db)):
    """Update an existing event result"""
    updated_event_result = event_result_service.update_event_result(db, event_result_id, event_result_update)
    if not updated_event_result:
        raise HTTPException(status_code=404, detail="EventResult not found")
    return updated_event_result

# Endpoint to delete an event result
@event_result_router.delete("/event_results/{event_result_id}", response_model=None)
def delete_event_result(event_result_id: int, db: Session = Depends(get_db)):
    """Delete an event result by its ID"""
    event_result_service.delete_event_result(db, event_result_id)
    return {"detail": "EventResult deleted successfully"}

# Endpoint to retrieve all event results evaluated by a specific evaluator
@event_result_router.get("/event_results/evaluator/{evaluator_login}", response_model=list[EventResultBase])
def get_event_results_by_evaluator(evaluator_login: str, db: Session = Depends(get_db)):
    """Get all event results evaluated by a specific evaluator"""
    event_results = event_result_service.get_event_results_by_evaluator(db, evaluator_login)
    if not event_results:
        raise HTTPException(status_code=404, detail="No event results found for this evaluator")
    return event_results
