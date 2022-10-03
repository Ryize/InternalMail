from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from core.models.auth.models import Users
from core.models.base import Base
from core.models.mixin import BaseMixin


class MailMessage(Base, BaseMixin):
    __tablename__ = "mail_message"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    sender = Column(Integer, ForeignKey('users.id'), nullable=False)
    recipient = Column(Integer, ForeignKey('users.id'), nullable=False)
    message = Column(String)
