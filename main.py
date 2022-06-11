from fastapi import FastAPI

from db.database import database
from endpoints.goods import goods_router

app = FastAPI()


@app.on_event("startup")
async def startup():
    print('Запуск бд..')
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    print('Остановка бд..')
    await database.disconnect()


app.include_router(goods_router)
