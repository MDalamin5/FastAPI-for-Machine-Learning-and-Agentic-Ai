from sqlmodel.ext.asyncio.session import AsyncSession
from schemas import Book, UpdateBook, BookCreateModel

class BookService():
    async def get_all_book(self, session: AsyncSession):
        pass

    async def get_book(self, book_uid: str,  session: AsyncSession):
        pass


    async def create_book(self, book_data: Book,  session: AsyncSession):
        pass