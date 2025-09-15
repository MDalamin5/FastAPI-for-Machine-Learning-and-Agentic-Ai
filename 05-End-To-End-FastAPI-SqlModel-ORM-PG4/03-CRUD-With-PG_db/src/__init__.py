from fastapi import FastAPI
from src.books.routes import book_router
from src.auth.routes import auth_router
from contextlib import asynccontextmanager
from src.db.main import init_db

@asynccontextmanager
async def life_span(app: FastAPI):
    print("Server is Started......")
    await init_db()
    yield

    print("Server is stopped")

version = "v1"

app = FastAPI(
    title="Advanced Api Building Using Router Process.",
    version=version,
    lifespan = life_span,
    description="Design REST API for book review web Service."
)

app.include_router(book_router, prefix=f"/api/{version}/books", tags=["books"]) # this prefix will be add every router as link: "/books/{other value in the define in router app}"

app.include_router(auth_router, prefix=f"/api/{version}/auth", tags=["auth"])