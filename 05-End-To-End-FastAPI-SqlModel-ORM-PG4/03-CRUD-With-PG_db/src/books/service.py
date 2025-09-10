from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, desc
from src.books.models import Book
from src.books.schemas import UpdateBook, BookCreateModel

class BookService():
    async def get_all_book(self, session: AsyncSession):
        stmt = select(Book).order_by(desc(Book.created_at))
        result = await session.execute(stmt)
        return result.scalars().all()

    async def get_book(self, book_uid: str, session: AsyncSession):
        stmt = select(Book).where(Book.uid == book_uid)
        result = await session.execute(stmt)
        return result.scalars().first()

    async def create_book(self, book_data: BookCreateModel, session: AsyncSession):
        new_book = Book(**book_data.model_dump())
        session.add(new_book)
        await session.commit()
        await session.refresh(new_book)  # refresh to get DB-generated values
        return new_book

    async def update_book(self, book_uid: str, update_data: UpdateBook, session: AsyncSession):
        stmt = select(Book).where(Book.uid == book_uid)
        result = await session.execute(stmt)
        book_to_update = result.scalars().first()

        if book_to_update:
            for k, v in update_data.model_dump().items():
                setattr(book_to_update, k, v)
            await session.commit()
            await session.refresh(book_to_update)
            return book_to_update
        return None

    async def delete_book(self, book_uid: str, session: AsyncSession):
        stmt = select(Book).where(Book.uid == book_uid)
        result = await session.execute(stmt)
        book_to_delete = result.scalars().first()

        if book_to_delete:
            await session.delete(book_to_delete)
            await session.commit()
            return {}
        return None
