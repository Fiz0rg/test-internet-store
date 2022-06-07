from db.database import database_on_event
from repositories.goods import BaseGoodsClass


def get_goods_repository():
    return BaseGoodsClass(database_on_event)
