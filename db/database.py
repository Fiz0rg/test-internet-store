import databases

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

DATABASE_URL = "postgresql+psycopg2://postgres:123@localhost:5432/postgres"

database = databases.Database(DATABASE_URL)

# metadata = MetaData()

engine = create_engine(DATABASE_URL, )

Base = declarative_base()







