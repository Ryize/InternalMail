from sqlalchemy import Column, Integer, String

from core.models.base import Base
from core.models.service import get_db


class BaseMixin:
    db = get_db()

    def save(self):
        self.db.add(self)
        self.db.commit()

    @classmethod
    def create(cls, *args, **kwargs):
        object = cls(*args, **kwargs)
        cls.db.add(object)
        cls.db.commit()


class Users(Base, BaseMixin):
    __tablename__ = "users"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    login = Column(String, unique=True)
    password = Column(String)
    code = Column(String, unique=True)
