import ast
import uuid
# Импорты для запросов (надо оптимизировать)
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_async_session

from sqlalchemy import insert

from app.apiDndServices.db_table.slclass import Slclass

from requests import get


class Api5EDndClass:
    """Класс запросов к Api 5eDnd для получения данных по основным классам и записи их в БД."""
    def __init__(self):
        pass

    def get_all_classes_5e(self, db: AsyncSession = Depends(get_async_session)):
        res = get('https://www.dnd5eapi.co/api/classes/')
        print(res.text)
        if res.status_code == 200:
            content = ast.literal_eval(res.text)  # converting string into dictionary
            print(content)
            for i in content['results']:
                stmt = insert(Slclass).values(
                    cdclass=uuid.uuid4(),
                    index=i['index'],
                    full_nmclass=i['name'],
                    url=i['url'],
                )
                res = db.execute(stmt)
        return res
