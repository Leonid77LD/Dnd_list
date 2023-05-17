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

from fastapi import FastAPI, Depends, Response
from fastapi.responses import JSONResponse
import json
from requests import get
from sqlalchemy import insert, select, text
from sqlalchemy.ext.asyncio import AsyncSession

from app.organizer.dbutils import execute_command_insert
from googletrans import Translator

from app.base_model import Test
from app.apiDndServices.db_table.slclass import Slclass

# Start main app
# Start local app in console "uvicorn app.main:app --reload"
from app.database import get_async_session


from app.apiDndServices.controller.slclass import router as slclass_router

app = FastAPI(
    title="DND App"
)



# @app.get('/test_req')
# def test_req():
#     return {'mess': 'All good'}


# @app.get('/test_sql')
# async def test_sql(name: str, session: AsyncSession = Depends(get_async_session)):
#
#     stmt = insert(Test).values(test_col=uuid.uuid4(),
#                                test_name=name)
#     await session.execute(stmt)
#     await session.commit()
#     return True


# @app.get('/get_all_classes')
# async def get_all_classes(db: AsyncSession = Depends(get_async_session)):
#     stmt = select(Test)
#     res = await db.execute(stmt)
#     res = res.all()
#     res_list = []
#     for qwe in res:
#         print(qwe)
#         res_list.append(qwe[0].as_dict())
#     return True, res_list


@app.get('/all_classes_5e')
def test_dnd_api():
    res = get('https://www.dnd5eapi.co/api/classes/')
    print(res.text)
    if res.status_code == 200:
        content = ast.literal_eval(res.text)  # converting string into dictionary
        print(content)
        for i in content['results']:
            stmt = insert(Test).values(test_col=uuid.uuid4(),
                                       test_name=i['name'],
                                       url=i['url']
                                       )
            execute_command_insert(stmt)

    return res.status_code, res.content



# translate = Translator()
# resp = translate.translate('cat', 'ru')


app.include_router(slclass_router)


# @app.on_event("startup")
# async def startup_event():
#     redis = aioredis.from_url("redis://localhost", encoding="utf8", decode_responses=True)
#     print('123', redis)
#     FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
#
