from .schemas import Book, UpdateBook
from typing import List
from fastapi import status
from fastapi.exceptions import HTTPException
from fastapi import APIRouter, status
from .data import books

book_router = APIRouter()  # its can access all HTTP method as GET, POST, DELETE, PATCH

@book_router.get("/", status_code=200)
def home():
    return {
        "messages": "Welcome to Test-Line API"
    }

# ---> Read <---
@book_router.get("/all", response_model=List[Book])
async def get_all_books() -> list:
    print("i'm hit")
    return books


# ----> Create <----
@book_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_a_book(request: Book) -> dict:
    new_book = request.model_dump()
    books.append(new_book)

    return new_book

## ---> Search By ID <----
@book_router.get("/{book_id}")
async def get_book(book_id: int) -> dict:
    for book in books:

        if book["id"] == book_id:
            return book
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Book Not Found."
    )

# ----> Update <----

@book_router.patch("/{book_id}")
async def update_book(book_id: int, book_update_data: UpdateBook):
    for book in books:
        if book['id'] == book_id:
            book["title"] = book_update_data.title
            book["publisher"] = book_update_data.publisher
            book["page_count"] = book_update_data.page_count
            book["language"] = book_update_data.language

            return book
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail = f"Book not found with the id: {book_id}"
    )
    
# ----> Delete <----

@book_router.delete("/{book_id}")
async def get_book(book_id: int) -> dict:
    for book in books:

        if book["id"] == book_id:
            books.remove(book)
            return {
                "response": "Book Remove Successfully."
            }
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Book Not Found."
    )