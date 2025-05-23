from fastapi import FastAPI, Path, Query, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Literal, Annotated
import json

app = FastAPI()

class Patient(BaseModel):
    id: Annotated[str, Field(..., description="User id", examples=["P001"])]
    name: Annotated[str, Field(..., description="Name of The Patient.", examples=["Md Al Amin"])]
    city: Annotated[str, Field(..., description="Name of the city of the patient", examples=['Dhaka'])]
    age: Annotated[int, Field(..., description="Age of the Patient", gt=0, le=100)]
    gender: Annotated[Literal["Male", "Female", "Other"], Field(..., description="Gender of the Patient")]
    height: Annotated[float, Field(..., description="Hight of the patient in Mtr.", examples=['1.77m'])]
    weight: Annotated[float, Field(..., description="Weight of the patient.", examples=["65kg"])]
    
    @computed_field
    @property
    def bmi(self) -> float:
        return round(self.weight / (self.height**2), 2)
    
    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return "Underweight"
        elif self.bmi < 25:
            return "Normal"
        elif self.bmi < 30:
            return "Normal"
        else:
            return "Obese"
    

def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)
        
        return data
    
def update_data(data):
    with open("patient.json", 'w') as f:
        json.dump(data, f)
        

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
    
    
@app.post("/create")
def create_patient(patient: Patient):
    ## load the existing data
    data = load_data()
    
    ## check patient already exist or not
    if patient.id in data:
        raise HTTPException(status_code=400, detail="Patient is already exist.")
    
    ## new patient add into the database
    data[patient.id] = patient.model_dump(exclude=['id'])
    
    ## save the data
    update_data(data)
    return JSONResponse(status_code=201, content={"messages": "Patient created successfully."})