from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "messages": "Assalamualikm sir."
    }
    
@app.get("/about")
def about():
    return {
        "messages": "This is test about page"
    }
    
