from fastapi import FastAPI
from fastapi_users import FastAPIUsers

from apps.auth.auth import auth_backend
from apps.auth.db_connect import User
from apps.auth.manager import get_user_manager
from apps.auth.schemas import UserRead, UserCreate
from apps.posts.router import router_posts

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app = FastAPI()


app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(router_posts)
