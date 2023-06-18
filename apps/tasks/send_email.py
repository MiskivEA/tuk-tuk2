import smtplib
from email.message import EmailMessage

from celery import Celery
from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from apps.auth.db_connect import get_async_session
from apps.auth.models import User
from apps.posts.models import PostDB
from settings.config import SMTP_USER, SMTP_PASSWORD

SMTP_HOST = 'smtp.gmail.com'
SMTP_PORT = 465

celery = Celery('side_tasks', broker='redis://localhost:63791')


def create_email(email_address):
    email = EmailMessage()
    email['Subject'] = 'Tuk-Tuk2'
    email['From'] = SMTP_USER
    email['To'] = SMTP_USER

    img = 'https://foodmood.ru/upload/iblock/b35/b35e9c1557d4e535aec4e2cfe560e3d2.jpg'
    email.set_content(
        '<div>'
        f'<h1 style="color: red;"> HELLO {email_address} </h1>'
        '<h2> Youre DATA:  </h2>'
        f'<img src="{img}">'
        f'<p> DATA\nDATA\nDATA\nDATA\n </p>'
        '</div>',
        subtype='html'
    )
    return email


@celery.task
def send_email_report(email_address: User):
    email = create_email(email_address)
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.send_message(email)
