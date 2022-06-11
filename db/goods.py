import sqlalchemy

from .database import metadata

goods = sqlalchemy.Table(
    'goods',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column('name', sqlalchemy.String),
    sqlalchemy.Column('description', sqlalchemy.String)
)
