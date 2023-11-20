
#app/db/base.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://apiUser:Kadit123@localhost:5432/postgres"

#  'dbname': 'postgres',
#     'user': 'apiUser',
#     'password': 'Kadit123',
#     'host': 'localhost',
#     'port': '5432',
# "postgresql://your_username:your_password@localhost/your_database_name"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)