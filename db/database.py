import databases

from sqlalchemy import create_engine, MetaData

DATABASE_URL = "postgresql://user:password@postgresserver/db"
database = databases.Database(DATABASE_URL)

metadata = MetaData()

engine = create_engine(
    DATABASE_URL,
)

