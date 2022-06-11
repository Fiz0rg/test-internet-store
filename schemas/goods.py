from pydantic import BaseModel


class GoodsSchemas(BaseModel):
    """ Reqiest товара. """

    name: str
    description: str


class GoodsSchemasId(GoodsSchemas):
    """ Responce товара. """

    id: int



