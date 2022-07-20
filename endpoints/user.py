from fastapi import APIRouter, Depends, Security


from schemas.user import UserPassword, User, TestSchema, GetUserAndId
from repositories.user import BaseUserClass
from security.user import get_current_active_user
from .depends import get_user_repository

user_router = APIRouter()


@user_router.post('/create', response_model=TestSchema)
async def create_user(user: UserPassword,
                      base_class: BaseUserClass = Depends(get_user_repository)):
    """ Созданеие пользователя. """

    return await base_class.create(u=user)


@user_router.get('/get', response_model=GetUserAndId)
async def get_user(user_class: BaseUserClass = Depends(get_user_repository),
                   current_user: User = Security(get_current_active_user, scopes=['user'])):
    """ Получение пользователя. """

    return await user_class.get_user(current_user.username)
