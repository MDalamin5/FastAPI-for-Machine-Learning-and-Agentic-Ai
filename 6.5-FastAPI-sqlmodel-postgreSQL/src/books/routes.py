from fastapi import APIRouter
from src.db.main import get_session
from sqlmodel.ext.asyncio.session import AsyncSession
from fastapi import Depends
from http import HTTPStatus
from typing import List
import uuid
from .service import BookService
from .schemas import BookCreateModel, BookResponseModel

book_router = APIRouter(
    prefix="/books"
)

## get the books
@book_router.get("/", response_model=List[BookResponseModel])
async def read_books(session: AsyncSession = Depends(get_session)):
    books = await BookService(session=session).get_all_books()

    return books

## post the books
@book_router.post("/", status_code= HTTPStatus.CREATED)
async def create_book(
    book_create_data: BookCreateModel,
    session: AsyncSession = Depends(get_session)
):
    new_book = await BookService(session).create_book(book_create_data)
    return new_book


## get book by employee
@book_router.get("/{book_id}", status_code=HTTPStatus.OK)
async def read_book(
    book_id: str,
    session: AsyncSession = Depends(get_session)
):
    book = await BookService(session).get_book(book_id)

    return book

@book_router.put("/{book_id}", status_code=HTTPStatus.OK)
async def update_book(
    book_id: str,
    book_update_data: BookCreateModel,
    session: AsyncSession = Depends(get_session)
):
    book = await BookService(session).update_book(book_id, book_update_data)
    return book

@book_router.delete("/{book_id}", status_code=HTTPStatus.OK)
async def delete_book(
    book_id: str,
    session: AsyncSession = Depends(get_session)
):
    await BookService(session).delete_book(book_id)

    return {
        "messages": f"This book is {book_id} Deleted."
    }