from fastapi import APIRouter, Depends, UploadFile, File

from schemas.goods import GoodsSchemas, GoodsPhotoSchemas
from repositories.goods import BaseGoodsClass
from endpoints.depends import get_goods_repository

goods_router = APIRouter(tags=['goods'])


@goods_router.post('/create_goods', response_model=GoodsPhotoSchemas)
async def create_goods(
        g: GoodsSchemas,
        base_class: BaseGoodsClass = Depends(get_goods_repository),
        photo: UploadFile = File(...),
):
    return await base_class.create_goods(g=g, photo=photo)
