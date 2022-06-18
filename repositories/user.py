from .base import BaseClass
from schemas.user import UserId, UserPassword
from security.user import hash_password
from db.user import user


class BaseUserClass(BaseClass):
    """ CRUD модели пользователей. """

    async def create(self, u: UserPassword):
        new_user = UserId(
            id=0,
            username=u.username,
            email=u.email,
            password=hash_password(u.password)
        )
        values = {**new_user.dict()}
        values.pop('id', None)
        query = user.insert().values(**values)
        new_user.id = await self.database.execute(query=query)
        return new_user

    async def get_user(self, name: str):
        get_user = user.select().where(user.c.username == name)
        return await self.database.fetch_one(get_user)
