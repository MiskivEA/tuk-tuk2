from fastapi import APIRouter
from .send_email import send_email_report


router = APIRouter(prefix='/tasks', tags=['Tasks'])


@router.get('/send_data')
def send_data(username: str):
    send_email_report(username)
