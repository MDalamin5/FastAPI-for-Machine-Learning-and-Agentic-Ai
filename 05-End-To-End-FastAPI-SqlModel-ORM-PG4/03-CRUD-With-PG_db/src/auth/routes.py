from fastapi import APIRouter
from .schemas import UserCreateModel

auth_router = APIRouter()

@auth_router.post("/signup", response_model="")
async def create_user_account(user_data: UserCreateModel):
    pass