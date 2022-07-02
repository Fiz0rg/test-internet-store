from typing import List

from fastapi import APIRouter, Security, Depends, HTTPException

from endpoints.depends import get_goods_repository, get_user_repository, get_basket_repository
from repositories.basket import BaseBasketClass
from repositories.goods import BaseGoodsClass
from repositories.user import BaseUserClass
from schemas.user import User
from schemas.basket import BasketSchemaId
from security.user import get_current_active_user

basket_router = APIRouter()


@basket_router.post("/add_goods", response_model=BasketSchemaId)
async def add_goods(goods_name: str,
                    current_user: User = Security(get_current_active_user, scopes=["user"]),
                    goods_db: BaseGoodsClass = Depends(get_goods_repository),
                    basket_class: BaseBasketClass = Depends(get_basket_repository),
                    users: BaseUserClass = Depends(get_user_repository)):
    user_id = await users.get_user(current_user.username)
    item = await goods_db.get_one(goods_name)
    if not item:
        raise HTTPException(status_code=400, detail="Goods not found")
    return await basket_class.add_goods(user_id=user_id.id, goods_id=item.id)


@basket_router.get("/get_all_goods", response_model=List[BasketSchemaId])
async def get_all_goods(offset: int = 0, limit: int = 15,
                        current_user: User = Security(get_current_active_user, scopes=["user"]),
                        basket_class: BaseBasketClass = Depends(get_basket_repository),):
    return await basket_class.get_all_goods(offset, limit)
