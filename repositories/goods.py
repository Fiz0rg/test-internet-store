from .base import BaseClass

from fastapi import File, UploadFile
from schemas.goods import GoodsSchemas
from db.goods import GoodsModel


class BaseGoodsClass(BaseClass):
    """ Обработка CRUD асинх функций для товаров. """

    async def create_goods(self, g: GoodsSchemas, photo: UploadFile = File(...)):
        photo_path = f'/photo/{photo.filename}'
        product = GoodsSchemas(name=g.name,
                               description=g.description,
                               photo=photo_path)
        values = {**product.dict()}
        query = GoodsModel(values)
        query.save()
        return query
