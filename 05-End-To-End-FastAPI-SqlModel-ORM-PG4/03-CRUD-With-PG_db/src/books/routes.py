from .schemas import UpdateBook, BookSchema, BookCreateModel
from typing import List
from fastapi import status, Depends
from fastapi.exceptions import HTTPException
from fastapi import APIRouter, status
from src.db.main import get_session
from sqlmodel.ext.asyncio.session import AsyncSession
from src.books.service import BookService
from src.books.models import Book

book_router = APIRouter()  # its can access all HTTP method as GET, POST, DELETE, PATCH
book_service = BookService()

@book_router.get("/", status_code=200)
def home():
    return {
        "messages": "Welcome to Test-Line API"
    }

# ---> Read <---
@book_router.get("/all", response_model=List[Book])
async def get_all_books(session: AsyncSession = Depends(get_session)) -> list:
    print("i'm hit")
    books = await book_service.get_all_book(session)
    return books


# ----> Create <----
@book_router.post("/", status_code=status.HTTP_201_CREATED, response_model=Book)
async def create_a_book(book_data: BookCreateModel, session: AsyncSession = Depends(get_session)) -> dict:
    new_book = await book_service.create_book(book_data, session)

    return new_book

## ---> Search By ID <----
@book_router.get("/{book_uid}", response_model=BookSchema)
async def get_book(book_uid: str, session: AsyncSession = Depends(get_session)) -> dict:
    print("im hare--->")
    book = await book_service.get_book(book_uid, session)

    if book:
        return book
    
    else:
    
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book Not Found."
        )

# ----> Update <----

@book_router.patch("/{book_uid}", response_model=Book)
async def update_book(book_uid: str, book_update_data: UpdateBook, session: AsyncSession = Depends(get_session)):
    update_book = await book_service.update_book(book_uid, book_update_data, session)

    if update_book:
        return update_book
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail = f"Book not found with the id: {book_uid}"
        )
    
# ----> Delete <----

@book_router.delete("/{book_uid}", status_code=status.HTTP_204_NO_CONTENT)
async def get_book(book_uid: str, session: AsyncSession = Depends(get_session)):
    del_book = await book_service.delete_book(book_uid, session)

    if del_book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book Not Found."
        )
    else:
        return {}
    
        
    




# ----> is book id is int <-----