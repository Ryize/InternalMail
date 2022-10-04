from typing import List, Dict, Optional

from pydantic import BaseModel


class Mail(BaseModel):
    email: str
    message: str


class Code(BaseModel):
    code: str


class SendMail(Mail, Code):
    pass


class SendMailResponse(BaseModel):
    success: bool
    description: str


class Message(BaseModel):
    id: int
    sender: str
    recipient: str
    message: str


class GetMyMessage(BaseModel):
    messages: Optional[List[Message]] = None
    detail: Optional[str] = None
