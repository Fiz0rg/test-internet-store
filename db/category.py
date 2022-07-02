from sqlalchemy import *

from .database import Base


class CategoryDb(Base):
    """ Model for caregories. """
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True)


category = CategoryDb.__table__
