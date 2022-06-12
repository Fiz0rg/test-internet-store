from typing import List

from fastapi import APIRouter, Depends

from schemas.category import CategorySchemas, CategorySchemasId
from repositories.category import BaseCategoryClass
from endpoints.depends import category_repository

category_router = APIRouter()


@category_router.post('/create', response_model=CategorySchemasId)
async def create_category(cat: CategorySchemas,
                          base_class: BaseCategoryClass = Depends(category_repository)):
    await base_class.create_category(cat=cat)


@category_router.get('/get', response_model=List[CategorySchemasId])
async def get_category(offset: int = 0,
                       limit: int = 10,
                       base_class: BaseCategoryClass = Depends(category_repository)):
    await base_class.get_category(offset, limit)
