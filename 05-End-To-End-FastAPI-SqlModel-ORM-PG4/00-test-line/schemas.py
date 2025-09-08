from pydantic import BaseModel

class BookCrateBookModel(BaseModel):
    title: str
    author: str