from sqlalchemy import *

from .database import Base


class BasketDB(Base):
    """ Модель товаров. """
    __tablename__ = "basket"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    goods_id = Column(Integer, ForeignKey("goods.id"))


basket = BasketDB.__table__
