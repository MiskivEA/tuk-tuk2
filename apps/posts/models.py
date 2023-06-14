import datetime

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import MetaData, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from apps.auth.db_connect import User

metadata = MetaData()


class BasePost(DeclarativeBase):
    pass


class PostDB(BasePost):
    __tablename__ = "posts"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    text: Mapped[str] = mapped_column(String(256), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey(User.id))
