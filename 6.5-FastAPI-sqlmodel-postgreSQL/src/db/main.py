from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import text
from . models import Book

from src.config import settings

async_engine = create_async_engine(
    url=settings.POSTGRES_URL,
    echo=True
)

async def init_db():
    async with AsyncSession(async_engine) as session:
        stmt = text("SELECT 'Hello';")
        result = await session.exec(stmt)
        print(result.all())