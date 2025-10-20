from pydantic import BaseModel
from src.db.models import Book


class BookResponseModel(Book):
    pass


class BookCreateModel(BaseModel):
    title: str
    author: str
    isbn: str
    description: str

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "Python Book",
                "author": "Md AL AMIN",
                "isbn": "isbn number",
                "description": "Enter your descriptions.."

            }
        }
    }