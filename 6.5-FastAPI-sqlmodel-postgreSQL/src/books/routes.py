from fastapi import APIRouter
from src.db.main import get_session
from sqlmodel.ext.asyncio.session import AsyncSession
from fastapi import Depends
from http import HTTPStatus
import uuid
from .service import BookService

book_router = APIRouter(
    prefix="/books"
)

## get the books
@book_router.get("/")
async def read_books(session: AsyncSession = Depends(get_session)):
    books = BookService(session=session)
    all_books = books.get_all_books()
    return all_books

## post the books
@book_router.post("/", status_code= HTTPStatus.CREATED)
async def create_book(
    session: AsyncSession = Depends(get_session)
):
    pass


## get book by employee
@book_router.get("/{book_id}", status_code=HTTPStatus.OK)
async def read_book(
    book_id: str,
    session: AsyncSession = Depends(get_session)
):
    pass

@book_router.put("/{book_id}", status_code=HTTPStatus.OK)
async def update_book(
    book_id: str,
    session: AsyncSession = Depends(get_session)
):
    pass

@book_router.delete("/{book_id}", status_code=HTTPStatus.OK)
async def delete_book(
    book_id: str,
    session: AsyncSession = Depends(get_session)
):
    pass