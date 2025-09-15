from fastapi import FastAPI


app  = FastAPI()

@app.get("/aminul")
def home(name: str, age: int):
    return {
        "messages": f"Test line {name} and age: {age}"
    }