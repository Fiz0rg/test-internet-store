from sqlalchemy import *

from db.database import metadata

user = Table(
    'user',
    metadata,
    Column("id", Integer, primary_key=True, unique=True, autoincrement=True),
    Column("username", String, index=True, unique=True),
    Column("email", String, unique=True, primary_key=True),
    Column("password", String)
)
