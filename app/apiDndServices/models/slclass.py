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

