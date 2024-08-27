from sqlalchemy import Column, Integer, String, Date, ForeignKey, DateTime, func, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Event(Base):
    __tablename__ = 'events'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    event_type = Column(Integer, nullable=False)  # 1 - physical test, 2 - shooting test, 3... - other test
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    location = Column(String, nullable=False)
    manager_id = Column(String, nullable=False)  # ID менеджера из Keycloak
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    test_results = relationship('TestResult', back_populates='event')

class TestResult(Base):
    __tablename__ = 'test_results'
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, nullable=False)  # ID пользователя из Keycloak
    event_id = Column(Integer, ForeignKey('events.id'))
    score = Column(Integer, nullable=False)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    event = relationship('Event', back_populates='test_results')
    