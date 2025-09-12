from pydantic import BaseModel
import uuid
from datetime import datetime, date


class BookSchema(BaseModel):
    uid: uuid.UUID
    title: str
    author: str
    publisher: str
    publish_date:date
    page_count: int
    language: str
    created_at: datetime
    update_at: datetime



class BookCreateModel(BaseModel):
    title: str
    author: str
    publisher: str
    publish_date: str   # use date type for consistency
    page_count: int
    language: str


class UpdateBook(BaseModel):
    title: str
    author: str
    publisher: str
    page_count: int
    language: str