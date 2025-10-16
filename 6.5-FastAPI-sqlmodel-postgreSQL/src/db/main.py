from sqlalchemy.ext.asyncio import create_async_engine
from src.config import settings
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import text, SQLModel
from models import Book

async_engine = create_async_engine(
    url=settings.POSTGRES_URL,
    echo=True
)
## This functions is test the db is connected or not

# async def init_db():
#     async with AsyncSession(async_engine) as session:
#         stmt = text("SELECT 'Hello sir!';")

#         result = await session.exec(stmt)

#         print(result.all())