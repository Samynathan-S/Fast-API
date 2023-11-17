# # app/models/type.py
# from sqlalchemy import Column, String, Integer
# from sqlalchemy.ext.declarative import declarative_base

# Base = declarative_base()

# class MovieModel(Base):
#     __tablename__ = "movies"
#     id = Column(String, primary_key=True, index=True)
#     title = Column(String)
#     director = Column(String)

# class BookModel(Base):
#     __tablename__ = "books"
#     id = Column(String, primary_key=True, index=True)
#     title = Column(String)
#     author = Column(String)

# class User(Base):
#     __tablename__ = "event_management.testtable"
#     user_id = Column(Integer, primary_key=True, index=True)
#     first_name = Column(String, nullable=False)
#     last_name = Column(String, nullable=False)
