from typing import List, Union

from fastapi import APIRouter, Depends, HTTPException

from schemas.goods import GoodsSchemas, GoodsSchemasId
from repositories.goods import BaseGoodsClass
from endpoints.depends import get_goods_repository

goods_router = APIRouter(tags=['goods'], )


@goods_router.post('/create_goods', response_model=GoodsSchemasId)
async def create_goods(
        g: GoodsSchemas,
        base_class: BaseGoodsClass = Depends(get_goods_repository),
):
    return await base_class.create_goods(g=g)


@goods_router.get('/get_goods', response_model=List[GoodsSchemasId])
async def get_goods(
        offset: int = 0,
        limit: int = 10,
        base_class: BaseGoodsClass = Depends(get_goods_repository)
):
    return await base_class.get_goods(offset, limit)


@goods_router.delete('/delete_goods')
async def delete_goods(
        name: str,
        base_class: BaseGoodsClass = Depends(get_goods_repository)):

    not_found = HTTPException(status_code=404, detail=f"Item {name} not found")
    item = await base_class.get_name(name)
    if item is None:
        return not_found
    result = await base_class.delete(name=name)
    return {'status': 'ok'}

