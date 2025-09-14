from .models import User
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from schemas import UserCreateModel

class UserService:
    async def get_user_by_email(self, email: str, session: AsyncSession):
        stmt = select(User).where(User.email == email)

        result = await session.exec(stmt)
        user = result.first()

        return user
    
    async def user_exists(self, email, session: AsyncSession):
        user = await self.get_user_by_email(email=email, session=session)

        return True if user is not None else False
    
    async def create_user(self, user_data: UserCreateModel, session: AsyncSession):
        user_data_dict = user_data.model_dump()

        new_user = User(
            **user_data_dict
        )