from fastapi import FastAPI
from typing import Optional

app = FastAPI(
    title="Practice FastAPI",
    description="Build CRUD api to interact with database."
)

"""
________________________________________
All About Get Method                    |
get Operation is use for Retrieve Data  |
-----------------------------------------
"""

@app.get("/")
def home():
    return {
        "data": {
            "name": "Md Al Amin",
            "Company": "GTR",
            "Role": "Ai Engineer"
        }
    }

"""
_________________________
| Complex path parameter |
-------------------------
"""

@app.get("/blog")
def index(limit: int=10, published: bool=True, sort: Optional[str]=None):
    
    data = {"1": "test line"}
    for i in range(limit):
        data[i+1] = f"This is blog {i+1}"
        
    if published:
        data = {
            "1": "This only one blog is published."
        }
        
    return {
        "blogs": data
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
def comments(id, limit=10):
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