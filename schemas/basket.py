from pydantic import BaseModel


class BasketSchema(BaseModel):
    user_id: int
    goods_id: int


class BasketSchemaId(BasketSchema):
    id: int
