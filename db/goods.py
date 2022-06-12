from sqlalchemy import *

from .database import metadata

goods = Table(
    'goods',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String),
    Column('description', String),
    Column('category_id', Integer, ForeignKey('category.id'))
)

