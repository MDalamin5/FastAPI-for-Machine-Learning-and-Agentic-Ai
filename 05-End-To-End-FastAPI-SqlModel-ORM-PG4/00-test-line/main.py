from fastapi import FastAPI, Header
from typing import Optional
from schemas import BookCrateBookModel

app = FastAPI(
    title="My Test Line APi",
    version="10.1.9"
)

@app.get("/")
async def home():
    return {
        "messages": "Test line of the api."
    }

# --------------------------------------------------
# @app.get("/greet/{name}")
# async def greet_name(name: str, age: int) -> dict:
# ---------------------------------------------------
# http://127.0.0.1:8000/greet/test?age=23 hwo you execute it.
# ---------------------------------------------------------------

@app.get("/greet/")
async def greet_name(name: Optional[str]="User", age: Optional[int]=25) -> dict:
    return {
        "messages": f"Hi {name} and Age: {age}"
    }


# request to the server
@app.post("/create_book")
async def create_book(book_data: BookCrateBookModel):
    return {
        "title": book_data.title,
        "author": book_data.author
    }

## ---> Get Header <-----
@app.get("/get_header", status_code=200)
async def get_header(
    accept: str = Header(None),
    content_type: str = Header(None),
    user_agent: str = Header(None)
):
    request_headers = {}
    request_headers["accept"] = accept
    request_headers["content-type"] = content_type
    request_headers["user-agent"] = user_agent

    return request_headers