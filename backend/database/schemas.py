# This module is for defining pydantic request/response classes

from pydantic import BaseModel
from typing import Optional
from datetime import datetime 

class User(BaseModel):
    username: str
    password: str

class UserCreateRequest(User):
    pass

class UserResponse(BaseModel):
    user_id: int
    username: str
    created_at: datetime

class UserSummaryResponse(BaseModel):
    user_id: int
    username: str
    created_at: datetime

class Thread(BaseModel):
    thread_title: str
    thread_body: str
    user_id: int

class ThreadCreateRequest(Thread):
    pass

class ThreadResponse(BaseModel):
    thread_id: int
    thread_title: str
    thread_body: str
    user_id: Optional[int] = None
    created_at: datetime

class ThreadSummaryResponse(BaseModel):
    thread_id: int
    thread_title: str
    thread_body: str
    user_id: Optional[int]
    username: Optional[str]
    created_at: datetime

class Post(BaseModel):
    post_body: str
    thread_id: int
    parent_post_id: Optional[int] = None
    user_id: int

class PostCreateRequest(Post):
    pass

class PostResponse(BaseModel):
    post_id: int
    post_body: str
    thread_id: int
    parent_post_id: Optional[int] = None
    user_id: Optional[int] = None
    created_at: datetime

class PostSummaryResponse(BaseModel):
    post_id: int
    post_body: str
    thread_id: int
    thread_title: str
    parent_post_id: Optional[int]
    user_id: Optional[int]
    username: Optional[str]
    created_at: datetime