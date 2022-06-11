from db.database import database
from repositories.goods import BaseGoodsClass


def get_goods_repository() -> BaseGoodsClass:
    return BaseGoodsClass(database)
