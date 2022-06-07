from fastapi import FastAPI

from db.database import database
from endpoints.goods import goods_router

app = FastAPI()

app.include_router(goods_router)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
