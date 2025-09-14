from pydantic import BaseModel, Field

class UserCreateModel(BaseModel):
    username: str = Field(max_length=10)
    email: str = Field(max_length=40)
    password: str = Field(min_length=7)