from sqlmodel import SQLModel
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from src.config import settings


# Create async engine the right way
async_engine = create_async_engine(
    url=settings.DATABASE_URL,
    echo=True
)


async def init_db() -> None:
    async with async_engine.begin() as conn:
        from src.books.models import Book
        # Create tables
        await conn.run_sync(SQLModel.metadata.create_all)


# Dependency for FastAPI routes
async def get_session() -> AsyncSession:
    Session = sessionmaker(
        bind=async_engine,
        class_=AsyncSession,
        expire_on_commit=False
    )
    async with Session() as session:
        yield session
