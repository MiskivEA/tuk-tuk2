from fastapi import FastAPI
from fastapi_users import FastAPIUsers

from apps.auth.auth import auth_backend
from apps.auth.db_connect import User
from apps.auth.manager import get_user_manager
from apps.auth.schemas import UserRead, UserCreate
from apps.posts.router import router_posts as post_router
from apps.tasks.router import router as task_router

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from redis import asyncio as aioredis
from apps.auth.auth import fastapi_users

app = FastAPI()

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["Auth"],
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(task_router)
app.include_router(post_router)


@app.on_event("startup")
async def startup():
    redis = aioredis.from_url("redis://localhost:63791", encoding="utf8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
