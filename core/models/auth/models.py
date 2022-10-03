from sqlalchemy import Column, Integer, String

from core.models.base import Base
from core.models.mixin import BaseMixin


class Users(Base, BaseMixin):
    __tablename__ = "users"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    login = Column(String, unique=True)
    password = Column(String)
    email = Column(String, unique=True)
    code = Column(String, unique=True)
