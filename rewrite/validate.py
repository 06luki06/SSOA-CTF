from pydantic import BaseModel, Field
from typing import List


class CommentBase(BaseModel):
    comment: str

class CommentCreate(CommentBase):
    recipient_id: int

class Comment(CommentBase):
    id: int
    author_id: int
    recipient_id: int

    class Config:
        from_attributes = True

class UserBase(BaseModel):
    username: str = Field(..., max_length=255)
    name: str = Field(..., max_length=255)
    is_admin: bool = Field(default=False)

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    comments_written: List[Comment] = []
    comments_received: List[Comment] = []

    class Config:
        from_attributes = True
