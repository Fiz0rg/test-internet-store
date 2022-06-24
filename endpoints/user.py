from fastapi import APIRouter, Depends, Security, HTTPException

from repositories.goods import BaseGoodsClass
from schemas.user import UserPassword, User, UserWithGoods, FullUser
from repositories.user import BaseUserClass
from security.user import get_current_active_user
from .depends import get_user_repository, get_goods_repository

user_router = APIRouter()


@user_router.post('/create', response_model=User)
async def create_user(user: UserPassword,
                      base_class: BaseUserClass = Depends(get_user_repository)):
    """ Созданеие пользователя. """

    return await base_class.create(u=user)


@user_router.get('/get', response_model=FullUser)
async def get_user(name: str,
                   base_class: BaseUserClass = Depends(get_user_repository)):
    """ Получение пользователя. """

    return await base_class.get_user(name)


@user_router.put('/add_goods', response_model=UserWithGoods)
async def add_goods(goods_name: str,
                    goods_db: BaseGoodsClass = Depends(get_goods_repository),
                    users: BaseUserClass = Depends(get_user_repository),
                    current_user: User = Security(get_current_active_user, scopes=['user'])):
    """ Добавление товаров в корзину. """

    item = await goods_db.get_one(goods_name)
    print(item)
    print(current_user)
    return await users.add_goods(item.id, current_user.username)
