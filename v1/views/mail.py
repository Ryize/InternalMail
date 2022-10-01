from core.models.auth.models import Users
from core.models.service import get_db
from core.schemas.auth_schema import RegisterResponse, Register
from v1.endpoints import user

db = get_db()


@user.post("/send_mail", response_model=RegisterResponse)
async def register(data: Register):
    pass


@user.post("/get_my_message", response_model=RegisterResponse)
async def get_new_code(data: Register):
    pass
