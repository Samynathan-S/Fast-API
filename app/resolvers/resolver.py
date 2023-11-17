# app/resolvers/resolver.py

from typing import List
import strawberry
from app.schema.schema import Movie, Books
from app.db.movie import movies_data
from app.db.books import books_data
# from app.db.base import engine, SessionLocal
# from app.models.type import User

@strawberry.type
class Query:
    @strawberry.field
    def movies(self) -> List[Movie]:
        return movies_data
    
    @strawberry.field
    def books(self) -> List[Books]:
        return books_data


@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_book(self, title: str, Author: str) -> Books:
        new_book = Books(title=title, Author=Author)
        books_data.append(new_book)
        return new_book

# @strawberry.field
# def get_user() -> TestTable:
#     db = SessionLocal()
#     user = db.query(User).first()
#     db.close()
#     return TestTable(user_id=user.user_id, first_name=user.first_name, last_name=user.last_name)
