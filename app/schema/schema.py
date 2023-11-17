# app/schema/schema.py

import strawberry

@strawberry.type
class Movie:
    title: str
    director: str

@strawberry.type
class Books:
    title: str
    Author: str

# @strawberry.type
# class TestTable:
#     user_id: int
#     first_name: str
#     last_name: str

