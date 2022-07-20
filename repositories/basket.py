from typing import List

from fastapi import HTTPException

from db.basket import basket
from schemas.basket import BasketSchemaId
from .base import BaseClass


class BaseBasketClass(BaseClass):
    """ CRUD для модели корзины товаров. """

    async def add_goods(self, user_id: int, goods_id: int) -> BasketSchemaId:
        item = BasketSchemaId(id=0, user_id=user_id, goods_id=goods_id)
        values = {**item.dict()}
        values.pop("id", None)
        query = basket.insert().values(**values)
        item.id = await self.database.execute(query=query)
        return item

    async def get_all_goods(self, offset: int, limit: int) -> List[BasketSchemaId]:
        query = basket.select().offset(offset).limit(limit)
        result = await self.database.fetch_all(query=query)
        if len(result) > 15:
            raise HTTPException(status_code=403, detail="So much goods")
        return result
