from sqlalchemy import *

from .database import Base


class GoodsDB(Base):
    """ Model for goods. """
    __tablename__ = "goods"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True)
    description = Column(String)
    category_id = Column(Integer, ForeignKey('category.id'))


goods = GoodsDB.__table__

# goods = Table(
#     'goods',
#     metadata,
#     Column('id', Integer, primary_key=True, autoincrement=True),
#     Column('name', String),
#     Column('description', String),
#     Column('category_id', Integer, ForeignKey('category.id'))
# )

