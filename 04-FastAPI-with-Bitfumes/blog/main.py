from fastapi import FastAPI
from pydantic import BaseModel
from typing import Literal, Optional

app = FastAPI(
    title="hil-bil blog api",
    description="This API mainly design for CRUD Operations"
)

@app.get("/")
def home():
    return {
        "messages": "Welcome to eil-pil Blog."
    }