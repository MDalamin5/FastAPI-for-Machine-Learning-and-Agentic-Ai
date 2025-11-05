from fastapi import FastAPI, HTTPException
from schemas import CreatePostModel
from app.db import Post, create_async_engine, get_async_session, create_db_and_table
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_table()
    yield

app = FastAPI(
    lifespan=lifespan
)

text_posts = {
    1: {
        "title": "Building a REST API with FastAPI",
        "content": "A step-by-step guide to creating your first FastAPI project with route handling and Pydantic models."
    },
    2: {
        "title": "Understanding Async I/O in Python",
        "content": "Learn how async and await improve performance in I/O-bound FastAPI applications."
    },
    3: {
        "title": "Connecting FastAPI with PostgreSQL",
        "content": "How to use SQLAlchemy and Alembic to integrate PostgreSQL into your FastAPI backend."
    },
    4: {
        "title": "JWT Authentication in FastAPI",
        "content": "Implement secure login and token-based authentication with OAuth2 and JWT."
    },
    5: {
        "title": "Deploying FastAPI on Render and Railway",
        "content": "Learn deployment strategies and CI/CD setup for FastAPI applications."
    }
}

text_posts[1]
text_posts.get(3)

@app.get("/posts")
def get_all_posts(limit: int = None):
    if limit:
        return list(text_posts.values())[:limit]
    return text_posts


@app.get("/posts/{id}")
def get_post(id: int):
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="Post not found")
    return text_posts.get(id)

## Create Post
@app.post("/posts")
def create_post(request: CreatePostModel) -> CreatePostModel:
    new_post = {
        "title": request.title,
        "content": request.title
    }

    max_id = max(text_posts.keys()) + 1
    text_posts[max_id] = new_post
    return new_post
