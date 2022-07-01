from fastapi import Depends

from db.database import database
from repositories.basket import BaseBasketClass
from repositories.goods import BaseGoodsClass
from repositories.category import BaseCategoryClass
from repositories.user import BaseUserClass


def get_goods_repository() -> BaseGoodsClass:
    """ Обращение к БД товаров. """

    return BaseGoodsClass(database)


def category_repository() -> BaseCategoryClass:
    """ Обращение к БД категорий товаров. """

    return BaseCategoryClass(database)


def get_user_repository() -> BaseUserClass:
    """ Обращение к БД пользователей. """

    return BaseUserClass(database)


def get_basket_repository() -> BaseBasketClass:
    """ Обращение к БД корзины товаров. """

    return BaseBasketClass(database)
