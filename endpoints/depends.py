from db.database import database

from repositories.goods import BaseGoodsClass
from repositories.category import BaseCategoryClass


def get_goods_repository() -> BaseGoodsClass:
    return BaseGoodsClass(database)


def category_repository() -> BaseCategoryClass:
    return BaseCategoryClass(database)
