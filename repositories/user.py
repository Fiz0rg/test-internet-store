from schemas.goods import GoodsSchemas
from .base import BaseClass
from schemas.user import UserId, UserPassword, ABC
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

    # async def add_goods(self, goods: GoodsSchemas, username: str):
    #     add = ABC(username=username,
    #               goods=GoodsSchemas(name=goods.name,
    #                                  description=goods.description,
    #                                  category_id=goods.category_id))
    #     values = {**add.dict()}
    #     query = user.update().where(user.c.username == username).values(**values)
    #     await self.database.execute(query)
    #     return add

    async def add_goods(self, item: GoodsSchemas, current_user: ABC):
        copy_current_user = current_user
        pydantic_copy_current_user = ABC(**copy_current_user)
        print(pydantic_copy_current_user)
        new_item = item.dict(exclude_unset=True)
        pydantic_copy_current_user.goods.append(new_item)
        updated_user = pydantic_copy_current_user.copy(update=new_item)
        # await self.database.execute(query=updated_user)
        return updated_user
