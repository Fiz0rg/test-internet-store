from sqlalchemy import *
from .database import metadata


category = Table(
    'category',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String, unique=True)
)