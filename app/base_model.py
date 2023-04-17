import uuid

from sqlalchemy import MetaData, Integer, String, UUID, DATE, DateTime, Table, Column

metadata = MetaData()

test = Table(
    'test', metadata,
    Column('test_col', UUID, primary_key=True, nullable=False, default=uuid.uuid4(), comment="Первичный Ключ"),
    Column('test_name', String, nullable=True, comment="Test name"),
    Column('url', String, nullable=True, comment="url")
)
