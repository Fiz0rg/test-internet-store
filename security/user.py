from datetime import timedelta, datetime

from fastapi import Depends, HTTPException
from pydantic import ValidationError
from jose import jwt, JWTError
from passlib.context import CryptContext
from starlette import status

from fastapi.security import OAuth2PasswordBearer, SecurityScopes

from schemas.auth import TokenData
from schemas.user import GetUser, User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='auth/token',
                                     scopes={"admin": "This scope allow you to add goods, categories",
                                             "user": "Just users community"})

SECRET_KEY = '09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30
pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def hash_password(password):
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    """ Верификация\разшэширование пароля. """

    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def authenticate_user(username: str, password: str, hashed_password: str):
    """ Валидация пользователя. """

    auth_user = GetUser(username=username, password=password)
    if not auth_user:
        return False
    if not verify_password(password, hashed_password):
        return False
    return auth_user


async def get_current_user(security_scopes: SecurityScopes, token: str = Depends(oauth2_scheme)):
    """ Проверка на scopes, выдача прав. Возвращает username и скопы. """

    if security_scopes:
        authenticate_value = f'Bearer scope="{security_scopes.scope_str}"'
    else:
        authenticate_value = f"Bearer"
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": authenticate_value},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_scopes = payload.get('scopes', [])
        token_data = TokenData(scopes=token_scopes, username=username)
    except (JWTError, ValidationError):
        raise credentials_exception
    for scope in security_scopes.scopes:
        if scope not in token_data.scopes:
            if scope not in token_data.scopes:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Not enough permissions",
                    headers={"WWW-Authenticate": authenticate_value},
                )
    return token_data


async def get_current_active_user(current_user: User = Depends(get_current_user)):

    return current_user
