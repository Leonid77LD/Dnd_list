import uuid

from sqlalchemy import MetaData, Integer, String, UUID, DATE, DateTime, Table, Column

from database import Base

metadata = MetaData()


class Test(Base):
    __tablename__ = 'test'

    test_col = Column(UUID, primary_key=True, nullable=False, default=uuid.uuid4(), comment="Первичный Ключ")
    test_name = Column(String, nullable=True, comment="Test name")
    url = Column(String, nullable=True, comment="url")

    def __init__(self, test_col: uuid.UUID, test_name: str, url: str):
        self.test_col = test_col
        self.test_name = test_name
        self.url = url
    #
    # def __repr__(self) -> str:
    #     return f"Test(test_col={self.test_col}, test_name={self.test_name}, url={self.url})"

    def as_dict(self):
        return {self.test_name: self.test_name}
