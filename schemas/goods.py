from typing import Union
from pydantic import BaseModel


class GoodsSchemas(BaseModel):
    """ Схема для модели товара. """

    id: int
    name: str
    description: Union[str, None] = None


class GoodsPhotoSchemas(GoodsSchemas):
    """ Схема для модели товара. """

    id: int
    name: str
    description: Union[str, None] = None
    photo: str

