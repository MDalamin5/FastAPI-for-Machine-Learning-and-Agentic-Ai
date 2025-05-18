from fastapi import FastAPI, Path, Query, HTTPException
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

@app.get("/patient/{patient_id}")
def view_patient(patient_id: str = Path(..., description="The id of the patient in the DB", example="P001")):
    ## load the data
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="Patient is not found")


## Query parameter are optional key value pairs appended to the end of url. use to pass additional dat to the server in an HTTP request. THis is use typically employed for operation like filtering, sorting, searching and pagination, without altering the endpoint path itself.

## Example .patients?city=dhaka&sort_by=age
## question mark is the query parameter 
## multiple parameters are separated by & sign

"""
New Endpoint sortby-- weight, height, bmp
            order -- asc or desc
"""

@app.get("/sort")
def sort_patients(sort_by: str = Query(..., description="Sort on the basis of height, weight or bmi"), order: str=Query('asc', description="sor in asc or desc order")):
    valid_fields = ['height', 'weight', 'bmi']
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f"Invalid field select from {valid_fields}.")
    
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail=f"Invalid input by the user.")
    
    data = load_data()
    
    sorted_order = True if order == 'desc' else False
    
    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sorted_order)
    return sorted_data
    
