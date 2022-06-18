from pydantic import BaseModel


class User(BaseModel):
    username: str
    email: str | None = None


class UserPassword(User):
    password: str


class UserId(UserPassword):
    id: int


class GetUser(BaseModel):
    username: str
    password: str
