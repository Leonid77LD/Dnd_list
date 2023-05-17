import uuid

from sqlalchemy import MetaData, Integer, String, UUID, DATE, DateTime, Table, Column

from app.database import Base


class Slclass(Base):
    __tablename__ = 'slclass'

    cdclass = Column(UUID, primary_key=True, nullable=False, default=uuid.uuid4(), comment="Ключь классов")
    nmclass = Column(String, nullable=False, comment="Наименование игрального класса")
    full_nmclass = Column(String, nullable=True, comment="Полное имя класса")
    url = Column(String, nullable=True, comment="url для получения следующего обьекта класса")

    def __init__(self,
                 cdclass: uuid.UUID,
                 nmclass: str,
                 full_nmclass: str,
                 url: str
                 ):
        self.cdclass = cdclass
        self.nmclass = nmclass
        self.full_nmclass = full_nmclass
        self.url = url

    def as_dict(self):
        return {
            self.cdclass: self.cdclass,
            self.nmclass: self.nmclass,
            self.full_nmclass: self.full_nmclass,
            self.url: self.url,
        }
