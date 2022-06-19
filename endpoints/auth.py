from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from starlette import status

from endpoints.depends import get_user_repository
from schemas.auth import Token
from schemas.user import GetUser, User
from repositories.user import BaseUserClass
from security.user import verify_password, create_access_token, authenticate_user, ACCESS_TOKEN_EXPIRE_MINUTES, \
    get_current_active_user
from db.user import user

auth_router = APIRouter()


@auth_router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(),
                                 users: BaseUserClass = Depends(get_user_repository)):
    take_user = await users.get_user(form_data.username)
    if take_user:
        one_user = authenticate_user(user, form_data.username, form_data.password, take_user.password)
        if not one_user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": one_user.username, "scopes": form_data.scopes}, expires_delta=access_token_expires
        )
        return {"access_token": access_token, "token_type": "bearer"}


@auth_router.get("/me", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user


@auth_router.get("/me/items")
async def read_own_items(current_user: User = Depends(get_current_active_user)):
    return [{"item_id": "Foo", "owner": current_user.username}]
