from typing import List

from db.database import database
from repositories.base import BaseClass
from schemas.category import CategorySchemas, CategorySchemasId
from db.category import category


class BaseCategoryClass(BaseClass):
    """ CRUD для категориев. """

    async def create_category(self, cat: CategorySchemas) -> CategorySchemasId:
        item = CategorySchemasId(id=0, name=cat.name)
        values = {**item.dict()}
        values.pop('id', None)
        query = category.insert().values(**values)
        item.id = await database.execute(query=query)
        return item

    async def get_category(self, offset: int = 0, limit: int = 10) -> List[CategorySchemasId]:
        take_goods = category.select().offset(offset).limit(limit)
        print(take_goods)
        return await database.fetch_all(take_goods)
