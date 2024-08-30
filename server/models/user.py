from sqlalchemy import Column, Integer, String, Date, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from models.base import Base

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    iin = Column(String, nullable=False, unique=True)
    
    event_results = relationship('EventResult', back_populates='user', cascade='all, delete-orphan')