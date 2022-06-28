from sqlalchemy import *

from .database import Base


class UserDB(Base):
    """ Model for user. """
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)
    goods_id = Column(Integer, ForeignKey('goods.id'), nullable=True)


user = UserDB.__table__

# user = Table(
#     'user',
#     metadata,
#     Column("id", Integer, primary_key=True, unique=True, autoincrement=True),
#     Column("username", String, index=True, unique=True),
#     Column("email", String, unique=True, primary_key=True),
#     Column("password", String),
#     Column("goods_id", Integer, ForeignKey("goods.id"), nullable=True)
# )
