from pydantic import BaseModel, Field
import uuid
from datetime import datetime
from sqlmodel import Column
import sqlalchemy.dialects.postgresql as pg

class UserCreateModel(BaseModel):
    username: str = Field(max_length=10)
    email: str = Field(max_length=40)
    password: str = Field(min_length=7)
    first_name:str = Field(max_length=25)
    last_name: str = Field(max_length=34)


class UserModel(BaseModel):
    uid: uuid.UUID
    username: str
    email: str
    first_name: str
    last_name: str
    is_verified: bool
    password_hash: str = Field(exclude=True) # its serializing time its not showing this password
    created_at: datetime 
    update_at: datetime 


class UserLogin(BaseModel):
    email: str = Field(max_length=40)
    password: str = Field(min_length=6)
    
