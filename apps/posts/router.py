import datetime
import time
from typing import List

from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from apps.auth.db_connect import get_async_session
from apps.posts.models import PostDB
from apps.posts.schemas import AddPost, RespPost

from fastapi_cache.decorator import cache

router_posts = APIRouter(
    prefix='/posts',
    tags=['Posts']
)


@router_posts.get('/')
@cache(10)
async def get_posts(session: AsyncSession = Depends(get_async_session)):
    """Получение всех объектов
    result = await db.execute(select(Task).order_by(Task.time.desc()).limit(20))
    return result.scalars().all()
    """
    time.sleep(3)
    users = await session.execute(select(PostDB))
    return {'users': users.scalars().all()}


@router_posts.get('/{post_id}')
async def get_posts(post_id: int, session: AsyncSession = Depends(get_async_session)):
    """Получение объекта по ИД"""
    user = await session.execute(select(PostDB).where(PostDB.id == post_id))

    return user.scalar()


@router_posts.get('/post_by_text')
async def get_posts(post_text: str, session: AsyncSession = Depends(get_async_session)):
    """Получение объекта по text"""
    user = await session.execute(select(PostDB).where(PostDB.text == post_text))

    return user.scalar()


@router_posts.post('/add')
async def add_post(post: AddPost, session: AsyncSession = Depends(get_async_session)):
    """Добавление одного объекта"""
    await session.execute(insert(PostDB).values(post.dict()))
    return {'message': 'OK', 'added_obj': RespPost(**post.dict())}


@router_posts.post('/adds')
async def bulk_create_post(posts: List[AddPost], session: AsyncSession = Depends(get_async_session)):
    """Добавление коллекции объектов"""
    for post in posts:
        post_obj = PostDB(**post.dict())
        session.add(post_obj)

    await session.commit()

    return posts
