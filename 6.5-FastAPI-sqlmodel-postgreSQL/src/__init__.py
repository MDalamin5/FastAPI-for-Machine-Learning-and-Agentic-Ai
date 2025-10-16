from fastapi import FastAPI
from src.db.main import init_db
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Server is starting...")
    await init_db()
    yield 
    print("Server is shutting down...")

app = FastAPI(
    title="Book Service ai",
    lifespan=lifespan
)

@app.get("/")
def home():
    return {
        "messages": "Welcome to SqlModel Building."
    }