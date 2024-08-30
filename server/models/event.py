from sqlalchemy import Column, Integer, String, Date, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from models.base import Base

class Event(Base):
    __tablename__ = 'events'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    event_type = Column(Integer, nullable=False, default=1)  # 1 - физический тест, 2 - стрельба, и т.д.
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    location = Column(String, nullable=False)
    manager_login = Column(String, nullable=False)
    manager_fullname = Column(String, nullable=False)
    
    exercise_category = Column(String, nullable=False)  # "Сила", "Выносливость", "Скорость"
    exercise_name = Column(String, nullable=False)      # "Отжимания", "3км бег", "100м спринт"
    
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    event_results = relationship('EventResult', back_populates='event', cascade='all, delete-orphan')