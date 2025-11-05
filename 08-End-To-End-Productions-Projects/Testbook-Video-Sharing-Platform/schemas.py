from pydantic import BaseModel

class CreatePostModel(BaseModel):
    title: str
    content: str