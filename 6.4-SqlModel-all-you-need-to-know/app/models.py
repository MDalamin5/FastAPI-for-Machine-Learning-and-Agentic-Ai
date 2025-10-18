from typing import Optional, List
from uuid import UUID, uuid4
from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship


# 1️⃣ Association table for Many-to-Many (Post <-> Tag)
class PostTagLink(SQLModel, table=True):
    post_id: UUID = Field(foreign_key="blogpost.id", primary_key=True)
    tag_id: UUID = Field(foreign_key="tag.id", primary_key=True)


# 2️⃣ User Table
class User(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    username: str = Field(index=True, unique=True)
    email: str = Field(index=True, unique=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    # Relationships
    profile: Optional["Profile"] = Relationship(
        back_populates="user",
        sa_relationship_kwargs={"uselist": False}  # One-to-One
    )
    blog_posts: List["BlogPost"] = Relationship(back_populates="author")


# 3️⃣ Profile Table (One-to-One with User)
class Profile(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    bio: Optional[str] = None
    website: Optional[str] = None
    user_id: UUID = Field(foreign_key="user.id", unique=True)

    # Relationship back to User
    user: Optional[User] = Relationship(back_populates="profile")


# 4️⃣ BlogPost Table
class BlogPost(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    title: str
    content: str
    published_at: datetime = Field(default_factory=datetime.utcnow)
    user_id: UUID = Field(foreign_key="user.id")

    # Relationships
    author: Optional[User] = Relationship(back_populates="blog_posts")
    tags: List["Tag"] = Relationship(back_populates="posts", link_model=PostTagLink)


# 5️⃣ Tag Table (Many-to-Many with BlogPost)
class Tag(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    name: str = Field(index=True, unique=True)

    posts: List[BlogPost] = Relationship(back_populates="tags", link_model=PostTagLink)
