from .base import BaseClass

from db.database import database
from schemas.goods import GoodsSchemas, GoodsSchemasId
from db.goods import goods


class BaseGoodsClass(BaseClass):
    """ Обработка CRUD асинх функций для товаров. """

    async def create_goods(self, g: GoodsSchemas):
        """ Создание товара. """

        product = GoodsSchemasId(id=0,
                                 name=g.name,
                                 description=g.description,
                                 category_id=g.category_id)
        values = {**product.dict()}
        values.pop('id', None)
        query = goods.insert().values(**values)
        product.id = await database.execute(query=query)
        return product

    async def get_goods(self, offset: int = 0, limit: int = 10):
        """ Выборка товаров. """

        take_goods = goods.select().offset(offset).limit(limit)
        return await database.fetch_all(take_goods)

    async def get_name(self, name: str):
        query = goods.select().where(goods.c.name == name)
        item = await database.fetch_one(query=query)
        if item is None:
            return None
        return GoodsSchemas.parse_obj(item)

    async def delete(self, name):
        query = goods.delete().where(goods.c.name == name)
        return await database.execute(query=query)
