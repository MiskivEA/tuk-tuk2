from typing import List

from pydantic import BaseModel


class AddPost(BaseModel):
    text: str
    user_id: int


class RespPost(BaseModel):
    text: str


class Posts(BaseModel):
    objects: List[RespPost]
