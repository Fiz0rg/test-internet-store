from fastapi import FastAPI

from db.database import database
from endpoints.goods import goods_router
from endpoints.category import category_router
from endpoints.user import user_router
from endpoints.auth import auth_router

app = FastAPI()


@app.on_event("startup")
async def startup():
    print('Запуск бд..')
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    print('Остановка бд..')
    await database.disconnect()


app.include_router(auth_router, prefix="/auth", tags=['auth'])
app.include_router(goods_router, prefix="/goods", tags=['goods'])
app.include_router(category_router, prefix="/category", tags=['category'])
app.include_router(user_router, prefix="/user", tags=['user'])
