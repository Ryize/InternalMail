from fastapi import APIRouter

user = APIRouter(prefix="/auth")
mail = APIRouter(prefix="/mail")

from .views.auth import *
from .views.mail import *
