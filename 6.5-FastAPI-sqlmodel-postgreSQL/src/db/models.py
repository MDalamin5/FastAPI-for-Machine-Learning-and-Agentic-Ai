from sqlmodel import SQLModel, Field, Column
from uuid import UUID, uuid4
from sqlalchemy.dialects import postgresql as pg
from datetime import datetime

class Book(SQLModel, table=True):
    __tablename__ = "books"

    uid: UUID = Field(
        sa_column=Column(pg.UUID, primary_key=True, unique=True, default=uuid4)
    )
    title: str
    author: str
    isbn: str
    description: str
    created_at: datetime = Field(default=datetime.now)
    updated_at: datetime = Field(default=datetime.now)

    def __repr__(self):
        return f"Book ==> {self.title}"