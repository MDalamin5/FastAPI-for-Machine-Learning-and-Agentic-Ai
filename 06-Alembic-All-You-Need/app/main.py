from fastapi import FastAPI, Depends
from sqlmodel import select
from .models import User, Company, Employee
from .db import get_session

app = FastAPI()

@app.get("/")
def root():
    return {"ok": True}

@app.post("/users/")
def create_user(user: User, session = Depends(get_session)):
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

@app.get("/companies/")
def list_companies(session = Depends(get_session)):
    companies = session.exec(select(Company)).all()
    return companies
