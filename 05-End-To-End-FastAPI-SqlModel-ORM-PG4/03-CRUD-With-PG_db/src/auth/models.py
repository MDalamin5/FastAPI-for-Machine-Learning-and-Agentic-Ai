from sqlmodel import SQLModel, Field
import uuid
from datetime import datetime
from sqlmodel import Column
import sqlalchemy.dialects.postgresql as pg



"""
class User:
    uid: uuid.UUID
    username: str
    email: str
    first_name: 
    last_name: str
    is_verified: bool = false
    created_at: datetime
    updated_at: datetime
"""

class User(SQLModel, table=True):
    __tablename__ = "users"

    uid: uuid.UUID = Field(
        sa_column=Column(
            pg.UUID,
            nullable=False,
            primary_key=True,
            default=uuid.uuid4
        )
        
    )
    username: str
    email: str
    first_name: str
    last_name: str
    is_verified: bool = Field(default=False)
    created_at: datetime = Field(
        sa_column=Column(pg.TIMESTAMP, default=datetime.now)
    )
    update_at: datetime =  Field(
        sa_column=Column(pg.TIMESTAMP, default=datetime.now)
    )


    def __repr__(self):
        return f"<User {self.username}>"