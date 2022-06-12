from pydantic import BaseModel


class GoodsSchemas(BaseModel):
    """ Reqiest товара. """

    name: str
    description: str
    category_id: int


class GoodsSchemasId(GoodsSchemas):
    """ Responce товара. """

    id: int





