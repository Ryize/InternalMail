from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from core.models.auth.models import Users
from core.models.base import Base


class MailMessage(Base):
    __tablename__ = "mail_message"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    sender = relationship(Users, back_populates="sender")
    recipient = relationship(Users, back_populates="recipient")
    message = Column(String, max_length=2048)
