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
