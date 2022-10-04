from core.models.auth.models import Users
from core.models.mail.models import MailMessage
from core.models.service import get_db
from core.schemas.mail_schema import Code, GetMyMessage, SendMail, SendMailResponse
from v1.endpoints import user

db = get_db()


@user.post("/send_mail", response_model=SendMailResponse)
async def send_mail(data: SendMail):
    """
    Используется для отправки сообщений по внутренней почте.
    """
    sender = db.query(Users).filter(Users.code == data.code).first()
    recipient = db.query(Users).filter(Users.email == data.email).first()
    if not (sender and recipient):
        return SendMailResponse(
            success=False, description="Код или email получателя неверны!"
        )
    MailMessage.create(sender=sender.id, recipient=recipient.id, message=data.message)
    return SendMailResponse(success=True, description="Письмо успешно доставлено!")


@user.post("/get_my_message", response_model=GetMyMessage)
async def get_my_message(data: Code):
    """
    Используется для получения списка со всеми сообщениями,
    которые отправил/получил указанный пользователь.
    """
    user = db.query(Users).filter(Users.code == data.code).first()
    if not user:
        return GetMyMessage(detail="Пользователь с таким кодом не найден!")
    messages = db.query(MailMessage).filter(Users.id == user.id).all()
    result = [i.to_json() for i in messages]
    return GetMyMessage(messages=result)
