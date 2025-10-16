from typing import Optional
from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime

class Company(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True, nullable=False, unique=True)
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)

    employees: list["Employee"] = Relationship(back_populates="company")


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(index=True, nullable=False, unique=True)
    full_name: str = Field(nullable=True)
    email: str = Field(nullable=False, unique=True)
    is_active: bool = Field(default=True)


class Employee(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id", nullable=False)
    company_id: int = Field(foreign_key="company.id", nullable=False)
    role: Optional[str] = Field(default=None)

    # relationships
    user: "User" = Relationship()
    company: "Company" = Relationship(back_populates="employees")
