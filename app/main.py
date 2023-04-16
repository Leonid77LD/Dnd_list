"""
Идея проекта, создать пошаговый сайт
Заполнения листа персонажа в ДНД

Например оптемизировать стартовые выборы с коротким описанием

что бы человок душой и быстро "накидал себе перса"
далее сохранить данного чара
написать API кидание кубов хитов (хочу поиграться с filter lambda )


Отправить лист на почту / напечатьтать лист

МБ генератор шутки в конце выполнения блоков.

-- Выбрать расу
-- Выбрать класс
-- Определить характеристики
-- Добавить заклинания
-- Выбрать снаряжение
-- Придумать описание
-- Отправиться на поиск приключений (печать /отправка на почту / позвонить и похвастаться родным и близким)

"""
import ast
import uuid

from fastapi import FastAPI
# from httpx import post, get
from requests import get
from sqlalchemy import insert

from app.organizer.dbutils import execute_command_insert


from app.base_model import test

# Start main app
# Start local app in console "uvicorn app.main:app --reload"
app = FastAPI(
    title="DND App"
)


@app.get('/test_req')
def test_req():
    return {'mess': 'All good'}


@app.get('/test_sql')
async def test_sql(name: str):

    stmt = insert(test).values(test_col=uuid.uuid4(),
                               test_name=name)
    await execute_command_insert(stmt)
    return {"status": "success"}


@app.get('/dnd5e_test_res')
def test_dnd_api():
    res = get('https://www.dnd5eapi.co/api/')
    print(res.status_code)
    if res.status_code == 200:
        content = ast.literal_eval(res.text)
        print(content)
    return res.status_code, res.content
#
# app.include_router(
#     fastapi_users.get_auth_router(auth_backend),
#     prefix="/auth",
#     tags=["Auth"],
# )
#
# app.include_router(
#     fastapi_users.get_register_router(UserRead, UserCreate),
#     prefix="/auth",
#     tags=["Auth"],
# )
#
# app.include_router(router_operation)
#

# @app.on_event("startup")
# async def startup_event():
#     redis = aioredis.from_url("redis://localhost", encoding="utf8", decode_responses=True)
#     print('123', redis)
#     FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
#
