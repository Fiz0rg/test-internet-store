from db.database import database
from fastapi.security import OAuth2PasswordBearer

from repositories.goods import BaseGoodsClass
from repositories.category import BaseCategoryClass


def get_goods_repository() -> BaseGoodsClass:
    return BaseGoodsClass(database)


def category_repository() -> BaseCategoryClass:
    return BaseCategoryClass(database)


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/token")
