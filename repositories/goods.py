from .base import BaseClass

from schemas.goods import GoodsSchemas, GoodsSchemasId
from db.goods import goods


class BaseGoodsClass(BaseClass):
    """ Обработка CRUD асинх функций для товаров. """

    async def create_goods(self, g: GoodsSchemas):
        product = GoodsSchemasId(id=0,
                                 name=g.name,
                                 description=g.description,
                                 category_id=g.category_id)
        values = {**product.dict()}
        values.pop('id', None)
        query = goods.insert().values(**values)
        product.id = await self.database.execute(query=query)
        return product

    async def get_goods(self, offset: int = 0, limit: int = 10):
        take_goods = goods.select().offset(offset).limit(limit)
        return await self.database.fetch_all(take_goods)

    async def get_name(self, name: str):
        query = goods.select().where(goods.c.name == name)
        item = await self.database.fetch_one(query=query)
        if item is None:
            return None
        return GoodsSchemas.parse_obj(item)

    async def delete(self, name):
        query = goods.delete().where(goods.c.name == name)
        return await self.database.execute(query=query)
