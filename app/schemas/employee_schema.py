from pydantic import BaseModel
from datetime import datetime


class EmployeeCreate(BaseModel):

    name: str
    email: str
    phone: str
    position: str
    salary: int
    department_id: int
    hire_date: datetime


class EmployeeResponse(BaseModel):

    id: int
    name: str
    email: str
    phone: str
    position: str
    salary: int
    department_id: int
    hire_date: datetime

    class Config:
        orm_mode = True
