from sqlalchemy import *
from sqlalchemy.orm import relationship

from .database import Base


class GoodsDB(Base):
    """ Model for goods. """
    __tablename__ = "goods"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True)
    description = Column(String)
    category_id = Column(Integer, ForeignKey('category.id'))
    user = relationship("UserDB", back_populates="user")


goods = GoodsDB.__table__
