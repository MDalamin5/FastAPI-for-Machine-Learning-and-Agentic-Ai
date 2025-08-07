from fastapi import FastAPI

app = FastAPI(
    title="Practice FastAPI",
    description="Build CRUD api to interact with database."
)

##

@app.get("/")
def home():
    return {
        "data": {
            "name": "Md Al Amin",
            "Company": "GTR",
            "Role": "Ai Engineer"
        }
    }
    
@app.get("/blog/unpublish")
def unpublish():
    return {
        "data": "List of unpublish blog"
    }
    
    
@app.get("/blog/{id}")
def show(id: int):
    # fetch the blog based on the id
    return {
        "data": id
    }

    

    
@app.get("/blog/{id}/comments")
def comments(id):
    ## fetch the comment of the blog with id = id
    
    return {
        "data": {
            'cmnt_1': "content...",
            'cmnt_2': "content...",
            'cmnt_3': "content...",
        }
    }
    
    
@app.get("/about")
def about():
    return {
        "about page": "list of content about GTR"
    }