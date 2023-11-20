# app/resolvers/resolver.py

from typing import List
import strawberry
from app.schema.schema import Movie, Books, TestTable, Events
from app.db.movie import movies_data
from app.db.books import books_data
from app.db.base import SessionLocal
from app.models.type import User, Event

@strawberry.type
class Query:
    @strawberry.field
    def movies(self) -> List[Movie]:
        return movies_data
    
    @strawberry.field
    def books(self) -> List[Books]:
        return books_data
    
    @strawberry.field
    def get_user() -> List[TestTable]:
        db = SessionLocal()
        users: List[User] = db.query(User).all()
        db.close()

        user_list: List[TestTable] = [
            TestTable(user_id=user.user_id, first_name=user.first_name, last_name=user.last_name)
            for user in users
        ]

        return user_list
    
    @strawberry.field
    def get_events() -> List[Events]:
        db = SessionLocal()
        events: List[Event] = db.query(Event).all()
        db.close()

        event_list: List[Events] = [
            Events(
                event_id = event.event_id,
                event_name = event.event_name,
                event_description = event.event_description,
                event_start_date = event.event_start_date,
                event_end_date = event.event_end_date,
                event_start_time = event.event_start_time,
                event_end_time = event.event_end_time,
                location_name = event.location_name,
                event_type = event.event_type,
                event_organizer_id = event.event_organizer_id,
                meeting_link = event.meeting_link,
                event_location_id = event.event_location_id,
                event_status = event.event_status,
                )
            for event in events
        ]

        return event_list


@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_book(self, title: str, Author: str) -> Books:
        new_book = Books(title=title, Author=Author)
        books_data.append(new_book)
        return new_book

