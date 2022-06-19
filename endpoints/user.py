from fastapi import APIRouter, Depends

from schemas.user import UserPassword, User
from repositories.user import BaseUserClass
from .depends import get_user_repository

user_router = APIRouter()


@user_router.post('/create', response_model=User)
async def create_user(user: UserPassword,
                      base_class: BaseUserClass = Depends(get_user_repository)):
    """ Созданеие пользователя. """

    return await base_class.create(u=user)


@user_router.get('/get', response_model=UserPassword)
async def get_user(name: str,
                   base_class: BaseUserClass = Depends(get_user_repository)):
    """ Получение пользователя. """

    return await base_class.get_user(name)
