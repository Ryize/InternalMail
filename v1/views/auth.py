from core.models.auth.models import Users
from core.models.service import get_db, get_auth_code
from core.schemas.auth_schema import RegisterResponse, Register
from v1.endpoints import user

db = get_db()


@user.post("/register", response_model=RegisterResponse)
async def register(data: Register):
    """
    Используется для регистрации в системе с помощью логина и пароля.
    Возвращает код, используемый для доступа к почте.
    """
    user = db.query(Users).filter(Users.login == data.login).first()
    if user:
        return RegisterResponse(
            success=False,
            description="Пользователь с таким логином уже зарегистрирован!",
        )
    code = get_auth_code()
    Users.create(login=data.login, password=data.password, code=code)
    return RegisterResponse(
        success=True,
        description="Используйте полученный код для входа на платформу",
        code=code,
    )


@user.post("/get_new_code", response_model=RegisterResponse)
async def get_new_code(data: Register):
    """
    Используется для получения нового кода.
    Восстановление кода происходит с помощью логина и пароля указанных при регистрации.
    """
    user = (
        db.query(Users)
        .filter(Users.login == data.login, Users.password == data.password)
        .first()
    )
    if not user:
        return RegisterResponse(
            success=False, description="Пользователь с таким логином/паролем не найден!"
        )
    code = get_auth_code()
    user.code = code
    user.save()
    return RegisterResponse(success=True, description="Получен новый код!", code=code)
