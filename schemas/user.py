from pydantic import BaseModel

from schemas.goods import GoodsSchemas


class User(BaseModel):
    username: str
    email: str | None = None


class GetUserAndId(User):
    id: int


class ABC(User):
    goods_id: list[int] = []


class UserPassword(User):
    password: str


class UserId(UserPassword):
    id: int


class Goods(BaseModel):
    goods_id: int


class FullUser(BaseModel):
    username: str
    email: str | None = None
    goods_id: int

    class Config:
        orm_mode = True


class TestSchema(UserId):
    goods: list[GoodsSchemas] = []


class UserWithGoods(Goods):
    username: str
    goods_id: int


class GetUser(BaseModel):
    username: str
    password: str
