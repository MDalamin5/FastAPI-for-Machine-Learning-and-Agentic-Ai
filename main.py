from fastapi import FastAPI
import json

app = FastAPI()

def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)
        
        return data

@app.get("/")
def home():
    return {
        "messages": "Patient Management System API"
    }
    
@app.get("/about")
def about():
    return {
        "messages": "A fully function API to manage your patient records."
    }
    
    
@app.get("/view")
def view():
    data = load_data()
    return data
    
