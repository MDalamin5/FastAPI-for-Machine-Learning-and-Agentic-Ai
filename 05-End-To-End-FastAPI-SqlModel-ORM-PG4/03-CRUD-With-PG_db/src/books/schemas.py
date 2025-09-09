from pydantic import BaseModel

class Book(BaseModel):
    id: int
    title: str
    author: str
    publisher: str
    publish_date: str
    page_count: int
    language: str


class UpdateBook(BaseModel):
    title: str
    author: str
    publisher: str
    page_count: int
    language: str