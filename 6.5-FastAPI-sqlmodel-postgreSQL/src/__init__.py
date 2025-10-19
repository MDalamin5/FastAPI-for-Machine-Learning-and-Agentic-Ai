from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.db.main import init_db
from src.books.routes import book_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Server is starting...")
    await init_db()
    yield 
    print("Server is shutting down...")

app = FastAPI(
    title="Book Service ai",
    description="This a book service API.",
    lifespan=lifespan
)

app.include_router(
    book_router, tags=["Books"]
)