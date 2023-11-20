# app/schema/schema.py

import strawberry
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
class Events:
    event_id : int
    event_name : str
    event_description : str
    event_start_date : date
    event_end_date : date
    event_start_time : time
    event_end_time : time
    location_name : str
    event_type : str
    event_organizer_id : int
    meeting_link : str
    event_location_id : int
    event_status : str
 



