from fastapi import FastAPI
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Server is starting...")
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