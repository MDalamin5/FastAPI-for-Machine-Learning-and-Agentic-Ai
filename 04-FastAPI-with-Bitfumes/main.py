from fastapi import FastAPI

app = FastAPI(
    title="Practice FastAPI",
    description="Build CRUD api to interact with database."
)


@app.get("/")
def home():
    return {
        "data": {
            "name": "Md Al Amin",
            "Company": "GTR",
            "Role": "Ai Engineer"
        }
    }
    
@app.get("/about")
def about():
    return {
        "about page": "list of content about GTR"
    }