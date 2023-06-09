"""
для основных команд с подписями

# Установки пакетов
pip install fastapi[all]


uvicorn main:app --reload

# инициализировать окружение для миграций
alembic init migrations

alembic upgrade 1c7319b2ac71

# прогон (создание файла миграции)
alembic revision --autogenerate -m "add your commit"

# Обновить до последней версии
alembic upgrade head


"""

"""
Пункты необходимые проекту:

1) Подключение БД +
2) проведение миграций +
3) написание модели примеров запроса +
3) создание хранилища для хранения моделей персов
4) создание пользователей 
5) сохранения пепрсов пользователей
6) "мясо персов"
7) чат пользователей (веб сокет)
 

"""