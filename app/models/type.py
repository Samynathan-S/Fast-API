# app/models/type.py
from sqlalchemy import Column, String, Integer, Date, Time
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class MovieModel(Base):
    __tablename__ = "movies"
    id = Column(String, primary_key=True, index=True)
    title = Column(String)
    director = Column(String)

class BookModel(Base):
    __tablename__ = "books"
    id = Column(String, primary_key=True, index=True)
    title = Column(String)
    author = Column(String)

class User(Base):
    __tablename__ = "testtable"  
    __table_args__ = {"schema": "event_management"}  

    user_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)

class Event(Base):
    __tablename__ = "events"  
    __table_args__ = {"schema": "event_management"}  

    event_id = Column(Integer, primary_key=True, index=True)
    event_name = Column(String, nullable=False)
    event_description = Column(String, nullable=False)
    event_start_date = Column(Date, nullable=False)
    event_end_date = Column(Date, nullable=False)
    event_start_time = Column(Time, nullable=False)
    event_end_time = Column(Time, nullable=False)
    location_name = Column(String, nullable=False)
    event_type = Column(String, nullable=False)
    event_organizer_id = Column(Integer , nullable=False)
    meeting_link = Column(String, nullable=False)
    event_location_id = Column(Integer , nullable=False)
    event_status = Column(String, nullable=False)
