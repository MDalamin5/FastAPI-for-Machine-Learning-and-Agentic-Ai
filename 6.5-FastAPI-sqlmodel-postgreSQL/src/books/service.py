from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from src.db.models import Book
from .schemas import BookCreateModel



class BookService():
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all_books(self):
        stmt = select(Book).order_by(Book.created_at)

        result = await self.session.exec(stmt)

        return result.all()
    
    async def create_book(self, book_data: BookCreateModel):
        new_book = Book(**book_data.model_dump())

        self.session.add(new_book)
        await self.session.commit()

        return new_book
    
    async def get_book(self, book_uid: str):
        stmt = select(Book).where(Book.uid == book_uid)

        result = await self.session.exec(stmt)
        return result.first()
    
    async def update_book(self, book_uid: str, book_update_data: BookCreateModel):
        stmt = select(Book).where(Book.uid == book_uid)

        result = await self.session.exec(stmt)
        book = result.first()

        for key, value in book_update_data.model_dump().items():
            setattr(book, key, value)
        
        await self.session.commit()


    async def delete_book(self, book_uid: str):
        stmt = select(Book).where(Book.uid == book_uid)

        result = await self.session.exec(stmt)
        book = result.first()

        await self.session.delete(book)

        await self.session.commit()