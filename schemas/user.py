from pydantic import BaseModel


class FullUser(BaseModel):
    username: str
    email: str | None = None
    goods_id: int


class User(BaseModel):
    username: str
    email: str | None = None


class UserPassword(User):
    password: str


class UserId(UserPassword):
    id: int


class Goods(BaseModel):
    goods_id: int


class UserWithGoods(Goods):
    username: str
    goods_id: int


class GetUser(BaseModel):
    username: str
    password: str


class TestGoods(BaseModel):
    username: str
    goods_id: int
