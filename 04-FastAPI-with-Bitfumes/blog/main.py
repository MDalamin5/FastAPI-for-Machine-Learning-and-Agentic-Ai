from fastapi import FastAPI
from  scheas import Blog
from database import engine
import scheas, models

app = FastAPI(
    title="Eil-Pil blog api",
    description="This API mainly design for CRUD Operations"
)

models.Base.metadata.create_all(engine)


@app.get("/")
def home():
    return {
        "messages": "Welcome to eil-pil Blog."
    }
    

@app.post("/blog")
def create(request: Blog):
    print(request.title)
    
    return {
        "blog_post": {
            "title": request.title,
            "body": request.body
        }
    }