from typing import Optional

from pydantic import BaseModel


class Register(BaseModel):
    login: str
    password: str


class ResponseStatus(BaseModel):
    success: bool
    description: str = ""


class RegisterResponse(ResponseStatus):
    code: Optional[str] = None
