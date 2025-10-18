from __future__ import annotations
from typing import Optional, List
from uuid import UUID, uuid4
from sqlmodel import SQLModel, Field, Relationship

# ---< User table >------

class User(SQLModel, table=True):
    __tablename__ = "users"

    id: UUID = Field(default_factory=uuid4, primary_key=True)
    name: str

    # Relations 1 ---> m
    blog_posts: List["BlogPost"] = Relationship(back_populates="author")




class BlogPost(SQLModel, table=True):
    __tablename__ = "blog_posts"

    id: UUID = Field(default_factory=uuid4, primary_key=True)
    title: str
    content: Optional[str] = None
    user_id: UUID = Field(foreign_key="users.id")

    # m ---> 1
    author: Optional["User"] = Relationship(back_populates="blog_posts")