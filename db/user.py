from sqlalchemy import *
from sqlalchemy.orm import relationship

from .database import Base


class UserDB(Base):
    """ Model for user. """
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)
    goods_id = Column(String, ForeignKey('goods.name'), nullable=True)
    goods = relationship("GoodsDB", back_populates="goods")


user = UserDB.__table__
