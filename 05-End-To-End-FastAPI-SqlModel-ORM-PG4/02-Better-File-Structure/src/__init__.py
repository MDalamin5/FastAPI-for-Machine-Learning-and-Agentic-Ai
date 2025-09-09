from fastapi import FastAPI
from src.books.routes import book_router

version = "v1"

app = FastAPI(
    title="Advanced Api Building Using Router Process.",
    version=version
)

app.include_router(book_router, prefix=f"/api/{version}/books", tags=["books"]) # this prefix will be add every router as link: "/books/{other value in the define in router app}"

