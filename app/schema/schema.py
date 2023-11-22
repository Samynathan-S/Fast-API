# app/schema/schema.py

import strawberry
from typing import Optional
from datetime import date, time

@strawberry.type
class Movie:
    title: str
    director: str

@strawberry.type
class Books:
    title: str
    Author: str

@strawberry.type
class TestTable:
    user_id: int
    first_name: str
    last_name: str

@strawberry.type
class EMsEventsType:
    event_id : strawberry.ID
    event_name : str
    event_description : str
    event_start_date : date
    event_end_date : date
    event_start_time : time
    event_end_time : time
    location_name : Optional[str]
    event_type : str
    event_organizer_id : int
    meeting_link : Optional[str]
    event_location_id : Optional[str]
    event_status : str

@strawberry.type
class EmsUserType:
    first_name : str
    last_name : str
    user_role : str
    user_id: strawberry.ID
    email_id : str
    image: Optional[str]



