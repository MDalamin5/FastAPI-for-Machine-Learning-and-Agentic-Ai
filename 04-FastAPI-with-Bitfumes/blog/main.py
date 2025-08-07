from fastapi import FastAPI, Depends
from  scheas import Blog
from database import engine, SessionLocal
import scheas, models
from sqlalchemy.orm import Session

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

def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        print(e)
    finally:
        db.close()

@app.post("/blog")
def create(request: Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.get("/blog")
def all_blog(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    
    return blogs

@app.get("/blog/{id}")
def show(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    return blog