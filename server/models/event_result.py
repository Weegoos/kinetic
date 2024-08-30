from sqlalchemy import Column, Integer, String, Date, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from models.base import Base

class EventResult(Base):
    __tablename__ = 'event_results'
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user_login = Column(String, nullable=False)
    user_fullname = Column(String, nullable=False)
    user_iin = Column(String, nullable=True)
    event_id = Column(Integer, ForeignKey('events.id'))
    score = Column(Integer, nullable=False)
    evaluator_login = Column(String, nullable=False)
    evaluator_fullname = Column(String, nullable=False)
    
    evaluated_at = Column(DateTime(timezone=True), nullable=True)
    created_at = Column(DateTime(timezone=True), default=func.now())
    
    user = relationship('User', back_populates='event_results')
    event = relationship('Event', back_populates='event_results')
