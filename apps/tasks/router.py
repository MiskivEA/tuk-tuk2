from fastapi import APIRouter, Depends

from .send_email import send_email_report
from ..auth.auth import fastapi_users

router = APIRouter(prefix='/tasks', tags=['Tasks'])

current_user = fastapi_users.current_user()


@router.get('/send_data')
def send_data(user=Depends(current_user)):
    send_email_report.delay(user.email)
    return {'message': f'На вашу электронную почту {user.email} будет отправлено письмо'}
